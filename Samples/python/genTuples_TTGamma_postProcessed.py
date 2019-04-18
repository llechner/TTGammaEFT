# Standard Imports
import os, sys
import ROOT

# RootTools Imports
from RootTools.core.Sample import Sample

# Logging
if __name__=="__main__":
    import Analysis.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
else:
    import logging
    logger = logging.getLogger(__name__)

# Colors
from TTGammaEFT.Samples.color import color

# Data directory
from TTGammaEFT.Tools.user import gridpack_directory
from TTGammaEFT.Tools.user import data_directory3             as data_directory
from TTGammaEFT.Tools.user import postprocessing_directoryGEN as postprocessing_directory

logger.info( "Loading MC samples from directory %s", os.path.join( data_directory, postprocessing_directory ) )

# Directories
dirs = {}

dirs['TTG_SingleLeptFromT_1L_test_SM']           = [ "TTGamma_SingleLeptFromT_SM_1Line_test" ]
dirs['TTG_SingleLeptFromT_3LBuggy_test_SM']      = [ "TTGamma_SingleLeptFromT_SM_3LineBuggy_test" ]
dirs['TTG_SingleLeptFromT_3LPatched_test_SM']    = [ "TTGamma_SingleLeptFromT_SM_3LinePatched_test" ]

dirs['TTG_SingleLeptFromT_1L_SM']                = [ "TTGamma_SingleLeptFromT_SM_1Line" ]
dirs['TTG_SingleLeptFromT_3LinePatched_SM']      = [ "TTGamma_SingleLeptFromT_SM_3LinePatched" ]

dirs['TTG_SingleLeptFromT_1L_test_EFT']          = [ "TTGamma_SingleLeptFromT_EFT_1Line_test" ]
dirs['TTGamma_DiLept_EFT_1Line_small']           = [ "TTGamma_DiLept_EFT_1Line_small" ]
dirs['TTGamma_DiLept_EFT_1Line']                 = [ "TTGamma_DiLept_EFT_1Line" ]

dirs['ttGamma_SingleLeptFromT_SM_1Line']         = [ "ttGamma_SingleLeptFromT_SM_1Line" ]
dirs['ttGamma_SingleLeptFromTbar_SM_1Line']      = [ "ttGamma_SingleLeptFromTbar_SM_1Line" ]

dirs['ttGamma_SingleLeptFromT_SM_central']       = [ "ttGamma_SingleLeptFromT_SM_central" ]
dirs['ttGamma_SingleLeptFromTbar_SM_central']    = [ "ttGamma_SingleLeptFromTbar_SM_central" ]
dirs['ttGamma_Dilept_SM_central']                = [ "ttGamma_Dilept_SM_central" ]
dirs['ttGamma_Hadronic_SM_central']              = [ "ttGamma_Hadronic_SM_central" ]

dirs['ttGamma_NoFullyHad_SM_CMSrunCard']          = [ "ttGamma_NoFullyHad_SM_CMSrunCard" ]
dirs['ttGamma_NoFullyHad_SM_CMSrunCard_small']    = [ "ttGamma_NoFullyHad_SM_CMSrunCard_small" ]
dirs['ttGamma_NoFullyHad_SM_ATLASrunCard']        = [ "ttGamma_NoFullyHad_SM_ATLASrunCard" ]
dirs['ttGamma_NoFullyHad_SM_ATLASrunCard_small']  = [ "ttGamma_NoFullyHad_SM_ATLASrunCard_small" ]
dirs['ttGamma_NoFullyHad_SM_CMSrunCard_noDeltaR'] = [ "ttGamma_NoFullyHad_SM_CMSrunCard_noDeltaR" ]

dirs['ttGamma_NoFullyHad_SM_CMSrunCard_xqcut'] = [ "ttGamma_NoFullyHad_SM_CMSrunCard_xqcut" ]
dirs['ttGamma_NoFullyHad_SM_CMSrunCard_noJetPtCut'] = [ "ttGamma_NoFullyHad_SM_CMSrunCard_noJetPtCut" ]
dirs['ttGamma_NoFullyHad_SM_CMSrunCard_noDeltaR_xqcut'] = [ "ttGamma_NoFullyHad_SM_CMSrunCard_noDeltaR_xqcut" ]
dirs['ttGamma_NoFullyHad_SM_CMSrunCard_xqcut'] = [ "ttGamma_NoFullyHad_SM_CMSrunCard_xqcut" ]
#dirs['ttGamma_NoFullyHad_SM_CMSrunCard_noDeltaR_noJetPtCut'] = [ "ttGamma_NoFullyHad_SM_CMSrunCard_noDeltaR_noJetPtCut" ]

dirs["ttGamma_NoFullyHad_SM_CMSrunCard_noDeltaR_noJetPtCut_xqcut"] = [ "ttGamma_NoFullyHad_SM_CMSrunCard_noDeltaR_noJetPtCut_xqcut" ]
dirs["ttGamma_NoFullyHad_SM_CMSrunCard_noJetPtCut_xqcut"] = [ "ttGamma_NoFullyHad_SM_CMSrunCard_noJetPtCut_xqcut" ]
dirs["ttGamma_NoFullyHad_SM_CMSrunCard_noDeltaR_noJetPtCut_xqcut_wideLepEta"] = [ "ttGamma_NoFullyHad_SM_CMSrunCard_noDeltaR_noJetPtCut_xqcut_wideLepEta" ]

directories = { key : [ os.path.join( data_directory, postprocessing_directory, dir) for dir in dirs[key] ] for key in dirs.keys() }

# Samples
#TTG_SingleLeptFromT_1L_test_SM                     = Sample.fromDirectory(name="TTG_SingleLeptFromT_1Line",        treeName="Events", isData=False, color=color.TTG1L,        texName="tt#gamma (1L)",         directory=directories['TTG_SingleLeptFromT_1L_test_SM'])
#TTG_SingleLeptFromT_1L_test_SM.reweight_pkl        = os.path.join( gridpack_directory, "SM/TTGamma_SingleLeptFromT_1Line_test/", "TTGamma_SingleLeptFromT_1Line_test_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )

#TTG_SingleLeptFromT_3LBuggy_test_SM                = Sample.fromDirectory(name="TTG_SingleLeptFromT_3LineBuggy",   treeName="Events", isData=False, color=color.TTG3LBuggy,   texName="tt#gamma (3L buggy)",   directory=directories['TTG_SingleLeptFromT_3LBuggy_test_SM'])
#TTG_SingleLeptFromT_3LBuggy_test_SM.reweight_pkl   = os.path.join( gridpack_directory, "SM/TTGamma_SingleLeptFromT_3LineBuggy_test/", "TTGamma_SingleLeptFromT_3LineBuggy_test_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )

#TTG_SingleLeptFromT_3LPatched_test_SM              = Sample.fromDirectory(name="TTG_SingleLeptFromT_3LinePatched", treeName="Events", isData=False, color=color.TTG3LPatched, texName="tt#gamma (3L patched)", directory=directories['TTG_SingleLeptFromT_3LPatched_test_SM'])
#TTG_SingleLeptFromT_3LPatched_test_SM.reweight_pkl = os.path.join( gridpack_directory, "SM/TTGamma_SingleLeptFromT_3LinePatched_test/", "TTGamma_SingleLeptFromT_3LinePatched_test_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )

#TTG_SingleLeptFromT_1L_SM                          = Sample.fromDirectory(name="TTG_SingleLeptFromT_1Line",        treeName="Events", isData=False, color=color.TTG1L,        texName="tt#gamma (1L)",         directory=directories['TTG_SingleLeptFromT_1L_SM'])
#TTG_SingleLeptFromT_1L_SM.reweight_pkl             = os.path.join( gridpack_directory, "SM/TTGamma_SingleLeptFromT_1Line/", "TTGamma_SingleLeptFromT_1Line_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )

#TTG_SingleLeptFromT_3LPatched_SM                   = Sample.fromDirectory(name="TTG_SingleLeptFromT_3LinePatched", treeName="Events", isData=False, color=color.TTG3LPatched, texName="tt#gamma (3L patched)", directory=directories['TTG_SingleLeptFromT_3LinePatched_SM'])
#TTG_SingleLeptFromT_3LPatched_SM.reweight_pkl      = os.path.join( gridpack_directory, "SM/TTGamma_SingleLeptFromT_3LinePatched/", "TTGamma_SingleLeptFromT_3LinePatched_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )

#TTG_SingleLeptFromT_1L_test_EFT                    = Sample.fromDirectory(name="TTG_SingleLeptFromT_1Line_EFT",    treeName="Events", isData=False, color=color.TTG,          texName="tt#gamma", directory=directories['TTG_SingleLeptFromT_1L_test_EFT'])
#TTG_SingleLeptFromT_1L_test_EFT.reweight_pkl       = os.path.join( gridpack_directory, "EFT/TTGamma_SingleLeptFromT_1Line_EFT_test/", "TTGamma_SingleLeptFromT_1Line_EFT_test_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )

#TTG_DiLept_1L_small_EFT                            = Sample.fromDirectory(name="TTG_DiLept_1L_small_EFT",          treeName="Events", isData=False, color=color.TTG,          texName="tt#gamma", directory=directories['TTGamma_DiLept_EFT_1Line_small'])
#TTG_DiLept_1L_small_EFT.reweight_pkl               = os.path.join( gridpack_directory, "EFT/TTGamma_DiLept_1Line_EFT/", "TTGamma_DiLept_1Line_EFT_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )

TTG_DiLept_1L_EFT                                  = Sample.fromDirectory(name="TTG_DiLept_1L_EFT",          treeName="Events", isData=False, color=color.TTG,          texName="tt#gamma", directory=directories['TTGamma_DiLept_EFT_1Line'])
TTG_DiLept_1L_EFT.reweight_pkl                     = os.path.join( gridpack_directory, "EFT/TTGamma_DiLept_1Line_EFT/", "TTGamma_DiLept_1Line_EFT_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )

signals = []

# Private 1Line Production
#ttGamma_SingleLeptFromT_SM_1Line                 = Sample.fromDirectory(name="ttGamma_SingleLeptFromT_SM_1Line",      treeName="Events", isData=False, color=color.TTG1L,          texName="tt#gamma (1Line)", directory=directories['ttGamma_SingleLeptFromT_SM_1Line'])
#ttGamma_SingleLeptFromTbar_SM_1Line              = Sample.fromDirectory(name="ttGamma_SingleLeptFromTbar_SM_1Line",   treeName="Events", isData=False, color=color.TTG1L,          texName="tt#gamma (1Line)", directory=directories['ttGamma_SingleLeptFromTbar_SM_1Line'])

# Central Samples
#ttGamma_SingleLeptFromT_SM_central               = Sample.fromDirectory(name="ttGamma_SingleLeptFromT_SM_central",    treeName="Events", isData=False, color=color.TTG3LBuggy,     texName="tt#gamma (central)", directory=directories['ttGamma_SingleLeptFromT_SM_central'])
#ttGamma_SingleLeptFromTbar_SM_central            = Sample.fromDirectory(name="ttGamma_SingleLeptFromTbar_SM_central", treeName="Events", isData=False, color=color.TTG3LBuggy,     texName="tt#gamma (central)", directory=directories['ttGamma_SingleLeptFromTbar_SM_central'])
#ttGamma_Dilept_SM_central                        = Sample.fromDirectory(name="ttGamma_Dilept_SM_central",             treeName="Events", isData=False, color=color.TTG3LBuggy,     texName="tt#gamma (central)", directory=directories['ttGamma_Dilept_SM_central'])
#ttGamma_Hadronic_SM_central                      = Sample.fromDirectory(name="ttGamma_Hadronic_SM_central",           treeName="Events", isData=False, color=color.TTG3LBuggy,     texName="tt#gamma (central)", directory=directories['ttGamma_Hadronic_SM_central'])

# CMS ATLAS runcard comparison
TTG_CMS_RunCard_noDeltaR                         = Sample.fromDirectory(name="TTG_CMS_RunCard_noDeltaR",   treeName="Events", isData=False, color=color.TTG3LPatched, texName="tt#gamma (CMS, no #DeltaR)",   directory=directories['ttGamma_NoFullyHad_SM_CMSrunCard_noDeltaR'])
TTG_CMS_RunCard                                  = Sample.fromDirectory(name="TTG_CMS_RunCard",            treeName="Events", isData=False, color=color.TTG6,        texName="tt#gamma (CMS)",   directory=directories['ttGamma_NoFullyHad_SM_CMSrunCard'])
#TTG_CMS_RunCard_small                            = Sample.fromDirectory(name="TTG_CMS_RunCard_small",      treeName="Events", isData=False, color=color.TTG1L,        texName="tt#gamma (CMS)",   directory=directories['ttGamma_NoFullyHad_SM_CMSrunCard_small'])
TTG_ATLAS_RunCard                                = Sample.fromDirectory(name="TTG_ATLAS_RunCard",          treeName="Events", isData=False, color=color.TTG3LBuggy,   texName="tt#gamma (ATLAS)", directory=directories['ttGamma_NoFullyHad_SM_ATLASrunCard'])
#TTG_ATLAS_RunCard_small                          = Sample.fromDirectory(name="TTG_ATLAS_RunCard_small",    treeName="Events", isData=False, color=color.TTG3LBuggy,   texName="tt#gamma (ATLAS)", directory=directories['ttGamma_NoFullyHad_SM_ATLASrunCard_small'])

TTG_CMS_RunCard_noJetPtCut                       = Sample.fromDirectory(name="TTG_CMS_RunCard_noJetPtCut",            treeName="Events", isData=False, color=color.TTG1, texName="tt#gamma (CMS, pT(jet)>0)",   directory=directories['ttGamma_NoFullyHad_SM_CMSrunCard_noJetPtCut'])
TTG_CMS_RunCard_xqcut                            = Sample.fromDirectory(name="TTG_CMS_RunCard_xqcut",                 treeName="Events", isData=False, color=color.TTG2, texName="tt#gamma (CMS, xqcut=0)",   directory=directories['ttGamma_NoFullyHad_SM_CMSrunCard_xqcut'])
#TTG_CMS_RunCard_noDeltaR_noJetPtCut              = Sample.fromDirectory(name="TTG_CMS_RunCard_noDeltaR_noJetPtCut",   treeName="Events", isData=False, color=color.TTG3LPatched, texName="tt#gamma (CMS, no #DeltaR, pT(jet)>0)",   directory=directories['ttGamma_NoFullyHad_SM_CMSrunCard_noDeltaR_noJetPtCut'])
TTG_CMS_RunCard_noDeltaR_xqcut                   = Sample.fromDirectory(name="TTG_CMS_RunCard_noDeltaR_xqcut",        treeName="Events", isData=False, color=color.TTG3, texName="tt#gamma (CMS, no #DeltaR, xqcut=0)",   directory=directories['ttGamma_NoFullyHad_SM_CMSrunCard_noDeltaR_xqcut'])

TTG_CMS_RunCard_noDeltaR_noJetPtCut_xqcut        = Sample.fromDirectory(name="TTG_CMS_RunCard_noDeltaR_noJetPtCut_xqcut",        treeName="Events", isData=False, color=color.TTG1, texName="tt#gamma (CMS, no #DeltaR, pT(jet)>0)",   directory=directories['ttGamma_NoFullyHad_SM_CMSrunCard_noDeltaR_noJetPtCut_xqcut'])
TTG_CMS_RunCard_noJetPtCut_xqcut                 = Sample.fromDirectory(name="TTG_CMS_RunCard_noJetPtCut_xqcut",                 treeName="Events", isData=False, color=color.TTG5, texName="tt#gamma (CMS, pT(jet)>0)",   directory=directories['ttGamma_NoFullyHad_SM_CMSrunCard_noJetPtCut_xqcut'])
TTG_CMS_RunCard_noDeltaR_noJetPtCut_xqcut_wideLepEta        = Sample.fromDirectory(name="TTG_CMS_RunCard_noDeltaR_noJetPtCut_xqcut_wideLepEta",        treeName="Events", isData=False, color=color.TTG4, texName="tt#gamma (CMS, no #DeltaR, pT(jet)>0, xqcut=0, abs(#eta(l))<5)",   directory=directories['ttGamma_NoFullyHad_SM_CMSrunCard_noDeltaR_noJetPtCut_xqcut_wideLepEta'])
