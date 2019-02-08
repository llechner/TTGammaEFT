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
#try:    data_directory = sys.modules['__main__'].data_directory
#except: from TTGammaEFT.Tools.user import data_datadirectory2018 as data_directory
from TTGammaEFT.Tools.user import data_datadirectory2018 as data_directory

# Take post processing directory if defined in main module
#try:    postprocessing_directory = sys.modules['__main__'].postprocessing_directory
#except: from TTGammaEFT.Tools.user import postprocessing_datadirectory2018
from TTGammaEFT.Tools.user import postprocessing_datadirectory2018

logger.info( "Loading data samples from directory %s", os.path.join(data_directory, postprocessing_datadirectory2018 ) )

allSamples = [ 'MuonEG', 'DoubleMuon', 'EGamma', 'SingleMuon' ]
#lumi       = 58.83

dirs = {}
for ( run, version ) in [ ( 'A', '_ver1' ), ( 'A', '_ver2' ), ( 'A', '_ver3' ), ( 'B', '_ver1' ), ( 'B', '_ver2' ), ( 'C', '_ver1' ), ( 'C', '_ver2' ), ( 'C', '_ver3' ), ( 'D', '_ver2' ) ]:
    runTag = 'Run2018' + run + '_14Sep2018' + version
    for pd in allSamples:
        dirs[ pd + "_Run2018" + run + version ] = [ pd + "_" + runTag ]

for pd in allSamples:
    merge( pd, 'Run2018ABC',    [ 'Run2018A_ver1', 'Run2018A_ver2', 'Run2018A_ver3', 'Run2018B_ver1', 'Run2018B_ver2', 'Run2018C_ver1', 'Run2018C_ver2', 'Run2018C_ver3' ], dirs )
    merge( pd, 'Run2018',       [ 'Run2018ABC', 'Run2018D_ver2' ], dirs )

for key in dirs:
    dirs[key] = [ os.path.join( data_directory, postprocessing_datadirectory2018, dir ) for dir in dirs[key] ]

allSamples_Data25ns  = []
for pd in allSamples:
    vars()[ pd + '_Run2018' ] = getSample( pd, 'Run2018', 58.83*1000, dirs )
    allSamples_Data25ns += [ vars()[ pd + '_Run2018' ] ]

Run2018      = Sample.combine( "Run2018", allSamples_Data25ns, texName = "Data" )
Run2018.lumi = 58.83*1000

for s in allSamples_Data25ns:
  s.color   = ROOT.kBlack
  s.isData  = True

