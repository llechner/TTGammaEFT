import os

from TTGammaEFT.Tools.user import results_directory, cache_directory

# Signal Regions Settings
SR3_SR_parameters    = { "name":"SR3",  "parameters":{"zWindow":"all", "nJet":(3,3),  "nBTag":(1,-1), "nPhoton":(1,-1)} }
SR4p_SR_parameters   = { "name":"SR4p", "parameters":{"zWindow":"all", "nJet":(4,-1), "nBTag":(1,-1), "nPhoton":(1,-1)} }
default_SR = SR4p_SR_parameters

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
#default_sampleList_cat0 = ["TTG","TT_pow","DY_LO","ZG","WG","WJets","other","QCD-DD"] #what samples to combine for category regions
#default_sampleList_cat1 = ["TTG","TT_pow","DY_LO","ZG","WG","WJets","other","QCD-DD"]
#default_sampleList_cat2 = ["TTG","TT_pow","DY_LO","ZG","WG","WJets","other","QCD-DD"]
#default_sampleList_cat3 = ["TTG","TT_pow","DY_LO","ZG","WG","WJets","other","QCD-DD"]

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

# dileptonic ee/mumu all m(l,l) nBTag0 nPhoton0 CR for DY ScaleFactor
DY3_CR_parameters     = { "name":"DY3",  "parameters":{"dileptonic":True, "zWindow":"onZSFllTight", "nJet":(3,3),  "nBTag":(0,0), "nPhoton":(0,0)} }
DY4p_CR_parameters    = { "name":"DY4p", "parameters":{"dileptonic":True, "zWindow":"onZSFllTight", "nJet":(4,-1), "nBTag":(0,0), "nPhoton":(0,0)} }

# nPhoton0 nBTag1p CR for TTbar
TT3_CR_parameters     = { "name":"TT3",  "parameters":{"zWindow":"all", "nJet":(3,3),  "nBTag":(1,-1), "nPhoton":(0,0)} }
TT4p_CR_parameters    = { "name":"TT4p", "parameters":{"zWindow":"all", "nJet":(4,-1), "nBTag":(1,-1), "nPhoton":(0,0)} }

# nPhoton0 nBTag0 CR for W+Jets
WJets3_CR_parameters  = { "name":"WJets3",  "parameters":{"zWindow":"all", "nJet":(3,3),  "nBTag":(0,0), "nPhoton":(0,0)} }
WJets4p_CR_parameters = { "name":"WJets4p", "parameters":{"zWindow":"all", "nJet":(4,-1), "nBTag":(0,0), "nPhoton":(0,0)} }

# nPhoton1p nBTag0 offZeg m(e,gamma) CR for V+Gamma
VG3_CR_parameters     = { "name":"VG3",  "parameters":{"zWindow":"offZeg", "nJet":(3,3),  "nBTag":(0,0), "nPhoton":(1,-1)} }
VG4p_CR_parameters    = { "name":"VG4p", "parameters":{"zWindow":"offZeg", "nJet":(4,-1), "nBTag":(0,0), "nPhoton":(1,-1)} }

# nPhoton1p nBTag0 onZeg m(e,gamma) CR for misID ScaleFactor DY
misDY3_CR_parameters  = { "name":"misDY3",  "parameters":{"zWindow":"onZeg", "nJet":(3,3),  "nBTag":(0,0), "nPhoton":(1,-1)} }
misDY4p_CR_parameters = { "name":"misDY4p", "parameters":{"zWindow":"onZeg", "nJet":(4,-1), "nBTag":(0,0), "nPhoton":(1,-1)} }

# nPhoton1p nBTag2 nJet2 offZeg m(e,gamma) CR for misID ScaleFactor TTbar
misTT2_CR_parameters  = { "name":"misTT2", "parameters":{"zWindow":"offZeg", "nJet":(2,2),  "nBTag":(2,2), "nPhoton":(1,-1)} }

# updates for QCD estimation (else same settings)
QCD_CR_updates        = {"invertLepIso":True, "nBTag":(0,0)}


allCR  = []
allCR += [ DY3_CR_parameters,    DY4p_CR_parameters    ]
allCR += [ VG3_CR_parameters,    VG4p_CR_parameters    ]
allCR += [ misDY3_CR_parameters, misDY4p_CR_parameters ]
allCR += [ misTT2_CR_parameters ]
#allCR += [ TT3_CR_parameters,    TT4p_CR_parameters    ]
#allCR += [ WJets3_CR_parameters, WJets4p_CR_parameters ]

allSR = [ SR3_SR_parameters, SR4p_SR_parameters ]

allSRCR = allSR + allCR
