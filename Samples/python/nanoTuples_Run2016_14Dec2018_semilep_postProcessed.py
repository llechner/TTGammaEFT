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
from TTGammaEFT.Tools.user import data_directory1                         as data_directory
from TTGammaEFT.Tools.user import postprocessing_directoryRun2016_semilep as postprocessing_directory

logger.info( "Loading data samples from directory %s", os.path.join(data_directory, postprocessing_directory ) )

#allSamples = [ 'MuonEG', 'DoubleMuon', 'DoubleEG', 'SingleMuon', 'SingleElectron' ]
allSamples = [ 'SingleMuon', 'SingleElectron' ]
lumi       = 35.92

dirs = {}
for ( run, version ) in [ ( 'B', '_ver2' ), ( 'C', '' ), ( 'D', '' ), ( 'E', '' ), ( 'F', '' ), ( 'G', '' ), ( 'H', '' ) ]:
    runTag = 'Run2016' + run + '_14Dec2018' + version
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
    vars()[ pd + '_Run2016' ] = getSample( pd, 'Run2016', lumi*1000, dirs )
    allSamples_Data25ns += [ vars()[ pd + '_Run2016' ] ]

Run2016      = Sample.combine( "Run2016", allSamples_Data25ns, texName = "Data" )
Run2016.lumi = lumi*1000

for s in allSamples_Data25ns:
  s.color   = ROOT.kBlack
  s.isData  = True

