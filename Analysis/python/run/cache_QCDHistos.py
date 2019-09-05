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

from TTGammaEFT.Analysis.SetupHelpers import default_misIDSF, default_DYSF

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
argParser.add_argument("--runOnLxPlus",        action="store_true",                                                                    help="Change the global redirector of samples")
args = argParser.parse_args()

# Logging
if __name__=="__main__":
    import Analysis.Tools.logger as logger
    logger = logger.get_logger( args.logLevel, logFile=None)
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger( args.logLevel, logFile=None )
else:
    import logging
    logger = logging.getLogger(__name__)

cache_dir = os.path.join(cache_directory, "qcdHistos")
dirDB = DirDB(cache_dir)
if not dirDB: raise

# Samples
if args.runOnLxPlus:
    # Set the redirector in the samples repository to the global redirector
    from Samples.Tools.config import redirector_global as redirector
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

def getYieldPlots():
    yieldPlots = []
    yieldPlots.append( Plot(
                name      = 'yield',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: event.nElectronTightInvIso,
                binning   = [ 2, 0, 2 ] if not args.selection.count("nLepTight2") else [ 3, 0, 3 ],
                ) )

    if "nPhoton0" in args.selection: return yieldPlots

    yieldPlots.append( Plot(
                name      = 'yield_20ptG120',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: event.nElectronTightInvIso if event.PhotonGood0_pt >= 20 and event.PhotonGood0_pt < 120 else -999,
                binning   = [ 2, 0, 2 ] if not args.selection.count("nLepTight2") else [ 3, 0, 3 ],
                ) )
    yieldPlots.append( Plot(
                name      = 'yield_120ptG220',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: event.nElectronTightInvIso if event.PhotonGood0_pt >= 120 and event.PhotonGood0_pt < 220 else -999,
                binning   = [ 2, 0, 2 ] if not args.selection.count("nLepTight2") else [ 3, 0, 3 ],
                ) )
    yieldPlots.append( Plot(
                name      = 'yield_220ptGinf',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: event.nElectronTightInvIso if event.PhotonGood0_pt >= 220 else -999,
                binning   = [ 2, 0, 2 ] if not args.selection.count("nLepTight2") else [ 3, 0, 3 ],
                ) )


    if not "NoChgIsoNoSieiePhoton" in args.selection: return yieldPlots

    yieldPlots.append( Plot(
                name      = 'yield_invSieie',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: event.nElectronTightInvIso if event.PhotonNoSieie0_sieie > 0.011 else -999,
                binning   = [ 2, 0, 2 ] if not args.selection.count("nLepTight2") else [ 3, 0, 3 ],
                ) )
    yieldPlots.append( Plot(
                name      = 'yield_invSieie_20ptG120',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: event.nElectronTightInvIso if event.PhotonNoSieie0_pt >= 20 and event.PhotonNoSieie0_pt < 120 and event.PhotonNoSieie0_sieie > 0.011 else -999,
                binning   = [ 2, 0, 2 ] if not args.selection.count("nLepTight2") else [ 3, 0, 3 ],
                ) )
    yieldPlots.append( Plot(
                name      = 'yield_invSieie_120ptG220',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: event.nElectronTightInvIso if event.PhotonNoSieie0_pt >= 120 and event.PhotonNoSieie0_pt < 220 and event.PhotonNoSieie0_sieie > 0.011 else -999,
                binning   = [ 2, 0, 2 ] if not args.selection.count("nLepTight2") else [ 3, 0, 3 ],
                ) )
    yieldPlots.append( Plot(
                name      = 'yield_invSieie_220ptGinf',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: event.nElectronTightInvIso if event.PhotonNoSieie0_pt >= 220 and event.PhotonNoSieie0_sieie > 0.011 else -999,
                binning   = [ 2, 0, 2 ] if not args.selection.count("nLepTight2") else [ 3, 0, 3 ],
                ) )



    yieldPlots.append( Plot(
                name      = 'yield_invChgIso',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: event.nElectronTightInvIso if event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt > 1.141 else -999,
                binning   = [ 2, 0, 2 ] if not args.selection.count("nLepTight2") else [ 3, 0, 3 ],
                ) )
    yieldPlots.append( Plot(
                name      = 'yield_invChgIso_20ptG120',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: event.nElectronTightInvIso if event.PhotonNoChgIso0_pt >= 20 and event.PhotonNoChgIso0_pt < 120 and event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt > 1.141 else -999,
                binning   = [ 2, 0, 2 ] if not args.selection.count("nLepTight2") else [ 3, 0, 3 ],
                ) )
    yieldPlots.append( Plot(
                name      = 'yield_invChgIso_120ptG220',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: event.nElectronTightInvIso if event.PhotonNoChgIso0_pt >= 120 and event.PhotonNoChgIso0_pt < 220 and event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt > 1.141 else -999,
                binning   = [ 2, 0, 2 ] if not args.selection.count("nLepTight2") else [ 3, 0, 3 ],
                ) )
    yieldPlots.append( Plot(
                name      = 'yield_invChgIso_220ptGinf',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: event.nElectronTightInvIso if event.PhotonNoChgIso0_pt >= 220 and event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt > 1.141 else -999,
                binning   = [ 2, 0, 2 ] if not args.selection.count("nLepTight2") else [ 3, 0, 3 ],
                ) )


    yieldPlots.append( Plot(
                name      = 'yield_invSieie_invChgIso',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: event.nElectronTightInvIso if event.PhotonNoChgIsoNoSieie0_sieie > 0.011 and event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt > 1.141 else -999,
                binning   = [ 2, 0, 2 ] if not args.selection.count("nLepTight2") else [ 3, 0, 3 ],
                ) )
    yieldPlots.append( Plot(
                name      = 'yield_invSieie_invChgIso_20ptG120',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: event.nElectronTightInvIso if event.PhotonNoChgIsoNoSieie0_pt >= 20 and event.PhotonNoChgIsoNoSieie0_pt < 120 and event.PhotonNoChgIsoNoSieie0_sieie > 0.011 and event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt > 1.141 else -999,
                binning   = [ 2, 0, 2 ] if not args.selection.count("nLepTight2") else [ 3, 0, 3 ],
                ) )
    yieldPlots.append( Plot(
                name      = 'yield_invSieie_invChgIso_120ptG220',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: event.nElectronTightInvIso if event.PhotonNoChgIsoNoSieie0_pt >= 120 and event.PhotonNoChgIsoNoSieie0_pt < 220 and event.PhotonNoChgIsoNoSieie0_sieie > 0.011 and event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt > 1.141 else -999,
                binning   = [ 2, 0, 2 ] if not args.selection.count("nLepTight2") else [ 3, 0, 3 ],
                ) )
    yieldPlots.append( Plot(
                name      = 'yield_invSieie_invChgIso_220ptGinf',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: event.nElectronTightInvIso if event.PhotonNoChgIsoNoSieie0_pt >= 220 and event.PhotonNoChgIsoNoSieie0_sieie > 0.011 and event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt > 1.141 else -999,
                binning   = [ 2, 0, 2 ] if not args.selection.count("nLepTight2") else [ 3, 0, 3 ],
                ) )

    return yieldPlots


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
                   "nElectronTightInvIso/I",
                   "nMuonTightInvIso/I",
                   "nLeptonTightNoIso/I",
                   "nLeptonTightInvIso/I",
                   "PV_npvsGood/I",
                   "PV_npvs/I", "PV_npvsGood/I",
                   "nJetGood/I", "nBTagGood/I",
                   "lpTight/F", "lpInvTight/F",
                   "nJet/I", "nBTag/I",
                   "Jet[%s]" %jetVarString,
                   "Lepton[%s]" %leptonVarString,
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

read_variables += map( lambda var: "PhotonMVA0_"              + var, photonVariables )
read_variables += map( lambda var: "PhotonGood0_"             + var, photonVariables )
read_variables += map( lambda var: "PhotonNoChgIso0_"         + var, photonVariables )
read_variables += map( lambda var: "PhotonNoSieie0_"          + var, photonVariables )
read_variables += map( lambda var: "PhotonNoChgIsoNoSieie0_"  + var, photonVariables )

read_variables += map( lambda var: "MisIDElectron0_"          + var, leptonVariables )

read_variables += map( lambda var: "LeptonGood0_"             + var, leptonVariables )
read_variables += map( lambda var: "LeptonGood1_"             + var, leptonVariables )
read_variables += map( lambda var: "LeptonTightInvIso0_"      + var, leptonVariables )
read_variables += map( lambda var: "LeptonTight0_"            + var, leptonVariables )
read_variables += map( lambda var: "LeptonTight1_"            + var, leptonVariables )
read_variables += map( lambda var: "Bj0_"                     + var, bJetVariables )
read_variables += map( lambda var: "Bj1_"                     + var, bJetVariables )

read_variables_MC = ["isTTGamma/I", "isZWGamma/I", "isTGamma/I", "overlapRemoval/I",
                     "nGenWElectron/I", "nGenWMuon/I", "nGenWTau/I", "nGenW/I", "nGenWJets/I", "nGenWTauElectron/I", "nGenWTauMuon/I", "nGenWTauJets/I",
                     "nGenElectron/I",
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
    mc = [ TTG_16, TT_pow_16, DY_LO_16, WJets_16, VG_16, rest_16 ]
    data_sample = Run2016
    qcd   = QCD_16
    gjets = GJets_16

elif args.year == 2017 and not args.checkOnly:
    mc = [ TTG_priv_17, TT_pow_17, DY_LO_17, WJets_17, VG_17, rest_17 ]
    data_sample = Run2017
    qcd   = QCD_17
    gjets = GJets_17

elif args.year == 2018 and not args.checkOnly:
    mc = [ TTG_priv_18, TT_pow_18, DY_LO_18, WJets_18, VG_18, rest_18 ]
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


sampleWeight = lambda event, sample: (event.reweightL1Prefire*event.reweightPU*event.reweightLeptonTightSF*event.reweightLeptonTrackingTightSF*event.reweightPhotonSF*event.reweightPhotonElectronVetoSF*event.reweightBTag_SF)+((default_misIDSF-1)*(event.nPhotonGood>0)*(event.PhotonGood0_photonCat==2)*event.reweightL1Prefire*event.reweightPU*event.reweightLeptonTightSF*event.reweightLeptonTrackingTightSF*event.reweightPhotonSF*event.reweightPhotonElectronVetoSF*event.reweightBTag_SF)
weightString = "reweightL1Prefire*reweightPU*reweightLeptonTightSF*reweightLeptonTrackingTightSF*reweightPhotonSF*reweightPhotonElectronVetoSF*reweightBTag_SF"

for sample in mc:
    sample.read_variables = read_variables_MC
    sample.scale          = lumi_scale
    if "DY" in sample.name:
        sample.scale     *= default_DYSF
    sample.weight         = sampleWeight

if args.small and not args.checkOnly:
    for sample in stack.samples:
        sample.normalization=1.
        sample.reduceFiles( factor=20 )
        sample.scale /= sample.normalization

weight_ = lambda event, sample: event.weight

selection = [ item if not "nBTag" in item else "nBTag0" for item in args.selection.split("-") ]
#selection = [ item for item in selection if not "nLepVeto" in item ]
selection = "-".join(selection)
preSelection = "&&".join( [ cutInterpreter.cutString( selection ) ] )#, "weight<15" ] )

if "nPhoton0" in args.selection:
    catSel = None
elif "NoChgIsoNoSieiePhoton" in args.selection:
    catSel = "photonhadcat" 
    ptSels = ["lowhadPT", "medhadPT", "highhadPT"]
else:
    catSel = "photoncat" 
    ptSels = ["lowPT", "medPT", "highPT"]

replaceSelection = {
    "nLeptonVetoIsoCorr":        "nLeptonTightNoIso",
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
    allModes = [ 'mu', 'e'] if not args.selection.count("nLepTight2") else ["mumutight","muetight","eetight"]
    if args.nJobs != 1:
        allModes = splitList( allModes, args.nJobs)[args.job]

filterCutData = getFilterCut( args.year, isData=True, skipBadChargedCandidate=True )
filterCutMc   = getFilterCut( args.year, isData=False, skipBadChargedCandidate=True )
tr            = TriggerSelector( args.year, singleLepton=True )
triggerCutMc  = tr.getSelection( "MC" )

invPlotNames = { 
                "leptonTightInvIso0_pt":              "leptonTight0_pt",
                "leptonTightInvIso0_eta":             "leptonTight0_eta",
                "leptonTightInvIso0_phi":             "leptonTight0_phi",
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
    plots += getYieldPlots()
#    plots += addPlots

    plots = [ plot for plot in plots if plot.name not in invPlotNames.values() ]
    plots = [ plot for plot in plots if not ("nBJet" in plot.name and "ptG" in plot.name) ]
    if bSelection and "p" in bSelection[0]: #remove bjet plots if more than 1 bjet bin in plots (can not be modeled by data driven QCD estimate)
        plots = [ plot for plot in plots if not "nBJet" in plot.name ]

    for plot in plots:
        if plot.name in invPlotNames.keys(): plot.name = invPlotNames[plot.name]

    if not args.overwrite:
        plots = [ plot for plot in plots if not dirDB.contains("_".join( ["qcdHisto", args.selection, plot.name, str(args.year), mode, "small" if args.small else "full"] + map( str, plot.binning ) )) ]
        if plots and args.checkOnly:
            print("Plot for year %i and selection %s and mode %s not cached!"%(args.year, args.selection, mode))
            continue
        if not plots: continue

    # Define selections
    isoleptonSelection = cutInterpreter.cutString( mode )
    leptonSelection    = cutInterpreter.cutString( mode + "Inv" )

    data_sample.setSelectionString( [ filterCutData, leptonSelection ] )
    for sample in mc + signals:
            sample.setSelectionString( [ filterCutMc, leptonSelection, triggerCutMc, "overlapRemoval==1" ] )

    plotting.fill( plots, read_variables=read_variables, sequence=sequence )

    # Transfer factor
    preSelectionCR = "&&".join( [ preSelection,                               filterCutMc, leptonSelection,    triggerCutMc, "overlapRemoval==1"  ] )
    preSelectionSR = "&&".join( [ cutInterpreter.cutString( args.selection ), filterCutMc, isoleptonSelection, triggerCutMc, "overlapRemoval==1"  ] )

    yield_QCD_CR  = qcd.getYieldFromDraw(   selectionString=preSelectionCR, weightString="weight*%f*%s"%(lumi_scale,weightString) )["val"]
    yield_QCD_CR += gjets.getYieldFromDraw( selectionString=preSelectionCR, weightString="weight*%f*%s"%(lumi_scale,weightString) )["val"]
    yield_QCD_SR  = qcd.getYieldFromDraw(   selectionString=preSelectionSR, weightString="weight*%f*%s"%(lumi_scale,weightString) )["val"]
    yield_QCD_SR += gjets.getYieldFromDraw( selectionString=preSelectionSR, weightString="weight*%f*%s"%(lumi_scale,weightString) )["val"]

    transFacQCD = {}
    transFacQCD["incl"] = yield_QCD_SR / yield_QCD_CR if yield_QCD_CR != 0 else 0.

    # Transfer factor for photon category plots
    for i in range(4):
        if catSel and yield_QCD_CR != 0:
            preSelectionSR_cat = "&&".join( [ cutInterpreter.cutString( "-".join([args.selection, catSel+str(i)]) ), filterCutMc, isoleptonSelection, triggerCutMc, "overlapRemoval==1"  ] )
            yield_QCD_SR_cat  = qcd.getYieldFromDraw(   selectionString=preSelectionSR_cat, weightString="weight*%f*%s"%(lumi_scale,weightString) )["val"]
            yield_QCD_SR_cat += gjets.getYieldFromDraw( selectionString=preSelectionSR_cat, weightString="weight*%f*%s"%(lumi_scale,weightString) )["val"]
            transFacQCD["incl_cat"+str(i)] = yield_QCD_SR_cat / yield_QCD_CR
        else:
            transFacQCD["incl_cat"+str(i)] = 0.

    if not "nPhoton0" in args.selection and transFacQCD["incl"] > 0:
        for pt in ptSels:
            yield_QCD_CR  = qcd.getYieldFromDraw(   selectionString=preSelectionCR + "&&" + cutInterpreter.cutString( pt ), weightString="weight*%f*%s"%(lumi_scale,weightString) )["val"]
            yield_QCD_CR += gjets.getYieldFromDraw( selectionString=preSelectionCR + "&&" + cutInterpreter.cutString( pt ), weightString="weight*%f*%s"%(lumi_scale,weightString) )["val"]
            yield_QCD_SR  = qcd.getYieldFromDraw(   selectionString=preSelectionSR + "&&" + cutInterpreter.cutString( pt ), weightString="weight*%f*%s"%(lumi_scale,weightString) )["val"]
            yield_QCD_SR += gjets.getYieldFromDraw( selectionString=preSelectionSR + "&&" + cutInterpreter.cutString( pt ), weightString="weight*%f*%s"%(lumi_scale,weightString) )["val"]

            transFacQCD[pt] = yield_QCD_SR / yield_QCD_CR if yield_QCD_CR != 0 else 0.

            # Transfer factor for photon category plots
            for i in range(4):
                if catSel and yield_QCD_CR != 0:
                    preSelectionSR_cat = "&&".join( [ cutInterpreter.cutString( "-".join([args.selection, pt, catSel+str(i)]) ), filterCutMc, isoleptonSelection, triggerCutMc, "overlapRemoval==1"  ] )
                    yield_QCD_SR_cat   = qcd.getYieldFromDraw(   selectionString=preSelectionSR_cat, weightString="weight*%f*%s"%(lumi_scale,weightString) )["val"]
                    yield_QCD_SR_cat  += gjets.getYieldFromDraw( selectionString=preSelectionSR_cat, weightString="weight*%f*%s"%(lumi_scale,weightString) )["val"]
                    transFacQCD[pt+"_cat"+str(i)] = yield_QCD_SR_cat / yield_QCD_CR
                else:
                    transFacQCD[pt+"_cat"+str(i)] = 0

    for plot in plots:
        qcdHist = copy.deepcopy(plot.histos[1][0])
        dataHist = copy.deepcopy(plot.histos[1][0])
        for h in plot.histos[0]:
            qcdHist.Add( h, -1 )

        if catSel:
            qcdHist_cat0 = copy.deepcopy(qcdHist)
            qcdHist_cat1 = copy.deepcopy(qcdHist)
            qcdHist_cat2 = copy.deepcopy(qcdHist)
            qcdHist_cat3 = copy.deepcopy(qcdHist)

        if "20ptG120" in plot.name:
            fac = "lowPT"
#            if "yield" in plot.name:
#                print fac, "data", dataHist.Integral(), "mc", sum([ h.Integral() for h in plot.histos[0]]), "data-mc", qcdHist.Integral(), "trans", transFacQCD[fac]
        elif "120ptG220" in plot.name:
            fac = "medPT"
#            if "yield" in plot.name:
#                print fac, "data", dataHist.Integral(), "mc", sum([ h.Integral() for h in plot.histos[0]]), "data-mc", qcdHist.Integral(), "trans", transFacQCD[fac]
        elif "220ptGinf" in plot.name:
            fac = "highPT"
#            if "yield" in plot.name:
#                print fac, "data", dataHist.Integral(), "mc", sum([ h.Integral() for h in plot.histos[0]]), "data-mc", qcdHist.Integral(), "trans", transFacQCD[fac]
        else:
            fac = "incl"
#            if "yield" in plot.name:
#                print fac, "data", dataHist.Integral(), "mc", sum([ h.Integral() for h in plot.histos[0]]), "data-mc", qcdHist.Integral(), "trans", transFacQCD[fac]

        qcdHist.Scale( transFacQCD[fac] )
        if catSel:
            qcdHist_cat0.Scale( transFacQCD[fac+"_cat0"] )
            qcdHist_cat1.Scale( transFacQCD[fac+"_cat1"] )
            qcdHist_cat2.Scale( transFacQCD[fac+"_cat2"] )
            qcdHist_cat3.Scale( transFacQCD[fac+"_cat3"] )

        cacheName = "_".join( ["qcdHisto", args.selection, plot.name, str(args.year), mode, "small" if args.small else "full"] + map( str, plot.binning ) )
        logger.info( "Adding QCD plot for %s for mode %s"%(plot.name, mode) )
        dirDB.add( cacheName, qcdHist, overwrite=True )
        if catSel:
            dirDB.add( cacheName.replace( args.selection, args.selection + "-" + catSel + "0" ), qcdHist_cat0, overwrite=True )
            dirDB.add( cacheName.replace( args.selection, args.selection + "-" + catSel + "1" ), qcdHist_cat1, overwrite=True )
            dirDB.add( cacheName.replace( args.selection, args.selection + "-" + catSel + "2" ), qcdHist_cat2, overwrite=True )
            dirDB.add( cacheName.replace( args.selection, args.selection + "-" + catSel + "3" ), qcdHist_cat3, overwrite=True )

