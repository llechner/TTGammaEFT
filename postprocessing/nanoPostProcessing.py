#!/usr/bin/env python

# standard imports
import ROOT
import sys
import os
import subprocess
import shutil
import uuid

from math                                        import sqrt
from operator                                    import mul

# RootTools
from RootTools.core.standard                     import *

# User specific
import TTGammaEFT.Tools.user as user

# Tools for systematics
from TTGammaEFT.Tools.helpers                    import checkRootFile, bestDRMatchInCollection
from TTGammaEFT.Tools.observables                import deltaR, deltaPhi, m3

from TTGammaEFT.Tools.objectSelection            import particlePtEtaSelection, deltaRCleaning, photonMediumIDSelector
from TTGammaEFT.Tools.objectSelection            import getLeptons, getGoodLeptons, getSortedParticles, getUnsortedParticles, getGoodParticles
from TTGammaEFT.Tools.objectSelection            import filterNonBJets, filterBJets, filterGenElectrons, filterGenMuons, filterGenPhotons, filterGenTops, filterGenBJets 
from TTGammaEFT.Tools.objectSelection            import jetSelector, muonSelector, eleSelector, photonSelector, genJetSelector, genLeptonSelector, genPhotonSelector

from TTGammaEFT.Tools.objectSelection            import nanoElectronVars, nanoMuonVars, nanoLeptonVars, nanoPhotonVars, nanoJetVars, nanoBJetVars, nanoGenVars, nanoGenJetVars
from TTGammaEFT.Tools.objectSelection            import nanoElectronVarString, nanoMuonVarString, nanoLeptonVarString, nanoPhotonVarString, nanoJetVarString, nanoGenVarString, nanoBJetVarString, nanoGenJetVarString
from TTGammaEFT.Tools.objectSelection            import nanoDataElectronVars, nanoDataMuonVars, nanoDataLeptonVars, nanoDataPhotonVars, nanoDataJetVars, nanoDataBJetVars
from TTGammaEFT.Tools.objectSelection            import nanoDataElectronVarString, nanoDataMuonVarString, nanoDataLeptonVarString, nanoDataPhotonVarString, nanoDataJetVarString, nanoDataBJetVarString

from TTGammaEFT.Tools.constants                  import defaultValue

from TTGammaEFT.Tools.overlapRemovalTTG          import photonFromTopDecay, hasMesonMother, getParentIds, isIsolatedPhoton, getPhotonCategory

from TTGammaEFT.Tools.WeightInfo                 import WeightInfo
from TTGammaEFT.Tools.HyperPoly                  import HyperPoly

from TTGammaEFT.Tools.puProfileCache             import puProfile

# central configuration
targetLumi = 1000 #pb-1 Which lumi to normalize to

logChoices      = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET', 'SYNC']

def get_parser():
    ''' Argument parser for post-processing module.
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for nanoPostProcessing")

    argParser.add_argument('--logLevel',                    action='store',         nargs='?',              choices=logChoices,     default='INFO',                     help="Log level for logging")
    argParser.add_argument('--overwrite',                   action='store_true',                                                                                        help="Overwrite existing output files, bool flag set to True  if used")
    argParser.add_argument('--samples',                     action='store',         nargs='*',  type=str,                           default=['WZTo3LNu'],               help="List of samples to be post-processed, given as CMG component name")
    argParser.add_argument('--eventsPerJob',                action='store',         nargs='?',  type=int,                           default=300000000,                  help="Maximum number of events per job (Approximate!).") # mul by 100
    argParser.add_argument('--nJobs',                       action='store',         nargs='?',  type=int,                           default=1,                          help="Maximum number of simultaneous jobs.")
    argParser.add_argument('--job',                         action='store',                     type=int,                           default=0,                          help="Run only job i")
    argParser.add_argument('--minNJobs',                    action='store',         nargs='?',  type=int,                           default=1,                          help="Minimum number of simultaneous jobs.")
    argParser.add_argument('--fileBasedSplitting',          action='store_true',                                                                                        help="Split njobs according to files")
    argParser.add_argument('--targetDir',                   action='store',         nargs='?',  type=str,                           default=user.postprocessing_output_directory, help="Name of the directory the post-processed files will be saved")
    argParser.add_argument('--processingEra',               action='store',         nargs='?',  type=str,                           default='TTGammaEFT_PP_v1',         help="Name of the processing era")
    argParser.add_argument('--skim',                        action='store',         nargs='?',  type=str,                           default='dilep',                    help="Skim conditions to be applied for post-processing")
    argParser.add_argument('--small',                       action='store_true',                                                                                        help="Run the file on a small sample (for test purpose), bool flag set to True if used")
    argParser.add_argument('--year',                        action='store',                     type=int,   choices=[2016,2017,2018],  required = True,                    help="Which year?")
    argParser.add_argument('--addReweights',                action='store_true',                                                                                        help="Add reweights for sample EFT reweighting?")
    argParser.add_argument('--interpolationOrder',          action='store',         nargs='?',  type=int,                           default=2,                          help="Interpolation order for EFT weights.")
    argParser.add_argument('--triggerSelection',            action='store_true',                                                                                        help="Trigger selection?" )
    argParser.add_argument('--addPreFiringFlag',            action='store_true',                                                                                        help="Add flag for events w/o prefiring?" )
    argParser.add_argument('--topReco',                     action='store_true',                                                                                        help="Run Top Reco?")

    return argParser

options = get_parser().parse_args()

# B-Tagger
tagger = 'DeepCSV'
#tagger = 'CSVv2'

# Logging
import TTGammaEFT.Tools.logger as logger
logFile = '/tmp/%s_%s_%s_njob%s.txt'%(options.skim, '_'.join(options.samples), os.environ['USER'], str(0 if options.nJobs==1 else options.job) )
logger  = logger.get_logger(options.logLevel, logFile = logFile)

import RootTools.core.logger as logger_rt
logger_rt = logger_rt.get_logger(options.logLevel, logFile = None )

import Samples.Tools.logger as logger_samples
logger_samples = logger_samples.get_logger(options.logLevel, logFile = None )

writeToDPM = options.targetDir == '/dpm/'

# Flags 
isDiLep   = options.skim.lower().startswith('dilep')
isSemiLep = options.skim.lower().startswith('semilep')

isPrivate = "private" in options.processingEra

#isInclusive = options.skim.lower().count('inclusive')
# Skim condition
skimConds = []
if isDiLep:
    skimConds.append( "(Sum$(Electron_pt>=15&&abs(Electron_eta)<2.5)+Sum$(Muon_pt>=15&&abs(Muon_eta)<2.5))>=2" )
elif isSemiLep:
    skimConds.append( "(Sum$(Electron_pt>=35&&abs(Electron_eta)<2.5)>=1)||(Sum$(Muon_pt>=30&&abs(Muon_eta)<2.5)>=1)" )
else:
    skimConds = ["(1)"]

#Samples: Load samples
maxNFiles = None
if options.small:
    maxNFiles = 1
    maxNEvents = 10
    options.job = 0
    options.nJobs = 1 # set high to just run over 1 input file

# Currently use MC private production CMSSW 10_2_9 and Data central production 2016/2017: CMSSW 10_2_9, 2018:CMSSW 10_2_5
if options.year == 2016:
    from Samples.nanoAOD.Summer16_private_legacy_v1 import *
    from Samples.nanoAOD.Run2016_14Dec2018          import *
elif options.year == 2017:
    from Samples.nanoAOD.Fall17_private_legacy_v1   import *
    from Samples.nanoAOD.Run2017_14Dec2018          import *
elif options.year == 2018:
    from Samples.nanoAOD.Autumn18_private_legacy_v1 import *
    from Samples.nanoAOD.Run2018_14Sep2018          import *

# Load all samples to be post processed
samples = map( eval, options.samples ) 
    
if len(samples)==0:
    logger.info( "No samples found. Was looking for %s. Exiting" % options.samples )
    sys.exit(-1)

isData = False not in [s.isData for s in samples]
isMC   = True not in [s.isData for s in samples]

# Check that all samples which are concatenated have the same x-section.
assert isData or len(set([s.xSection for s in samples]))==1, "Not all samples have the same xSection: %s !"%(",".join([s.name for s in samples]))
assert isMC or len(samples)==1, "Don't concatenate data samples"

#Samples: combine if more than one
if len(samples)>1:
    sample_name =  samples[0].name+"_comb"
    logger.info( "Combining samples %s to %s.", ",".join(s.name for s in samples), sample_name )
    sample = Sample.combine(sample_name, samples, maxN = maxNFiles)
    # Clean up
    for s in samples:
        sample.clear()
elif len(samples)==1:
    sample = samples[0]

if options.small:
    sample.reduceFiles( to = 1 )

# Cross section for postprocessed sample
xSection = samples[0].xSection if isMC else None

# Trigger selection
if isData and options.triggerSelection:
    from TTGammaEFT.Tools.TriggerSelector import TriggerSelector
    era         = options.samples[0].split( str(options.year) )[1].split("_")[0]
    Ts          = TriggerSelector( options.year, era, singleLepton = isSemiLep )
    triggerCond = Ts.getSelection( options.samples[0] if isData else "MC" )
    logger.info("Sample will have the following trigger skim: %s"%triggerCond)
    skimConds.append( triggerCond )

# Reweighting, Scalefactors, Efficiencies
from TTGammaEFT.Tools.LeptonSF import LeptonSF as LeptonSF_
LeptonSF = LeptonSF_( year=options.year )

from TTGammaEFT.Tools.LeptonTrackingEfficiency import LeptonTrackingEfficiency
LeptonTrackingSF = LeptonTrackingEfficiency( year=options.year )

from TTGammaEFT.Tools.PhotonSF import PhotonSF as PhotonSF_
PhotonSF = PhotonSF_( year=options.year )

from TTGammaEFT.Tools.PhotonReconstructionEfficiency import PhotonReconstructionEfficiency
PhotonRecEff = PhotonReconstructionEfficiency( year=options.year )

# Update to other years when available
from TTGammaEFT.Tools.PhotonElectronVetoEfficiency import PhotonElectronVetoEfficiency
PhotonElectronVetoSF = PhotonElectronVetoEfficiency()

from TTGammaEFT.Tools.TriggerEfficiency import TriggerEfficiency
TriggerEff_withBackup = TriggerEfficiency( with_backup_triggers = True,  year=options.year )
TriggerEff            = TriggerEfficiency( with_backup_triggers = False, year=options.year )

# Update to other years when available
from TTGammaEFT.Tools.BTagEfficiency import BTagEfficiency
BTagEff = BTagEfficiency( year=options.year, tagger=tagger ) # default medium WP

if isMC:
    from TTGammaEFT.Tools.puReweighting import getReweightingFunction
    if options.year == 2016:
        nTrueInt_puRW       = getReweightingFunction(data="PU_2016_35920_XSecCentral",  mc="Summer16")
        nTrueInt_puRWDown   = getReweightingFunction(data="PU_2016_35920_XSecDown",     mc="Summer16")
        nTrueInt_puRWUp     = getReweightingFunction(data="PU_2016_35920_XSecUp",       mc="Summer16")
        nTrueInt_puRWVDown  = getReweightingFunction(data="PU_2016_35920_XSecVDown",    mc="Summer16")
        nTrueInt_puRWVUp    = getReweightingFunction(data="PU_2016_35920_XSecVUp",      mc="Summer16")
    elif options.year == 2017:
        # messed up MC PU profiles
        puProfiles          = puProfile( source_sample = samples[0] )
        mcHist              = puProfiles.cachedTemplate( selection="( 1 )", weight='genWeight', overwrite=False ) # use genWeight for amc@NLO samples. No problems encountered so far
        nTrueInt_puRW       = getReweightingFunction(data="PU_2017_41860_XSecCentral",  mc=mcHist)
        nTrueInt_puRWDown   = getReweightingFunction(data="PU_2017_41860_XSecDown",     mc=mcHist)
        nTrueInt_puRWUp     = getReweightingFunction(data="PU_2017_41860_XSecUp",       mc=mcHist)
        nTrueInt_puRWVDown  = getReweightingFunction(data="PU_2017_41860_XSecVDown",    mc=mcHist)
        nTrueInt_puRWVUp    = getReweightingFunction(data="PU_2017_41860_XSecVUp",      mc=mcHist)
    elif options.year == 2018:
        nTrueInt_puRW       = getReweightingFunction(data="PU_2018_58830_XSecCentral",  mc="Autumn18")
        nTrueInt_puRWDown   = getReweightingFunction(data="PU_2018_58830_XSecDown",     mc="Autumn18")
        nTrueInt_puRWUp     = getReweightingFunction(data="PU_2018_58830_XSecUp",       mc="Autumn18")
        nTrueInt_puRWVDown  = getReweightingFunction(data="PU_2018_58830_XSecVDown",    mc="Autumn18")
        nTrueInt_puRWVUp    = getReweightingFunction(data="PU_2018_58830_XSecVUp",      mc="Autumn18")

# Single file post processing
if options.fileBasedSplitting:
    len_orig = len(sample.files)
    sample = sample.split( n=options.nJobs, nSub=options.job)
    if sample is None:  
        logger.info( "No such sample. nJobs %i, job %i numer of files %i", options.nJobs, options.job, len_orig )
        sys.exit(0)
    logger.info( "fileBasedSplitting: Run over %i/%i files for job %i/%i."%(len(sample.files), len_orig, options.job, options.nJobs))
    logger.debug( "fileBasedSplitting: Files to be run over:\n%s", "\n".join(sample.files) )

# output directory (store temporarily when running on dpm)
if writeToDPM:
    # Allow parallel processing of N threads on one worker
    directory = os.path.join( '/tmp/%s'%os.environ['USER'], str(uuid.uuid4()), options.processingEra )
    from TTGammaEFT.Tools.user import dpm_directory as user_dpm_directory
else:
    directory  = os.path.join( options.targetDir, options.processingEra ) 

postfix = '_small' if options.small else ''
output_directory = os.path.join( directory, options.skim+postfix, sample.name )

if os.path.exists( output_directory ) and options.overwrite:
    if options.nJobs > 1:
        logger.warning( "NOT removing directory %s because nJobs = %i", output_directory, options.nJobs )
    else:
        logger.info( "Output directory %s exists. Deleting.", output_directory )
        shutil.rmtree( output_directory, ignore_errors=True )

if not os.path.exists( output_directory ):
    try:
        os.makedirs( output_directory )
        logger.info( "Created output directory %s.", output_directory )
    except:
        logger.info( "Directory %s already exists.", output_directory )
        pass


#branches to be kept for data and MC
branchKeepStrings_DATAMC = [\
    "run", "luminosityBlock", "event",
    "PV_npvs", "PV_npvsGood",
    "MET_*",
    "Flag_*", "HLT_*",
#    "nJet", "Jet_*",
#    "nElectron", "Electron_*",
#    "nMuon", "Muon_*",
#    "nPhoton", "Photon_*",
    #"nTau", "Tau_*",
]

#branches to be kept for MC samples only
branchKeepStrings_MC = [\
    "Generator_*",
    "genWeight",
    "Pileup_nTrueInt",
    "GenPart_*", "nGenPart",
    "GenJet_*", "nGenJet",
    "Pileup_*",
    "LHE_*"
]

#branches to be kept for data only
branchKeepStrings_DATA = []

if sample.isData:
    lumiScaleFactor   = None
    branchKeepStrings = branchKeepStrings_DATAMC + branchKeepStrings_DATA
    from FWCore.PythonUtilities.LumiList import LumiList

    # Apply golden JSON
    if options.year == 2016:
        sample.json = '$CMSSW_BASE/src/TTGammaEFT/Tools/data/json/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt'
    elif options.year == 2017:
        sample.json = '$CMSSW_BASE/src/TTGammaEFT/Tools/data/json/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
    elif options.year == 2018:
        sample.json = '$CMSSW_BASE/src/TTGammaEFT/Tools/data/json/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'
    else:
        raise NotImplementedError

    lumiList = LumiList( os.path.expandvars( sample.json ) )
    logger.info( "Loaded json %s", sample.json )
else:
    lumiScaleFactor = xSection * targetLumi / float( sample.normalization ) if xSection is not None else None
    branchKeepStrings = branchKeepStrings_DATAMC + branchKeepStrings_MC

if sample.isData:
    nanoElectronVarString = nanoDataElectronVarString
    nanoMuonVarString     = nanoDataMuonVarString
    nanoLeptonVarString   = nanoDataLeptonVarString
    nanoJetVarString      = nanoDataJetVarString
    nanoBJetVarString     = nanoDataBJetVarString
    nanoPhotonVarString   = nanoDataPhotonVarString

    nanoElectronVars = nanoDataElectronVars
    nanoMuonVars     = nanoDataMuonVars
    nanoLeptonVars   = nanoDataLeptonVars
    nanoJetVars      = nanoDataJetVars
    nanoBJetVars     = nanoDataBJetVars
    nanoPhotonVars   = nanoDataPhotonVars

# change in the var naming for different years
if options.year != 2016:
    nanoPhotonVarString = nanoPhotonVarString.replace('cutBased','cutBasedBitmap')
    nanoPhotonVars      = [ item if item != 'cutBased' else 'cutBasedBitmap' for item in nanoPhotonVars ]

# Read Variables
read_variables  = map( TreeVariable.fromString, ['run/I', 'luminosityBlock/I', 'event/l'] )
read_variables += map( TreeVariable.fromString, ['MET_pt/F', 'MET_phi/F'] )
read_variables += [ TreeVariable.fromString('nElectron/I'),
                    VectorTreeVariable.fromString('Electron[%s]'%nanoElectronVarString) ]
read_variables += [ TreeVariable.fromString('nMuon/I'),
                    VectorTreeVariable.fromString('Muon[%s]'%nanoMuonVarString) ]
read_variables += [ TreeVariable.fromString('nPhoton/I'),
                    VectorTreeVariable.fromString('Photon[%s]'%nanoPhotonVarString) ]
read_variables += [ TreeVariable.fromString('nJet/I'),
                    VectorTreeVariable.fromString('Jet[%s]'%nanoJetVarString) ]
if isMC:
    read_variables += [ TreeVariable.fromString('genWeight/F') ]
    read_variables += [ TreeVariable.fromString('Pileup_nTrueInt/F') ]
    read_variables += [ TreeVariable.fromString('nGenPart/I'),
                        VectorTreeVariable.fromString('GenPart[%s]'%nanoGenVarString) ]
    read_variables += [ TreeVariable.fromString('nGenJet/I'),
                        VectorTreeVariable.fromString('GenJet[%s]'%nanoGenJetVarString) ]
    read_variables += [ TreeVariable.fromString('genWeight/F') ]

    nanoPhotonVarString += ',photonCat/I'

# Load reweight pickle file if supposed to keep weights. 
reweight_variables = []
if options.addReweights and isMC:

    # Determine coefficients for storing in vector
    # Sort Ids wrt to their position in the card file

    weightInfo = WeightInfo( sample.reweight_pkl )

    # weights for the ntuple
    rw_vector       = TreeVariable.fromString( "rw[w/F,"+",".join(w+'/F' for w in weightInfo.variables)+"]")
    rw_vector.nMax  = weightInfo.nid
    reweight_variables.append(rw_vector)

    # coefficients for the weight parametrization
    param_vector      = TreeVariable.fromString( "p[C/F]" )
    param_vector.nMax = HyperPoly.get_ndof(weightInfo.nvar, options.interpolationOrder)
    hyperPoly         = HyperPoly( options.interpolationOrder )
    reweight_variables.append(param_vector)
    reweight_variables.append(TreeVariable.fromString( "chi2_ndof/F"))

# Write Variables
new_variables  = reweight_variables
new_variables += [ 'weight/F', 'ref_weight/F' ]
new_variables += [ 'triggerDecision/I', 'isData/I']

# Jets
new_variables += [ 'nJet/I' ]
new_variables += [ 'nJetClean/I' ]
new_variables += [ 'nJetGood/I' ] 

new_variables += [ 'Jet[%s]'      %nanoJetVarString ]
new_variables += [ 'JetClean[%s]' %nanoJetVarString ]
new_variables += [ 'JetGood[%s]'  %nanoJetVarString ]

# BJets
new_variables += [ 'nBTag/I']
new_variables += [ 'nBTagClean/I']
new_variables += [ 'nBTagGood/I']

new_variables += [ 'Bj0_' + var for var in nanoBJetVarString.split(',') ]
new_variables += [ 'Bj1_' + var for var in nanoBJetVarString.split(',') ]

# Leptons
new_variables += [ 'nLepton/I' ] 
new_variables += [ 'nLeptonVeto/I']
new_variables += [ 'nLeptonGood/I' ] 
new_variables += [ 'nLeptonGoodLead/I' ] 
new_variables += [ 'nLeptonTight/I']

new_variables += [ 'nElectron/I', 'nMuon/I']
new_variables += [ 'nElectronVeto/I', 'nMuonVeto/I']
new_variables += [ 'nElectronGood/I', 'nMuonGood/I']
new_variables += [ 'nElectronGoodLead/I', 'nMuonGoodLead/I']
new_variables += [ 'nElectronTight/I', 'nMuonTight/I']

new_variables += [ 'Lepton[%s]'     %nanoLeptonVarString.replace('/b','/I') ]

new_variables += [ 'LeptonGood0_'  + var for var in nanoLeptonVarString.replace('/b','/I').split(',') ]
new_variables += [ 'LeptonGood1_'  + var for var in nanoLeptonVarString.replace('/b','/I').split(',') ]
new_variables += [ 'LeptonTight0_' + var for var in nanoLeptonVarString.replace('/b','/I').split(',') ]
new_variables += [ 'LeptonTight1_' + var for var in nanoLeptonVarString.replace('/b','/I').split(',') ]

# Photons
new_variables += [ 'nPhoton/I' ] 
new_variables += [ 'nPhotonGood/I' ] 
new_variables += [ 'Photon[%s]'     %nanoPhotonVarString.replace('/b','/I') ]

new_variables += [ 'PhotonGood0_'            + var for var in nanoPhotonVarString.replace('/b','/I').split(',') ]
new_variables += [ 'PhotonGood1_'            + var for var in nanoPhotonVarString.replace('/b','/I').split(',') ]
new_variables += [ 'PhotonNoChgIso0_'        + var for var in nanoPhotonVarString.replace('/b','/I').split(',') ]
new_variables += [ 'PhotonNoChgIsoNoSieie0_' + var for var in nanoPhotonVarString.replace('/b','/I').split(',') ]

# Others
new_variables += [ 'ht/F', 'METSig/F' ]
new_variables += [ 'photonJetdR/F', 'photonLepdR/F', 'leptonJetdR/F', 'tightLeptonJetdR/F' ] 
new_variables += [ 'MET_pt_photonEstimated/F', 'MET_phi_photonEstimated/F', 'METSig_photonEstimated/F' ]
new_variables += [ 'mll/F',  'mllgamma/F' ] 
new_variables += [ 'mlltight/F',  'mllgammatight/F' ] 
new_variables += [ 'm3/F',   'm3wBJet/F' ] 
new_variables += [ 'lldR/F', 'lldPhi/F' ] 
new_variables += [ 'bbdR/F', 'bbdPhi/F' ] 
new_variables += [ 'mLtight0Gamma/F',  'mL0Gamma/F',  'mL1Gamma/F' ] 
new_variables += [ 'l0GammadR/F',  'l0GammadPhi/F' ] 
new_variables += [ 'ltight0GammadR/F', 'ltight0GammadPhi/F' ] 
new_variables += [ 'l1GammadR/F',  'l1GammadPhi/F' ] 
new_variables += [ 'j0GammadR/F',  'j0GammadPhi/F' ] 
new_variables += [ 'j1GammadR/F',  'j1GammadPhi/F' ] 

if options.addPreFiringFlag: new_variables += [ 'unPreFirableEvent/I' ]

if isMC:
    new_variables += [ 'GenElectron[%s]' %nanoGenVarString ]
    new_variables += [ 'GenMuon[%s]'     %nanoGenVarString ]
    new_variables += [ 'GenPhoton[%s]'   %nanoGenVarString ]
    new_variables += [ 'GenJet[%s]'      %nanoGenJetVarString ]
    new_variables += [ 'GenBJet[%s]'     %nanoGenJetVarString ]
    new_variables += [ 'GenTop[%s]'      %nanoGenVarString ]
    new_variables += [ 'isTTGamma/I', 'isZWGamma/I', 'isSingleTopTch/I' ]

    new_variables += [ 'reweightPU/F', 'reweightPUDown/F', 'reweightPUUp/F', 'reweightPUVDown/F', 'reweightPUVUp/F' ]

    new_variables += [ 'reweightLeptonSF/F', 'reweightLeptonSFUp/F', 'reweightLeptonSFDown/F' ]
    new_variables += [ 'reweightLeptonTrackingSF/F' ]

    new_variables += [ 'reweightDilepTrigger/F', 'reweightDilepTriggerUp/F', 'reweightDilepTriggerDown/F' ]
    new_variables += [ 'reweightDilepTriggerBackup/F', 'reweightDilepTriggerBackupUp/F', 'reweightDilepTriggerBackupDown/F' ]

    new_variables += [ 'reweightPhotonSF/F', 'reweightPhotonSFUp/F', 'reweightPhotonSFDown/F' ]
    new_variables += [ 'reweightPhotonElectronVetoSF/F' ]
    new_variables += [ 'reweightPhotonReconstructionSF/F' ]

    # Btag weights Method 1a
    for var in BTagEff.btagWeightNames:
        if var!='MC':
            new_variables += [ 'reweightBTag_'+var+'/F' ]

# TopReco
if options.topReco:
    # Import the main top reco class
    from Analysis.TopReco.TopReco import topReco
    # Variables
    for name in [ "lp", "lm", "jetB", "jetBbar", "Wp", "Wm", "neutrino", "neutrinoBar", "top", "topBar" ]:
        for var in ["pt", "eta", "phi", "mass"]:
            new_variables.append( "topReco_"+name+"_"+var+'/F' )
    # Simple setter for top reco candidates
    def setParticle( event, name, particle ):
        setattr( event, "topReco_"+name+"_pt", particle.Pt() )
        setattr( event, "topReco_"+name+"_eta", particle.Eta() )
        setattr( event, "topReco_"+name+"_phi", particle.Phi() )
        setattr( event, "topReco_"+name+"_mass", particle.M() )

if isData:
    new_variables += ['jsonPassed/I']


# Read Prefiring File
unPreFirableEvents = []
allUnPreFirableEvents = []
if options.addPreFiringFlag: 
    preFiringFile = '$CMSSW_BASE/src/TTGammaEFT/postprocessing/L1Prefiring/UnprefirableEventList_SingleMuon_Run2017BtoF.root'
    f = ROOT.TFile.Open( preFiringFile )
    for event in f.tree:
        allUnPreFirableEvents.append( ( int(event.event), int(event.run), int(event.lumi) ) )
        unPreFirableEvents.append(    ( int(event.event), int(event.run) ) )

# Define a reader
reader = sample.treeReader( variables=read_variables, selectionString="&&".join(skimConds) )

# Calculate photonEstimated met
def getMetPhotonEstimated( met_pt, met_phi, photon ):
  met = ROOT.TLorentzVector()
  met.SetPtEtaPhiM(met_pt, 0, met_phi, 0 )
  gamma = ROOT.TLorentzVector()
  gamma.SetPtEtaPhiM(photon['pt'], photon['eta'], photon['phi'], photon['mass'] )
  metGamma = met + gamma
  return (metGamma.Pt(), metGamma.Phi())

def addMissingVariables( coll, vars ):
    for p in coll:
        for var_ in vars:
            var = var_.split("/")[0]
            if not var in p:
                p[var] = 0 if var_.endswith("/O") else defaultValue

# Replace unsign. char type with integer (only necessary for output electrons)
def convertUnits( coll ):
    for p in coll:
        if abs(p['pdgId'])==11 and isinstance( p['lostHits'], basestring ): p['lostHits']    = ord( p['lostHits'] )
        if abs(p['pdgId'])==13 and isinstance( p['pfIsoId'], basestring ):  p['pfIsoId']     = ord( p['pfIsoId'] )
        if isMC and isinstance( p['genPartFlav'], basestring ):             p['genPartFlav'] = ord( p['genPartFlav'] )

def get4DVec( part ):
  vec = ROOT.TLorentzVector()
  vec.SetPtEtaPhiM( part['pt'], part['eta'], part['phi'], 0 )
  return vec

def interpret_weight(weight_id):
    str_s = weight_id.split('_')
    res={}
    for i in range(len(str_s)/2):
        res[str_s[2*i]] = float(str_s[2*i+1].replace('m','-').replace('p','.'))
    return res

def fill_vector_collection( event, collection_name, collection_varnames, objects):
    setattr( event, "n"+collection_name, len(objects) )
    for i_obj, obj in enumerate(objects):
        for var in collection_varnames:
            getattr(event, collection_name+"_"+var)[i_obj] = obj[var]

def fill_vector( event, collection_name, collection_varnames, obj):
    for var in collection_varnames:
        setattr(event, collection_name+"_"+var, obj[var] )

def filler( event ):
    # shortcut
    r = reader.event

    event.isData = isData

    if options.addPreFiringFlag:
        event.unPreFirableEvent = ( int(r.event), int(r.run) ) in unPreFirableEvents

    if isMC:

        # weight
        event.weight = lumiScaleFactor*r.genWeight if lumiScaleFactor is not None else defaultValue

        # GEN Particles
        gPart = getUnsortedParticles( r, collVars=nanoGenVars, coll="GenPart" )
        # GEN Jets
        gJets = getSortedParticles( r, collVars=nanoGenJetVars, coll="GenJet" )

        # Overlap removal flags for ttgamma/ttbar and Zgamma/DY
        GenPhoton                  = filterGenPhotons( gPart, status='last' )
        GenIsoPhoton               = filter( lambda g: isIsolatedPhoton( g, gPart, coneSize=0.2,  ptCut=5, excludedPdgIds=[12,-12,14,-14,16,-16] ), GenPhoton    )
        GenIsoPhotonSingleT        = filter( lambda g: isIsolatedPhoton( g, gPart, coneSize=0.05, ptCut=5, excludedPdgIds=[12,-12,14,-14,16,-16] ), GenPhoton    )
        GenIsoPhotonNoMeson        = filter( lambda g: not hasMesonMother( getParentIds( g, gPart ) ), GenIsoPhoton )
        GenIsoPhotonNoMesonSingleT = filter( lambda g: not hasMesonMother( getParentIds( g, gPart ) ), GenIsoPhotonSingleT )
        GenIsoPhotonNoMesonSingleT = filter( lambda g: not photonFromTopDecay( getParentIds( g, gPart ) ), GenIsoPhotonNoMesonSingleT )

        event.isTTGamma      = len( getGoodParticles( genPhotonSelector( 'overlapTTGamma' ),      GenIsoPhotonNoMeson        ) ) > 0 
        event.isZWGamma      = len( getGoodParticles( genPhotonSelector( 'overlapZWGamma' ),      GenIsoPhotonNoMeson        ) ) > 0 
        event.isSingleTopTch = len( getGoodParticles( genPhotonSelector( 'overlapSingleTopTch' ), GenIsoPhotonNoMesonSingleT ) ) > 0 
     
        # Split gen particles
        GenElectron = getGoodParticles( genLeptonSelector(), filterGenElectrons( gPart, status='last' ) )
        GenMuon     = getGoodParticles( genLeptonSelector(), filterGenMuons( gPart, status='last' )     )
        GenPhoton   = getGoodParticles( genPhotonSelector(), GenPhoton                                  )
        GenTop      = getGoodParticles( genJetSelector(),    filterGenTops( gPart )                     )
        GenJet      = getGoodParticles( genJetSelector(),    gJets                                      )  
        GenBJet     = getGoodParticles( genJetSelector(),    filterGenBJets( gJets )                    )

        # Store
        if len(GenElectron) > 0: fill_vector_collection( event, "GenElectron", nanoGenVars,    GenElectron )
        if len(GenMuon) > 0:     fill_vector_collection( event, "GenMuon",     nanoGenVars,    GenMuon )
        if len(GenPhoton) > 0:   fill_vector_collection( event, "GenPhoton",   nanoGenVars,    GenPhoton )
        if len(GenBJet) > 0:     fill_vector_collection( event, "GenBJet",     nanoGenJetVars, GenBJet )
        if len(GenJet) > 0:      fill_vector_collection( event, "GenJet",      nanoGenJetVars, GenJet )
        if len(GenTop) > 0:      fill_vector_collection( event, "GenTop",      nanoGenVars,    GenTop )

        # EFT event weights
        if options.addReweights:
            event.nrw    = weightInfo.nid
            lhe_weights  = reader.products['lhe'].weights()
            weights      = []
            param_points = []
            for weight in lhe_weights:
                # Store nominal weight (First position!) 
                if weight.id == 'rwgt_1': event.rw_nominal = weight.wgt
                if not weight.id in weightInfo.id: continue
                pos = weightInfo.data[weight.id]
                event.rw_w[pos] = weight.wgt
                weights.append( weight.wgt )
                interpreted_weight = interpret_weight(weight.id)
                for var in weightInfo.variables:
                    getattr( event, "rw_"+var )[pos] = interpreted_weight[var]
                # weight data for interpolation
                if not hyperPoly.initialized:
                    param_points.append( tuple(interpreted_weight[var] for var in weightInfo.variables) )

            # get list of values of ref point in specific order
            ref_point_coordinates = [ weightInfo.ref_point_coordinates[var] for var in weightInfo.variables ]

            # Initialize with Reference Point
            if not hyperPoly.initialized: hyperPoly.initialize( param_points, ref_point_coordinates )
            coeff = hyperPoly.get_parametrization( weights )

            # = HyperPoly(weight_data, args.interpolationOrder)
            event.np = hyperPoly.ndof
            event.chi2_ndof = hyperPoly.chi2_ndof( coeff, weights )
            #logger.debug( "chi2_ndof %f coeff %r", event.chi2_ndof, coeff )
            if event.chi2_ndof>10**-6: logger.warning( "chi2_ndof is large: %f", event.chi2_ndof )
            for n in xrange( hyperPoly.ndof ):
                event.p_C[n] = coeff[n]

            event.ref_weight = event.weight / event.p_C[0]

    elif isData:
        event.weight     = 1.
        event.ref_weight = 1.
        # lumi lists and vetos
        event.jsonPassed  = lumiList.contains( r.run, r.luminosityBlock )
        # make data weight zero if JSON was not passed
        if not event.jsonPassed: event.weight = 0
        # store decision to use after filler has been executed
        event.jsonPassed_ = event.jsonPassed

    else:
        raise NotImplementedError( "isMC %r isData %r " % (isMC, isData) )

    # Leptons
    allElectrons = getSortedParticles( r, nanoElectronVars, coll="Electron" )
    allMuons     = getSortedParticles( r, nanoMuonVars,     coll="Muon" )

    addMissingVariables( allElectrons, nanoLeptonVarString.split(",") )
    addMissingVariables( allMuons,     nanoLeptonVarString.split(",") )
    convertUnits( allElectrons )
    convertUnits( allMuons )

    allLeptons = allElectrons + allMuons
    allLeptons.sort( key = lambda l: -l['pt'] )

    # Filter leptons
    vetoElectrons = getGoodParticles( eleSelector(  'veto' ), allElectrons )
    vetoMuons     = getGoodParticles( muonSelector( 'veto' ), allMuons )
    vetoLeptons   = vetoElectrons + vetoMuons
    vetoLeptons.sort( key = lambda l: -l['pt'] )

    mediumElectrons = getGoodParticles( eleSelector(  'medium' ), allElectrons )
    mediumMuons     = getGoodParticles( muonSelector( 'medium' ), allMuons )
    mediumLeptons   = mediumElectrons + mediumMuons
    mediumLeptons.sort( key = lambda l: -l['pt'] )

    mediumLeadingElectrons = getGoodParticles( eleSelector(  'medium', leading=True ), mediumElectrons )
    mediumLeadingMuons     = getGoodParticles( muonSelector( 'medium', leading=True ), mediumMuons )
    mediumLeadingLeptons   = mediumLeadingElectrons + mediumLeadingMuons
    mediumLeadingLeptons.sort( key = lambda l: -l['pt'] )

    tightElectrons = getGoodParticles( eleSelector(  'tight' ), allElectrons )
    tightMuons     = getGoodParticles( muonSelector( 'tight' ), allMuons )
    tightLeptons   = tightElectrons + tightMuons
    tightLeptons.sort( key = lambda l: -l['pt'] )

    # Leptons for allJets deltaR cleaning
    cleanElectrons = getGoodParticles( eleSelector(  'veto', noPtEtaCut=True ), allElectrons )
    cleanMuons     = getGoodParticles( muonSelector( 'veto', noPtEtaCut=True ), allMuons )
    cleanLeptons   = cleanElectrons + cleanMuons
    cleanLeptons.sort( key = lambda l: -l['pt'] )

    # Select one tight and one medium lepton, the tight is included in the medium collection
    selectedLeptons = mediumLeptons[:2]
    selectedTightLepton = tightLeptons[:1]

    # Store lepton number
    event.nLepton           = len(allLeptons)
    event.nElectron         = len(allElectrons)
    event.nMuon             = len(allMuons)

    event.nLeptonVeto       = len(vetoLeptons)         
    event.nElectronVeto     = len(vetoElectrons)
    event.nMuonVeto         = len(vetoMuons)

    event.nLeptonGood       = len(mediumLeptons)
    event.nElectronGood     = len(mediumElectrons)
    event.nMuonGood         = len(mediumMuons)

    event.nLeptonGoodLead   = len(mediumLeadingLeptons)
    event.nElectronGoodLead = len(mediumLeadingElectrons)
    event.nMuonGoodLead     = len(mediumLeadingMuons)

    event.nLeptonTight      = len(tightLeptons)
    event.nElectronTight    = len(tightElectrons)
    event.nMuonTight        = len(tightMuons)

    # Store analysis Leptons
    l0, l1   = ( selectedLeptons + [None, None] )[:2]
    lt0, lt1 = ( tightLeptons + [None, None] )[:2]
    # Dileptonic analysis
    if l0:  fill_vector( event, "LeptonGood0",  nanoLeptonVars, l0 )
    if l1:  fill_vector( event, "LeptonGood1",  nanoLeptonVars, l1 )
    # Semi-leptonic analysis
    if lt0: fill_vector( event, "LeptonTight0", nanoLeptonVars, lt0 )
    if lt1: fill_vector( event, "LeptonTight1", nanoLeptonVars, lt1 )

    # Store all Leptons
    fill_vector_collection( event, "Lepton",     nanoLeptonVars, allLeptons )

    # Photons
    allPhotons = getSortedParticles( r, nanoPhotonVars, coll="Photon" )
    convertUnits( allPhotons )

    cleanPhotons                 = getGoodParticles( photonSelector( 'loose',  year=options.year, noPtEtaCut=True ),                         allPhotons )
    mediumPhotons                = getGoodParticles( photonSelector( 'medium', year=options.year ),                                          allPhotons )
    mediumPhotonsNoChgIso        = getGoodParticles( photonSelector( 'medium', year=options.year, removedCuts=["pfRelIso03_chg"] ),          allPhotons )
    mediumPhotonsNoChgIsoNoSieie = getGoodParticles( photonSelector( 'medium', year=options.year, removedCuts=["sieie", "pfRelIso03_chg"] ), allPhotons )

    # DeltaR cleaning
    cleanPhotons                 = deltaRCleaning( cleanPhotons,                 cleanLeptons,                                        dRCut=0.1 )
    mediumPhotons                = deltaRCleaning( mediumPhotons,                selectedLeptons if isDiLep else selectedTightLepton, dRCut=0.1 )
    mediumPhotonsNoChgIso        = deltaRCleaning( mediumPhotonsNoChgIso,        selectedLeptons if isDiLep else selectedTightLepton, dRCut=0.1 )
    mediumPhotonsNoChgIsoNoSieie = deltaRCleaning( mediumPhotonsNoChgIsoNoSieie, selectedLeptons if isDiLep else selectedTightLepton, dRCut=0.1 )

    # Photons are stored later in this script

    # Jets
    allJets = getSortedParticles( r, collVars=nanoJetVars, coll="Jet" )

    if isMC:
        for j in allJets: BTagEff.addBTagEffToJet( j )

    # Loose jets w/o pt/eta requirement
    allJets   = getGoodParticles( jetSelector( options.year, noPtEtaCut=True  ), allJets )
    # Loose jets w/ pt/eta requirement (analysis jets)
    looseJets = getGoodParticles( jetSelector( options.year, noPtEtaCut=False ), allJets )

    # DeltaR cleaning
    cleanJets = deltaRCleaning( allJets,   cleanLeptons,  dRCut=0.4 ) # clean all jets against a very loose lepton selection
    cleanJets = deltaRCleaning( cleanJets, cleanPhotons,  dRCut=0.1 ) # clean all jets against a very loose photon selection
    looseJets = deltaRCleaning( looseJets, selectedLeptons if isDiLep else selectedTightLepton, dRCut=0.4 ) # clean all jets against analysis leptons
    looseJets = deltaRCleaning( looseJets, mediumPhotons, dRCut=0.1 ) # clean all jets against analysis photons
    
    # Store jets
    event.nJet      = len(allJets)
    event.nJetClean = len(cleanJets)
    event.nJetGood  = len(looseJets)

    # store all loose jets
    fill_vector_collection( event, "Jet",      nanoJetVars, allJets )
    # store all loose jets, cleaned against vetoLeptons and loose photons
    fill_vector_collection( event, "JetClean", nanoJetVars, cleanJets )
    # store analysis jets
    fill_vector_collection( event, "JetGood",  nanoJetVars, looseJets )

    # bJets
    allBJets   = filterBJets( allJets,   tagger=tagger, year=options.year )
    cleanBJets = filterBJets( cleanJets, tagger=tagger, year=options.year )

    looseBJets    = filterBJets(    looseJets, tagger=tagger, year=options.year )
    looseNonBJets = filterNonBJets( looseJets, tagger=tagger, year=options.year )

    # Store bJets
    bj0, bj1 = ( list(looseBJets) + [None, None] )[:2]
    if bj0: fill_vector( event, "Bj0", nanoBJetVars, bj0 )
    if bj1: fill_vector( event, "Bj1", nanoBJetVars, bj1 )

    event.nBTag      = len(allBJets)
    event.nBTagClean = len(cleanBJets)
    event.nBTagGood  = len(looseBJets)

    # Additional observables
    event.m3          = m3( looseJets )[0]
    event.m3wBJet     = m3( looseJets, nBJets=1, tagger=tagger, year=options.year )[0]

    event.ht          = sum( [ j['pt'] for j in looseJets ] )
    event.METSig      = r.MET_pt / sqrt( event.ht ) if event.ht > 0 else defaultValue

    if isMC:
        # match photon with gen-particle and get its photon category -> reco Photon categorization
        for g in mediumPhotonsNoChgIsoNoSieie[:1] + mediumPhotonsNoChgIso[:1]:
            genMatch = filter( lambda p: p['index'] == g['genPartIdx'], gPart )[0] if g['genPartIdx'] > 0 and isMC else None
            g['photonCat'] = getPhotonCategory( genMatch, gPart )

    # variables w/ photons
    if len(mediumPhotons) > 0:

        if isMC:
            # match photon with gen-particle and get its photon category -> reco Photon categorization
            for g in mediumPhotons:
                genMatch = filter( lambda p: p['index'] == g['genPartIdx'], gPart )[0] if g['genPartIdx'] > 0 and isMC else None
                g['photonCat'] = getPhotonCategory( genMatch, gPart )

        # additional observables
        event.MET_pt_photonEstimated, event.MET_phi_photonEstimated = getMetPhotonEstimated( r.MET_pt, r.MET_phi, mediumPhotons[0] )

        if event.ht > 0:     event.METSig_photonEstimated     = event.MET_pt_photonEstimated / sqrt( event.ht )

        if looseJets:        event.photonJetdR                = min( deltaR( p, j ) for j in looseJets       for p in mediumPhotons )
        if selectedLeptons:  event.photonLepdR                = min( deltaR( p, l ) for l in selectedLeptons for p in mediumPhotons )

        if len(tightLeptons) > 0:
            event.ltight0GammadPhi = deltaPhi( tightLeptons[0]['phi'], mediumPhotons[0]['phi'] )
            event.ltight0GammadR   = deltaR(   tightLeptons[0],        mediumPhotons[0] )
            event.mLtight0Gamma    = ( get4DVec(tightLeptons[0]) + get4DVec(mediumPhotons[0]) ).M()

        if len(selectedLeptons) > 0:
            event.l0GammadPhi = deltaPhi( selectedLeptons[0]['phi'], mediumPhotons[0]['phi'] )
            event.l0GammadR   = deltaR(   selectedLeptons[0],        mediumPhotons[0] )
            event.mL0Gamma    = ( get4DVec(selectedLeptons[0]) + get4DVec(mediumPhotons[0]) ).M()

        if len(selectedLeptons) > 1:
            event.l1GammadPhi = deltaPhi( selectedLeptons[1]['phi'], mediumPhotons[0]['phi'] )
            event.l1GammadR   = deltaR(   selectedLeptons[1],        mediumPhotons[0] )
            event.mL1Gamma    = ( get4DVec(selectedLeptons[1]) + get4DVec(mediumPhotons[0]) ).M()

        if len(looseJets) > 0:
            event.j0GammadPhi = deltaPhi( looseJets[0]['phi'], mediumPhotons[0]['phi'] )
            event.j0GammadR   = deltaR(   looseJets[0],        mediumPhotons[0] )

        if len(looseJets) > 1:
            event.j1GammadPhi = deltaPhi( looseJets[1]['phi'], mediumPhotons[0]['phi'] )
            event.j1GammadR   = deltaR(   looseJets[1],        mediumPhotons[0] )

    event.nPhoton      = len( allPhotons )
    event.nPhotonGood  = len( mediumPhotons )

    # store all photons
    fill_vector_collection( event, "Photon",      nanoPhotonVars, allPhotons )

    # Store analysis photons
    p0, p1 = ( mediumPhotons + [None, None] )[:2]
    if p0: fill_vector( event, "PhotonGood0",  nanoPhotonVars + ['photonCat'] if isMC else nanoPhotonVars, p0 )
    if p1: fill_vector( event, "PhotonGood1",  nanoPhotonVars + ['photonCat'] if isMC else nanoPhotonVars, p1 )

    p0NoChgNoSieie = ( mediumPhotonsNoChgIsoNoSieie + [None] )[0]
    if p0NoChgNoSieie: fill_vector( event, "PhotonNoChgIsoNoSieie0",  nanoPhotonVars + ['photonCat'] if isMC else nanoPhotonVars, p0NoChgNoSieie )

    p0NoChg = ( mediumPhotonsNoChgIso + [None] )[0]
    if p0NoChg: fill_vector( event, "PhotonNoChgIso0",  nanoPhotonVars + ['photonCat'] if isMC else nanoPhotonVars, p0NoChg )

    if bj1:
        event.bbdR   = deltaR( bj0, bj1 )
        event.bbdPhi = deltaPhi( bj0['phi'], bj1['phi'] )

    if len(tightLeptons) > 1:
        event.lldRtight   = deltaR( tightLeptons[0], tightLeptons[1] )
        event.lldPhitight = deltaPhi( tightLeptons[0]['phi'], tightLeptons[1]['phi'] )
        event.mlltight    = ( get4DVec(tightLeptons[0]) + get4DVec(tightLeptons[1]) ).M()

        if len(mediumPhotons) > 0:
            event.mllgammatight = ( get4DVec(tightLeptons[0]) + get4DVec(tightLeptons[1]) + get4DVec(mediumPhotons[0]) ).M()

    if len(looseJets) > 0 and len(tightLeptons) > 0:
        event.tightLeptonJetdR = min( deltaR( tightLeptons[0], j ) for j in looseJets )

    if len(selectedLeptons) > 1:
        event.lldR   = deltaR( selectedLeptons[0], selectedLeptons[1] )
        event.lldPhi = deltaPhi( selectedLeptons[0]['phi'], selectedLeptons[1]['phi'] )
        event.mll    = ( get4DVec(selectedLeptons[0]) + get4DVec(selectedLeptons[1]) ).M()

        if len(mediumPhotons) > 0:
            event.mllgamma = ( get4DVec(selectedLeptons[0]) + get4DVec(selectedLeptons[1]) + get4DVec(mediumPhotons[0]) ).M()

    if len(looseJets) > 0 and len(selectedLeptons) > 0:
        event.leptonJetdR = min( deltaR( l, j ) for j in looseJets for l in selectedLeptons )

    # Topreco
    if options.topReco:
        #topReco = TopReco( ROOT.Era.run2_13tev_2016_25ns, 2, 1, 0, 'btagDeepB', 0.6321 )
        solution = topReco.evaluate( selectedLeptons, looseJets, met = {'pt':r.MET_pt, 'phi':r.MET_phi})
        if solution:
            print "t/tbar:", selectedLeptons[0]['pt'], r.MET_pt,r.MET_phi, solution.top.Pt(), solution.topBar.Pt()

            event.topReco_nBTag   = solution.ntags
            event.topReco_weight  = solution.weight
            event.topReco_recMtop = solution.recMtop
            event.topReco_met_pt  = solution.met.Pt()
            event.topReco_met_phi = solution.met.Phi()
            
            setParticle(event, "lp",        solution.lp) 
            setParticle(event, "lm",        solution.lm) 
            setParticle(event, "jetB",      solution.jetB) 
            setParticle(event, "jetBbar",   solution.jetBbar) 
            setParticle(event, "Wp",        solution.Wplus) 
            setParticle(event, "Wm",        solution.Wminus) 
            setParticle(event, "neutrino",       solution.neutrino) 
            setParticle(event, "neutrinoBar",    solution.neutrinoBar) 
            setParticle(event, "top",       solution.top) 
            setParticle(event, "topBar",    solution.topBar) 

    # Reweighting
    if isMC:
        # PU reweighting
        event.reweightPU      = nTrueInt_puRW      ( r.Pileup_nTrueInt )
        event.reweightPUDown  = nTrueInt_puRWDown  ( r.Pileup_nTrueInt )
        event.reweightPUUp    = nTrueInt_puRWUp    ( r.Pileup_nTrueInt )
        event.reweightPUVDown = nTrueInt_puRWVDown ( r.Pileup_nTrueInt )
        event.reweightPUVUp   = nTrueInt_puRWVUp   ( r.Pileup_nTrueInt )

        # Lepton reweighting
        event.reweightLeptonSF     = reduce( mul, [ LeptonSF.getSF( pdgId=l['pdgId'], pt=l['pt'], eta=((l['eta']+l['deltaEtaSC']) if abs(l['pdgId'])==11 else l['eta'])             ) for l in selectedLeptons ], 1 )
        event.reweightLeptonSFUp   = reduce( mul, [ LeptonSF.getSF( pdgId=l['pdgId'], pt=l['pt'], eta=((l['eta']+l['deltaEtaSC']) if abs(l['pdgId'])==11 else l['eta']), sigma = +1 ) for l in selectedLeptons ], 1 )
        event.reweightLeptonSFDown = reduce( mul, [ LeptonSF.getSF( pdgId=l['pdgId'], pt=l['pt'], eta=((l['eta']+l['deltaEtaSC']) if abs(l['pdgId'])==11 else l['eta']), sigma = -1 ) for l in selectedLeptons ], 1 )

        event.reweightLeptonTrackingSF = reduce( mul, [ LeptonTrackingSF.getSF( pdgId=l['pdgId'], pt=l['pt'], eta=((l['eta']+l['deltaEtaSC']) if abs(l['pdgId'])==11 else l['eta']) ) for l in selectedLeptons ], 1 )

        # Photon reweighting
        event.reweightPhotonSF     = reduce( mul, [ PhotonSF.getSF( pt=p['pt'], eta=p['eta']             ) for p in mediumPhotons ], 1 )
        event.reweightPhotonSFUp   = reduce( mul, [ PhotonSF.getSF( pt=p['pt'], eta=p['eta'], sigma = +1 ) for p in mediumPhotons ], 1 )
        event.reweightPhotonSFDown = reduce( mul, [ PhotonSF.getSF( pt=p['pt'], eta=p['eta'], sigma = -1 ) for p in mediumPhotons ], 1 )

        event.reweightPhotonElectronVetoSF   = reduce( mul, [ PhotonElectronVetoSF.getSF( pt=p['pt'], eta=p['eta'] ) for p in mediumPhotons ], 1 )
        event.reweightPhotonReconstructionSF = reduce( mul, [ PhotonRecEff.getSF( pt=p['pt'], eta=p['eta'] )         for p in mediumPhotons ], 1 )

        # B-Tagging efficiency method 1a
        for var in BTagEff.btagWeightNames:
            if var!='MC': setattr( event, 'reweightBTag_'+var, BTagEff.getBTagSF_1a( var, looseBJets, looseNonBJets ) )

        if len(selectedLeptons) > 1:
            # Trigger reweighting
            trig_eff, trig_eff_err         = TriggerEff.getSF( selectedLeptons[0], selectedLeptons[1] )
            event.reweightDilepTrigger     = trig_eff
            event.reweightDilepTriggerUp   = trig_eff + trig_eff_err
            event.reweightDilepTriggerDown = trig_eff - trig_eff_err

            trig_eff, trig_eff_err               = TriggerEff_withBackup.getSF( selectedLeptons[0], selectedLeptons[1] )
            event.reweightDilepTriggerBackup     = trig_eff
            event.reweightDilepTriggerBackupUp   = trig_eff + trig_eff_err
            event.reweightDilepTriggerBackupDown = trig_eff - trig_eff_err

        else:
            event.reweightDilepTrigger     = 0
            event.reweightDilepTriggerUp   = 0
            event.reweightDilepTriggerDown = 0
            
            event.reweightDilepTriggerBackup     = 0
            event.reweightDilepTriggerBackupUp   = 0
            event.reweightDilepTriggerBackupDown = 0

# Create a maker. Maker class will be compiled. This instance will be used as a parent in the loop
treeMaker_parent = TreeMaker(
    sequence  = [ filler ],
    variables = [ TreeVariable.fromString(x) for x in new_variables ],
    treeName = "Events"
    )

# Split input in ranges
if options.nJobs>1 and not options.fileBasedSplitting:
    eventRanges = reader.getEventRanges( nJobs = options.nJobs )
else:
    eventRanges = reader.getEventRanges( maxNEvents = options.eventsPerJob, minJobs = options.minNJobs )

logger.info( "Splitting into %i ranges of %i events on average. FileBasedSplitting: %s. Job number %s",  
        len(eventRanges), 
        (eventRanges[-1][1] - eventRanges[0][0])/len(eventRanges), 
        'Yes' if options.fileBasedSplitting else 'No',
        options.job)
#Define all jobs
jobs = [ (i, range) for i, range in enumerate( eventRanges ) ]

#assert False, ""

filename, ext = os.path.splitext( os.path.join( output_directory, sample.name + '.root' ) )

if options.fileBasedSplitting and len(eventRanges)>1:
    raise RuntimeError("Using fileBasedSplitting but have more than one event range!")

clonedEvents = 0
convertedEvents = 0
outputLumiList = {}

for ievtRange, eventRange in enumerate( eventRanges ):

    if not options.fileBasedSplitting and options.nJobs>1:
        if ievtRange != options.job: continue

    logger.info( "Processing range %i/%i from %i to %i which are %i events.",  ievtRange, len(eventRanges), eventRange[0], eventRange[1], eventRange[1]-eventRange[0] )

    # Check whether file exists
    fileNumber = options.job if options.job is not None else 0
    outfilename = filename+'_'+str(fileNumber)+ext
    if os.path.isfile(outfilename):
        logger.info( "Output file %s found.", outfilename)
        if not checkRootFile(outfilename, checkForObjects=["Events"]):
            logger.info( "File %s is broken. Overwriting.", outfilename)
        elif not options.overwrite:
            logger.info( "Skipping.")
            continue
        else:
            logger.info( "Overwriting.")

    tmp_directory = ROOT.gDirectory
    outputfile = ROOT.TFile.Open(outfilename, 'recreate')
    tmp_directory.cd()

    if options.small: 
        logger.info("Running 'small'. Not more than 10000 events") 
        numEvents  = eventRange[1] - eventRange[0]
        eventRange = ( eventRange[0], eventRange[0] +  min( [ numEvents, maxNEvents ] ) )
        print eventRange[0], numEvents, maxNEvents

    # Set the reader to the event range
    reader.setEventRange( eventRange )

    # Clone the empty maker in order to avoid recompilation at every loop iteration
    clonedTree    = reader.cloneTree( branchKeepStrings, newTreename = "Events", rootfile = outputfile )
    clonedEvents += clonedTree.GetEntries()
    maker = treeMaker_parent.cloneWithoutCompile( externalTree=clonedTree )

    maker.start()
    # Do the thing
    reader.start()

    while reader.run():
        maker.run()
        if isData and maker.event.jsonPassed_:
            if reader.event.run not in outputLumiList.keys():
                outputLumiList[reader.event.run] = set( [ reader.event.luminosityBlock ] )
            else:
                if reader.event.luminosityBlock not in outputLumiList[reader.event.run]:
                    outputLumiList[reader.event.run].add(reader.event.luminosityBlock)

    convertedEvents += maker.tree.GetEntries()
    maker.tree.Write()
    outputfile.Close()
    logger.info( "Written %s", outfilename)

    # Destroy the TTree
    maker.clear()
    
logger.info( "Converted %i events of %i, cloned %i",  convertedEvents, reader.nEvents , clonedEvents )

# Storing JSON file of processed events
if isData:
    jsonFile = filename + '_%s.json' %( 0 if options.nJobs==1 else options.job )
    LumiList( runsAndLumis = outputLumiList ).writeJSON( jsonFile )
    logger.info( "Written JSON file %s",  jsonFile )

logger.info( "Copying log file to %s", output_directory )
copyLog = subprocess.call( [ 'cp', logFile, output_directory ] )
if copyLog:
    logger.info( "Copying log from %s to %s failed", logFile, output_directory )
else:
    logger.info( "Successfully copied log file" )
    os.remove( logFile )
    logger.info( "Removed temporary log file" )

if writeToDPM:
    for dirname, subdirs, files in os.walk( directory ):
        logger.debug( 'Found directory: %s',  dirname )
        for fname in files:
            source  = os.path.abspath( os.path.join( dirname, fname ) )
            postfix = '_small' if options.small else ''
            cmd     = [ 'xrdcp', source, 'root://hephyse.oeaw.ac.at/%s' % os.path.join( user_dpm_directory, 'postprocessed',  options.processingEra + postfix, options.skim, sample.name, fname ) ]
            logger.info( "Issue copy command: %s", " ".join( cmd ) )
            subprocess.call( cmd )

    # Clean up.
    subprocess.call( [ 'rm', '-rf', directory ] ) # Let's risk it.

