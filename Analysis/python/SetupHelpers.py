import os

from TTGammaEFT.Tools.user       import results_directory, cache_directory
from TTGammaEFT.Analysis.regions import regionsTTG, noPhotonRegionTTG, inclRegionsTTG

lepChannels   = ["e", "mu"]
dilepChannels = ["eetight", "mumutight"]
allChannels   = ["all", "e", "mu", "eetight", "mumutight", "SFtight"]

signalRegions = {}
# Signal Regions Settings
# processes.keys() will be the proc visible in the combine card
# processes.values() is a list of processes that will be combined for the entry in combine
signalRegions["SR3"]  = { "parameters": { "zWindow":"all", "nJet":(3,3), "nBTag":(1,-1), "nPhoton":(1,-1) },
                          "channels":   lepChannels,
                          "regions":    regionsTTG,
                          "noPhotonCR": False,
                          "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
                                          "TTG_had": ["TTG_had"],
                                          "DY":      ["DY_LO_gen","DY_LO_misID","DY_LO_had"],
                                          "TT":      ["TT_pow_gen","TT_pow_misID","TT_pow_had"],
                                          "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
                                          "other":   ["WJets_gen","WJets_misID","WJets_had",
                                                      "other_gen","other_misID","other_had",
                                                      "QCD-DD",
                                                     ]
                                        }
                         }

signalRegions["SR4p"] = { "parameters": { "zWindow":"all", "nJet":(4,-1), "nBTag":(1,-1), "nPhoton":(1,-1) },
                          "channels":   lepChannels,
                          "regions":    regionsTTG,
                          "noPhotonCR": False,
                          "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
                                          "TTG_had": ["TTG_had"],
                                          "DY":      ["DY_LO_gen","DY_LO_misID","DY_LO_had"],
                                          "TT":      ["TT_pow_gen","TT_pow_misID","TT_pow_had"],
                                          "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
                                          "other":   ["WJets_gen","WJets_misID","WJets_had",
                                                      "other_gen","other_misID","other_had",
                                                      "QCD-DD",
                                                     ]
                                        }
                         }


default_SR = signalRegions["SR4p"]

#Define defaults here
default_nJet         = default_SR["parameters"]["nJet"]
default_nBTag        = default_SR["parameters"]["nBTag"]
default_nPhoton      = default_SR["parameters"]["nPhoton"]
default_zWindow      = default_SR["parameters"]["zWindow"]
default_dileptonic   = False
default_invLepIso    = False
default_addMisIDSF   = False
default_photonCat    = "all"

default_misIDSF      = 2.25
default_DYSF         = 1.10

default_sampleList      = ["TTG","TT_pow","DY_LO","ZG","WG","WJets","other","QCD-DD"]
default_processes       = { p:[p] for p in default_sampleList } # defaults are pure samples

# all processes are all samples + them splitted in photon categories
allProcesses            = default_sampleList
allProcesses           += [ s+"_gen"   for s in default_sampleList ]
allProcesses           += [ s+"_misID" for s in default_sampleList ]
allProcesses           += [ s+"_had"   for s in default_sampleList ]

analysis_results = os.path.join( results_directory, "analysis" )
cache_dir        = os.path.join( cache_directory,   "analysis" )
jmeVariations    = ["jer", "jerUp", "jerDown", "jesTotalUp", "jesTotalDown"]

# Control Regions Settings
controlRegions = {}
# dileptonic ee/mumu all m(l,l) nBTag0 nPhoton0 CR for DY ScaleFactor
controlRegions["DY2"]  = { "parameters": { "dileptonic":True, "zWindow":"onZSFllTight", "nJet":(2,2),  "nBTag":(0,0), "nPhoton":(0,0) },
                           "channels":   dilepChannels,
                           "regions":    noPhotonRegionTTG,
                           "noPhotonCR": True,
                           "processes":  { "signal": ["TTG"], # Signal is always needed
                                           "DY":     ["DY_LO"],
                                           "other":  ["TT_pow","ZG","WG","WJets","other"],
                                         }
                         }
                            
controlRegions["DY3"]  = { "parameters": { "dileptonic":True, "zWindow":"onZSFllTight", "nJet":(3,3),  "nBTag":(0,0), "nPhoton":(0,0) },
                           "channels":   dilepChannels,
                           "regions":    noPhotonRegionTTG,
                           "noPhotonCR": True,
                           "processes":  { "signal": ["TTG"], # Signal is always needed
                                           "DY":     ["DY_LO"],
                                           "other":  ["TT_pow","ZG","WG","WJets","other"],
                                         }
                         }

controlRegions["DY4"]  = { "parameters":{"dileptonic":True, "zWindow":"onZSFllTight", "nJet":(4,4),  "nBTag":(0,0), "nPhoton":(0,0) },
                           "channels":   dilepChannels,
                           "regions":    noPhotonRegionTTG,
                           "noPhotonCR": True,
                           "processes":  { "signal": ["TTG"], # Signal is always needed
                                           "DY":     ["DY_LO"],
                                           "other":  ["TT_pow","ZG","WG","WJets","other"],
                                         }
                         }

controlRegions["DY5"]  = { "parameters": { "dileptonic":True, "zWindow":"onZSFllTight", "nJet":(5,5),  "nBTag":(0,0), "nPhoton":(0,0) },
                           "channels":   dilepChannels,
                           "regions":    noPhotonRegionTTG,
                           "noPhotonCR": True,
                           "processes":  { "signal": ["TTG"], # Signal is always needed
                                           "DY":     ["DY_LO"],
                                           "other":  ["TT_pow","ZG","WG","WJets","other"],
                                         }
                         }

controlRegions["DY4p"] = { "parameters": { "dileptonic":True, "zWindow":"onZSFllTight", "nJet":(4,-1), "nBTag":(0,0), "nPhoton":(0,0) },
                           "channels":   dilepChannels,
                           "regions":    noPhotonRegionTTG,
                           "noPhotonCR": True,
                           "processes":  { "signal": ["TTG"], # Signal is always needed
                                           "DY":     ["DY_LO"],
                                           "other":  ["TT_pow","ZG","WG","WJets","other"],
                                         }
                         }


# nPhoton0 nBTag1p CR for TTbar
controlRegions["TT3"]  = { "parameters": { "zWindow":"all", "nJet":(3,3),  "nBTag":(1,-1), "nPhoton":(0,0) },
                           "channels":   lepChannels,
                           "regions":    noPhotonRegionTTG,
                           "noPhotonCR": True,
                           "processes":  { "signal": ["TTG"], # Signal is always needed
                                           "TT":     ["TT_pow"],
                                           "QCD":    ["QCD-DD"],
                                           "other":  ["DY_LO","ZG","WG","WJets","other"],
                                         }
                         }

controlRegions["TT4p"] = { "parameters": { "zWindow":"all", "nJet":(4,-1), "nBTag":(1,-1), "nPhoton":(0,0) },
                           "channels":   lepChannels,
                           "regions":    noPhotonRegionTTG,
                           "noPhotonCR": True,
                           "processes":  { "signal": ["TTG"], # Signal is always needed
                                           "TT":     ["TT_pow"],
                                           "QCD":    ["QCD-DD"],
                                           "other":  ["DY_LO","ZG","WG","WJets","other"],
                                         }
                         }


# nPhoton0 nBTag0 CR for W+Jets
controlRegions["WJets3"]  = { "parameters": { "zWindow":"all", "nJet":(3,3),  "nBTag":(0,0), "nPhoton":(0,0) },
                              "channels":   lepChannels,
                              "regions":    noPhotonRegionTTG,
                              "noPhotonCR": True,
                              "processes":  { "signal": ["TTG"], # Signal is always needed
                                              "WJets":  ["WJets"],
                                              "QCD":    ["QCD-DD"],
                                              "other":  ["TT_pow","ZG","WG","DY_LO","other"],
                                            }
                         }

controlRegions["WJets4p"] = { "parameters": { "zWindow":"all", "nJet":(4,-1), "nBTag":(0,0), "nPhoton":(0,0) },
                              "channels":   lepChannels,
                              "regions":    noPhotonRegionTTG,
                              "noPhotonCR": True,
                              "processes":  { "signal": ["TTG"], # Signal is always needed
                                              "WJets":  ["WJets"],
                                              "QCD":    ["QCD-DD"],
                                              "other":  ["TT_pow","ZG","WG","DY_LO","other"],
                                            }
                         }


# nPhoton1p nBTag0 offZeg m(e,gamma) CR for V+Gamma
controlRegions["VG3"]  = { "parameters": { "zWindow":"offZeg", "nJet":(3,3), "nBTag":(0,0), "nPhoton":(1,-1) },
                           "channels":   lepChannels,
                           "regions":    regionsTTG,
                           "noPhotonCR": False,
                           "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
                                           "TTG_had": ["TTG_had"],
                                           "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
                                           "QCD":     ["QCD-DD"],
                                           "other":   ["DY_LO_gen","DY_LO_misID","DY_LO_had",
                                                       "TT_pow_gen","TT_pow_misID","TT_pow_had",
                                                       "WJets_gen","WJets_misID","WJets_had",
                                                       "other_gen","other_misID","other_had",
                                                    ]
                                         }
                         }

controlRegions["VG4p"] = { "parameters": { "zWindow":"offZeg", "nJet":(4,-1), "nBTag":(0,0), "nPhoton":(1,-1)  },
                           "channels":   lepChannels,
                           "regions":    regionsTTG,
                           "noPhotonCR": False,
                           "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
                                           "TTG_had": ["TTG_had"],
                                           "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
                                           "QCD":     ["QCD-DD"],
                                           "other":   ["DY_LO_gen","DY_LO_misID","DY_LO_had",
                                                       "TT_pow_gen","TT_pow_misID","TT_pow_had",
                                                       "WJets_gen","WJets_misID","WJets_had",
                                                       "other_gen","other_misID","other_had",
                                                      ]
                                         }
                         }


# nPhoton1p nBTag0 onZeg m(e,gamma) CR for misID ScaleFactor DY
controlRegions["misDY2"]  = { "parameters": { "zWindow":"onZeg", "nJet":(2,2), "nBTag":(0,0), "nPhoton":(1,-1) },
                              "channels":   ["e"],
                              "regions":    regionsTTG,
                              "noPhotonCR": False,
                              "processes":  { "signal":      ["TTG_gen","TTG_misID"], # Signal is always needed
                                              "TTG_had":     ["TTG_had"],
                                              "DY_misID":    ["DY_LO_misID"],
                                              "other_misID": ["TT_pow_misID","ZG_misID","WG_misID","WJets_misID","other_misID"],
                                              "QCD":         ["QCD-DD"],
                                              "other":       ["DY_LO_gen",  "DY_LO_had",
                                                              "TT_pow_gen", "TT_pow_had",
                                                              "WG_gen",     "WG_had",
                                                              "ZG_gen",     "ZG_had",
                                                              "WJets_gen",  "WJets_had",
                                                              "other_gen",  "other_had",
                                                             ]
                                            }
                            }

controlRegions["misDY3"]  = { "parameters": { "zWindow":"onZeg", "nJet":(3,3), "nBTag":(0,0), "nPhoton":(1,-1) },
                              "channels":   ["e"],
                              "regions":    regionsTTG,
                              "noPhotonCR": False,
                              "processes":  { "signal":      ["TTG_gen","TTG_misID"], # Signal is always needed
                                              "TTG_had":     ["TTG_had"],
                                              "DY_misID":    ["DY_LO_misID"],
                                              "other_misID": ["TT_pow_misID","ZG_misID","WG_misID","WJets_misID","other_misID"],
                                              "QCD":         ["QCD-DD"],
                                              "other":       ["DY_LO_gen",  "DY_LO_had",
                                                              "TT_pow_gen", "TT_pow_had",
                                                              "WG_gen",     "WG_had",
                                                              "ZG_gen",     "ZG_had",
                                                              "WJets_gen",  "WJets_had",
                                                              "other_gen",  "other_had",
                                                             ]
                                            }
                            }

controlRegions["misDY4"]  = { "parameters": { "zWindow":"onZeg", "nJet":(4,4), "nBTag":(0,0), "nPhoton":(1,-1) },
                              "channels":   ["e"],
                              "regions":    regionsTTG,
                              "noPhotonCR": False,
                              "processes":  { "signal":      ["TTG_gen","TTG_misID"], # Signal is always needed
                                              "TTG_had":     ["TTG_had"],
                                              "DY_misID":    ["DY_LO_misID"],
                                              "other_misID": ["TT_pow_misID","ZG_misID","WG_misID","WJets_misID","other_misID"],
                                              "QCD":         ["QCD-DD"],
                                              "other":       ["DY_LO_gen",  "DY_LO_had",
                                                              "TT_pow_gen", "TT_pow_had",
                                                              "WG_gen",     "WG_had",
                                                              "ZG_gen",     "ZG_had",
                                                              "WJets_gen",  "WJets_had",
                                                              "other_gen",  "other_had",
                                                             ]
                                            }
                            }

controlRegions["misDY5"]  = { "parameters": { "zWindow":"onZeg", "nJet":(5,5), "nBTag":(0,0), "nPhoton":(1,-1) },
                              "channels":   ["e"],
                              "regions":    regionsTTG,
                              "noPhotonCR": False,
                              "processes":  { "signal":      ["TTG_gen","TTG_misID"], # Signal is always needed
                                              "TTG_had":     ["TTG_had"],
                                              "DY_misID":    ["DY_LO_misID"],
                                              "other_misID": ["TT_pow_misID","ZG_misID","WG_misID","WJets_misID","other_misID"],
                                              "QCD":         ["QCD-DD"],
                                              "other":       ["DY_LO_gen",  "DY_LO_had",
                                                              "TT_pow_gen", "TT_pow_had",
                                                              "WG_gen",     "WG_had",
                                                              "ZG_gen",     "ZG_had",
                                                              "WJets_gen",  "WJets_had",
                                                              "other_gen",  "other_had",
                                                             ]
                                            }
                            }

controlRegions["misDY4p"] = { "parameters": { "zWindow":"onZeg", "nJet":(4,-1), "nBTag":(0,0), "nPhoton":(1,-1) },
                              "channels":   ["e"],
                              "regions":    regionsTTG,
                              "noPhotonCR": False,
                              "processes":  { "signal":      ["TTG_gen","TTG_misID"], # Signal is always needed
                                              "TTG_had":     ["TTG_had"],
                                              "DY_misID":    ["DY_LO_misID"],
                                              "other_misID": ["TT_pow_misID","ZG_misID","WG_misID","WJets_misID","other_misID"],
                                              "QCD":         ["QCD-DD"],
                                              "other":       ["DY_LO_gen",  "DY_LO_had",
                                                              "TT_pow_gen", "TT_pow_had",
                                                              "WG_gen",     "WG_had",
                                                              "ZG_gen",     "ZG_had",
                                                              "WJets_gen",  "WJets_had",
                                                              "other_gen",  "other_had",
                                                             ]
                                            }
                            }


# nPhoton1p nBTag2 nJet2 offZeg m(e,gamma) CR for misID ScaleFactor TTbar
controlRegions["misTT2"] = { "parameters": { "zWindow":"offZeg", "nJet":(2,2), "nBTag":(2,2), "nPhoton":(1,-1) },
                             "channels":   lepChannels,
                             "regions":    regionsTTG,
                             "noPhotonCR": False,
                             "processes":  { "signal":      ["TTG_gen","TTG_misID"], # Signal is always needed
                                             "TTG_had":     ["TTG_had"],
                                             "TT_misID":    ["TT_pow_misID"],
                                             "other_misID": ["DY_LO_misID","ZG_misID","WG_misID","WJets_misID","other_misID"],
                                             "other":       ["DY_LO_gen",  "DY_LO_had",
                                                             "TT_pow_gen", "TT_pow_had",
                                                             "WG_gen",     "WG_had",
                                                             "ZG_gen",     "ZG_had",
                                                             "WJets_gen",  "WJets_had",
                                                             "other_gen",  "other_had",
                                                             "QCD-DD",
                                                            ]
                                            }
                           }


# updates for QCD estimation (else same settings)
QCD_updates = {"invertLepIso":True, "nBTag":(0,0), "addMisIDSF":True}


allRegions = controlRegions
allRegions.update(signalRegions)

