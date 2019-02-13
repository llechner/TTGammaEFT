# Standard Imports
import os, sys
import ROOT

# RootTools Imports
from RootTools.core.Sample import Sample

# TTGammaEFT Imports
from TTGammaEFT.Samples.helpers import getSample, merge

# Logging
import logging
logger = logging.getLogger(__name__)

# Data directory
from TTGammaEFT.Tools.user import data_directory1                         as data_directory
from TTGammaEFT.Tools.user import postprocessing_directoryRun2018_semilep as postprocessing_directory

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
    vars()[ pd + '_Run2018' ] = getSample( pd, 'Run2018', lumi*1000, dirs )
    allSamples_Data25ns += [ vars()[ pd + '_Run2018' ] ]

Run2018      = Sample.combine( "Run2018", allSamples_Data25ns, texName = "Data" )
Run2018.lumi = lumi*1000

for s in allSamples_Data25ns:
  s.color   = ROOT.kBlack
  s.isData  = True

