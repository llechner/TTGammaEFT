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
try:    data_directory = sys.modules['__main__'].data_directory
except: from TTGammaEFT.Tools.user import data_directory

# Take post processing directory if defined in main module
#try:    postprocessing_directory = sys.modules['__main__'].postprocessing_directory
#except: from TTGammaEFT.Tools.user import postprocessing_datadirectory2016
from TTGammaEFT.Tools.user import postprocessing_datadirectory2016

logger.info( "Loading data samples from directory %s", os.path.join(data_directory, postprocessing_datadirectory2016 ) )

allSamples = [ 'MuonEG', 'DoubleMuon', 'DoubleEG', 'SingleMuon', 'SingleElectron' ]
#lumi       = 35.92

dirs = {}
for ( run, version ) in [ ( 'B', '_ver2' ), ( 'C', '' ), ( 'D', '' ), ( 'E', '' ), ( 'F', '' ), ( 'G', '' ), ( 'H', '_ver2' ), ( 'H', '_ver3' ) ]:
    runTag = 'Run2016' + run + '_05Feb2018' + version
    for pd in allSamples:
        dirs[ pd + "_Run2016" + run + version ] = [ pd + "_" + runTag ]

for pd in allSamples:
    merge( pd, 'Run2016BCD',    [ 'Run2016B_ver2', 'Run2016C', 'Run2016D'           ], dirs )
    merge( pd, 'Run2016BCDEFG', [ 'Run2016BCD', 'Run2016E', 'Run2016F', 'Run2016G'  ], dirs )
    merge( pd, 'Run2016',       [ 'Run2016BCDEFG', 'Run2016H_ver2', 'Run2016H_ver3' ], dirs )

for key in dirs:
    dirs[key] = [ os.path.join( data_directory, postprocessing_datadirectory2016, dir ) for dir in dirs[key] ]

allSamples_Data25ns  = []
for pd in allSamples:
    vars()[ pd + '_Run2016' ] = getSample( pd, 'Run2016', 35.92*1000, dirs )
    allSamples_Data25ns += [ vars()[ pd + '_Run2016' ] ]

Run2016      = Sample.combine( "Run2016", allSamples_Data25ns, texName = "Data" )
Run2016.lumi = 35.92*1000

for s in allSamples_Data25ns:
  s.color   = ROOT.kBlack
  s.isData  = True

