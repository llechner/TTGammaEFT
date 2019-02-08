# Standard
import os

# RootTools
from RootTools.core.standard import *

# TTGammaEFT
from TTGammaEFT.Tools.user   import gridpack_directory

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
    return argParser

# Logging
if __name__=="__main__":
    import TTGammaEFT.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    options = get_parser().parse_args()
    ov = options.overwrite
else:
    import logging
    logger = logging.getLogger(__name__)
    ov = False

from Samples.Tools.config import dbDir, redirector, redirector_global
dbFile = dbDir+"DB_TTGamma_GEN.sql"

logger.info("Using db file: %s", dbFile)

# SM point, no weights
TTGamma_SingleLeptFromT_SM_1Line_test                     = FWLiteSample.fromDAS("TTGamma_SingleLeptFromT_SM_1Line_test", "/TTGamma_SingleLeptFromT_1Line_test_GENSIM/llechner-TTGamma_SingleLeptFromT_1Line_test_GENSIM-b3122b77720ca80362007ff086008b03/USER", "phys03", dbFile=dbFile, overwrite=ov, prefix='root://hephyse.oeaw.ac.at/')
TTGamma_SingleLeptFromT_SM_1Line_test.reweight_pkl        = os.path.join( gridpack_directory, "SM/TTGamma_SingleLeptFromT_1Line_test/", "TTGamma_SingleLeptFromT_1Line_test_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )
TTGamma_SingleLeptFromT_SM_1Line_test.xSection            = 0.1267
TTGamma_SingleLeptFromT_SM_1Line_test.nEvents             = 100000

TTGamma_SingleLeptFromT_SM_3LineBuggy_test                = FWLiteSample.fromDAS("TTGamma_SingleLeptFromT_SM_3LineBuggy_test", "/TTGamma_SingleLeptFromT_3LineBuggy_test_GENSIM/llechner-TTGamma_SingleLeptFromT_3LineBuggy_test_GENSIM-f3ebe776d7309479b1058aff34e27155/USER", "phys03", dbFile=dbFile, overwrite=ov, prefix='root://hephyse.oeaw.ac.at/')
TTGamma_SingleLeptFromT_SM_3LineBuggy_test.reweight_pkl   = os.path.join( gridpack_directory, "SM/TTGamma_SingleLeptFromT_3LineBuggy_test/", "TTGamma_SingleLeptFromT_3LineBuggy_test_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )
TTGamma_SingleLeptFromT_SM_3LineBuggy_test.xSection       = 0.1266
TTGamma_SingleLeptFromT_SM_3LineBuggy_test.nEvents        = 100000

TTGamma_SingleLeptFromT_SM_3LinePatched_test              = FWLiteSample.fromDAS("TTGamma_SingleLeptFromT_SM_3LinePatched_test", "/TTGamma_SingleLeptFromT_3LinePatched_test_GENSIM/llechner-TTGamma_SingleLeptFromT_3LinePatched_test_GENSIM-e94234d067bc2f081eff982fc497c503/USER", "phys03", dbFile=dbFile, overwrite=ov, prefix='root://hephyse.oeaw.ac.at/')
TTGamma_SingleLeptFromT_SM_3LinePatched_test.reweight_pkl = os.path.join( gridpack_directory, "SM/TTGamma_SingleLeptFromT_3LinePatched_test/", "TTGamma_SingleLeptFromT_3LinePatched_test_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )
TTGamma_SingleLeptFromT_SM_3LinePatched_test.xSection     = 0.1293
TTGamma_SingleLeptFromT_SM_3LinePatched_test.nEvents      = 100000

# EFT weights included + reference point
TTGamma_SingleLeptFromT_EFT_1Line_test                    = FWLiteSample.fromDAS("TTGamma_SingleLeptFromT_EFT_1Line_test", "/TTGamma_SingleLeptFromT_1Line_EFT_test_GENSIM/llechner-TTGamma_SingleLeptFromT_1Line_EFT_test_GENSIM-c9d6edd965db7012e7f57ed560889b60/USER", "phys03", dbFile=dbFile, overwrite=ov, prefix='root://hephyse.oeaw.ac.at/')
TTGamma_SingleLeptFromT_EFT_1Line_test.reweight_pkl       = os.path.join( gridpack_directory, "EFT/TTGamma_SingleLeptFromT_1Line_EFT_test/", "TTGamma_SingleLeptFromT_1Line_EFT_test_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )
TTGamma_SingleLeptFromT_EFT_1Line_test.xSection           = 0.1724
TTGamma_SingleLeptFromT_EFT_1Line_test.nEvents            = 100000

TTGamma_DiLept_EFT_1Line_small                           = FWLiteSample.fromDAS("TTGamma_DiLept_EFT_1Line_small", "/TTGamma_DiLept_1Line_EFT_GENSIM_small_v2/llechner-TTGamma_DiLept_1Line_EFT_GENSIM_small_v2-f2b65dd54e97daa1934ff1f579c2bf2e/USER", "phys03", dbFile=dbFile, overwrite=ov, prefix='root://hephyse.oeaw.ac.at/')
TTGamma_DiLept_EFT_1Line_small.reweight_pkl              = os.path.join( gridpack_directory, "EFT/TTGamma_DiLept_1Line_EFT/", "TTGamma_DiLept_1Line_EFT_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )
TTGamma_DiLept_EFT_1Line_small.xSection                  = 0.3948
TTGamma_DiLept_EFT_1Line_small.nEvents                   = 100000

#TTGamma_DiLept_EFT_1Line                                 = FWLiteSample.fromDAS("TTGamma_DiLept_EFT_1Line", "/TTGamma_DiLept_1Line_EFT_GENSIM/llechner-TTGamma_DiLept_1Line_EFT_GENSIM-f2b65dd54e97daa1934ff1f579c2bf2e/USER", "phys03", dbFile=dbFile, overwrite=ov, prefix='root://hephyse.oeaw.ac.at/')
#TTGamma_DiLept_EFT_1Line.reweight_pkl                    = os.path.join( gridpack_directory, "EFT/TTGamma_DiLept_1Line_EFT/", "TTGamma_DiLept_1Line_EFT_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl" )
#TTGamma_DiLept_EFT_1Line.xSection                        = 0.3948
#TTGamma_DiLept_EFT_1Line.nEvents                         = 1000000

SM = [
    TTGamma_SingleLeptFromT_SM_1Line_test,
    TTGamma_SingleLeptFromT_SM_3LineBuggy_test,
    TTGamma_SingleLeptFromT_SM_3LinePatched_test,
]

EFT = [
    TTGamma_SingleLeptFromT_EFT_1Line_test,
    TTGamma_DiLept_EFT_1Line_small,
#    TTGamma_DiLept_EFT_1Line,
]

allSamples = SM + EFT

for s in allSamples:
    s.isData = False
