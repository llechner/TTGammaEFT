#!/usr/bin/env python

import sys

from TTGammaEFT.Analysis.regions         import regionsTTG, noPhotonRegionTTG, inclRegionsTTG
from TTGammaEFT.Analysis.Setup           import Setup
from TTGammaEFT.Analysis.estimators      import *
from TTGammaEFT.Analysis.MCBasedEstimate import MCBasedEstimate
from TTGammaEFT.Analysis.DataObservation import DataObservation
from TTGammaEFT.Analysis.SetupHelpers    import dilepChannels, lepChannels, default_sampleList, allSRCR

loggerChoices = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']
CRChoices     = [r["name"] for r in allSRCR]
# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument("--logLevel",         action="store",  default="INFO",           choices=loggerChoices, help="Log level for logging")
argParser.add_argument("--noSystematics",    action="store_true",                                              help="no systematics?")
argParser.add_argument("--selectEstimator",  action="store",  default=None,   type=str,                        help="select estimator?")
argParser.add_argument("--selectRegion",     action="store",  default=-1,     type=int,                        help="select region?")
argParser.add_argument("--year",             action="store",  default=2016,   type=int,                        help="Which year?")
argParser.add_argument("--cores",            action="store",  default=1,      type=int,                        help="How many threads?")
argParser.add_argument("--controlRegion",    action="store",  default=None,   type=str, choices=CRChoices,     help="For CR region?")
argParser.add_argument("--overwrite",        action="store_true",                                              help="overwrite existing results?")
argParser.add_argument("--checkOnly",        action="store_true",                                              help="check values?")
argParser.add_argument("--createExecFile",   action="store_true",                                              help="get exec file for missing estimates?")
args = argParser.parse_args()

# Logging
if __name__=="__main__":
    import Analysis.Tools.logger as logger
    logger = logger.get_logger( args.logLevel, logFile=None)
else:
    import logging
    logger = logging.getLogger(__name__)

CR_para = {}
if args.controlRegion:
    CR_para = filter( lambda d: d["name"]==args.controlRegion, allSRCR )[0]["parameters"]

photonSelection = not ("nPhoton" in CR_para and CR_para["nPhoton"][1] == 0)

setup          = Setup(year=args.year, photonSelection=photonSelection)
estimators     = estimatorList(setup)
allEstimators  = estimators.constructEstimatorList( default_sampleList )

# Select estimate
if args.selectEstimator == "Data":
    estimate = DataObservation(name="Data", sample=setup.samples["Data"], cacheDir=setup.defaultCacheDir())
    estimate.isSignal = False
    estimate.isData   = True
else:
    estimate = next((e for e in allEstimators if e.name == args.selectEstimator), None)
    estimate.isData = False

if not estimate:
    logger.warn(args.selectEstimator + " not known")
    sys.exit(0)


if args.controlRegion:
    setup = setup.sysClone(parameters=CR_para)

allRegions = inclRegionsTTG + regionsTTG if photonSelection else noPhotonRegionTTG

setup.verbose=True

def wrapper(arg):
        r,channel,setup = arg
        logger.debug("Running estimate for region %s, channel %s in setup %s for estimator %s"%(r,channel, args.controlRegion if args.controlRegion else "None", args.selectEstimator if args.selectEstimator else "None"))
        res = estimate.cachedEstimate(r, channel, setup, save=True, overwrite=args.overwrite, checkOnly=(args.checkOnly or args.createExecFile))
        return (estimate.uniqueKey(r, channel, setup), res )

estimate.initCache(setup.defaultCacheDir())

if args.controlRegion and args.controlRegion.startswith('DY'):
    channels = dilepChannels
    combChannel = 'SFtight'
else:
    channels = lepChannels
    combChannel = 'all'

jobs=[]
for channel in channels:
    for (i, r) in enumerate(allRegions):
        if args.selectRegion != i: continue
        jobs.append((r, channel, setup))
        if not estimate.isData and not args.noSystematics:
            jobs.extend(estimate.getBkgSysJobs(r, channel, setup))


if args.cores==1:
    results = map(wrapper, jobs)
else:
    from multiprocessing import Pool
    pool = Pool(processes=args.cores)
    results = pool.map(wrapper, jobs)
    pool.close()
    pool.join()

if args.checkOnly:
    for res in results:
        print args.selectEstimator, res[0][0], res[0][1], args.controlRegion, res[1].val

if args.createExecFile:
    for res in results:
        if res[1].val < 0:
            with open( "missingEstimates.sh", "w" if args.overwrite else "a" ) as f:
                f.write( " ".join( [ item for item in sys.argv if item not in ["--createExecFile", "--checkOnly"] ] ) + "\n" )
            sys.exit(0)

if args.createExecFile or args.checkOnly: sys.exit(0)

# Combine Channles
for (i, r) in enumerate(allRegions):
    if args.selectRegion != i: continue
    logger.debug("Running estimate for region %s, channel %s in setup %s for estimator %s"%(r,combChannel, args.controlRegion if args.controlRegion else "None", args.selectEstimator if args.selectEstimator else "None"))
    estimate.cachedEstimate(r, combChannel, setup, save=True, overwrite=args.overwrite, checkOnly=args.checkOnly)
    if not estimate.isData and not args.noSystematics:
        map(lambda arg:estimate.cachedEstimate(*arg, save=True, overwrite=args.overwrite, checkOnly=args.checkOnly), estimate.getBkgSysJobs(r, combChannel, setup))

