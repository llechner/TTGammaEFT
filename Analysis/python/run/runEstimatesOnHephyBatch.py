#!/usr/bin/env python
import os
import time

from TTGammaEFT.Analysis.SetupHelpers import *
from TTGammaEFT.Analysis.regions      import regionsTTG, inclRegionsTTG, noPhotonRegionTTG

allPhotonRegions = regionsTTG
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

#submitCMD = "submitBatch.py --dpm "
submitCMD = "echo "
#submitCMD = ""

option  = ""
#option += " --noSystematics"
option += " --year " + year
option += " --overwrite"
#option += " --checkOnly"
#option += " --createExecFile"

#regions  = signalRegions.keys()
#regions  = controlRegions.keys()
regions  = allRegions.keys()

if "--dryrun" in option or "--createExecFile" in option: submitCMD = ""

for control in regions:
    controlString = " --controlRegion %s"%control if control else ""
    for i, estimator in enumerate(estimators):
        title = " --title est%s_%s"%(year[2:], estimator) if submitCMD.count("submit") else ""
#        if "DD" in estimator and control: continue # safe time for qcd estimate
#        if not "DD" in estimator and control: continue # qcd estimate only

        allPhotonRegions = noPhotonRegionTTG if "nPhoton" in allRegions[control]["parameters"] and allRegions[control]["parameters"]["nPhoton"][1] == 0 else inclRegionsTTG + regionsTTG
        for j, region in enumerate(allPhotonRegions):
            if submitCMD.count("submit") or submitCMD.count("echo"):
                os.system( submitCMD + title + ' "python run_estimate.py --cores 1 --selectRegion %i --selectEstimator '%j + estimator + controlString + option + '"' )
            else:
                os.system( "python run_estimate.py --cores 1 --selectRegion %i --selectEstimator "%j + estimator + controlString + option )
#            if submitCMD.count("submit"): time.sleep(0.5)
