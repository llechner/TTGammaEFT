import os

from TTGammaEFT.Tools.user import results_directory, cache_directory

signalRegions = {}
# Signal Regions Settings
signalRegions["SR3"]  = { "parameters":{"zWindow":"all", "nJet":(3,3),  "nBTag":(1,-1), "nPhoton":(1,-1)} }
signalRegions["SR4p"] = { "parameters":{"zWindow":"all", "nJet":(4,-1), "nBTag":(1,-1), "nPhoton":(1,-1)} }
default_SR = signalRegions["SR4p"]

#Define defaults here
default_nJet         = default_SR["parameters"]["nJet"]
default_nBTag        = default_SR["parameters"]["nBTag"]
default_nPhoton      = default_SR["parameters"]["nPhoton"]
default_zWindow      = default_SR["parameters"]["zWindow"]
default_dileptonic   = False
default_invLepIso    = False
default_addMisIDSF   = False

default_misIDSF      = 2.25
default_DYSF         = 1.17

default_sampleList      = ["TTG","TT_pow","DY_LO","ZG","WG","WJets","other","QCD-DD"]
#default_sampleList      = ["TTG_cat0,"TT_pow_cat0","DY_LO_cat0","ZG_cat0","WG_cat0","WJets_cat0","other_cat0","QCD-DD_cat0"]
#default_sampleList     += ["TTG_cat2,"TT_pow_cat2","DY_LO_cat2","ZG_cat2","WG_cat2","WJets_cat2","other_cat2","QCD-DD_cat2"]
#default_sampleList     += ["TTG_cat13,"TT_pow_cat13","DY_LO_cat13","ZG_cat13","WG_cat13","WJets_cat13","other_cat13","QCD-DD_cat13"]

analysis_results = os.path.join( results_directory, "analysis" )
cache_dir        = os.path.join( cache_directory,   "analysis" )

lepChannels   = ["e", "mu"]
dilepChannels = ["eetight", "mumutight"]
allChannels   = ["all", "e", "mu", "eetight", "mumutight", "SFtight"]
jmeVariations = ["jer", "jerUp", "jerDown", "jesTotalUp", "jesTotalDown"]
#metVariations = ["unclustEnUp", "unclustEnDown"]


# Region Settings
# 3 ... = 3 jets
# 3 ... >= 4 jets

# Control Regions Settings

controlRegions = {}
# dileptonic ee/mumu all m(l,l) nBTag0 nPhoton0 CR for DY ScaleFactor
controlRegions["DY2"]  = { "parameters":{"dileptonic":True, "zWindow":"onZSFllTight", "nJet":(2,2),  "nBTag":(0,0), "nPhoton":(0,0)} }
controlRegions["DY3"]  = { "parameters":{"dileptonic":True, "zWindow":"onZSFllTight", "nJet":(3,3),  "nBTag":(0,0), "nPhoton":(0,0)} }
controlRegions["DY4"]  = { "parameters":{"dileptonic":True, "zWindow":"onZSFllTight", "nJet":(4,4),  "nBTag":(0,0), "nPhoton":(0,0)} }
controlRegions["DY5"]  = { "parameters":{"dileptonic":True, "zWindow":"onZSFllTight", "nJet":(5,5),  "nBTag":(0,0), "nPhoton":(0,0)} }
controlRegions["DY4p"] = { "parameters":{"dileptonic":True, "zWindow":"onZSFllTight", "nJet":(4,-1), "nBTag":(0,0), "nPhoton":(0,0)} }

# nPhoton0 nBTag1p CR for TTbar
controlRegions["TT3"]  = { "parameters":{"zWindow":"all", "nJet":(3,3),  "nBTag":(1,-1), "nPhoton":(0,0)} }
controlRegions["TT4p"] = { "parameters":{"zWindow":"all", "nJet":(4,-1), "nBTag":(1,-1), "nPhoton":(0,0)} }

# nPhoton0 nBTag0 CR for W+Jets
controlRegions["WJets3"]  = { "parameters":{"zWindow":"all", "nJet":(3,3),  "nBTag":(0,0), "nPhoton":(0,0)} }
controlRegions["WJets4p"] = { "parameters":{"zWindow":"all", "nJet":(4,-1), "nBTag":(0,0), "nPhoton":(0,0)} }

# nPhoton1p nBTag0 offZeg m(e,gamma) CR for V+Gamma
controlRegions["VG3"]  = { "parameters":{"zWindow":"offZeg", "nJet":(3,3),  "nBTag":(0,0), "nPhoton":(1,-1)} }
controlRegions["VG4p"] = { "parameters":{"zWindow":"offZeg", "nJet":(4,-1), "nBTag":(0,0), "nPhoton":(1,-1)} }

# nPhoton1p nBTag0 onZeg m(e,gamma) CR for misID ScaleFactor DY
controlRegions["misDY2"]  = { "parameters":{"zWindow":"onZeg", "nJet":(2,2),  "nBTag":(0,0), "nPhoton":(1,-1)} }
controlRegions["misDY3"]  = { "parameters":{"zWindow":"onZeg", "nJet":(3,3),  "nBTag":(0,0), "nPhoton":(1,-1)} }
controlRegions["misDY4"]  = { "parameters":{"zWindow":"onZeg", "nJet":(4,4),  "nBTag":(0,0), "nPhoton":(1,-1)} }
controlRegions["misDY5"]  = { "parameters":{"zWindow":"onZeg", "nJet":(5,5),  "nBTag":(0,0), "nPhoton":(1,-1)} }
controlRegions["misDY4p"] = { "parameters":{"zWindow":"onZeg", "nJet":(4,-1), "nBTag":(0,0), "nPhoton":(1,-1)} }

# nPhoton1p nBTag2 nJet2 offZeg m(e,gamma) CR for misID ScaleFactor TTbar
controlRegions["misTT2"] = { "parameters":{"zWindow":"offZeg", "nJet":(2,2),  "nBTag":(2,2), "nPhoton":(1,-1)} }

# updates for QCD estimation (else same settings)
QCD_updates = {"invertLepIso":True, "nBTag":(0,0), "addMisIDSF":True}


allRegions = controlRegions
allRegions.update(signalRegions)

