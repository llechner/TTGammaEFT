#!/usr/bin/env python
import os
import time

from TTGammaEFT.Analysis.SetupHelpers import *
from TTGammaEFT.Analysis.regions      import regionsTTG, inclRegionsTTG, noPhotonRegionTTG

allRegions = regionsTTG
year = "2016"

# Here, all the estimators are defined
estimators  = default_sampleList
estimators += ["Data"]
#estimators = [
#                "TTG",
#                "TT",
#                "DY",
#                "ZG",
#                "singletop",
#                "TG",
#                "WJets",
#                "WG",
#                "other",
#                "QCD-DD"
#]

submitCMD = "submitBatch.py --dpm "
#submitCMD = "echo "
#submitCMD = ""

option  = ""
#option += " --noSystematics"
option += " --year " + year
option += " --overwrite"
#option += " --checkOnly"
#option += " --createExecFile"

#regions = [{"name":None, "parameters":None}]
#regions  = allSR
#regions  = allCR
#regions  = allCR + allSR
regions  = [ misDY3, misDY4p ]

if "--dryrun" in option or "--createExecFile" in option: submitCMD = ""

for control in regions:
    controlString = " --controlRegion %s"%control["name"] if control["name"] else ""
    for i, estimator in enumerate(estimators):
        title = " --title est%s_%s"%(year[2:], estimator) if submitCMD.count("submit") else ""
#        if "DD" in estimator and control["name"]: continue # safe time for qcd estimate
#        if not "DD" in estimator and control["name"]: continue # qcd estimate only

        allRegions = noPhotonRegionTTG if "nPhoton" in control["parameters"] and control["parameters"]["nPhoton"][1] == 0 else inclRegionsTTG + regionsTTG
        for j, region in enumerate(allRegions):
            if submitCMD.count("submit") or submitCMD.count("echo"):
                os.system( submitCMD + title + ' "python run_estimate.py --cores 1 --selectRegion %i --selectEstimator '%j + estimator + controlString + option + '"' )
            else:
                os.system( "python run_estimate.py --cores 1 --selectRegion %i --selectEstimator "%j + estimator + controlString + option )
#            if submitCMD.count("submit"): time.sleep(0.5)
