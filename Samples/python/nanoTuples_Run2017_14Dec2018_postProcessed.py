# Standard Imports
import os, sys
import ROOT

# RootTools Imports
from RootTools.core.Sample import Sample 

# TTGammaEFT Imports
from TTGammaEFT.Samples.helpers import getSample, merge

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
from TTGammaEFT.Tools.user import data_directory2                 as data_directory
from TTGammaEFT.Tools.user import postprocessing_directoryRun2017 as postprocessing_directory

logger.info( "Loading data samples from directory %s", os.path.join(data_directory, postprocessing_directory ) )

allSamples = [ 'MuonEG', 'DoubleMuon', 'DoubleEG', 'SingleMuon', 'SingleElectron' ]
lumi       = 41.86

dirs = {}
for ( run, version ) in [ ( 'B', '' ), ( 'C', '' ), ( 'D', '' ), ( 'E', '' ), ( 'F', '' ) ]:
    runTag = 'Run2017' + run + '_14Dec2018' + version
    for pd in allSamples:
        dirs[ pd + "_Run2017" + run + version ] = [ pd + "_" + runTag ]

for pd in allSamples:
    merge( pd, 'Run2017',    [ 'Run2017B', 'Run2017C', 'Run2017D', 'Run2017E', 'Run2017F' ], dirs )
    merge( pd, 'Run2017CDE', [ 'Run2017C', 'Run2017D', 'Run2017E' ], dirs )

for key in dirs:
    dirs[key] = [ os.path.join( data_directory, postprocessing_directory, dir ) for dir in dirs[key] ]

allSamples_Data25ns  = []
for pd in allSamples:
    vars()[ pd + '_Run2017' ] = getSample( pd, 'Run2017', lumi*1000, dirs )
    allSamples_Data25ns += [ vars()[ pd + '_Run2017' ] ]

Run2017      = Sample.combine( "Run2017", allSamples_Data25ns, texName = "Data" )
Run2017.lumi = lumi*1000

for s in allSamples_Data25ns:
    s.color   = ROOT.kBlack
    s.isData  = True
