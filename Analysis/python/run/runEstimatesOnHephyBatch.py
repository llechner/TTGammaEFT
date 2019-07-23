#!/usr/bin/env python
import os
import time

from TTGammaEFT.Analysis.SetupHelpers import allCR, allSR, allSRCR, default_sampleList
from TTGammaEFT.Analysis.regions      import regionsTTG, inclRegionsTTG, noPhotonRegionTTG

allRegions = regionsTTG
year = "2016"

# Here, all the estimators are defined
estimators  = default_sampleList
#estimators += "Data"
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
#option += " --dryrun"


#regions = [{"name":None, "parameters":None}]
#regions  = allSR
#regions  = allCR
regions  = allCR + allSR

for control in regions:
    controlString = " --controlRegion %s"%control["name"] if control["name"] else ""
    for i, estimator in enumerate(estimators):
        title = " --title est%s_%s"%(year[2:], estimator) if submitCMD.count("submit") else ""
        if "DD" in estimator and control["name"]: continue # safe time for qcd estimate
#        if not "DD" in estimator and control["name"]: continue # qcd estimate only

        allRegions = noPhotonRegionTTG if "nPhoton" in control["parameters"] and control["parameters"]["nPhoton"][1] == 0 else regionsTTG
        for j, region in enumerate(allRegions):
            os.system( submitCMD + title + ' "python run_estimate.py --cores 1 --selectRegion %i --selectEstimator '%j + estimator + controlString + option + '"' )
#            if submitCMD.count("submit"): time.sleep(0.5)
