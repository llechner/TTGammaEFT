#!/usr/bin/env python
''' Analysis script for standard plots
'''

# Standard imports
import ROOT, os, imp, sys, copy
ROOT.gROOT.SetBatch(True)
import itertools
from math                             import isnan, ceil, pi

# RootTools
from RootTools.core.standard          import *

# Internal Imports
from TTGammaEFT.Tools.user            import plot_directory
from TTGammaEFT.Tools.helpers         import splitList
from TTGammaEFT.Tools.cutInterpreter  import cutInterpreter
from TTGammaEFT.Tools.TriggerSelector import TriggerSelector
from TTGammaEFT.Tools.Variables       import NanoVariables
from TTGammaEFT.Tools.objectSelection import isBJet, photonSelector, vidNestedWPBitMapNamingListPhoton

from Analysis.Tools.metFilters        import getFilterCut
from Analysis.Tools.helpers           import getCollection

# Default Parameter
loggerChoices = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']
photonCatChoices = [ "None", "PhotonGood0", "PhotonGood1", "PhotonMVA0", "PhotonNoChgIso0", "PhotonNoSieie0", "PhotonNoChgIsoNoSieie0" ]

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO', nargs='?', choices=loggerChoices,                     help="Log level for logging")
argParser.add_argument('--plot_directory',     action='store',      default='102X_TTG_ppv1_v1')
#argParser.add_argument('--plotFile',           action='store',      default='all_noPhoton')
argParser.add_argument('--selection',          action='store',      default='dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40')
argParser.add_argument('--small',              action='store_true',                                                                       help='Run only on a small subset of the data?', )
argParser.add_argument('--noData',             action='store_true', default=False,                                                        help='also plot data?')
argParser.add_argument('--year',               action='store',      default=None,      type=int,  choices=[2016,2017,2018],                  help="Which year to plot?")
argParser.add_argument('--onlyTT',             action='store_true', default=False,                                                        help="Plot only tt")
#argParser.add_argument('--normalize',          action='store_true', default=False,                                                        help="Normalize yields" )
argParser.add_argument('--addOtherBg',         action='store_true', default=False,                                                        help="add others background" )
argParser.add_argument('--categoryPhoton',     action='store',      default="PhotonNoChgIsoNoSieie0", type=str, choices=photonCatChoices,                   help="plot in terms of photon category, choose which photon to categorize!" )
argParser.add_argument('--mode',               action='store',      default="None",    type=str, choices=["mu", "e", "mumu", "mue", "ee", "SF", "all"], help="plot lepton mode" )
argParser.add_argument('--nJobs',              action='store',      default=1,         type=int, choices=[1,2,3,4,5],                        help="Maximum number of simultaneous jobs.")
argParser.add_argument('--job',                action='store',      default=0,         type=int, choices=[0,1,2,3,4],                        help="Run only job i")
argParser.add_argument('--sideband',           action='store',      default="sieie",   type=str, choices=["chgIso", "sieie"],                help="which sideband to plot?")
args = argParser.parse_args()

# Logger
import Analysis.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if args.small:           args.plot_directory += "_small"
if args.noData:          args.plot_directory += "_noData"

# Samples
if "dilep" in args.selection:
    if args.year == 2016:
        from TTGammaEFT.Samples.nanoTuples_Summer16_private_postProcessed      import *
        if not args.noData:
            from TTGammaEFT.Samples.nanoTuples_Run2016_14Dec2018_postProcessed import *

    elif args.year == 2017:
        from TTGammaEFT.Samples.nanoTuples_Fall17_private_postProcessed        import *
        if not args.noData:
            from TTGammaEFT.Samples.nanoTuples_Run2017_14Dec2018_postProcessed import *

    elif args.year == 2018:
        from TTGammaEFT.Samples.nanoTuples_Autumn18_private_postProcessed      import *
        if not args.noData:
            from TTGammaEFT.Samples.nanoTuples_Run2018_14Dec2018_postProcessed import *
else:
    if args.year == 2016:
        from TTGammaEFT.Samples.nanoTuples_Summer16_private_semilep_postProcessed      import *
        if not args.noData:
            from TTGammaEFT.Samples.nanoTuples_Run2016_14Dec2018_semilep_postProcessed import *

    elif args.year == 2017:
        from TTGammaEFT.Samples.nanoTuples_Fall17_private_semilep_postProcessed        import *
        if not args.noData:
            from TTGammaEFT.Samples.nanoTuples_Run2017_14Dec2018_semilep_postProcessed import *

    elif args.year == 2018:
        from TTGammaEFT.Samples.nanoTuples_Autumn18_private_semilep_postProcessed      import *
        if not args.noData:
            from TTGammaEFT.Samples.nanoTuples_Run2018_14Dec2018_semilep_postProcessed import *


# Text on the plots
def drawObjects( plotData, lumi_scale ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS #bf{#it{Preliminary}}' if plotData else 'CMS #bf{#it{Simulation Preliminary}}'), 
      (0.65, 0.95, '%3.1f fb{}^{-1} (13 TeV)' % lumi_scale)
    ]
    return [tex.DrawLatex(*l) for l in lines] 

# Plotting
def drawPlots( plots, mode ):
    for log in [False, True]:
        sc = args.sideband + "_"
        sc += "log" if log else "lin"
        plot_directory_ = os.path.join( plot_directory, 'ratioPlots', str(args.year), args.plot_directory, args.selection, mode, sc )

        for plot in plots:
            if not max(l[0].GetMaximum() for l in plot.histos): 
                continue # Empty plot
            postFix = ""
            if args.sideband == "sieie":
                postFix = " (high #sigma_{i#etai#eta})"
            elif args.sideband == "chgIso":
                postFix = " (high chg Iso)"
            plot.histos[0][0].style          = styles.lineStyle( ROOT.kCyan+2, width = 2, dotted=False, dashed=False, errors = False )
            plot.histos[1][0].style          = styles.lineStyle( ROOT.kRed+2, width = 2, dotted=False, dashed=False, errors = False )
            if not args.noData: 
                plot.histos[2][0].style          = styles.errorStyle( ROOT.kBlack )
                if mode == "all":
                    plot.histos[2][0].legendText = "data" + postFix
                if mode == "SF":
                    plot.histos[2][0].legendText = "data (SF)" + postFix
            extensions_ = ["pdf", "png", "root"] if mode in ['all', 'SF', 'mue', "mu", "e"] else ['png']

            scaling = { 0:1 } if args.noData or "_cat" in plot.name else { 0:2, 1:2 } 

            plotting.draw( plot,
	                       plot_directory = plot_directory_,
                           extensions = extensions_,
                           ratio = {'histos':[(0,2), (1,2)] if not args.noData else [(0,1)], 'texY': 'Ratio', 'yRange':(0.1,1.9)},
	                       logX = False, logY = log, sorting = False,
	                       yRange = (0.03, "auto") if log else (0.001, "auto"),
	                       scaling = scaling,
	                       legend = [ (0.2,0.87-0.04*sum(map(len, plot.histos)),0.8,0.87), 1],
	                       drawObjects = drawObjects( not args.noData , lumi_scale ),
                           copyIndexPHP = True,
                         )


# get nano variable lists
NanoVars         = NanoVariables( args.year )
jetVarString     = NanoVars.getVariableString(   "Jet",    postprocessed=True, data=(not args.noData), plot=True )
jetVariableNames = NanoVars.getVariableNameList( "Jet",    postprocessed=True, data=(not args.noData), plot=True )
bJetVariables    = NanoVars.getVariables(        "BJet",   postprocessed=True, data=(not args.noData), plot=True )
leptonVariables  = NanoVars.getVariables(        "Lepton", postprocessed=True, data=(not args.noData), plot=True )
leptonVarString  = NanoVars.getVariableString(   "Lepton", postprocessed=True, data=(not args.noData), plot=True )
photonVariables  = NanoVars.getVariables(        "Photon", postprocessed=True, data=(not args.noData), plot=True )
photonVarString  = NanoVars.getVariableString(   "Photon", postprocessed=True, data=(not args.noData), plot=True )
photonVarList    = NanoVars.getVariableNameList( "Photon", postprocessed=True, data=(not args.noData), plot=True )

# Read variables and sequences
read_variables  = ["weight/F",
                   "PV_npvsGood/I",
                   "Jet[%s]" %jetVarString,
                   "PV_npvs/I", "PV_npvsGood/I",
                   "nJetGood/I", "nBTagGood/I",
                   "nJet/I", "nBTag/I",
                   "nLepton/I","nElectron/I", "nMuon/I",
                   "nLeptonGood/I","nElectronGood/I", "nMuonGood/I",
                   "nLeptonGoodLead/I","nElectronGoodLead/I", "nMuonGoodLead/I",
                   "nLeptonTight/I", "nElectronTight/I", "nMuonTight/I",
                   "nLeptonVeto/I", "nElectronVeto/I", "nMuonVeto/I",
                   "Photon[%s]" %photonVarString,
                   "nPhoton/I",
                   "nPhotonGood/I",
                   "MET_pt/F", "MET_phi/F", "METSig/F", "ht/F",
                   "mll/F", "mllgamma/F",
                   "mlltight/F", "mllgammatight/F",
                   "mLtight0Gamma/F",
                   "ltight0GammadR/F", "ltight0GammadPhi/F",
                   "m3/F", "m3wBJet/F",
                   "lldR/F", "lldPhi/F", "bbdR/F", "bbdPhi/F",
                   "photonJetdR/F", "photonLepdR/F", "leptonJetdR/F", "tightLeptonJetdR/F",
                   "mL0Gamma/F",  "mL1Gamma/F",
                   "l0GammadR/F", "l0GammadPhi/F",
                   "l1GammadR/F", "l1GammadPhi/F",
                   "j0GammadR/F", "j0GammadPhi/F",
                   "j1GammadR/F", "j1GammadPhi/F",
                  ]

read_variables += [ "%s_photonCat/I"%item for item in photonCatChoices if item != "None" ]

#read_variables += [ VectorTreeVariable.fromString('Lepton[%s]'%leptonVarString, nMax=10) ]
#read_variables += [ VectorTreeVariable.fromString('Photon[%s]'%photonVarString, nMax=10) ]
#read_variables += [ VectorTreeVariable.fromString('Photon[%s]'%photonVarString, nMax=10) ]
#read_variables += [ VectorTreeVariable.fromString('Jet[%s]'%jetVarString, nMax=10) ]
#read_variables += [ VectorTreeVariable.fromString('JetGood[%s]'%jetVarString, nMax=10) ]

read_variables += map( lambda var: args.categoryPhoton + "_"  + var, photonVariables )

read_variables_MC = ["isTTGamma/I", "isZWGamma/I", "isTGamma/I", "overlapRemoval/I",
                     "reweightPU/F", "reweightPUDown/F", "reweightPUUp/F", "reweightPUVDown/F", "reweightPUVUp/F",
                     "reweightLeptonTightSF/F", "reweightLeptonTightSFUp/F", "reweightLeptonTightSFDown/F",
                     "reweightLeptonTrackingTightSF/F",
                     "reweightLeptonMediumSF/F", "reweightLeptonMediumSFUp/F", "reweightLeptonMediumSFDown/F",
                     "reweightLeptonTrackingMediumSF/F",
                     "reweightDilepTrigger/F", "reweightDilepTriggerUp/F", "reweightDilepTriggerDown/F",
                     "reweightDilepTriggerBackup/F", "reweightDilepTriggerBackupUp/F", "reweightDilepTriggerBackupDown/F",
                     "reweightPhotonSF/F", "reweightPhotonSFUp/F", "reweightPhotonSFDown/F",
                     "reweightPhotonElectronVetoSF/F",
                     "reweightBTag_SF/F", "reweightBTag_SF_b_Down/F", "reweightBTag_SF_b_Up/F", "reweightBTag_SF_l_Down/F", "reweightBTag_SF_l_Up/F",
                     'reweightL1Prefire/F', 'reweightL1PrefireUp/F', 'reweightL1PrefireDown/F',
                    ]

# Sequence
sequence = [ ]# makePhotons ]#\
#            clean_Jets,
#            make_Zpt,
#           ]

# Sample definition
if args.year == 2016:
    if args.onlyTT: all = TT_pow_16
    elif args.addOtherBg: all = all_16
    else: all = all_noOther_16
elif args.year == 2017:
    if args.onlyTT: all = TT_pow_17
    elif args.addOtherBg: all = all_17
    else: all = all_noOther_17
elif args.year == 2018:
    if args.onlyTT: all = TT_pow_18
    elif args.addOtherBg: all = all_18
    else: all = all_noOther_18

all_sb = copy.deepcopy(all)
all_sb.name = "sb"
all_sb.texName  = "tt " if args.onlyTT else "MC "
if args.sideband == "chgIso":
    all_sb.texName += "high chg Iso"
elif args.sideband == "sieie":
    all_sb.texName += "high #sigma_{i#etai#eta}"
all_sb.color   = ROOT.kRed+2

all_fit = copy.deepcopy(all_sb)
all_fit.name = "fit"
all_fit.texName  = "tt " if args.onlyTT else "MC "
if args.sideband == "chgIso":
    all_fit.texName += "low chg Iso"
elif args.sideband == "sieie":
    all_fit.texName += "low #sigma_{i#etai#eta}"
all_fit.syles    = styles.lineStyle( ROOT.kOrange, width = 2, dotted=False, dashed=False, errors = False )
all_fit.color   = ROOT.kCyan+2

mc  = [ all_fit, all_sb ]
stackSamples  = [ [s] for s in mc ]

if args.noData:
    if args.year == 2016:   lumi_scale = 35.92
    elif args.year == 2017: lumi_scale = 41.86
    elif args.year == 2018: lumi_scale = 58.83
    stack = Stack( *stackSamples )
else:
    if args.year == 2016:   data_sample = Run2016
    elif args.year == 2017: data_sample = Run2017
    elif args.year == 2018: data_sample = Run2018
    data_sample.texName        = "data (legacy)"
    data_sample.name           = "data"
    data_sample.read_variables = [ "event/I", "run/I" ]
    data_sample.scale          = 1
    lumi_scale                 = data_sample.lumi * 0.001
    stackSamples              += [data_sample]

stack = Stack( *stackSamples )

for sample in mc:
    sample.read_variables = read_variables_MC
    sample.scale          = lumi_scale
    sample.style          = styles.fillStyle( sample.color )
    if "dilep" in args.selection:
        sample.weight         = lambda event, sample: event.reweightL1Prefire*event.reweightPU*event.reweightLeptonMediumSF*event.reweightLeptonTrackingMediumSF*event.reweightPhotonSF*event.reweightPhotonElectronVetoSF*event.reweightBTag_SF
    else:
        sample.weight         = lambda event, sample: event.reweightL1Prefire*event.reweightPU*event.reweightLeptonTightSF*event.reweightLeptonTrackingTightSF*event.reweightPhotonSF*event.reweightPhotonElectronVetoSF*event.reweightBTag_SF

if args.small:
    for sample in stack.samples:
        sample.normalization=1.
        sample.reduceFiles( factor=20 )
        sample.scale /= sample.normalization

weight_ = lambda event, sample: event.weight

# Use some defaults (set defaults before you create/import list of Plots!!)
#preSelection = "&&".join( [ cutInterpreter.cutString( args.selection ), "overlapRemoval==1"] )
preSelection = "&&".join( [ cutInterpreter.cutString( args.selection ) ] )
Plot.setDefaults( stack=stack, weight=staticmethod( weight_ ), selectionString=preSelection )#, addOverFlowBin='upper' )

# Import plots list (AFTER setDefaults!!)
#plotListFile = os.path.join( os.path.dirname( os.path.realpath( __file__ ) ), 'plotLists', args.plotFile + '.py' )
#if not os.path.isfile( plotListFile ):
#    logger.info( "Plot file not found: %s", plotListFile )
#    sys.exit(1)

#plotModule = imp.load_source( "plotLists", os.path.expandvars( plotListFile ) )
#if args.noData: from plotLists import plotListDataMC as plotList
#else:           from plotLists import plotListData   as plotList

# plotList
addPlots = []

addPlots.append( Plot(
    name      = '%s_sieie_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "%s_sieie/F"%args.categoryPhoton ),
    binning   = [ 20, 0.005, 0.025 ],
))

addPlots.append( Plot(
    name      = '%s_sieie_20ptG120_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_sieie" ) if getattr( event, args.categoryPhoton + "_pt" ) > 20 and getattr( event, args.categoryPhoton + "_pt" ) < 120 else -999,
    binning   = [ 20, 0.005, 0.025 ],
))

addPlots.append( Plot(
    name      = '%s_sieie_120ptG220_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_sieie" ) if getattr( event, args.categoryPhoton + "_pt" ) > 120 and getattr( event, args.categoryPhoton + "_pt" ) < 220 else -999,
    binning   = [ 20, 0.005, 0.025 ],
))

addPlots.append( Plot(
    name      = '%s_sieie_220ptGinf_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_sieie" ) if getattr( event, args.categoryPhoton + "_pt" ) > 220 else -999,
    binning   = [ 20, 0.005, 0.025 ],
))




addPlots.append( Plot(
    name      = '%s_pfIso03_chg_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_pfRelIso03_chg" ) * getattr( event, args.categoryPhoton + "_pt" ),
    binning   = [ 20, 0, 20 ],
))

addPlots.append( Plot(
    name      = '%s_pfIso03_chg_20ptG120_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_pfRelIso03_chg" ) * getattr( event, args.categoryPhoton + "_pt" ) if getattr( event, args.categoryPhoton + "_pt" ) > 20 and getattr( event, args.categoryPhoton + "_pt" ) < 120 else -999,
    binning   = [ 20, 0, 20 ],
))

addPlots.append( Plot(
    name      = '%s_pfIso03_chg_120ptG220_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_pfRelIso03_chg" ) * getattr( event, args.categoryPhoton + "_pt" ) if getattr( event, args.categoryPhoton + "_pt" ) > 120 and getattr( event, args.categoryPhoton + "_pt" ) < 220 else -999,
    binning   = [ 20, 0, 20 ],
))

addPlots.append( Plot(
    name      = '%s_pfIso03_chg_220ptGinf_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_pfRelIso03_chg" ) * getattr( event, args.categoryPhoton + "_pt" ) if getattr( event, args.categoryPhoton + "_pt" ) > 220 else -999,
    binning   = [ 20, 0, 20 ],
))




addPlots.append( Plot(
    name      = '%s_sieie_cat1_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_sieie" ) if getattr( event, args.categoryPhoton + "_photonCat" ) == 1 else -999,
    binning   = [ 20, 0.005, 0.025 ],
))

addPlots.append( Plot(
    name      = '%s_sieie_cat1_20ptG120_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_sieie" ) if getattr( event, args.categoryPhoton + "_pt" ) > 20 and getattr( event, args.categoryPhoton + "_pt" ) < 120 and getattr( event, args.categoryPhoton + "_photonCat" ) == 1 else -999,
    binning   = [ 20, 0.005, 0.025 ],
))

addPlots.append( Plot(
    name      = '%s_sieie_cat1_120ptG220_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_sieie" ) if getattr( event, args.categoryPhoton + "_pt" ) > 120 and getattr( event, args.categoryPhoton + "_pt" ) < 220 and getattr( event, args.categoryPhoton + "_photonCat" ) == 1 else -999,
    binning   = [ 20, 0.005, 0.025 ],
))

addPlots.append( Plot(
    name      = '%s_sieie_cat1_220ptGinf_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_sieie" ) if getattr( event, args.categoryPhoton + "_pt" ) > 220 and getattr( event, args.categoryPhoton + "_photonCat" ) == 1 else -999,
    binning   = [ 20, 0.005, 0.025 ],
))



addPlots.append( Plot(
    name      = '%s_sieie_cat2_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_sieie" ) if getattr( event, args.categoryPhoton + "_photonCat" ) == 2 else -999,
    binning   = [ 20, 0.005, 0.025 ],
))

addPlots.append( Plot(
    name      = '%s_sieie_cat2_20ptG120_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_sieie" ) if getattr( event, args.categoryPhoton + "_pt" ) > 20 and getattr( event, args.categoryPhoton + "_pt" ) < 120 and getattr( event, args.categoryPhoton + "_photonCat" ) == 2 else -999,
    binning   = [ 20, 0.005, 0.025 ],
))

addPlots.append( Plot(
    name      = '%s_sieie_cat2_120ptG220_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_sieie" ) if getattr( event, args.categoryPhoton + "_pt" ) > 120 and getattr( event, args.categoryPhoton + "_pt" ) < 220 and getattr( event, args.categoryPhoton + "_photonCat" ) == 2 else -999,
    binning   = [ 20, 0.005, 0.025 ],
))

addPlots.append( Plot(
    name      = '%s_sieie_cat2_220ptGinf_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_sieie" ) if getattr( event, args.categoryPhoton + "_pt" ) > 220 and getattr( event, args.categoryPhoton + "_photonCat" ) == 2 else -999,
    binning   = [ 20, 0.005, 0.025 ],
))



addPlots.append( Plot(
    name      = '%s_sieie_cat3_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_sieie" ) if getattr( event, args.categoryPhoton + "_photonCat" ) == 3 else -999,
    binning   = [ 20, 0.005, 0.025 ],
))

addPlots.append( Plot(
    name      = '%s_sieie_cat3_20ptG120_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_sieie" ) if getattr( event, args.categoryPhoton + "_pt" ) > 20 and getattr( event, args.categoryPhoton + "_pt" ) < 120 and getattr( event, args.categoryPhoton + "_photonCat" ) == 3 else -999,
    binning   = [ 20, 0.005, 0.025 ],
))

addPlots.append( Plot(
    name      = '%s_sieie_cat3_120ptG220_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_sieie" ) if getattr( event, args.categoryPhoton + "_pt" ) > 120 and getattr( event, args.categoryPhoton + "_pt" ) < 220 and getattr( event, args.categoryPhoton + "_photonCat" ) == 3 else -999,
    binning   = [ 20, 0.005, 0.025 ],
))

addPlots.append( Plot(
    name      = '%s_sieie_cat3_220ptGinf_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_sieie" ) if getattr( event, args.categoryPhoton + "_pt" ) > 220 and getattr( event, args.categoryPhoton + "_photonCat" ) == 3 else -999,
    binning   = [ 20, 0.005, 0.025 ],
))



addPlots.append( Plot(
    name      = '%s_pfIso03_chg_cat2_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_pfRelIso03_chg" ) * getattr( event, args.categoryPhoton + "_pt" ) if getattr( event, args.categoryPhoton + "_photonCat" ) == 2 else -999,
    binning   = [ 20, 0, 20 ],
))

addPlots.append( Plot(
    name      = '%s_pfIso03_chg_cat2_20ptG120_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_pfRelIso03_chg" ) * getattr( event, args.categoryPhoton + "_pt" ) if getattr( event, args.categoryPhoton + "_pt" ) > 20 and getattr( event, args.categoryPhoton + "_pt" ) < 120 and getattr( event, args.categoryPhoton + "_photonCat" ) == 2 else -999,
    binning   = [ 20, 0, 20 ],
))

addPlots.append( Plot(
    name      = '%s_pfIso03_chg_cat2_120ptG220_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_pfRelIso03_chg" ) * getattr( event, args.categoryPhoton + "_pt" ) if getattr( event, args.categoryPhoton + "_pt" ) > 120 and getattr( event, args.categoryPhoton + "_pt" ) < 220 and getattr( event, args.categoryPhoton + "_photonCat" ) == 2 else -999,
    binning   = [ 20, 0, 20 ],
))

addPlots.append( Plot(
    name      = '%s_pfIso03_chg_cat2_220ptGinf_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_pfRelIso03_chg" ) * getattr( event, args.categoryPhoton + "_pt" ) if getattr( event, args.categoryPhoton + "_pt" ) > 220 and getattr( event, args.categoryPhoton + "_photonCat" ) == 2 else -999,
    binning   = [ 20, 0, 20 ],
))




addPlots.append( Plot(
    name      = '%s_pfIso03_chg_cat3_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_pfRelIso03_chg" ) * getattr( event, args.categoryPhoton + "_pt" ) if getattr( event, args.categoryPhoton + "_photonCat" ) == 3 else -999,
    binning   = [ 20, 0, 20 ],
))

addPlots.append( Plot(
    name      = '%s_pfIso03_chg_cat3_20ptG120_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_pfRelIso03_chg" ) * getattr( event, args.categoryPhoton + "_pt" ) if getattr( event, args.categoryPhoton + "_pt" ) > 20 and getattr( event, args.categoryPhoton + "_pt" ) < 120 and getattr( event, args.categoryPhoton + "_photonCat" ) == 3 else -999,
    binning   = [ 20, 0, 20 ],
))

addPlots.append( Plot(
    name      = '%s_pfIso03_chg_cat3_120ptG220_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_pfRelIso03_chg" ) * getattr( event, args.categoryPhoton + "_pt" ) if getattr( event, args.categoryPhoton + "_pt" ) > 120 and getattr( event, args.categoryPhoton + "_pt" ) < 220 and getattr( event, args.categoryPhoton + "_photonCat" ) == 3 else -999,
    binning   = [ 20, 0, 20 ],
))

addPlots.append( Plot(
    name      = '%s_pfIso03_chg_cat3_220ptGinf_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_pfRelIso03_chg" ) * getattr( event, args.categoryPhoton + "_pt" ) if getattr( event, args.categoryPhoton + "_pt" ) > 220 and getattr( event, args.categoryPhoton + "_photonCat" ) == 3 else -999,
    binning   = [ 20, 0, 20 ],
))




addPlots.append( Plot(
    name      = '%s_category_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "%s_photonCat/I"%args.categoryPhoton ),
    binning   = [ 4, 0, 4 ],
))

addPlots.append( Plot(
    name      = '%s_category_20ptG120_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_photonCat" ) if getattr( event, args.categoryPhoton + "_pt" ) > 20 and getattr( event, args.categoryPhoton + "_pt" ) < 120 else -999,
    binning   = [ 4, 0, 4 ],
))

addPlots.append( Plot(
    name      = '%s_category_120ptG220_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_photonCat" ) if getattr( event, args.categoryPhoton + "_pt" ) > 120 and getattr( event, args.categoryPhoton + "_pt" ) < 220 else -999,
    binning   = [ 4, 0, 4 ],
))

addPlots.append( Plot(
    name      = '%s_category_220ptGinf_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_photonCat" ) if getattr( event, args.categoryPhoton + "_pt" ) > 220 else -999,
    binning   = [ 4, 0, 4 ],
))

# Loop over channels
yields   = {}
allPlots = {}
if args.mode != "None":
    allModes = [ args.mode ]
elif args.nJobs != 1:
    allModes = [ 'mumu', 'mue', 'ee', 'SF', 'all'] if "dilep" in args.selection else [ "mu", "e", "all" ]
    allModes = splitList( allModes, args.nJobs)[args.job]
else:
    allModes = [ 'mumu', 'mue', 'ee' ] if "dilep" in args.selection else [ "mu", "e" ]

filterCutData = getFilterCut( args.year, isData=True )
filterCutMc   = getFilterCut( args.year, isData=False )
tr            = TriggerSelector( args.year )
triggerCutMc  = tr.getSelection( "MC" )

if args.sideband == "sieie":
    sb_sel  = ["%s_sieie>0.011"%(args.categoryPhoton) ] #, "%s_sieie<0.02"%(args.categoryPhoton) ]
    fit_sel = ["%s_sieie<0.01015"%(args.categoryPhoton)]
elif args.sideband == "chgIso":
    sb_sel  = ["(%s_pfRelIso03_chg*%s_pt)>=1.141"%(args.categoryPhoton, args.categoryPhoton)]
    fit_sel = ["(%s_pfRelIso03_chg*%s_pt)<1.141"%(args.categoryPhoton, args.categoryPhoton)]

for index, mode in enumerate( allModes ):
    logger.info( "Computing plots for mode %s", mode )

    yields[mode] = {}

    # always initialize with [], elso you get in trouble with pythons references!
    plots  = []
#    plots += plotList
#    plots += [ getYieldPlot( index ) ]
    plots += addPlots

    # Define 2l selections
    leptonSelection = cutInterpreter.cutString( mode )
#    mcSelection = [ filterCutMc, leptonSelection, triggerCutMc ] if args.onlyTT else mcSelection = [ filterCutMc, leptonSelection, triggerCutMc, "overlapRemoval==1" ]
    mcSelection = [ filterCutMc, leptonSelection, triggerCutMc, "overlapRemoval==1" ]
#    if not args.noData:    data_sample.setSelectionString( [ filterCutData, leptonSelection ] )
#    for sample in mc: sample.setSelectionString( mcSelection )

    # sideband/fit region cuts
    if not args.noData: data_sample.setSelectionString( [filterCutData, leptonSelection ] + sb_sel )
    all_sb.setSelectionString( mcSelection + sb_sel )
    all_fit.setSelectionString( mcSelection + fit_sel )

    plotting.fill( plots, read_variables=read_variables, sequence=sequence )

    logger.info( "Plotting mode %s", mode )
    allPlots[mode] = copy.deepcopy(plots) # deep copy for creating SF/all plots afterwards!
    drawPlots( allPlots[mode], mode )

if args.mode != "None" or args.nJobs != 1:
    sys.exit(0)

# Add the different channels into SF and all
if "dilep" in args.selection:
    for mode in [ "SF", "all" ]:
        for plot in allPlots['mumu']:
            for pl in ( p for p in ( allPlots['ee'] if mode=="SF" else allPlots["mue"] ) if p.name == plot.name ):  #For SF add EE, second round add EMu for all
                for i, j in enumerate( list( itertools.chain.from_iterable( plot.histos ) ) ):
                    j.Add( list( itertools.chain.from_iterable( pl.histos ) )[i] )

        drawPlots( allPlots['mumu'], mode )

else:
    for plot in allPlots['mu']:
        for pl in ( p for p in allPlots['e'] if p.name == plot.name ):
            for i, j in enumerate( list( itertools.chain.from_iterable( plot.histos ) ) ):
                j.Add( list( itertools.chain.from_iterable( pl.histos ) )[i] )

    drawPlots( allPlots['mu'], "all" )


