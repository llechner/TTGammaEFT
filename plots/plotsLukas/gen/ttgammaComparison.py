#!/usr/bin/env python
''' Analysis script for standard plots
'''

# Standard imports
import ROOT, os, imp, sys, copy
ROOT.gROOT.SetBatch(True)
import itertools
import pickle
from math                                import isnan, ceil, pi

# RootTools
from RootTools.core.standard             import *

# Internal Imports
from TTGammaEFT.Tools.user               import plot_directory
from TTGammaEFT.Tools.genCutInterpreter  import cutInterpreter

from Analysis.Tools.WeightInfo           import WeightInfo
from Analysis.Tools.helpers              import getCollection, deltaR, deltaR2

# Default Parameter
loggerChoices = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO', nargs='?', choices=loggerChoices,                                help="Log level for logging")
argParser.add_argument('--plot_directory',     action='store',      default='gen')
argParser.add_argument('--plotFile',           action='store',      default='all')
argParser.add_argument('--selection',          action='store',      default='all')
argParser.add_argument('--version',            action='store',      default='v2')
argParser.add_argument('--small',              action='store_true',                                                                                  help='Run only on a small subset of the data?', )
argParser.add_argument('--normalize',          action='store_true', default=False,                                                                   help="Normalize yields" )
args = argParser.parse_args()

# Logger
import Analysis.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if args.small:     args.plot_directory += "_small"
if args.normalize: args.plot_directory += "_normalize"

# Samples
from TTGammaEFT.Samples.genTuples_TTGamma_postProcessed      import *

def drawObjects( lumi_scale ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS #bf{#it{Simulation Preliminary}}'), 
      (0.65, 0.95, '%3.1f fb{}^{-1} (13 TeV)' % lumi_scale)
    ]
    return [tex.DrawLatex(*l) for l in lines] 

if args.normalize:
    scaling = { 0:i for i, _ in enumerate(comparisonSamples) }

# Plotting
def drawPlots( plots, mode ):
    for log in [False, True]:
        plot_directory_ = os.path.join( plot_directory, 'comparisonPlots', "runCardTest_%s"%args.version, args.selection, mode, "log" if log else "lin" )

        for plot in plots:
            if not max(l[0].GetMaximum() for l in plot.histos): 
                continue # Empty plot
            postFix = " (legacy)"
            extensions_ = ["pdf", "png", "root"] if mode in ['all', 'SF', 'mue'] else ['png']

            plotting.draw( plot,
	                       plot_directory = plot_directory_,
                           extensions = extensions_,
                           ratio = {'yRange': (0.5, 1.5), 'histos':[(i+1,0) for i, _ in enumerate(comparisonSamples[1:])], 'texY':'Ratio'},
#	                       ratio = None,
	                       logX = False, logY = log, sorting = False,
	                       yRange = (0.03, "auto") if log else (0.001, "auto"),
	                       scaling = scaling if args.normalize else {},
	                       legend = [ (0.18,0.85-0.03*sum(map(len, plot.histos)),0.9,0.88), 2],
	                       drawObjects = drawObjects( lumi_scale ) if not args.normalize else drawObjects( lumi_scale ),
                           copyIndexPHP = True,
                         )

def getYieldPlot( index ):
    return Plot(
                name      = 'yield',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: 0.5 + index,
                binning   = [ 3, 0, 3 ],
                )

genJetVarString      = "pt/F,eta/F,phi/F,isMuon/I,isElectron/I,isPhoton/I,matchBParton/I"
genJetVars           = [ item.split("/")[0] for item in genJetVarString.split(",") ]

genTopVarString      = "pt/F,eta/F,phi/F,mass/F"
genTopVars           = [ item.split("/")[0] for item in genTopVarString.split(",") ]

genLeptonVarString   = "pt/F,eta/F,phi/F,pdgId/I,motherPdgId/I,grandmotherPdgId/I"
genLeptonVars        = [ item.split("/")[0] for item in genLeptonVarString.split(",") ]

#genPhotonVarString   = "pt/F,status/I,phi/F,eta/F,mass/F,motherPdgId/I,relIso04_all/F,photonLepdR/F,photonJetdR/F"
genPhotonVarString   = "pt/F,phi/F,eta/F,mass/F,motherPdgId/I,relIso04_all/F,photonLepdR/F,photonJetdR/F"
genPhotonVars        = [ item.split("/")[0] for item in genPhotonVarString.split(",") ]

# Read variables and sequences
read_variables  = ["weight/F",
                   "nGenBJet/I",
                   "nGenMuon/I",
                   "nGenElectron/I",
                   "GenMET_pt/F", "GenMET_phi/F",
                   "nGenLepton/I",
                   "GenLepton[%s]"   %genLeptonVarString,
                   "nGenPhoton/I",
                   "GenPhoton[%s]"   %genPhotonVarString,
                   "nGenJet/I",
                   "GenJet[%s]"      %genJetVarString,
                   "nGenTop/I",
                   "GenTop[%s]"      %genTopVarString,
                   "mll/F", "mllgamma/F",
                  ]

# Read variables and sequences
read_variables  += [
#                   "weight/F",
#                   "nGenBJet/I",
#                   "nGenMuon/I",
#                   "nGenElectron/I",
#                   "GenMET_pt/F", "GenMET_phi/F",
                   "nGenAllLepton/I",
                   "GenAllLepton[%s]"   %genLeptonVarString,
                   "nGenAllPhoton/I",
                   "GenAllPhoton[%s]"   %genPhotonVarString,
#                   "nGenPhotonAll/I",
#                   "GenPhotonAll[%s]"   %genPhotonVarString,
#                   "nGenPhotonPT/I",
#                   "GenPhotonPT[%s]"   %genPhotonVarString,
                   "nGenAllJet/I",
                   "GenAllJet[%s]"      %genJetVarString,
#                   "nGenTop/I",
#                   "GenTop[%s]"      %genTopVarString,
#                   "mll/F", "mllgamma/F",
                   "minDRjj/F",
                   "minDRbb/F",
                   "minDRll/F",
                   "minDRaa/F",
                   "minDRbj/F",
                   "minDRaj/F",
                   "minDRjl/F",
                   "minDRab/F",
                   "minDRbl/F",
                   "minDRal/F",
                  ]

read_variables += [ "GenBj0_" + var for var in genJetVarString.split(",") ]
read_variables += [ "GenBj1_" + var for var in genJetVarString.split(",") ]

read_variables_EFT = [
                      "ref_weight/F",
                      VectorTreeVariable.fromString('p[C/F]', nMax=100)
                     ]

def getlowPtPhotons( event, sample ):
    GenAllPhotons    = getCollection( event, 'GenAllPhoton', ["pt","eta","phi"], 'nGenAllPhoton' )
    GenAllLeptons    = getCollection( event, 'GenAllLepton', ["pt","eta","phi"], 'nGenAllLepton' )
    GenAllJets       = getCollection( event, 'GenAllJet',    ["pt","eta","phi","matchBParton"], 'nGenAllJet' )
    GenJets          = getCollection( event, 'GenJet',       ["pt","eta","phi","matchBParton"], 'nGenJet' )

    GenAllJets.sort( key = lambda p:-p['pt'] )
    GenJets.sort( key = lambda p:-p['pt'] )
    GenAllPhotons.sort( key = lambda p:-p['pt'] )
    if GenAllPhotons:
        event.GenAllPhotonsEta  = GenAllPhotons[0]["eta"]
        event.GenAllPhotonsPt   = GenAllPhotons[0]["pt"]
    else:
        event.GenAllPhotonsEta  = -999
        event.GenAllPhotonsPt   = -999

    GenBJets      = list( filter( lambda g: g["matchBParton"], GenJets ) )
    GenNonBJets   = list( filter( lambda g: not g["matchBParton"], GenJets ) )
    event.nGenBJets     = len(GenBJets)
    event.nGenNonBJets  = len(GenNonBJets)

    GenAllBJets      = list( filter( lambda g: g["matchBParton"], GenAllJets ) )
    GenAllNonBJets   = list( filter( lambda g: not g["matchBParton"], GenAllJets ) )
    event.nGenAllBJets     = len(GenBJets)
    event.nGenAllNonBJets  = len(GenNonBJets)

    if len(GenAllBJets)>0:
        event.GenAllBJets0Pt  = GenAllBJets[0]["pt"]
        event.GenAllBJets0Eta = GenAllBJets[0]["eta"]
    else:
        event.GenAllBJets0Pt  = -999
        event.GenAllBJets0Eta = -999

    if len(GenAllBJets)>1:
        event.GenAllBJets1Pt  = GenAllBJets[1]["pt"]
        event.GenAllBJets1Eta = GenAllBJets[1]["eta"]
    else:
        event.GenAllBJets1Pt  = -999
        event.GenAllBJets1Eta = -999

    GenJetlowPT   = list( filter( lambda g: g["pt"]<20, GenAllJets ) )
    event.nGenJetlowPT  = len(GenJetlowPT)

    GenPhotonlowPT   = list( filter( lambda g: g["pt"]<20, GenAllPhotons ) )
    event.nGenPhotonlowPT  = len(GenPhotonlowPT)

    GenLeptonlowPT   = list( filter( lambda g: g["pt"]<20, GenAllLeptons ) )
    event.nGenLeptonlowPT  = len(GenLeptonlowPT)

    if GenJetlowPT:
        event.GenJetlowPTEta  = GenJetlowPT[0]["eta"]
        event.GenJetlowPTPt   = GenJetlowPT[0]["pt"]
    else:
        event.GenJetlowPTEta  = -999
        event.GenJetlowPTPt   = -999

    if GenPhotonlowPT:
        GenPhotonlowPT[0]["clean"] = 1 #dont clean the high pT photons
        for i, GenPhoton in enumerate(GenPhotonlowPT[::-1][:-1]):
            GenPhoton['clean'] = min( [999] + [ deltaR2( GenPhoton, p ) for p in GenPhotonlowPT[::-1][i+1:] ] ) > 0.09
        event.GenPhotonlowPTEta  = GenPhotonlowPT[0]["eta"]
        event.GenPhotonlowPTPt   = GenPhotonlowPT[0]["pt"]
        GenPhotonlowPT = list( filter( lambda j: j["clean"], GenPhotonlowPT ) )
        event.nGenPhotonlowPTDR  = len(GenPhotonlowPT)
    else:
        event.nGenPhotonlowPTDR  = -999
        event.GenPhotonlowPTEta  = -999
        event.GenPhotonlowPTPt   = -999


def getMinDR( event, sample ):
    GenJets    = getCollection( event, 'GenJet', ["pt","eta","phi","pdgId","matchBParton"], 'nGenJet' )
    trueBjets    = list( filter( lambda j: j['matchBParton'], GenJets ) )
    trueNonBjets = list( filter( lambda j: not j['matchBParton'], GenJets ) )

    GenPromptLeptons = getCollection( event, 'GenLepton', ["pt","eta","phi"], 'nGenLepton' )

#    trueNonBjets = list( filter( lambda g: abs(g["pdgId"]) in [1,2,3,4], trueNonBjets ) )

#    GenPhotonPT      = getCollection( event, 'GenPhotonPT', ["pt","eta","phi","status"], 'nGenPhotonPT' )
#    GenPhoton        = getCollection( event, 'GenPhoton', ["pt","eta","phi","status"], 'nGenPhoton' )
    GenPhotonsAll     = getCollection( event, 'GenPhoton', ["pt","eta","phi","status", "motherPdgId"], 'nGenPhoton' )

#    GenPhotonAll = GenPhotonsAll #list( filter( lambda g: g["status"] , GenPhotonsAll ) )
#    GenPhotonPT = list( filter( lambda g: g["pt"]>13 , GenPhotonsAll ) )
#    GenPhoton = list( filter( lambda g: g["pt"]>13 and abs(g["motherPdgId"]) in [6,21], GenPhotonsAll ) )

#    event.nGenPhotonAll  = len(GenPhotonAll)
#    event.nGenPhotonPt   = len(GenPhotonPT)
#    event.nGenPhotonStat = len(GenPhoton)

#    event.minDRstataa = min( [ deltaR(g1, g2) for i, g1 in enumerate(GenPhoton[:-1])   for g2 in GenPhoton[i+1:]       ] + [999] )
#    event.minDRstataj = min( [ deltaR( a, j ) for a     in GenPhoton                       for j  in trueNonBjets           ] + [999] )
#    event.minDRstatab = min( [ deltaR( a, b ) for a     in GenPhoton                       for b  in trueBjets              ] + [999] )
#    event.minDRstatal = min( [ deltaR( l, a ) for l     in GenPromptLeptons                 for a  in GenPhoton             ] + [999] )

#    event.minDRpt13aa = min( [ deltaR(g1, g2) for i, g1 in enumerate(GenPhotonPT[:-1])   for g2 in GenPhotonPT[i+1:]       ] + [999] )
#    event.minDRpt13aj = min( [ deltaR( a, j ) for a     in GenPhotonPT                       for j  in trueNonBjets           ] + [999] )
#    event.minDRpt13ab = min( [ deltaR( a, b ) for a     in GenPhotonPT                       for b  in trueBjets              ] + [999] )
#    event.minDRpt13al = min( [ deltaR( l, a ) for l     in GenPromptLeptons                 for a  in GenPhotonPT             ] + [999] )

#    event.minDRallaa = min( [ deltaR(g1, g2) for i, g1 in enumerate(GenPhotonAll[:-1])   for g2 in GenPhotonAll[i+1:]       ] + [999] )
#    event.minDRallaj = min( [ deltaR( a, j ) for a     in GenPhotonAll                       for j  in trueNonBjets           ] + [999] )
#    event.minDRallab = min( [ deltaR( a, b ) for a     in GenPhotonAll                       for b  in trueBjets              ] + [999] )
#    event.minDRallal = min( [ deltaR( l, a ) for l     in GenPromptLeptons                 for a  in GenPhotonAll             ] + [999] )

    event.minDRjj = min( [ deltaR(j1, j2) for i, j1 in enumerate(trueNonBjets[:-1])     for j2 in trueNonBjets[i+1:]     ] + [999] )
    event.minDRbb = min( [ deltaR(b1, b2) for i, b1 in enumerate(trueBjets[:-1])        for b2 in trueBjets[i+1:]        ] + [999] )
    event.minDRll = min( [ deltaR(l1, l2) for i, l1 in enumerate(GenPromptLeptons[:-1]) for l2 in GenPromptLeptons[i+1:] ] + [999] )
    event.minDRaa = min( [ deltaR(g1, g2) for i, g1 in enumerate(GenPhotonsAll[:-1])   for g2 in GenPhotonsAll[i+1:]       ] + [999] )
    event.minDRbj = min( [ deltaR( b, j ) for b     in trueBjets                        for j  in trueNonBjets           ] + [999] )
    event.minDRaj = min( [ deltaR( a, j ) for a     in GenPhotonsAll                       for j  in trueNonBjets           ] + [999] )
    event.minDRjl = min( [ deltaR( l, j ) for l     in GenPromptLeptons                 for j  in trueNonBjets           ] + [999] )
    event.minDRab = min( [ deltaR( a, b ) for a     in GenPhotonsAll                       for b  in trueBjets              ] + [999] )
    event.minDRbl = min( [ deltaR( l, b ) for l     in GenPromptLeptons                 for b  in trueBjets              ] + [999] )
    event.minDRal = min( [ deltaR( l, a ) for l     in GenPromptLeptons                 for a  in GenPhotonsAll             ] + [999] )

# Sequence
sequence = [ getlowPtPhotons ]#getMinDR]

lumi_scale = 136.6

#comparisonSamples = [ [ttGamma_SingleLeptFromT_SM_1Line], [ttGamma_SingleLeptFromT_SM_central] ]
#comparisonSamples = [ [ttGamma_SingleLeptFromTbar_SM_1Line], [ttGamma_SingleLeptFromTbar_SM_central] ]
#comparisonSamples = [ [TTG_CMS_RunCard], [TTG_ATLAS_RunCard], [TTG_CMS_RunCard_noDeltaR], [TTG_CMS_RunCard_noJetPtCut], [TTG_CMS_RunCard_noDeltaR_xqcut], [TTG_CMS_RunCard_xqcut], [TTG_CMS_RunCard_noDeltaR_noJetPtCut_xqcut], [TTG_CMS_RunCard_noJetPtCut_xqcut] ]
#comparisonSamples = [ [TTG_CMS_RunCard], [TTG_ATLAS_RunCard], [TTG_CMS_RunCard_noDeltaR_xqcut], [TTG_CMS_RunCard_noJetPtCut_xqcut], [TTG_CMS_RunCard_noDeltaR_noJetPtCut_xqcut] ]
#comparisonSamples = [ [TTG_CMS_RunCard], [TTG_ATLAS_RunCard], [TTG_CMS_RunCard_noJetPtCut_xqcut], [TTG_CMS_RunCard_noDeltaR_noJetPtCut_xqcut_wideLepEta] ]
#comparisonSamples = [ [TTG_CMS_RunCard], [TTG_ATLAS_RunCard], [TTG_CMS_RunCard_noJetPtCut_xqcut], [TTG_CMS_RunCard_noDeltaR_noJetPtCut_xqcut] ]
comparisonSamples = [ [TTG_CMS_RunCard], [TTG_ATLAS_RunCard], [TTG_TTBar_RunCard_modified] ]

#print args.selection
#print "CMS", TTG_CMS_RunCard.getYieldFromDraw( weightString="weight*%f"%lumi_scale, selectionString=cutInterpreter.cutString( args.selection ) )['val']
#print "ATLAS", TTG_ATLAS_RunCard.getYieldFromDraw( weightString="weight*%f"%lumi_scale, selectionString=cutInterpreter.cutString( args.selection ) )['val']

#exit()

#comparisonSamples = [ [TTG_SingleLeptFromT_3LPatched_SM], [TTG_SingleLeptFromT_1L_SM] ]
#comparisonSamples = [ [TTG_SingleLeptFromT_3LBuggy_SM], [TTG_SingleLeptFromT_3LPatched_SM], [TTG_SingleLeptFromT_1L_SM] ]
signals = []

stack      = Stack( *comparisonSamples )

for sample in stack.samples:
    sample.style = styles.lineStyle( sample.color, width=2  )
    sample.scale = lumi_scale
#    sample.weight = lambda event, sample: event.weight

if args.small:
    for sample in stack.samples:
        sample.normalization=1.
        sample.reduceFiles( factor=10 )
        sample.scale /= sample.normalization

weight_ = lambda event, sample: event.weight

# Use some defaults (set defaults before you create/import list of Plots!!)
Plot.setDefaults( stack=stack, weight=staticmethod( weight_ ), selectionString=cutInterpreter.cutString( args.selection ) )#, addOverFlowBin='upper' )

# Import plots list (AFTER setDefaults!!)
plotListFile = os.path.join( os.path.dirname( os.path.realpath( __file__ ) ), 'plotLists', args.plotFile + '.py' )
if not os.path.isfile( plotListFile ):
    logger.info( "Plot file not found: %s", plotListFile )
    sys.exit(1)

plotModule = imp.load_source( "plotLists", os.path.expandvars( plotListFile ) )
from plotLists import plotListDataMC as plotList

# plotList
addPlots = []

addPlots.append( Plot(
    name      = 'GenAllBJets0_pt',
    texX      = 'p_{T}(b_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenAllBJets0Pt,
    binning   = [ 20, 0, 200 ],
))

addPlots.append( Plot(
    name      = 'GenAllBJets0_eta',
    texX      = '#eta(b_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenAllBJets0Eta,
    binning   = [ 20, -5, 5 ],
))

addPlots.append( Plot(
    name      = 'GenAllBJets1_pt',
    texX      = 'p_{T}(b_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenAllBJets1Pt,
    binning   = [ 20, 0, 200 ],
))

addPlots.append( Plot(
    name      = 'GenAllBJets1_eta',
    texX      = '#eta(b_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenAllBJets1Eta,
    binning   = [ 20, -5, 5 ],
))


addPlots.append( Plot(
    name      = 'nGenLeptonAll',
    texX      = 'N_{l}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nGenAllLepton,
    binning   = [ 6, 0, 6 ],
))

addPlots.append( Plot(
    name      = 'nGenJetsAll',
    texX      = 'N_{jets}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nGenAllJet,
    binning   = [ 20, 0, 20 ],
))

addPlots.append( Plot(
    name      = 'nGenBJets',
    texX      = 'N_{b-jets}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nGenBJets,
    binning   = [4, 0, 4 ],
))

addPlots.append( Plot(
    name      = 'nGenNonBJets',
    texX      = 'N_{non b-jets}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nGenNonBJets,
    binning   = [10, 0, 10 ],
))

addPlots.append( Plot(
    name      = 'nGenAllBJets',
    texX      = 'N_{b-jets}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nGenAllBJets,
    binning   = [4, 0, 4 ],
))

addPlots.append( Plot(
    name      = 'nGenAllNonBJets',
    texX      = 'N_{non b-jets}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nGenAllNonBJets,
    binning   = [10, 0, 10 ],
))

addPlots.append( Plot(
    name      = 'nGenJetsLowPt',
    texX      = 'N_{jets}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nGenJetlowPT,
    binning   = [ 20, 0, 20 ],
))

addPlots.append( Plot(
    name      = 'nGenLeptonLowPT',
    texX      = 'N_{#gamma}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nGenLeptonlowPT,
    binning   = [ 6, 0, 6 ],
))

addPlots.append( Plot(
    name      = 'GenPhotonAll0_pt',
    texX      = 'p_{T}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenAllPhotonsPt,
    binning   = [ 20, 0, 400 ],
))

addPlots.append( Plot(
    name      = 'GenPhotonAll0_eta',
    texX      = '#eta',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenAllPhotonsEta,
    binning   = [ 40, -5, 5 ],
))

addPlots.append( Plot(
    name      = 'nGenPhotonAll',
    texX      = 'N_{#gamma}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nGenAllPhoton,
    binning   = [ 8, 0, 8 ],
))

addPlots.append( Plot(
    name      = 'nGenPhotonLowPT',
    texX      = 'N_{#gamma}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nGenPhotonlowPT,
    binning   = [ 8, 0, 8 ],
))

addPlots.append( Plot(
    name      = 'GenPhotonLowPT0_pt',
    texX      = 'p_{T}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenPhotonlowPTPt,
    binning   = [ 20, 0, 20 ],
))

addPlots.append( Plot(
    name      = 'GenPhotonLowPT0_eta',
    texX      = '#eta',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenPhotonlowPTEta,
    binning   = [ 40, -5, 5 ],
))

addPlots.append( Plot(
    name      = 'GenJetLowPT0_pt',
    texX      = 'p_{T}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenJetlowPTPt,
    binning   = [ 20, 0, 20 ],
))

addPlots.append( Plot(
    name      = 'GenJetLowPT0_eta',
    texX      = '#eta',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenJetlowPTEta,
    binning   = [ 40, -5, 5 ],
))

addPlots.append( Plot(
    name      = 'nGenPhotonAllLowPTDRclean',
    texX      = 'N_{#gamma}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nGenPhotonlowPTDR,
    binning   = [ 8, 0, 8 ],
))


# Loop over channels
yields   = {}
allPlots = {}
if args.selection.count("dilep"): allModes = [ 'mumu', 'mue', 'ee', "SF", "all" ]
else: allModes = [ 'e', "mu", "all" ]

for index, mode in enumerate( allModes ):
    logger.info( "Computing plots for mode %s", mode )

    yields[mode] = {}

    # always initialize with [], elso you get in trouble with pythons references!
    plots  = []
    plots += plotList
    plots += addPlots
    if mode != 'all': plots += [ getYieldPlot( index ) ]

    # Define 2l selections
    leptonSelection = cutInterpreter.cutString( mode )

    for sample in signals: sample.setSelectionString( [ leptonSelection ] )

    plotting.fill( plots, read_variables=read_variables, sequence=sequence )

    # Get normalization yields from yield histogram
    for plot in plots:
        if plot.name != "yield": continue
        for i, l in enumerate( plot.histos ):
            for j, h in enumerate( l ):
                h.GetXaxis().SetBinLabel( 1, "#mu#mu" )
                h.GetXaxis().SetBinLabel( 2, "#mue" )
                h.GetXaxis().SetBinLabel( 3, "ee" )

    logger.info( "Plotting mode %s", mode )
    allPlots[mode] = copy.deepcopy(plots) # deep copy for creating SF/all plots afterwards!
    drawPlots( allPlots[mode], mode )

exit()

# Add the different channels into SF and all
for mode in [ "SF", "all" ]:
    yields[mode] = {}

    for plot in allPlots['mumu']:
        for pl in ( p for p in ( allPlots['ee'] if mode=="SF" else allPlots["mue"] ) if p.name == plot.name ):  #For SF add EE, second round add EMu for all
            for i, j in enumerate( list( itertools.chain.from_iterable( plot.histos ) ) ):
                j.Add( list( itertools.chain.from_iterable( pl.histos ) )[i] )

    drawPlots( allPlots['mumu'], mode )

