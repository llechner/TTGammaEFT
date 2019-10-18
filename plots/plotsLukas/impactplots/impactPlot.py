#!/usr/bin/env python

import os
import ROOT
import shutil
import uuid

from TTGammaEFT.Tools.user  import analysis_results, plot_directory, combineReleaseLocation, cache_directory

import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument("--logLevel",       action="store", default="INFO",          nargs="?", choices=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "TRACE", "NOTSET"],    help="Log level for logging")
argParser.add_argument("--label",          action="store", default="defaultSetup",  type=str,                               help="Label of results directory" )
argParser.add_argument("--keepDir",        action="store_true",                                                             help="Keep the directory in the combine release after study is done?")
argParser.add_argument("--expected",       action="store_true",                                                             help="Use expected results?")
argParser.add_argument("--carddir",        action="store", default="limits/cardFiles/defaultSetup/observed",              nargs="?",                              help="which cardfile directory?")
argParser.add_argument("--cardfile",       action="store", default="",              nargs="?",                              help="which cardfile?")
argParser.add_argument("--cores",          action="store", default=1,               type=int,                               help="Run on n cores in parallel")
argParser.add_argument("--year",           action="store", default=2016,            type=int,                               help="Which year?")
argParser.add_argument("--bkgOnly",        action="store_true",                                                             help="Allow no signal?")
args = argParser.parse_args()


# Logging
import Analysis.Tools.logger as logger
logger = logger.get_logger(args.logLevel, logFile = None )
import RootTools.core.logger as logger_rt
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None )

def wrapper( cardDir, cardName ):
    logger.info("Processing mass point %s"%cardName)
    cardFile       = "%s_shapeCard.txt"%cardName
    baseDir        = os.path.join( cache_directory, "analysis", str(args.year), "limits" )
    limitDir       = os.path.join( baseDir, "cardFiles", args.label, "expected" if args.expected else "observed" )
    cardFilePath   = os.path.join( limitDir, cardFile)
    combineDirname = os.path.join( combineReleaseLocation, str(args.year), cardName )
    logger.info("Creating %s"%combineDirname)
    if not os.path.isdir(combineDirname): os.makedirs(combineDirname)
    shutil.copyfile(cardFilePath,combineDirname+"/"+cardFile)
    shutil.copyfile(cardFilePath.replace("shapeCard.txt", "shape.root"),combineDirname+"/"+cardFile.replace("shapeCard.txt", "shape.root"))

    scram = "echo ''"#eval `scramv1 runtime -sh`"
    if args.bkgOnly:
        prepWorkspace   = "text2workspace.py %s --X-allow-no-signal -m 125"%cardFile
        robustFit       = "combineTool.py -M Impacts -d %s_shapeCard.root -m 125 --doInitialFit --robustFit 1 --rMin -0.01 --rMax 0.0"%cardName
        impactFits      = "combineTool.py -M Impacts -d %s_shapeCard.root -m 125 --robustFit 1 --doFits --parallel %s --rMin -0.01 --rMax 0.0"%(cardName,str(args.cores))
    else:
        prepWorkspace   = "text2workspace.py %s -m 125"%cardFile
        robustFit       = "combineTool.py -M Impacts -d %s_shapeCard.root -m 125 --doInitialFit --robustFit 1 --rMin -10 --rMax 10"%cardName
        impactFits      = "combineTool.py -M Impacts -d %s_shapeCard.root -m 125 --robustFit 1 --doFits --parallel %s --rMin -10 --rMax 10"%(cardName,str(args.cores))

    extractImpact   = "combineTool.py -M Impacts -d %s_shapeCard.root -m 125 -o impacts.json"%cardName
    plotImpacts     = "plotImpacts.py -i impacts.json -o impacts"
    combineCommand  = ";".join(["cd %s"%combineDirname,scram,prepWorkspace,robustFit,impactFits,extractImpact,plotImpacts])
    logger.info("Will run the following command, might take a few hours:\n%s"%combineCommand)
    
    os.system(combineCommand)
    
    plotDir  = os.path.join( plot_directory, "impacts", str(args.year), "expected" if args.expected else "observed" )
    plotName = cardName if not args.bkgOnly else cardName + "_bkgOnly"
    if not os.path.isdir(plotDir): os.makedirs(plotDir)
    shutil.copyfile(combineDirname+"/impacts.pdf", "%s/%s.pdf"%(plotDir,plotName))
    logger.info("Copied result to %s"%plotDir)

    if not args.keepDir:
        logger.info("Removing directory in release location")
        shutil.rmtree(combineDirname)


wrapper( args.carddir, args.cardfile )
