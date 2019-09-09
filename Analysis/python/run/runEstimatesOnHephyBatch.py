#!/usr/bin/env python
import os, time, copy

from TTGammaEFT.Analysis.SetupHelpers import *
from TTGammaEFT.Analysis.regions      import regionsTTG, inclRegionsTTG, noPhotonRegionTTG

allPhotonRegions = regionsTTG
year = "2016"

# Here, all the estimators are defined, if empty: CR specific estimators are used
#estimators  = default_sampleList
#estimators = ["WJets"]
#estimators = ["QCD-DD"]
estimators = ["Data"]
#estimators = []

#submitCMD = "submitBatch.py --dpm "
submitCMD = "echo "
#submitCMD = ""

option  = ""
#option += " --noSystematics"
option += " --year " + year
#option += " --overwrite"
#option += " --checkOnly"
#option += " --createExecFile"

#regions  = signalRegions
#regions  = controlRegions
#crs       = allRegions
#crs       = {"WJets3":allRegions["WJets3"], "WJets4p":allRegions["WJets4p"]}
crs       = {"VG3":allRegions["VG3"]}
#crs       = {"SR3lowIso":allRegions["SR3lowIso"], "SR3highIso":allRegions["SR3highIso"], "SR4plowIso":allRegions["SR4plowIso"], "SR4phighIso":allRegions["SR4phighIso"]}
#crs       = {"SR4poffM3":allRegions["SR4poffM3"]}
#crs.update({"SR4ponM3":allRegions["SR4ponM3"], "SR4poffM3":allRegions["SR4poffM3"], "SR4plowIso":allRegions["SR4plowIso"], "SR4phighIso":allRegions["SR4phighIso"]})

if "--dryrun" in option or "--createExecFile" in option: submitCMD = ""

for name, cr in crs.items():

    if cr["noPhotonCR"]: continue

    est = copy.copy(estimators)
    if not est and not "processes" in cr: est = default_sampleList
    elif not est:                         est = [ e for eList in cr["processes"].values() for e in eList["process"] ]

    for estimator in est:
        opt = option if not "DD" in estimator else option + " --noSystematics"
        title = " --title est%s_%s"%(year[2:], estimator) if submitCMD.count("submit") else ""
        if "DD" in estimator: continue # safe time for qcd estimate
#        if not "DD" in estimator and control: continue # qcd estimate only
#        if not cr["noPhotonCR"]: continue
#        if not "TTG" in estimator: continue

        photonRegions = cr["inclRegion"] + cr["regions"] if not cr["noPhotonCR"] else cr["regions"]

        for j, region in enumerate( photonRegions ):
            if submitCMD.count("submit") or submitCMD.count("echo"):
                os.system( submitCMD + title + ' "python run_estimate.py --cores 1 --selectRegion %i --controlRegion %s --selectEstimator '%(j,name) + estimator + opt + '"' )
            else:
                os.system( "python run_estimate.py --cores 1 --selectRegion %i --selectEstimator "%j + estimator + controlString + opt )
