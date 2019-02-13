# Standard Imports
import os, sys
import ROOT

# RootTools Imports
from RootTools.core.Sample import Sample

# Logging
import logging
logger = logging.getLogger(__name__)

# Colors
from TTGammaEFT.Samples.color import color

# Data directory
from TTGammaEFT.Tools.user import gridpack_directory
from TTGammaEFT.Tools.user import data_directory2             as data_directory
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

directories = { key : [ os.path.join( data_directory, postprocessing_directory, dir) for dir in dirs[key] ] for key in dirs.keys() }

# Samples
TTG_SingleLeptFromT_1L_test_SM                     = Sample.fromDirectory(name="TTG_SingleLeptFromT_1Line",        treeName="Events", isData=False, color=color.TTG1L,        texName="tt#gamma (1L)",         directory=directories['TTG_SingleLeptFromT_1L_test_SM'])
TTG_SingleLeptFromT_1L_test_SM.reweight_pkl        = os.path.join( gridpack_directory, "SM/TTGamma_SingleLeptFromT_1Line_test/", "TTGamma_SingleLeptFromT_1Line_test_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )

TTG_SingleLeptFromT_3LBuggy_test_SM                = Sample.fromDirectory(name="TTG_SingleLeptFromT_3LineBuggy",   treeName="Events", isData=False, color=color.TTG3LBuggy,   texName="tt#gamma (3L buggy)",   directory=directories['TTG_SingleLeptFromT_3LBuggy_test_SM'])
TTG_SingleLeptFromT_3LBuggy_test_SM.reweight_pkl   = os.path.join( gridpack_directory, "SM/TTGamma_SingleLeptFromT_3LineBuggy_test/", "TTGamma_SingleLeptFromT_3LineBuggy_test_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )

TTG_SingleLeptFromT_3LPatched_test_SM              = Sample.fromDirectory(name="TTG_SingleLeptFromT_3LinePatched", treeName="Events", isData=False, color=color.TTG3LPatched, texName="tt#gamma (3L patched)", directory=directories['TTG_SingleLeptFromT_3LPatched_test_SM'])
TTG_SingleLeptFromT_3LPatched_test_SM.reweight_pkl = os.path.join( gridpack_directory, "SM/TTGamma_SingleLeptFromT_3LinePatched_test/", "TTGamma_SingleLeptFromT_3LinePatched_test_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )

TTG_SingleLeptFromT_1L_SM                          = Sample.fromDirectory(name="TTG_SingleLeptFromT_1Line",        treeName="Events", isData=False, color=color.TTG1L,        texName="tt#gamma (1L)",         directory=directories['TTG_SingleLeptFromT_1L_SM'])
TTG_SingleLeptFromT_1L_SM.reweight_pkl             = os.path.join( gridpack_directory, "SM/TTGamma_SingleLeptFromT_1Line/", "TTGamma_SingleLeptFromT_1Line_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )

TTG_SingleLeptFromT_3LPatched_SM                   = Sample.fromDirectory(name="TTG_SingleLeptFromT_3LinePatched", treeName="Events", isData=False, color=color.TTG3LPatched, texName="tt#gamma (3L patched)", directory=directories['TTG_SingleLeptFromT_3LinePatched_SM'])
TTG_SingleLeptFromT_3LPatched_SM.reweight_pkl      = os.path.join( gridpack_directory, "SM/TTGamma_SingleLeptFromT_3LinePatched/", "TTGamma_SingleLeptFromT_3LinePatched_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )

TTG_SingleLeptFromT_1L_test_EFT                    = Sample.fromDirectory(name="TTG_SingleLeptFromT_1Line_EFT",    treeName="Events", isData=False, color=color.TTG,          texName="tt#gamma", directory=directories['TTG_SingleLeptFromT_1L_test_EFT'])
TTG_SingleLeptFromT_1L_test_EFT.reweight_pkl       = os.path.join( gridpack_directory, "EFT/TTGamma_SingleLeptFromT_1Line_EFT_test/", "TTGamma_SingleLeptFromT_1Line_EFT_test_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )

TTG_DiLept_1L_small_EFT                            = Sample.fromDirectory(name="TTG_DiLept_1L_small_EFT",          treeName="Events", isData=False, color=color.TTG,          texName="tt#gamma", directory=directories['TTGamma_DiLept_EFT_1Line_small'])
TTG_DiLept_1L_small_EFT.reweight_pkl               = os.path.join( gridpack_directory, "EFT/TTGamma_DiLept_1Line_EFT/", "TTGamma_DiLept_1Line_EFT_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )

TTG_DiLept_1L_EFT                                  = Sample.fromDirectory(name="TTG_DiLept_1L_EFT",          treeName="Events", isData=False, color=color.TTG,          texName="tt#gamma", directory=directories['TTGamma_DiLept_EFT_1Line'])
TTG_DiLept_1L_EFT.reweight_pkl                     = os.path.join( gridpack_directory, "EFT/TTGamma_DiLept_1Line_EFT/", "TTGamma_DiLept_1Line_EFT_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )

signals = []

