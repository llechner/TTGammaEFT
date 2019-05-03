# Standard
import os, imp
import ROOT
import subprocess

# RootTools
from RootTools.core.standard                     import *

# User specific
from TTGammaEFT.Tools.user import dpm_directory
redirector        = 'root://hephyse.oeaw.ac.at/'

moduleChoices  = [ item for item in os.listdir( os.path.expandvars( "$CMSSW_BASE/python/Samples/nanoAOD/" ) ) if item.endswith(".py") ]
moduleChoices += [ item.split(".py")[0] for item in moduleChoices ]
fileChoices    = [ item for item in os.listdir( os.path.expandvars( "$CMSSW_BASE/src/TTGammaEFT/postprocessing/" ) ) if item.endswith(".sh") and item.startswith("nano") ]
fileChoices   += [ item.split(".sh")[0] for item in fileChoices ]

def get_parser():
    ''' Argument parser for post-processing module.
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for nanoPostProcessing")
    argParser.add_argument('--file',       action='store', type=str, default='nanoPostProcessing_Summer16', choices=fileChoices,   help="postprocessing sh file to check")
    argParser.add_argument('--module',     action='store', type=str, default='Autumn18_private_legacy_v1',  choices=moduleChoices, help="Sample module file")
    return argParser

args = get_parser().parse_args()

# Logging
if __name__=="__main__":
    import Analysis.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )

else:
    import logging
    logger = logging.getLogger(__name__)

if args.file.endswith(".sh"):
    args.file = args.file.rstrip(".sh")

if args.module.endswith(".py"):
    args.module = args.module.rstrip(".py")


module_file = os.path.expandvars( "$CMSSW_BASE/python/Samples/nanoAOD/%s.py" % args.module )
try:
    tmp_module = imp.load_source( "allSamples", os.path.expandvars( module_file ) )
    allSamples   = getattr(tmp_module, "allSamples")
except:
    raise RuntimeError( "Module not found" )
allSamples = [s.name for s in allSamples]

filePath = os.path.expandvars( "$CMSSW_BASE/src/TTGammaEFT/postprocessing/%s.sh"%args.file )
with open( filePath, "r" ) as f:
    subList = f.readlines()

subList = [ item.split("#SPLIT")[0].split("--sample ")[1].split("--")[0] for item in subList if item.startswith("python") ]
subSamples = []
for s in subList:
    subSamples += [item for item in s.split(" ") if item] if len(s.split(" ")) > 1 else [s]
 
for sample in allSamples:
    if sample not in subSamples:
        logger.info( "Sample %s not considered for postprocessing!"% sample )
    else:
        subSamples.remove(sample)

if subSamples:
    logger.info( "Samples not in Module: %s"% ", ".join(subSamples) )
