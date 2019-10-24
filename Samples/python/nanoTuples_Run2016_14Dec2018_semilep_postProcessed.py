# Standard Imports
import os, sys, copy
import ROOT

# RootTools Imports
from RootTools.core.Sample import Sample

# TTGammaEFT Imports
from TTGammaEFT.Samples.helpers import getDataSample, merge

# Data directory
try:
    data_directory = sys.modules['__main__'].data_directory
except:
    from TTGammaEFT.Tools.user import dpm_directory as data_directory
    data_directory += "postprocessed/"
try:
    postprocessing_directory = sys.modules['__main__'].postprocessing_directory
except:
    from TTGammaEFT.Samples.default_locations import postprocessing_locations
    postprocessing_directory = postprocessing_locations.Run2016_semilep

try:
    fromDPM = sys.modules['__main__'].fromEOS != "True"
except:
    fromDPM = True

if "gammaSkim" in os.environ and os.environ["gammaSkim"] == "True":
    postprocessing_directory = postprocessing_directory.replace("/semilep/", "/semilepGamma/")
    if fromDPM: postprocessing_directory = postprocessing_directory.replace("v20","v19")

# Redirector
try:
    redirector = sys.modules['__main__'].redirector
except:
    from TTGammaEFT.Tools.user import redirector as redirector

# Logging
if __name__=="__main__":
    import Analysis.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
else:
    import logging
    logger = logging.getLogger(__name__)

logger.info( "Loading data samples from directory %s", os.path.join(data_directory, postprocessing_directory ) )

allSamples = [ 'SingleMuon', 'SingleElectron' ]
lumi       = 35.92

dirs = {}
for ( run, version ) in [ ( 'B', '_ver2' ), ( 'C', '' ), ( 'D', '' ), ( 'E', '' ), ( 'F', '' ), ( 'G', '' ), ( 'H', '' ) ]:
#    runTag = 'Run2016' + run + '_14Dec2018' + version
    runTag = 'Run2016' + run + '_17Jul2018' + version
    for pd in allSamples:
        dirs[ pd + "_Run2016" + run + version ] = [ pd + "_" + runTag ]

for pd in allSamples:
    merge( pd, 'Run2016BCD',    [ 'Run2016B_ver2', 'Run2016C', 'Run2016D'           ], dirs )
    merge( pd, 'Run2016BCDEFG', [ 'Run2016BCD', 'Run2016E', 'Run2016F', 'Run2016G'  ], dirs )
    merge( pd, 'Run2016',       [ 'Run2016BCDEFG', 'Run2016H' ], dirs )

for key in dirs:
    dirs[key] = [ os.path.join( data_directory, postprocessing_directory, dir ) for dir in dirs[key] ]

allSamples_Data25ns  = []
for pd in allSamples:
    vars()[ pd + '_Run2016' ] = getDataSample( pd, 'Run2016', lumi*1000, dirs, redirector=redirector, fromDPM=fromDPM )
    allSamples_Data25ns += [ vars()[ pd + '_Run2016' ] ]

Run2016      = Sample.combine( "Run2016", allSamples_Data25ns, texName = "Data" )
Run2016.lumi = lumi*1000

for s in allSamples_Data25ns:
  s.color   = ROOT.kBlack
  s.isData  = True


if __name__ == "__main__":

    def get_parser():
        ''' Argument parser for post-processing module.
        '''
        import argparse
        argParser = argparse.ArgumentParser(description = "Argument parser for nanoPostProcessing")
        argParser.add_argument('--check',   action='store_true', help="check root files?")
        argParser.add_argument('--deepcheck',   action='store_true', help="check events of root files?")
        argParser.add_argument('--checkWeight', action='store_true', help="check weight?")
        argParser.add_argument('--remove',  action='store_true', help="remove corrupt root files?")
        argParser.add_argument('--log',         action='store_true', help="print each filename?")
        return argParser

    args = get_parser().parse_args()

    if not (args.check or args.deepcheck or args.checkWeight): sys.exit(0)

    # check Root Files
    from Analysis.Tools.helpers import checkRootFile, deepCheckRootFile, deepCheckWeight
    from multiprocessing        import Pool

    def checkFile( file ):
                if args.log: logger.info( "Checking filepath: %s"%file )
                corrupt = False
                if args.check:
                    corrupt = not checkRootFile(file, checkForObjects=["Events"])
                if args.deepcheck and not corrupt:
                    corrupt = not deepCheckRootFile(file)
                if args.checkWeight and not corrupt:
                    corrupt = not deepCheckWeight(file)
                if corrupt:
                    if file.startswith("root://hephyse.oeaw.ac.at/"):
                        file = file.split("root://hephyse.oeaw.ac.at/")[1]
                    logger.info( "File corrupt: %s"%file )
                    if args.remove:
                        logger.info( "Removing file: %s"%file )
                        os.system( "/usr/bin/rfrm -f %s"%file )

    pool = Pool( processes=16 )
    _ = pool.map( checkFile, Run2016.files )
    pool.close()

