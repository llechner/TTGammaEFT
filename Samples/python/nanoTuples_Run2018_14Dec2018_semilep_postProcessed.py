# Standard Imports
import os, sys, copy
import ROOT

# RootTools Imports
from RootTools.core.Sample import Sample

# TTGammaEFT Imports
from TTGammaEFT.Samples.helpers import getDPMSample, merge

# Logging
if __name__=="__main__":
    import Analysis.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
else:
    import logging
    logger = logging.getLogger(__name__)

# Data directory
from TTGammaEFT.Tools.user import dpm_directory as data_directory
data_directory += "postprocessed/"
from TTGammaEFT.Tools.user import postprocessing_directoryRun2018_semilep as postprocessing_directory

# Redirector
try:
    redirector = sys.modules['__main__'].redirector
except:
    from TTGammaEFT.Tools.user import redirector as redirector

logger.info( "Loading data samples from directory %s", os.path.join(data_directory, postprocessing_directory ) )

#allSamples = [ 'MuonEG', 'DoubleMuon', 'EGamma', 'SingleMuon' ]
allSamples = [ 'EGamma', 'SingleMuon' ]
lumi       = 58.83

dirs = {}
for ( run, version ) in [ ( 'A', '' ), ( 'B', '' ), ( 'C', '' ), ( 'D', '_ver2' ) ]:
    runTag = 'Run2018' + run + '_14Dec2018' + version
    for pd in allSamples:
        dirs[ pd + "_Run2018" + run + version ] = [ pd + "_" + runTag ]

for pd in allSamples:
    merge( pd, 'Run2018ABC',    [ 'Run2018A', 'Run2018B', 'Run2018C' ], dirs )
    merge( pd, 'Run2018',       [ 'Run2018ABC', 'Run2018D_ver2' ], dirs )

for key in dirs:
    dirs[key] = [ os.path.join( data_directory, postprocessing_directory, dir ) for dir in dirs[key] ]

allSamples_Data25ns  = []
for pd in allSamples:
    vars()[ pd + '_Run2018' ] = getDPMSample( pd, 'Run2018', lumi*1000, dirs, redirector )
    allSamples_Data25ns += [ vars()[ pd + '_Run2018' ] ]

Run2018      = Sample.combine( "Run2018", allSamples_Data25ns, texName = "Data" )
Run2018.lumi = lumi*1000

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
    _ = pool.map( checkFile, Run2018.files )
    pool.close()

