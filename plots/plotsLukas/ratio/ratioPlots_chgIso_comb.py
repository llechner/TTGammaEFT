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
argParser.add_argument('--year',               action='store',      default=None,   type=int,  choices=[2016,2017,2018],                  help="Which year to plot?")
argParser.add_argument('--onlyTT',             action='store_true', default=False,                                                        help="Plot only tt")
#argParser.add_argument('--normalize',          action='store_true', default=False,                                                        help="Normalize yields" )
argParser.add_argument('--addOtherBg',         action='store_true', default=False,                                                        help="add others background" )
argParser.add_argument('--categoryPhoton',     action='store',      default="PhotonNoChgIsoNoSieie0", type=str, choices=photonCatChoices,                   help="plot in terms of photon category, choose which photon to categorize!" )
argParser.add_argument('--mode',               action='store',      default="None", type=str, choices=["mu", "e", "mumu", "mue", "ee", "SF", "all"], help="plot lepton mode" )
argParser.add_argument('--nJobs',              action='store',      default=1,      type=int, choices=[1,2,3,4,5],                        help="Maximum number of simultaneous jobs.")
argParser.add_argument('--job',                action='store',      default=0,      type=int, choices=[0,1,2,3,4],                        help="Run only job i")
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

scaling = { 1:0, 2:0, 3:0, 4:0, 5:0 } if args.noData else { 1:0, 2:0, 3:0, 4:0, 5:0, 6:0 } 

# Plotting
def drawPlots( plots, mode ):
    for log in [False, True]:
        sc = "log" if log else "lin"
        plot_directory_ = os.path.join( plot_directory, 'ratioPlots', str(args.year), args.plot_directory, args.selection, mode, sc )

        for plot in plots:
            if not max(l[0].GetMaximum() for l in plot.histos): 
                continue # Empty plot
            postFix = " (#sigma_{i#etai#eta} sideband)"
            plot.histos[0][0].style          = styles.lineStyle( ROOT.kCyan+2, width = 2, dotted=False, dashed=False, errors = False )
            plot.histos[1][0].style          = styles.lineStyle( ROOT.kCyan+2, width = 2, dotted=False, dashed=True, errors = False )
            plot.histos[2][0].style          = styles.lineStyle( ROOT.kCyan+2, width = 2, dotted=True, dashed=False, errors = False )
            plot.histos[3][0].style          = styles.lineStyle( ROOT.kRed+2, width = 2, dotted=False, dashed=False, errors = False )
            plot.histos[4][0].style          = styles.lineStyle( ROOT.kRed+2, width = 2, dotted=False, dashed=True, errors = False )
            plot.histos[5][0].style          = styles.lineStyle( ROOT.kRed+2, width = 2, dotted=True, dashed=False, errors = False )
            if not args.noData: 
                plot.histos[6][0].style          = styles.errorStyle( ROOT.kBlack )
                if mode == "all":
                    plot.histos[6][0].legendText = "data" + postFix
                if mode == "SF":
                    plot.histos[6][0].legendText = "data (SF)" + postFix
            extensions_ = ["pdf", "png", "root"] if mode in ['all', 'SF', 'mue', "mu", "e"] else ['png']

            plotting.draw( plot,
	                       plot_directory = plot_directory_,
                           extensions = extensions_,
                           ratio = {'histos':[(1,0),(2,0),(3,0),(4,0),(5,0),(6,0)] if not args.noData else [(1,0),(2,0),(3,0),(4,0),(5,0)], 'texY': 'Ratio', 'yRange':(0.1,1.9)},
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

recoPhotonSel_medium_noSieie = photonSelector( 'medium', year=args.year, removedCuts=["sieie"] )

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

all_sb_20To120 = copy.deepcopy(all)
all_sb_20To120.name = "sb_20To120"
all_sb_20To120.texName  = "tt " if args.onlyTT else "MC "
all_sb_20To120.texName += "#sigma_{i#etai#eta} sideband, 20<p_{T}(#gamma)<120 GeV"
#all_sb_20To120.color   = ROOT.kCyan+2

all_sb_120To220 = copy.deepcopy(all)
all_sb_120To220.name = "sb_120To220"
all_sb_120To220.texName  = "tt " if args.onlyTT else "MC "
all_sb_120To220.texName += "#sigma_{i#etai#eta} sideband, 120<p_{T}(#gamma)<220 GeV"
#all_sb_120To220.color   = ROOT.kCyan+2

all_sb_220Toinf = copy.deepcopy(all)
all_sb_220Toinf.name = "sb_220Toinf"
all_sb_220Toinf.texName  = "tt " if args.onlyTT else "MC "
all_sb_220Toinf.texName += "#sigma_{i#etai#eta} sideband, p_{T}(#gamma)>220 GeV"
#all_sb_220toinf.color   = ROOT.kCyan+2

all_fit_20To120 = copy.deepcopy(all)
all_fit_20To120.name = "fit_20To120"
all_fit_20To120.texName  = "tt " if args.onlyTT else "MC "
all_fit_20To120.texName += "#sigma_{i#etai#eta} fit region, 20<p_{T}(#gamma)<120 GeV"
#all_fit_20To120.color   = ROOT.kCyan+2

all_fit_120To220 = copy.deepcopy(all)
all_fit_120To220.name = "fit_120To220"
all_fit_120To220.texName  = "tt " if args.onlyTT else "MC "
all_fit_120To220.texName += "#sigma_{i#etai#eta} fit region, 120<p_{T}(#gamma)<220 GeV"
#all_fit_120To220.color   = ROOT.kCyan+2

all_fit_220Toinf = copy.deepcopy(all)
all_fit_220Toinf.name = "fit_220Toinf"
all_fit_220Toinf.texName  = "tt " if args.onlyTT else "MC "
all_fit_220Toinf.texName += "#sigma_{i#etai#eta} fit region, p_{T}(#gamma)>220 GeV"
#all_fit_220toinf.color   = ROOT.kCyan+2

mc  = [ all_fit_20To120, all_fit_120To220, all_fit_220Toinf, all_sb_20To120, all_sb_120To220, all_sb_220Toinf ]

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
    name      = '%s_pfIso03_chg_comb_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: getattr( event, args.categoryPhoton + "_pfRelIso03_chg" ) * getattr( event, args.categoryPhoton + "_pt" ),
    binning   = [ 20, 0, 20 ],
))

addPlots.append( Plot(
    name      = '%s_category_comb_%s'%(args.categoryPhoton, "ttOnly" if args.onlyTT else "fullMC"),
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "%s_photonCat/I"%args.categoryPhoton ),
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
    if not args.noData: data_sample.setSelectionString( [filterCutData, leptonSelection, "%s_sieie>0.011&&%s_sieie<0.02"%(args.categoryPhoton, args.categoryPhoton) ] )

    all_sb_20To120.setSelectionString( mcSelection   + ["%s_sieie>0.011"%(args.categoryPhoton), "%s_sieie<0.02"%(args.categoryPhoton), "%s_pt>20&&%s_pt<120"%(args.categoryPhoton, args.categoryPhoton)] )
    all_sb_120To220.setSelectionString( mcSelection  + ["%s_sieie>0.011"%(args.categoryPhoton), "%s_sieie<0.02"%(args.categoryPhoton), "%s_pt>120&&%s_pt<220"%(args.categoryPhoton, args.categoryPhoton)] )
    all_sb_220Toinf.setSelectionString( mcSelection  + ["%s_sieie>0.011"%(args.categoryPhoton), "%s_sieie<0.02"%(args.categoryPhoton), "%s_pt>220"%(args.categoryPhoton)] )
    all_fit_20To120.setSelectionString( mcSelection  + ["%s_sieie<0.0102"%(args.categoryPhoton), "%s_pt>20&&%s_pt<120"%(args.categoryPhoton, args.categoryPhoton)] )
    all_fit_120To220.setSelectionString( mcSelection + ["%s_sieie<0.0102"%(args.categoryPhoton), "%s_pt>120&&%s_pt<220"%(args.categoryPhoton, args.categoryPhoton)] )
    all_fit_220Toinf.setSelectionString( mcSelection + ["%s_sieie<0.0102"%(args.categoryPhoton), "%s_pt>220"%(args.categoryPhoton)] )

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


