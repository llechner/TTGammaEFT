import os, copy

from TTGammaEFT.Tools.user       import results_directory, cache_directory
from TTGammaEFT.Analysis.regions import regionsTTG, noPhotonRegionTTG, inclRegionsTTG, inclRegionsTTGfake, regionsTTGfake
from TTGammaEFT.Samples.color    import color
lepChannels   = ["e", "mu"]
dilepChannels = ["eetight", "mumutight"]
allChannels   = ["all", "e", "mu", "eetight", "mumutight", "SFtight"]

default_sampleList      = ["TTG","TT_pow","DY_LO","ZG","WG","WJets","other","QCD-DD"]

# processes
signal      = ["TTG_gen","TTG_misID"]
#TTG_had     = ["TTG_had"]
DY_misID    = ["DY_LO_misID"]
DY          = ["DY_LO_gen","DY_LO_had"]
TT_misID    = ["TT_pow_misID"]
TT          = ["TT_pow_gen","TT_pow_had", "TTG_had"]
#VG_misID    = ["WG_misID","ZG_misID"]
VG          = ["WG_gen","WG_had","ZG_gen","ZG_had"]
other_misID = ["WJets_misID","other_misID","WG_misID","ZG_misID"]
other       = ["other_gen","other_had"]
WJets       = ["WJets_gen","WJets_had"]
QCD         = ["QCD-DD"]

processes = {
             "signal":      { "process":signal,      "color":color.TTG,          "texName":"tt#gamma (gen, misID)" },
             "DY":          { "process":DY,          "color":color.DY,           "texName":"DY (gen, had)"         },
             "DY_misID":    { "process":DY_misID,    "color":color.DY_misID,     "texName":"DY (misID)"            },
             "TT":          { "process":TT,          "color":color.TT,           "texName":"tt+tt#gamma (had)"     },
             "TT_misID":    { "process":TT_misID,    "color":color.TT_misID,     "texName":"tt (misID)"            },
             "VG":          { "process":VG,          "color":color.VGamma,       "texName":"V#gamma (gen, had)"    },
#             "VG_misID":    { "process":VG_misID,    "color":color.VGamma_misID, "texName":"V#gamma (misID)"      },
             "WJets":       { "process":WJets,       "color":color.WJets,        "texName":"WJets (gen, had)"      },
             "other":       { "process":other,       "color":color.Other,        "texName":"other (gen, had)"      },
             "other_misID": { "process":other_misID, "color":color.Other_misID,  "texName":"WJets+V#gamma+other (misID)" },
             "QCD":         { "process":QCD,         "color":color.QCD,          "texName":"multijets"             },
}

processesNoPhoton = {
                     "signal":      { "process":["TTG"],      "color":color.TTG,          "texName":"tt#gamma (gen, misID)" },
                     "DY":          { "process":["DY_LO"],    "color":color.DY,           "texName":"DY (gen, had)"         },
                     "DY_misID":    { "process":[],           "color":color.DY_misID,     "texName":"DY (misID)"            },
                     "TT":          { "process":["TT_pow"],   "color":color.TT,           "texName":"tt+tt#gamma (had)"     },
                     "TT_misID":    { "process":[],           "color":color.TT_misID,     "texName":"tt (misID)"            },
                     "VG":          { "process":["ZG","WG"],  "color":color.VGamma,       "texName":"V#gamma (gen, had)"    },
#                     "VG_misID":    { "process":[],           "color":color.VGamma_misID, "texName":"V#gamma (misID)"      },
                     "WJets":       { "process":["WJets"],    "color":color.WJets,        "texName":"WJets (gen, had)"      },
                     "other":       { "process":["other"],    "color":color.Other,        "texName":"other (gen, had)"      },
                     "other_misID": { "process":[],           "color":color.Other_misID,  "texName":"WJets+V#gamma+other (misID)" },
                     "QCD":         { "process":QCD,          "color":color.QCD,          "texName":"multijets"             },
}

default_processes = {
             "signal":      { "process":["TTG"]+signal,  "color":color.TTG,          "texName":"tt#gamma (gen, misID)" },
             "DY":          { "process":["DY_LO"]+DY,    "color":color.DY,           "texName":"DY  (gen, had)"        },
             "DY_misID":    { "process":DY_misID,        "color":color.DY_misID,     "texName":"DY (misID)"            },
             "TT":          { "process":["TT_pow"]+TT,   "color":color.TT,           "texName":"tt+tt#gamma (had)"     },
             "TT_misID":    { "process":TT_misID,        "color":color.TT_misID,     "texName":"tt (misID)"            },
             "VG":          { "process":["ZG","WG"]+VG,  "color":color.VGamma,       "texName":"V#gamma (gen, had)"    },
#             "VG_misID":    { "process":VG_misID,        "color":color.VGamma_misID, "texName":"V#gamma (misID)"      },
             "WJets":       { "process":["WJets"]+WJets, "color":color.WJets,        "texName":"WJets (gen, had)"      },
             "other":       { "process":["other"]+other, "color":color.Other,        "texName":"other (gen, had)"      },
             "other_misID": { "process":other_misID,     "color":color.Other_misID,  "texName":"WJets+V#gamma+other (misID)" },
             "QCD":         { "process":QCD,             "color":color.QCD,          "texName":"multijets"             },
}

processesMisIDPOI = {
             "signal":      { "process":other_misID+TT_misID+DY_misID, "color":color.DY_misID,     "texName":"misID (tt+DY+V#gamma+other)" },
             "TTG":         { "process":signal,                        "color":color.TTG,          "texName":"tt#gamma (gen, misID)" },
             "DY":          { "process":DY,                            "color":color.DY,           "texName":"DY (gen, had)"         },
             "TT":          { "process":TT,                            "color":color.TT,           "texName":"tt+tt#gamma (had)"     },
             "VG":          { "process":VG,                            "color":color.VGamma,       "texName":"V#gamma (gen, had)"    },
             "WJets":       { "process":WJets,                         "color":color.WJets,        "texName":"WJets (gen, had)"      },
             "other":       { "process":other,                         "color":color.Other,        "texName":"other (gen, had)"      },
             "QCD":         { "process":QCD,                           "color":color.QCD,          "texName":"multijets"             },
}


signalRegions = {}
# Signal Regions Settings
# processes.keys() will be the proc visible in the combine card
# processes.values() is a list of processes that will be combined for the entry in combine
signalRegions["SR3"]  = { "parameters": { "zWindow":"all", "nJet":(3,3), "nBTag":(1,-1), "nPhoton":(1,-1) },
                          "channels":   lepChannels,
                          "regions":    regionsTTG,
                          "inclRegion": inclRegionsTTG,
                          "noPhotonCR": False,
                          "processes":  processes,
#                          "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
#                                          "TTG_had": ["TTG_had"],
#                                          "DY":      ["DY_LO_gen","DY_LO_misID","DY_LO_had"],
#                                          "TT":      ["TT_pow_gen","TT_pow_misID","TT_pow_had"],
#                                          "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
#                                          "other":   ["WJets_gen","WJets_misID","WJets_had",
#                                                      "other_gen","other_misID","other_had",
#                                                      "QCD-DD",
#                                                     ]
#                                        }
                         }

signalRegions["SR4p"] = { "parameters": { "zWindow":"all", "nJet":(4,-1), "nBTag":(1,-1), "nPhoton":(1,-1) },
                          "channels":   lepChannels,
                          "regions":    regionsTTG,
                          "inclRegion": inclRegionsTTG,
                          "noPhotonCR": False,
                          "processes":  processes,
#                          "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
#                                          "TTG_had": ["TTG_had"],
#                                          "DY":      ["DY_LO_gen","DY_LO_misID","DY_LO_had"],
#                                          "TT":      ["TT_pow_gen","TT_pow_misID","TT_pow_had"],
#                                          "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
#                                          "other":   ["WJets_gen","WJets_misID","WJets_had",
#                                                      "other_gen","other_misID","other_had",
#                                                      "QCD-DD",
#                                                     ]
#                                        }
                         }

#lowChgIsolowSieie, highChgIsolowSieie, lowChgIsohighSieie, highChgIsohighSieie
signalRegions["SR3onM3"]  = { "parameters": { "zWindow":"all", "nJet":(3,3), "nBTag":(1,-1), "nPhoton":(1,-1), "m3Window":"onM3" },
                              "channels":   lepChannels,
                              "regions":    regionsTTG,
                              "inclRegion": inclRegionsTTG,
                              "noPhotonCR": False,
                              "processes":  processes,
#                              "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
#                                              "TTG_had": ["TTG_had"],
#                                              "DY":      ["DY_LO_gen","DY_LO_misID","DY_LO_had"],
#                                              "TT":      ["TT_pow_gen","TT_pow_misID","TT_pow_had"],
#                                              "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
#                                              "other":   ["WJets_gen","WJets_misID","WJets_had",
#                                                          "other_gen","other_misID","other_had",
#                                                          "QCD-DD",
#                                                         ]
#                                            }
                            }

signalRegions["SR3offM3"]  = { "parameters": { "zWindow":"all", "nJet":(3,3), "nBTag":(1,-1), "nPhoton":(1,-1), "m3Window":"offM3" },
                               "channels":   lepChannels,
                               "regions":    regionsTTG,
                               "inclRegion": inclRegionsTTG,
                               "noPhotonCR": False,
                               "processes":  processes,
#                               "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
#                                               "TTG_had": ["TTG_had"],
#                                               "DY":      ["DY_LO_gen","DY_LO_misID","DY_LO_had"],
#                                               "TT":      ["TT_pow_gen","TT_pow_misID","TT_pow_had"],
#                                               "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
#                                               "other":   ["WJets_gen","WJets_misID","WJets_had",
#                                                           "other_gen","other_misID","other_had",
#                                                           "QCD-DD",
#                                                          ]
#                                             }
                             }

signalRegions["SR3lowIso"]  = { "parameters": { "zWindow":"all", "nJet":(3,3), "nBTag":(1,-1), "nPhoton":(1,-1), "photonIso":"lowChgIsohighSieie" },
                                "channels":   lepChannels,
                                "regions":    regionsTTGfake,
                                "inclRegion": inclRegionsTTGfake,
                                "noPhotonCR": False,
                                "processes":  processes,
#                                "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
#                                                "TTG_had": ["TTG_had"],
#                                                "DY":      ["DY_LO_gen","DY_LO_misID","DY_LO_had"],
#                                                "TT":      ["TT_pow_gen","TT_pow_misID","TT_pow_had"],
#                                                "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
#                                                "other":   ["WJets_gen","WJets_misID","WJets_had",
#                                                            "other_gen","other_misID","other_had",
#                                                            "QCD-DD",
#                                                           ]
#                                              }
                              }

signalRegions["SR3highIso"]  = { "parameters": { "zWindow":"all", "nJet":(3,3), "nBTag":(1,-1), "nPhoton":(1,-1), "photonIso":"highChgIsohighSieie" },
                                 "channels":   lepChannels,
                                 "regions":    regionsTTGfake,
                                 "inclRegion": inclRegionsTTGfake,
                                 "noPhotonCR": False,
                                 "processes":  processes,
#                                 "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
#                                                 "TTG_had": ["TTG_had"],
#                                                 "DY":      ["DY_LO_gen","DY_LO_misID","DY_LO_had"],
#                                                 "TT":      ["TT_pow_gen","TT_pow_misID","TT_pow_had"],
#                                                 "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
#                                                 "other":   ["WJets_gen","WJets_misID","WJets_had",
#                                                             "other_gen","other_misID","other_had",
#                                                             "QCD-DD",
#                                                            ]
#                                               }
                               }

signalRegions["SR4ponM3"]  = { "parameters": { "zWindow":"all", "nJet":(4,-1), "nBTag":(1,-1), "nPhoton":(1,-1), "m3Window":"onM3" },
                              "channels":   lepChannels,
                              "regions":    regionsTTG,
                              "inclRegion": inclRegionsTTG,
                              "noPhotonCR": False,
                              "processes":  processes,
#                              "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
#                                              "TTG_had": ["TTG_had"],
#                                              "DY":      ["DY_LO_gen","DY_LO_misID","DY_LO_had"],
#                                              "TT":      ["TT_pow_gen","TT_pow_misID","TT_pow_had"],
#                                              "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
#                                              "other":   ["WJets_gen","WJets_misID","WJets_had",
#                                                          "other_gen","other_misID","other_had",
#                                                          "QCD-DD",
#                                                         ]
#                                            }
                            }

signalRegions["SR4poffM3"]  = { "parameters": { "zWindow":"all", "nJet":(4,-1), "nBTag":(1,-1), "nPhoton":(1,-1), "m3Window":"offM3" },
                               "channels":   lepChannels,
                               "regions":    regionsTTG,
                               "inclRegion": inclRegionsTTG,
                               "noPhotonCR": False,
                               "processes":  processes,
#                               "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
#                                               "TTG_had": ["TTG_had"],
#                                               "DY":      ["DY_LO_gen","DY_LO_misID","DY_LO_had"],
#                                               "TT":      ["TT_pow_gen","TT_pow_misID","TT_pow_had"],
#                                               "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
#                                               "other":   ["WJets_gen","WJets_misID","WJets_had",
#                                                           "other_gen","other_misID","other_had",
#                                                           "QCD-DD",
#                                                          ]
#                                             }
                             }

signalRegions["SR4plowIso"]  = { "parameters": { "zWindow":"all", "nJet":(4,-1), "nBTag":(1,-1), "nPhoton":(1,-1), "photonIso":"lowChgIsohighSieie" },
                                "channels":   lepChannels,
                                "regions":    regionsTTGfake,
                                "inclRegion": inclRegionsTTGfake,
                                "noPhotonCR": False,
                                "processes":  processes,
#                                "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
#                                                "TTG_had": ["TTG_had"],
#                                                "DY":      ["DY_LO_gen","DY_LO_misID","DY_LO_had"],
#                                                "TT":      ["TT_pow_gen","TT_pow_misID","TT_pow_had"],
#                                                "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
#                                                "other":   ["WJets_gen","WJets_misID","WJets_had",
#                                                            "other_gen","other_misID","other_had",
#                                                            "QCD-DD",
#                                                           ]
#                                              }
                              }

signalRegions["SR4phighIso"]  = { "parameters": { "zWindow":"all", "nJet":(4,-1), "nBTag":(1,-1), "nPhoton":(1,-1), "photonIso":"highChgIsohighSieie" },
                                 "channels":   lepChannels,
                                 "regions":    regionsTTGfake,
                                 "inclRegion": inclRegionsTTGfake,
                                 "noPhotonCR": False,
                                 "processes":  processes,
#                                 "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
#                                                 "TTG_had": ["TTG_had"],
#                                                 "DY":      ["DY_LO_gen","DY_LO_misID","DY_LO_had"],
#                                                 "TT":      ["TT_pow_gen","TT_pow_misID","TT_pow_had"],
#                                                 "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
#                                                 "other":   ["WJets_gen","WJets_misID","WJets_had",
#                                                             "other_gen","other_misID","other_had",
#                                                             "QCD-DD",
#                                                            ]
#                                               }
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
default_m3Window     = "all"
default_photonIso    = "lowChgIsolowSieie"

default_misIDSF      = 2.6
default_DYSF         = 1.09

# all processes are all samples + them splitted in photon categories
allProcesses            = copy.copy(default_sampleList)
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
                           "inclRegion": noPhotonRegionTTG,
                           "noPhotonCR": True,
                           "processes":  processesNoPhoton,
#                           "processes":  { "signal": ["TTG"], # Signal is always needed
#                                           "DY":     ["DY_LO"],
#                                           "other":  ["TT_pow","ZG","WG","WJets","other"],
#                                         }
                         }
                            
controlRegions["DY3"]  = { "parameters": { "dileptonic":True, "zWindow":"onZSFllTight", "nJet":(3,3),  "nBTag":(0,0), "nPhoton":(0,0) },
                           "channels":   dilepChannels,
                           "regions":    noPhotonRegionTTG,
                           "inclRegion": noPhotonRegionTTG,
                           "noPhotonCR": True,
                           "processes":  processesNoPhoton,
#                           "processes":  { "signal": ["TTG"], # Signal is always needed
#                                           "DY":     ["DY_LO"],
#                                           "other":  ["TT_pow","ZG","WG","WJets","other"],
#                                         }
                         }

controlRegions["DY4"]  = { "parameters":{"dileptonic":True, "zWindow":"onZSFllTight", "nJet":(4,4),  "nBTag":(0,0), "nPhoton":(0,0) },
                           "channels":   dilepChannels,
                           "regions":    noPhotonRegionTTG,
                           "inclRegion": noPhotonRegionTTG,
                           "noPhotonCR": True,
                           "processes":  processesNoPhoton,
#                           "processes":  { "signal": ["TTG"], # Signal is always needed
#                                           "DY":     ["DY_LO"],
#                                           "other":  ["TT_pow","ZG","WG","WJets","other"],
#                                         }
                         }

controlRegions["DY5"]  = { "parameters": { "dileptonic":True, "zWindow":"onZSFllTight", "nJet":(5,5),  "nBTag":(0,0), "nPhoton":(0,0) },
                           "channels":   dilepChannels,
                           "regions":    noPhotonRegionTTG,
                           "inclRegion": noPhotonRegionTTG,
                           "noPhotonCR": True,
                           "processes":  processesNoPhoton,
#                           "processes":  { "signal": ["TTG"], # Signal is always needed
#                                           "DY":     ["DY_LO"],
#                                           "other":  ["TT_pow","ZG","WG","WJets","other"],
#                                         }
                         }

controlRegions["DY4p"] = { "parameters": { "dileptonic":True, "zWindow":"onZSFllTight", "nJet":(4,-1), "nBTag":(0,0), "nPhoton":(0,0) },
                           "channels":   dilepChannels,
                           "regions":    noPhotonRegionTTG,
                           "inclRegion": noPhotonRegionTTG,
                           "noPhotonCR": True,
                           "processes":  processesNoPhoton,
#                           "processes":  { "signal": ["TTG"], # Signal is always needed
#                                           "DY":     ["DY_LO"],
#                                           "other":  ["TT_pow","ZG","WG","WJets","other"],
#                                         }
                         }


# nPhoton0 nBTag1p CR for TTbar
controlRegions["TT3"]  = { "parameters": { "zWindow":"all", "nJet":(3,3),  "nBTag":(1,-1), "nPhoton":(0,0) },
                           "channels":   lepChannels,
                           "regions":    noPhotonRegionTTG,
                           "inclRegion": noPhotonRegionTTG,
                           "noPhotonCR": True,
                           "processes":  processesNoPhoton,
#                           "processes":  { "signal": ["TTG"], # Signal is always needed
#                                           "TT":     ["TT_pow"],
#                                           "QCD":    ["QCD-DD"],
#                                           "other":  ["DY_LO","ZG","WG","WJets","other"],
#                                         }
                         }

controlRegions["TT4p"] = { "parameters": { "zWindow":"all", "nJet":(4,-1), "nBTag":(1,-1), "nPhoton":(0,0) },
                           "channels":   lepChannels,
                           "regions":    noPhotonRegionTTG,
                           "inclRegion": noPhotonRegionTTG,
                           "noPhotonCR": True,
                           "processes":  processesNoPhoton,
#                           "processes":  { "signal": ["TTG"], # Signal is always needed
#                                           "TT":     ["TT_pow"],
#                                           "QCD":    ["QCD-DD"],
#                                           "other":  ["DY_LO","ZG","WG","WJets","other"],
#                                         }
                         }


# nPhoton0 nBTag0 CR for W+Jets
controlRegions["WJets3"]  = { "parameters": { "zWindow":"all", "nJet":(3,3),  "nBTag":(0,0), "nPhoton":(0,0) },
                              "channels":   lepChannels,
                              "regions":    noPhotonRegionTTG,
                              "inclRegion": noPhotonRegionTTG,
                              "noPhotonCR": True,
                              "processes":  processesNoPhoton,
#                              "processes":  { "signal": ["TTG"], # Signal is always needed
#                                              "WJets":  ["WJets"],
#                                              "QCD":    ["QCD-DD"],
#                                              "other":  ["TT_pow","ZG","WG","DY_LO","other"],
#                                            }
                         }

controlRegions["WJets4p"] = { "parameters": { "zWindow":"all", "nJet":(4,-1), "nBTag":(0,0), "nPhoton":(0,0) },
                              "channels":   lepChannels,
                              "regions":    noPhotonRegionTTG,
                              "inclRegion": noPhotonRegionTTG,
                              "noPhotonCR": True,
                              "processes":  processesNoPhoton,
#                              "processes":  { "signal": ["TTG"], # Signal is always needed
#                                              "WJets":  ["WJets"],
#                                              "QCD":    ["QCD-DD"],
#                                              "other":  ["TT_pow","ZG","WG","DY_LO","other"],
#                                            }
                         }


# nPhoton1p nBTag0 offZeg m(e,gamma) CR for V+Gamma
controlRegions["VG2"]  = { "parameters": { "zWindow":"offZeg", "nJet":(2,2), "nBTag":(0,0), "nPhoton":(1,-1) },
                           "channels":   lepChannels,
                           "regions":    regionsTTG,
                           "inclRegion": inclRegionsTTG,
                           "noPhotonCR": False,
                           "processes":  processes,
#                           "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
#                                           "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
#                                           "QCD":     ["QCD-DD"],
#                                           "other":   ["DY_LO_gen","DY_LO_misID","DY_LO_had",
#                                                       "TT_pow_gen","TT_pow_misID","TT_pow_had",
#                                                       "WJets_gen","WJets_misID","WJets_had",
#                                                       "other_gen","other_misID","other_had",
#                                                       "TTG_had",
#                                                    ]
#                                         }
                         }

controlRegions["VG3"]  = { "parameters": { "zWindow":"offZeg", "nJet":(3,3), "nBTag":(0,0), "nPhoton":(1,-1) },
                           "channels":   lepChannels,
                           "regions":    regionsTTG,
                           "inclRegion": inclRegionsTTG,
                           "noPhotonCR": False,
                           "processes":  processes,
#                           "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
#                                           "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
#                                           "QCD":     ["QCD-DD"],
#                                           "other":   ["DY_LO_gen","DY_LO_misID","DY_LO_had",
#                                                       "TT_pow_gen","TT_pow_misID","TT_pow_had",
#                                                       "WJets_gen","WJets_misID","WJets_had",
#                                                       "other_gen","other_misID","other_had",
#                                                       "TTG_had",
#                                                    ]
#                                         }
                         }

controlRegions["VG4"]  = { "parameters": { "zWindow":"offZeg", "nJet":(4,4), "nBTag":(0,0), "nPhoton":(1,-1) },
                           "channels":   lepChannels,
                           "regions":    regionsTTG,
                           "inclRegion": inclRegionsTTG,
                           "noPhotonCR": False,
                           "processes":  processes,
#                           "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
#                                           "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
#                                           "QCD":     ["QCD-DD"],
#                                           "other":   ["DY_LO_gen","DY_LO_misID","DY_LO_had",
#                                                       "TT_pow_gen","TT_pow_misID","TT_pow_had",
#                                                       "WJets_gen","WJets_misID","WJets_had",
#                                                       "other_gen","other_misID","other_had",
#                                                       "TTG_had",
#                                                    ]
#                                         }
                         }

controlRegions["VG5"]  = { "parameters": { "zWindow":"offZeg", "nJet":(5,5), "nBTag":(0,0), "nPhoton":(1,-1) },
                           "channels":   lepChannels,
                           "regions":    regionsTTG,
                           "inclRegion": inclRegionsTTG,
                           "noPhotonCR": False,
                           "processes":  processes,
#                           "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
#                                           "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
#                                           "QCD":     ["QCD-DD"],
#                                           "other":   ["DY_LO_gen","DY_LO_misID","DY_LO_had",
#                                                       "TT_pow_gen","TT_pow_misID","TT_pow_had",
#                                                       "WJets_gen","WJets_misID","WJets_had",
#                                                       "other_gen","other_misID","other_had",
#                                                       "TTG_had",
#                                                    ]
#                                         }
                         }

controlRegions["VG4p"] = { "parameters": { "zWindow":"offZeg", "nJet":(4,-1), "nBTag":(0,0), "nPhoton":(1,-1)  },
                           "channels":   lepChannels,
                           "regions":    regionsTTG,
                           "inclRegion": inclRegionsTTG,
                           "noPhotonCR": False,
                           "processes":  processes,
#                           "processes":  { "signal":  ["TTG_gen","TTG_misID"], # Signal is always needed
#                                           "VG":      ["WG_gen","WG_misID","WG_had","ZG_gen","ZG_misID","ZG_had"],
#                                           "QCD":     ["QCD-DD"],
#                                           "other":   ["DY_LO_gen","DY_LO_misID","DY_LO_had",
#                                                       "TT_pow_gen","TT_pow_misID","TT_pow_had",
#                                                       "WJets_gen","WJets_misID","WJets_had",
#                                                       "other_gen","other_misID","other_had",
#                                                       "TTG_had",
#                                                      ]
#                                         }
                         }


# nPhoton1p nBTag0 onZeg m(e,gamma) CR for misID ScaleFactor DY
controlRegions["misDY2"]  = { "parameters": { "zWindow":"onZeg", "nJet":(2,2), "nBTag":(0,0), "nPhoton":(1,-1) },
                              "channels":   ["e"],
                              "regions":    regionsTTG,
                              "inclRegion": inclRegionsTTG,
                              "noPhotonCR": False,
                              "processes":  processes,
#                              "processes":  { "signal":      ["TTG_gen"], # Signal is always needed
#                                              "misID":       ["TTG_misID", "DY_LO_misID","TT_pow_misID","ZG_misID","WG_misID","WJets_misID","other_misID"],
#                                              "QCD":         ["QCD-DD"],
#                                              "other":       ["DY_LO_gen",  "DY_LO_had",
#                                                              "TT_pow_gen", "TT_pow_had",
#                                                              "WG_gen",     "WG_had",
#                                                              "ZG_gen",     "ZG_had",
#                                                              "WJets_gen",  "WJets_had",
#                                                              "other_gen",  "other_had",
#                                                              "TTG_had",
#                                                             ]
#                                            }
                            }

controlRegions["misDY3"]  = { "parameters": { "zWindow":"onZeg", "nJet":(3,3), "nBTag":(0,0), "nPhoton":(1,-1) },
                              "channels":   ["e"],
                              "regions":    regionsTTG,
                              "inclRegion": inclRegionsTTG,
                              "noPhotonCR": False,
                              "processes":  processes,
#                              "processes":  { "signal":      ["TTG_gen"], # Signal is always needed
#                                              "misID":       ["TTG_misID","DY_LO_misID","TT_pow_misID","ZG_misID","WG_misID","WJets_misID","other_misID"],
#                                              "QCD":         ["QCD-DD"],
#                                              "other":       ["DY_LO_gen",  "DY_LO_had",
#                                                              "TT_pow_gen", "TT_pow_had",
#                                                              "WG_gen",     "WG_had",
#                                                              "ZG_gen",     "ZG_had",
#                                                              "WJets_gen",  "WJets_had",
#                                                              "other_gen",  "other_had",
#                                                              "TTG_had",
#                                                             ]
#                                            }
                            }

controlRegions["misDY4"]  = { "parameters": { "zWindow":"onZeg", "nJet":(4,4), "nBTag":(0,0), "nPhoton":(1,-1) },
                              "channels":   ["e"],
                              "regions":    regionsTTG,
                              "inclRegion": inclRegionsTTG,
                              "noPhotonCR": False,
                              "processes":  processes,
#                              "processes":  { "signal":      ["TTG_gen"], # Signal is always needed
#                                              "misID":       ["TTG_misID","DY_LO_misID","TT_pow_misID","ZG_misID","WG_misID","WJets_misID","other_misID"],
#                                              "QCD":         ["QCD-DD"],
#                                              "other":       ["DY_LO_gen",  "DY_LO_had",
#                                                              "TT_pow_gen", "TT_pow_had",
#                                                              "WG_gen",     "WG_had",
#                                                              "ZG_gen",     "ZG_had",
#                                                              "WJets_gen",  "WJets_had",
#                                                              "other_gen",  "other_had",
#                                                              "TTG_had",
#                                                             ]
#                                            }
                            }

controlRegions["misDY5"]  = { "parameters": { "zWindow":"onZeg", "nJet":(5,5), "nBTag":(0,0), "nPhoton":(1,-1) },
                              "channels":   ["e"],
                              "regions":    regionsTTG,
                              "inclRegion": inclRegionsTTG,
                              "noPhotonCR": False,
                              "processes":  processes,
#                              "processes":  { "signal":      ["TTG_gen"], # Signal is always needed
#                                              "misID":       ["TTG_misID","DY_LO_misID","TT_pow_misID","ZG_misID","WG_misID","WJets_misID","other_misID"],
#                                              "QCD":         ["QCD-DD"],
#                                              "other":       ["DY_LO_gen",  "DY_LO_had",
#                                                              "TT_pow_gen", "TT_pow_had",
#                                                              "WG_gen",     "WG_had",
#                                                              "ZG_gen",     "ZG_had",
#                                                              "WJets_gen",  "WJets_had",
#                                                              "other_gen",  "other_had",
#                                                              "TTG_had",
#                                                             ]
#                                            }
                            }

controlRegions["misDY4p"] = { "parameters": { "zWindow":"onZeg", "nJet":(4,-1), "nBTag":(0,0), "nPhoton":(1,-1) },
                              "channels":   ["e"],
                              "regions":    regionsTTG,
                              "inclRegion": inclRegionsTTG,
                              "noPhotonCR": False,
                              "processes":  processes,
#                              "processes":  { "signal":      ["TTG_gen"], # Signal is always needed
#                                              "misID":       ["TTG_misID","DY_LO_misID","TT_pow_misID","ZG_misID","WG_misID","WJets_misID","other_misID"],
#                                              "QCD":         ["QCD-DD"],
#                                              "other":       ["DY_LO_gen",  "DY_LO_had",
#                                                              "TT_pow_gen", "TT_pow_had",
#                                                              "WG_gen",     "WG_had",
#                                                              "ZG_gen",     "ZG_had",
#                                                              "WJets_gen",  "WJets_had",
#                                                              "other_gen",  "other_had",
#                                                              "TTG_had",
#                                                             ]
#                                            }
                            }


# nPhoton1p nBTag2 nJet2 offZeg m(e,gamma) CR for misID ScaleFactor TTbar
controlRegions["misTT2"] = { "parameters": { "zWindow":"offZeg", "nJet":(2,2), "nBTag":(2,2), "nPhoton":(1,-1) },
                             "channels":   lepChannels,
                             "regions":    regionsTTG,
                             "inclRegion": inclRegionsTTG,
                             "noPhotonCR": False,
                             "processes":  processes,
#                             "processes":  { "signal":      ["TTG_gen"], # Signal is always needed
#                                             "misID":       ["TTG_misID","TT_pow_misID", "DY_LO_misID","ZG_misID","WG_misID","WJets_misID","other_misID"],
#                                             "other":       ["DY_LO_gen",  "DY_LO_had",
#                                                             "TT_pow_gen", "TT_pow_had",
#                                                             "WG_gen",     "WG_had",
#                                                             "ZG_gen",     "ZG_had",
#                                                             "WJets_gen",  "WJets_had",
#                                                             "other_gen",  "other_had",
#                                                             "TTG_had",
#                                                             "QCD-DD",
#                                                            ]
#                                            }
                           }


# updates for QCD estimation (else same settings)
QCD_updates = {"invertLepIso":True, "nBTag":(0,0), "addMisIDSF":True, "zWindow":"all"}


allRegions = copy.copy(controlRegions)
allRegions.update(signalRegions)

# RegionPlot ordering
limitOrdering  = []

noPCR = [ key for key, val in allRegions.items() if val["noPhotonCR"] ]
noPCR.sort()
limitOrdering += noPCR

pCR = [ key for key, val in controlRegions.items() if not val["noPhotonCR"] ]
pCR.sort()
limitOrdering += pCR

pSR = [ key for key, val in signalRegions.items() ]
pSR.sort()
limitOrdering += pSR
