#!/usr/bin/env python
''' Analysis script for standard plots
'''

# Standard imports
import ROOT, os, imp, sys, copy
ROOT.gROOT.SetBatch(True)
import itertools
from math                             import isnan, ceil, pi, sqrt

# RootTools
from RootTools.core.standard          import *

# Internal Imports
from TTGammaEFT.Tools.user            import cache_directory
from TTGammaEFT.Tools.cutInterpreter  import cutInterpreter
from TTGammaEFT.Tools.TriggerSelector import TriggerSelector
from TTGammaEFT.Tools.Variables       import NanoVariables

from Analysis.Tools.metFilters        import getFilterCut
from Analysis.Tools.u_float           import u_float
from Analysis.Tools.DirDB             import DirDB

# Default Parameter
loggerChoices = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']
photonCatChoices = [ "None", "PhotonGood0", "PhotonGood1", "PhotonMVA0", "PhotonNoChgIso0", "PhotonNoChgIsoNoSieie0", "PhotonNoSieie0" ]
recoPlotsPath = os.path.expandvars( "$CMSSW_BASE/src/TTGammaEFT/plots/plotsLukas/reco/" )

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO', nargs='?', choices=loggerChoices,                  help="Log level for logging")
#argParser.add_argument('--plot_directory',     action='store',      default='102X_TTG_ppv1_v1')
argParser.add_argument('--plotFile',           action='store',      default='all_noPhoton')
argParser.add_argument('--selection',          action='store',      default='dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40')
argParser.add_argument('--small',              action='store_true',                                                                    help='Run only on a small subset of the data?', )
argParser.add_argument('--overwrite',          action='store_true',                                                                    help='overwrite cache entry?', )
argParser.add_argument('--checkOnly',          action='store_true',                                                                    help='check cached histos?', )
argParser.add_argument('--year',               action='store',      default=None,   type=int,  choices=[2016,2017,2018],               help="Which year to plot?")
argParser.add_argument('--mode',               action='store',      default="None", type=str, choices=["mu", "e", "all"],              help="plot lepton mode" )
argParser.add_argument('--nJobs',              action='store',      default=1,      type=int, choices=[1,2,3,4,5],                     help="Maximum number of simultaneous jobs.")
argParser.add_argument('--job',                action='store',      default=0,      type=int, choices=[0,1,2,3,4],                     help="Run only job i")
args = argParser.parse_args()

# Logger
import Analysis.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

cache_dir = os.path.join(cache_directory, "qcdHistos")
dirDB = DirDB(cache_dir)
if not dirDB: raise



""" 
#QCD yields
yield_cache_dir = os.path.join(cache_directory, "yields", str(args.year))
yieldDB = DirDB( yield_cache_dir )
if not yieldDB: raise

qcdYields = {}
#qcdModes = [ 'mu', 'e', 'all'] if not args.selection.count("nLepTight2") else ["mumutight","muetight","eetight","SFtight","all"]
qcdModes = [ 'mu', 'e'] if not args.selection.count("nLepTight2") else ["mumutight","muetight","eetight"]
qcdsel = args.selection.split("-photoncat")[0].split("-photonhadcat")[0]
cat = [sel for sel in args.selection.split("-") if "photoncat" in sel or "photonhadcat" in sel][:1]

for index, mode in enumerate( qcdModes ):
    qcdYields[mode] = 0
    for pt in ["lowPT","medPT","highPT"]: #fix for missing caches
        res = "_".join( ["QCD", "-".join( [qcdsel,mode,pt] + cat ), "small" if args.small else "full"] )
        if not yieldDB.contains( res ):
            logger.info("No cache found for res %s"%res)
            sys.exit(0)
        qcdYields[mode] += float( yieldDB.get( res ) )

if args.selection.count("nLepTight2"):
    qcdYields["all"]  = qcdYields["eetight"] 
    qcdYields["all"] += qcdYields["mumutight"] 
    qcdYields["all"] += qcdYields["muetight"] 
    qcdYields["SFtight"]  = qcdYields["eetight"] 
    qcdYields["SFtight"] += qcdYields["mumutight"] 
else:
    qcdYields["all"]  = qcdYields["e"] 
    qcdYields["all"] += qcdYields["mu"] 

"""

# Samples
os.environ["gammaSkim"]="False" #always false for QCD estimate
if args.year == 2016 and not args.checkOnly:
    from TTGammaEFT.Samples.nanoTuples_Summer16_private_semilep_postProcessed      import *
    from TTGammaEFT.Samples.nanoTuples_Run2016_14Dec2018_semilep_postProcessed import *
elif args.year == 2017 and not args.checkOnly:
    from TTGammaEFT.Samples.nanoTuples_Fall17_private_semilep_postProcessed        import *
    from TTGammaEFT.Samples.nanoTuples_Run2017_14Dec2018_semilep_postProcessed import *
elif args.year == 2018 and not args.checkOnly:
    from TTGammaEFT.Samples.nanoTuples_Autumn18_private_semilep_postProcessed      import *
    from TTGammaEFT.Samples.nanoTuples_Run2018_14Dec2018_semilep_postProcessed import *

def getYieldPlot( index ):
    return Plot(
                name      = 'yield',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: event.nElectronTightInvIso,
                binning   = [ 2, 0, 2 ] if not args.selection.count("nLepTight2") else [ 3, 0, 3 ],
                )

# get nano variable lists
NanoVars        = NanoVariables( args.year )

jetVarString     = NanoVars.getVariableString(   "Jet",    postprocessed=True, data=True, plot=True )
jetVariableNames = NanoVars.getVariableNameList( "Jet",    postprocessed=True, data=True, plot=True )
bJetVariables    = NanoVars.getVariables(        "BJet",   postprocessed=True, data=True, plot=True )
leptonVarString  = NanoVars.getVariableString(   "Lepton", postprocessed=True, data=True, plot=True )
leptonVariables  = NanoVars.getVariables(        "Lepton", postprocessed=True, data=True, plot=True )
leptonVarList    = NanoVars.getVariableNameList( "Lepton", postprocessed=True, data=True, plot=True )
photonVariables  = NanoVars.getVariables(        "Photon", postprocessed=True, data=True, plot=True )
photonVarList    = NanoVars.getVariableNameList( "Photon", postprocessed=True, data=True, plot=True )
photonVarString  = NanoVars.getVariableString(   "Photon", postprocessed=True, data=True, plot=True )
genVariables     = NanoVars.getVariables(        "Gen",    postprocessed=True, data=False,             plot=True )
genVarString     = NanoVars.getVariableString(   "Gen",    postprocessed=True, data=False,             plot=True )
genVarList       = NanoVars.getVariableNameList( "Gen",    postprocessed=True, data=False,             plot=True )

# Read variables and sequences
read_variables  = ["weight/F",
                   "PV_npvsGood/I",
                   "PV_npvs/I", "PV_npvsGood/I",
                   "nJetGood/I", "nBTagGood/I",
                   "lpTight/F", "lpInvTight/F",
                   "nJet/I", "nBTag/I",
                   "Jet[%s]" %jetVarString,
                   "nLepton/I", "nElectron/I", "nMuon/I",
                   "nLeptonGood/I", "nElectronGood/I", "nMuonGood/I",
                   "nLeptonTight/I", "nElectronTight/I", "nMuonTight/I",
                   "nLeptonVeto/I", "nElectronVeto/I", "nMuonVeto/I",
                   "Photon[%s]" %photonVarString,
                   "nPhoton/I",
                   "nPhotonGood/I",
                   "MET_pt/F", "MET_phi/F", "METSig/F", "ht/F",
                   "mlltight/F", "mllgammatight/F",
                   "mLtight0Gamma/F",
                   "mLinvtight0Gamma/F",
                   "ltight0GammadR/F", "ltight0GammadPhi/F",
                   "m3/F", "m3wBJet/F", "mT/F", "mT2lg/F", "mTinv/F", "mT2linvg/F",
                   "photonJetdR/F", "tightLeptonJetdR/F",
                  ]

read_variables += [ "%s_photonCat/I"%item for item in photonCatChoices if item != "None" ]

#read_variables += [ VectorTreeVariable.fromString('Lepton[%s]'%leptonVarString, nMax=100) ]
#read_variables += [ VectorTreeVariable.fromString('Photon[%s]'%photonVarString, nMax=100) ]
#read_variables += [ VectorTreeVariable.fromString('Jet[%s]'%jetVarString, nMax=10) ]
#read_variables += [ VectorTreeVariable.fromString('JetGood[%s]'%jetVarString, nMax=10) ]

read_variables += map( lambda var: "PhotonMVA0_"              + var, photonVariables )
read_variables += map( lambda var: "PhotonGood0_"             + var, photonVariables )
read_variables += map( lambda var: "PhotonNoChgIso0_"         + var, photonVariables )
read_variables += map( lambda var: "PhotonNoSieie0_"          + var, photonVariables )
read_variables += map( lambda var: "PhotonNoChgIsoNoSieie0_"  + var, photonVariables )

read_variables += map( lambda var: "MisIDElectron0_"          + var, leptonVariables )

read_variables += map( lambda var: "LeptonGood0_"             + var, leptonVariables )
read_variables += map( lambda var: "LeptonGood1_"             + var, leptonVariables )
read_variables += map( lambda var: "LeptonTight0_"            + var, leptonVariables )
read_variables += map( lambda var: "LeptonTight1_"            + var, leptonVariables )
read_variables += map( lambda var: "Bj0_"                     + var, bJetVariables )
read_variables += map( lambda var: "Bj1_"                     + var, bJetVariables )

read_variables_MC = ["isTTGamma/I", "isZWGamma/I", "isTGamma/I", "overlapRemoval/I",
                     "nGenWElectron/I", "nGenWMuon/I", "nGenWTau/I", "nGenW/I", "nGenWJets/I", "nGenWTauElectron/I", "nGenWTauMuon/I", "nGenWTauJets/I",
                     "nGenElectron/I",
                     "nElectronTightInvIso/I",
                     "nMuonTightInvIso/I",
                     "nLeptonTightInvIso/I",
                     "nGenMuon/I",
                     "nGenPhoton/I",
                     "nGenBJet/I",
                     "nGenTop/I",
                     "nGenJet/I",
                     "nGenPart/I",
                     "reweightPU/F", "reweightPUDown/F", "reweightPUUp/F", "reweightPUVDown/F", "reweightPUVUp/F",
                     "reweightLeptonTightSF/F", "reweightLeptonTightSFUp/F", "reweightLeptonTightSFDown/F",
                     "reweightLeptonTrackingTightSF/F",
                     "reweightDilepTrigger/F", "reweightDilepTriggerUp/F", "reweightDilepTriggerDown/F",
                     "reweightDilepTriggerBackup/F", "reweightDilepTriggerBackupUp/F", "reweightDilepTriggerBackupDown/F",
                     "reweightPhotonSF/F", "reweightPhotonSFUp/F", "reweightPhotonSFDown/F",
                     "reweightPhotonElectronVetoSF/F",
                     "reweightBTag_SF/F", "reweightBTag_SF_b_Down/F", "reweightBTag_SF_b_Up/F", "reweightBTag_SF_l_Down/F", "reweightBTag_SF_l_Up/F",
                     'reweightL1Prefire/F', 'reweightL1PrefireUp/F', 'reweightL1PrefireDown/F',
                    ]

sequence = []

# Sample definition
if args.year == 2016 and not args.checkOnly:
    mc = [ TTG_priv_16, TT_pow_16, DY_LO_16, singleTop_16, WJets_16, TG_16, WG_NLO_16, ZG_16, other_16 ]
    data_sample = Run2016
    qcd   = QCD_16
    gjets = GJets_16

elif args.year == 2017 and not args.checkOnly:
    mc = [ TTG_priv_17, TT_pow_17, DY_LO_17, singleTop_17, WJets_17, TG_17, WG_NLO_17, ZG_17, other_17 ]
    data_sample = Run2017
    qcd   = QCD_17
    gjets = GJets_17

elif args.year == 2018 and not args.checkOnly:
    mc = [ TTG_priv_18, TT_pow_18, DY_LO_18, singleTop_18, WJets_18, TG_18, WG_NLO_18, ZG_18, other_18 ]
    data_sample = Run2018
    qcd   = QCD_18
    gjets = GJets_18


if not args.checkOnly:
    data_sample.read_variables = [ "event/I", "run/I", "luminosityBlock/I" ]
    data_sample.scale          = 1
    lumi_scale                 = data_sample.lumi * 0.001
    stack                      = Stack( mc, data_sample )

else:
    mc = []
    stack = Stack( mc )


sampleWeight = lambda event, sample: (2.25 if event.nPhotonGood>0 and event.PhotonGood0_photonCat==2 else 1.)*(1.17 if "DY" in sample.name else 1.)*event.reweightL1Prefire*event.reweightPU*event.reweightLeptonTightSF*event.reweightLeptonTrackingTightSF*event.reweightPhotonSF*event.reweightPhotonElectronVetoSF*event.reweightBTag_SF
weightString = "reweightL1Prefire*reweightPU*reweightLeptonTightSF*reweightLeptonTrackingTightSF*reweightPhotonSF*reweightPhotonElectronVetoSF*reweightBTag_SF"

for sample in mc:
    sample.read_variables = read_variables_MC
    sample.scale          = lumi_scale
    sample.weight         = sampleWeight

if args.small and not args.checkOnly:
    for sample in stack.samples:
        sample.normalization=1.
        sample.reduceFiles( factor=20 )
        sample.scale /= sample.normalization

weight_ = lambda event, sample: event.weight
tr = TriggerSelector( args.year, singleLepton=True )

selection = [ item if not "nBTag" in item else "nBTag0" for item in args.selection.split("-") ]
selection = [ item for item in selection if not "photoncat" in item and not "photonhadcat" in item and not "nLepVeto" in item ]
selection = "-".join(selection)
preSelection = "&&".join( [ cutInterpreter.cutString( selection ), "weight<15" ] )

replaceSelection = {
    "nLeptonTight":    "nLeptonTightInvIso",
    "nMuonTight":      "nMuonTightInvIso",
    "nElectronTight":  "nElectronTightInvIso",
    "mLtight0Gamma":   "mLinvtight0Gamma",
}

for key, val in replaceSelection.items():
    preSelection = preSelection.replace(key, val)

Plot.setDefaults(   stack=stack, weight=staticmethod( weight_ ), selectionString=preSelection, addOverFlowBin="upper" )

# Import plots list (AFTER setDefaults!!)
plotListFile = os.path.join( recoPlotsPath, 'plotLists', args.plotFile + '.py' )
if not os.path.isfile( plotListFile ):
    logger.info( "Plot file not found: %s", plotListFile )
    sys.exit(1)

plotModule = imp.load_source( "plotLists", os.path.expandvars( plotListFile ) )
from plotLists import plotListData   as plotList

# plotList
addPlots = []

# Loop over channels
yields   = {}
allPlots = {}
if args.mode != "None":
    allModes = [ args.mode ]
else:
#    allModes = [ 'mu', 'e', 'all'] if not args.selection.count("nLepTight2") else ["mumutight","muetight","eetight","SFtight","all"]
    allModes = [ 'mu', 'e'] if not args.selection.count("nLepTight2") else ["mumutight","muetight","eetight"]
    if args.nJobs != 1:
        allModes = splitList( allModes, args.nJobs)[args.job]

filterCutData = getFilterCut( args.year, isData=True )
filterCutMc   = getFilterCut( args.year, isData=False )
tr            = TriggerSelector( args.year )
triggerCutMc  = tr.getSelection( "MC" )

invPlotNames = { 
                "mLinv0PhotonTight":                  "mL0PhotonTight",
                "mLinv0PhotonTight_20ptG120":         "mL0PhotonTight_20ptG120",
                "mLinv0PhotonTight_120ptG220":        "mL0PhotonTight_120ptG220",
                "mLinv0PhotonTight_220ptGinf":        "mL0PhotonTight_220ptGinf",
                "mLinv0PhotonTight_coarse":           "mL0PhotonTight_coarse",
                "mLinv0PhotonTight_20ptG120_coarse":  "mL0PhotonTight_20ptG120_coarse",
                "mLinv0PhotonTight_120ptG220_coarse": "mL0PhotonTight_120ptG220_coarse",
                "mLinv0PhotonTight_220ptGinf_coarse": "mL0PhotonTight_220ptGinf_coarse",
                "mTinv":                              "mT",
                "mTinv_20ptG120":                     "mT_20ptG120",
                "mTinv_120ptG220":                    "mT_120ptG220",
                "mTinv_220ptGinf":                    "mT_220ptGinf",
                "mT2lginv":                           "mT2lg",
                "mT2lginv_20ptG120":                  "mT2lg_20ptG120",
                "mT2lginv_120ptG220":                 "mT2lg_120ptG220",
                "mT2lginv_220ptGinf":                 "mT2lg_220ptGinf",
                "Lpinv":                              "Lp",
                "nElectronGoodInvIso":                "nElectronGood",
                "nMuonGoodInvIso":                    "nMuonGood",
                "nLeptonGoodInvIso":                  "nLeptonGood",
                "nElectronTightInvIso":               "nElectronTight",
                "nMuonTightInvIso":                   "nMuonTight",
                "nLeptonTightInvIso":                 "nLeptonTight",
 }

bSelection = [ sel for sel in args.selection.split("-") if "nBTag" in sel ][:1]

for index, mode in enumerate( allModes ):
    logger.info( "Computing plots for mode %s", mode )

    plots  = []
    plots += plotList
    plots += [ getYieldPlot( index ) ]
#    plots += addPlots

    plots = [ plot for plot in plots if plot.name not in invPlotNames.values() ]
    plots = [ plot for plot in plots if not ("nBJet" in plot.name and "ptG" in plot.name) ]
    if bSelection and "p" in bSelection[0]: #remove bjet plots if more than 1 bjet bin in plots (can not be modeled by data driven QCD estimate)
        plots = [ plot for plot in plots if not "nBJet" in plot.name ]
    plots = [ plot for plot in plots if plot.name not in invPlotNames.values() ]
    for plot in plots:
        if plot.name in invPlotNames.keys(): plot.name = invPlotNames[plot.name]

    if not args.overwrite:
        plots = [ plot for plot in plots if not dirDB.contains("_".join( ["qcdHisto", args.selection, plot.name, str(args.year), mode, "small" if args.small else "full"] + map( str, plot.binning ) )) ]
        if plots and args.checkOnly:
            print("Plot for year %i and selection %s and mode %s not cached!"%(args.year, args.selection, mode))
            continue
        if not plots: continue

    # Define 2l selections
    isoleptonSelection = cutInterpreter.cutString( mode )
    leptonSelection    = isoleptonSelection.replace("Tight","TightInvIso")

    data_sample.setSelectionString( [ filterCutData, leptonSelection ] )
    for sample in mc + signals: sample.setSelectionString( [ filterCutMc, leptonSelection, triggerCutMc, "overlapRemoval==1" ] )

    preSelectionSR = "&&".join( [ cutInterpreter.cutString( args.selection ), "weight<15", filterCutMc, isoleptonSelection, triggerCutMc, "overlapRemoval==1"  ] )
    preSelectionCR = "&&".join( [ preSelection, "weight<15", filterCutMc, leptonSelection,    triggerCutMc, "overlapRemoval==1"  ] )

    yield_QCD_CR  = qcd.getYieldFromDraw(   selectionString=preSelectionCR, weightString="weight*%f*%s"%(lumi_scale,weightString) )["val"]
    yield_QCD_CR += gjets.getYieldFromDraw( selectionString=preSelectionCR, weightString="weight*%f*%s"%(lumi_scale,weightString) )["val"]
    yield_QCD_SR  = qcd.getYieldFromDraw(   selectionString=preSelectionSR, weightString="weight*%f*%s"%(lumi_scale,weightString) )["val"]
    yield_QCD_SR += gjets.getYieldFromDraw( selectionString=preSelectionSR, weightString="weight*%f*%s"%(lumi_scale,weightString) )["val"]

    transFacQCD    = yield_QCD_SR / yield_QCD_CR if yield_QCD_CR != 0 else 0.

    plotting.fill( plots, read_variables=read_variables, sequence=sequence )

    for plot in plots:
        qcdHist = copy.deepcopy(plot.histos[1][0])
        for h in plot.histos[0]:
            qcdHist.Add( h, -1 )
        qcdHist.Scale( transFacQCD )

        cacheName = "_".join( ["qcdHisto", args.selection, plot.name, str(args.year), mode, "small" if args.small else "full"] + map( str, plot.binning ) )
        logger.info( "Adding QCD plot for %s for mode %s"%(plot.name, mode) )
        dirDB.add( cacheName, qcdHist )

