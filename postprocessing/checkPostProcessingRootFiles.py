# Standard
import os
import ROOT
import subprocess

# RootTools
from RootTools.core.standard                     import *

# User specific
from TTGammaEFT.Tools.user import dpm_directory
redirector        = 'root://hephyse.oeaw.ac.at/'

def get_parser():
    ''' Argument parser for post-processing module.
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for nanoPostProcessing")
    argParser.add_argument('--file',       action='store', type=str, default='nanoPostProcessing_Summer16', help="postprocessing sh file to check")
    argParser.add_argument('--semilep',    action='store_true', help="check semiLep samples?")
    argParser.add_argument('--createExec', action='store_true', help="create .sh file with missing files?")
    argParser.add_argument('--overwrite',  action='store_true', help="overwrite existing missingFiles.sh file?")
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

def filterEmpty( strList ):
    return list( filter ( bool, strList ) )

def getDataDictList( filepath ):
    ''' Read postprocessing sh file and format it to dictionary
    '''
    with open( filepath, 'r' ) as f:
        ppLines = f.readlines()

    ppLines = [ line for line in ppLines if line.startswith('python') ]

    dictList = []
    for line in ppLines:
        skim    = filterEmpty( line.split("--skim ")[1].split(" ") )[0]
        year    = filterEmpty( line.split("--year ")[1].split(" ") )[0]
        dir     = filterEmpty( line.split("--processingEra ")[1].split(" ") )[0]
        sample  = filterEmpty( line.split("--sample ")[1].split(" ") )[0]
        command = line
        if not filterEmpty( line.split("--sample ")[1].split(" ") )[1].startswith("--") and not filterEmpty( line.split("--sample ")[1].split(" ") )[1].startswith("#SPLIT"):
            sample += "_comb"
        nFiles = filterEmpty( line.split("#SPLIT")[1].split(" ") )[0].split("\n")[0]
        dictList.append( { "skim":skim, "year":int(year), "dir":dir, "sample":sample, "nFiles":int(nFiles), "command":command} )

    return dictList

# Load File
logger.info( "Now running on pp file %s" %args.file )
file          = os.path.expandvars( "$CMSSW_BASE/src/TTGammaEFT/postprocessing/%s.sh" % args.file )
dictList      = getDataDictList( file )
isData        = "Run" in args.file
execCommand   = []
for ppEntry in dictList:
    sample = ppEntry['sample']
    logger.debug("Checking sample %s" %sample)

    # Check whether file exists on DPM, no check if root file is ok implemented for now
    dirPath = os.path.join( dpm_directory, 'postprocessed', ppEntry["dir"], ppEntry["skim"], sample  )
    p = subprocess.Popen( ["dpns-ls -l %s" %dirPath], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )

    rootFiles = [ line[:-1].split()[-1].split(".root")[0] for line in p.stdout.readlines() if line[:-1].split()[-1].endswith(".root") ]
    if not rootFiles:
        logger.info("Sample %s not processed" %sample)
        if args.createExec:
            execCommand += [ ppEntry["command"] ]
        continue

    if len(rootFiles) != ppEntry['nFiles']:
        logger.debug("Not all files of sample %s processed: %i of %i" %(sample, len(rootFiles), ppEntry["nFiles"]) )
#        if len(rootFiles) > ppEntry['nFiles']:
#            os.system(" ".join(["xrdfs", redirector, "rm", "/cms" + dirPath.split("/cms")[1] + "/" + sample + ".root" ]) )
#            os.system(" ".join(["dpns-ls", dirPath + "/" + sample + ".root" ]) )
        missingFiles = [ int( item.split("_")[-1] ) if item.split("_")[-1].isdigit() else item for item in rootFiles ]
        missingFiles = list( set( range( ppEntry['nFiles'] ) ) - set( missingFiles ) )
        missingFiles.sort()
        missingFiles = map( str, missingFiles )
        logger.info("Missing filenumbers of sample %s: %s" %(sample, ', '.join(missingFiles) ))

        if args.createExec:
            for miss in missingFiles:
                execCommand += [ ppEntry["command"].split("#SPLIT")[0] + "--nJobs %s --job %s"%(ppEntry["nFiles"], miss) ]

if args.createExec:
    with open( "missingFiles.sh", 'w' if args.overwrite else "a" ) as f:
        for line in execCommand:
            f.write(line.split("\n")[0] + "\n")
        f.write("\n")

