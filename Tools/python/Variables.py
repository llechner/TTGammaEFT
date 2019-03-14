# Definition of variables and types in nanoAOD and GENSIM Samples
# flags for variables also in data nanoAOD and if it is used in plots
# read:   read variable from central nanoAOD (used in postprocessing)
# write:  write variable to root file in postprocessing
# inData: variable is also contained in data root files (not the case for e.g. gen-info variables)
# inPlot: variable is used in skim plot script (useful to reduce memory in plot scripts)
# postprocessed: chooses either 'read' (postprocessed = False) or 'write' (postProcessed = True)

class Variable:

    def __init__( self, name, type, read=True, write=True, inData=False, inPlot=False ):

        self.name   = name
        self.type   = type
        self.inData = inData
        self.inPlot = inPlot
        self.read   = read
        self.write  = write


class NanoVariables:
    """ Definition of variables in nanoAOD samples
    """

    def __init__( self, year ):

        if year not in [ 2016, 2017, 2018 ]:
            raise Exception( "Variables not implemented for year %s"%year )

        self.knownParticleLists = [ "Electron", "Muon", "Lepton", "Jet", "BJet", "Photon", "Gen", "GenJet" ]

        self.ElectronVariables = [\
                                  Variable( "pt",                       "F", read=True,  write=True,  inData=True,  inPlot=True ),
                                  Variable( "eta",                      "F", read=True,  write=True,  inData=True,  inPlot=True ),
                                  Variable( "phi",                      "F", read=True,  write=True,  inData=True,  inPlot=True ),
                                  Variable( "pfRelIso03_all",           "F", read=True,  write=True,  inData=True,  inPlot=True ),
                                  Variable( "pfRelIso03_chg",           "F", read=True,  write=True,  inData=True,  inPlot=True ),
                                  Variable( "eInvMinusPInv",            "F", read=True,  write=True,  inData=True,  inPlot=True ),
                                  Variable( "hoe",                      "F", read=True,  write=True,  inData=True,  inPlot=True ),
                                  Variable( "sieie",                    "F", read=True,  write=True,  inData=True,  inPlot=True ),
                                  Variable( "sip3d",                    "F", read=True,  write=True,  inData=True,  inPlot=True ),
                                  Variable( "convVeto",                 "O", read=True,  write=True,  inData=True,  inPlot=True ),
                                  Variable( "cutBased",                 "I", read=True,  write=True,  inData=True,  inPlot=True ),
                                  Variable( "pdgId",                    "I", read=True,  write=True,  inData=True,  inPlot=True ),
                                  Variable( "vidNestedWPBitmap",        "I", read=True,  write=True,  inData=True,  inPlot=True ),

                                  Variable( "lostHits",                 "b", read=True,  write=False, inData=True,  inPlot=False ),
                                  Variable( "lostHits",                 "I", read=False, write=True,  inData=True,  inPlot=True ),

                                  Variable( "deltaEtaSC",               "F", read=True,  write=True,  inData=True,  inPlot=False ),
                                  Variable( "dr03EcalRecHitSumEt",      "F", read=True,  write=False, inData=True,  inPlot=False ),
                                  Variable( "dr03HcalDepth1TowerSumEt", "F", read=True,  write=False, inData=True,  inPlot=False ),
                                  Variable( "dr03TkSumPt",              "F", read=True,  write=False, inData=True,  inPlot=False ),
                                  Variable( "dxy",                      "F", read=True,  write=True,  inData=True,  inPlot=False ),
                                  Variable( "dxyErr",                   "F", read=True,  write=True,  inData=True,  inPlot=False ),
                                  Variable( "dz",                       "F", read=True,  write=True,  inData=True,  inPlot=False ),
                                  Variable( "dzErr",                    "F", read=True,  write=True,  inData=True,  inPlot=False ),
                                  Variable( "energyErr",                "F", read=True,  write=False, inData=True,  inPlot=False ),
                                  Variable( "ip3d",                     "F", read=True,  write=True,  inData=True,  inPlot=False ),
                                  Variable( "mass",                     "F", read=True,  write=True,  inData=True,  inPlot=False ),
                                  Variable( "miniPFRelIso_all",         "F", read=True,  write=True,  inData=True,  inPlot=False ),
                                  Variable( "miniPFRelIso_chg",         "F", read=True,  write=True,  inData=True,  inPlot=False ),
                                  Variable( "r9",                       "F", read=True,  write=True,  inData=True,  inPlot=False ),
                                  Variable( "mvaTTH",                   "F", read=True,  write=False, inData=True,  inPlot=False ),
                                  Variable( "charge",                   "I", read=True,  write=True,  inData=True,  inPlot=False ),
                                  Variable( "jetIdx",                   "I", read=True,  write=False, inData=True,  inPlot=False ),
                                  Variable( "photonIdx",                "I", read=True,  write=False, inData=True,  inPlot=False ),
                                  Variable( "tightCharge",              "I", read=True,  write=False, inData=True,  inPlot=False ),
                                  Variable( "cutBased_HEEP",            "O", read=True,  write=True,  inData=True,  inPlot=False ),
                                  Variable( "isPFcand",                 "O", read=True,  write=True,  inData=True,  inPlot=False ),
                                  Variable( "cleanmask",                "O", read=True,  write=True,  inData=True,  inPlot=False ),

                                  Variable( "genPartIdx",               "I", read=True,  write=True,  inData=False, inPlot=False ),

                                  Variable( "genPartFlav",              "b", read=True,  write=False, inData=False, inPlot=False ),
                                  Variable( "genPartFlav",              "I", read=False, write=True,  inData=False, inPlot=False ),
                                 ]

        self.MuonVariables = [\
                              Variable( "pt",               "F", read=True,  write=True,  inData=True,  inPlot=True ),
                              Variable( "eta",              "F", read=True,  write=True,  inData=True,  inPlot=True ),
                              Variable( "phi",              "F", read=True,  write=True,  inData=True,  inPlot=True ),
                              Variable( "pfRelIso03_all",   "F", read=True,  write=True,  inData=True,  inPlot=True ),
                              Variable( "pfRelIso03_chg",   "F", read=True,  write=True,  inData=True,  inPlot=True ),
                              Variable( "sip3d",            "F", read=True,  write=True,  inData=True,  inPlot=True ),
                              Variable( "mediumId",         "O", read=True,  write=True,  inData=True,  inPlot=True ),
                              Variable( "pdgId",            "I", read=True,  write=True,  inData=True,  inPlot=True ),

                              Variable( "dxy",              "F", read=True,  write=True,  inData=True,  inPlot=False ),
                              Variable( "dxyErr",           "F", read=True,  write=True,  inData=True,  inPlot=False ),
                              Variable( "dz",               "F", read=True,  write=True,  inData=True,  inPlot=False ),
                              Variable( "dzErr",            "F", read=True,  write=True,  inData=True,  inPlot=False ),
                              Variable( "mass",             "F", read=True,  write=True,  inData=True,  inPlot=False ),
                              Variable( "dxy",              "F", read=True,  write=True,  inData=True,  inPlot=False ),
                              Variable( "miniPFRelIso_all", "F", read=True,  write=True,  inData=True,  inPlot=False ),
                              Variable( "miniPFRelIso_chg", "F", read=True,  write=True,  inData=True,  inPlot=False ),
                              Variable( "pfRelIso04_all",   "F", read=True,  write=True,  inData=True,  inPlot=False ),
                              Variable( "ptErr",            "F", read=True,  write=False, inData=True,  inPlot=False ),
                              Variable( "segmentComp",      "F", read=True,  write=False, inData=True,  inPlot=False ),
                              Variable( "mvaTTH",           "F", read=True,  write=False, inData=True,  inPlot=False ),
                              Variable( "charge",           "I", read=True,  write=True,  inData=True,  inPlot=False ),
                              Variable( "jetIdx",           "I", read=True,  write=False, inData=True,  inPlot=False ),
                              Variable( "nStations",        "I", read=True,  write=True,  inData=True,  inPlot=False ),
                              Variable( "nTrackerLayers",   "I", read=True,  write=True,  inData=True,  inPlot=False ),
                              Variable( "tightCharge",      "I", read=True,  write=False, inData=True,  inPlot=False ),
                              Variable( "highPtId",         "I", read=True,  write=False, inData=True,  inPlot=False ),
                              Variable( "isPFcand",         "O", read=True,  write=True,  inData=True,  inPlot=False ),
                              Variable( "softId",           "O", read=True,  write=True,  inData=True,  inPlot=False ),
                              Variable( "tightId",          "O", read=True,  write=True,  inData=True,  inPlot=False ),
                              Variable( "cleanmask",        "O", read=True,  write=True,  inData=True,  inPlot=False ),
                              Variable( "isGlobal",         "O", read=True,  write=True,  inData=True,  inPlot=False ),
                              Variable( "isTracker",        "O", read=True,  write=True,  inData=True,  inPlot=False ),

                              Variable( "genPartIdx",       "I", read=True,  write=True,  inData=False, inPlot=False ),

                              Variable( "pfIsoId",          "b", read=True,  write=False, inData=True,  inPlot=False ),
                              Variable( "pfIsoId",          "I", read=False, write=True,  inData=True,  inPlot=False ),
                              Variable( "genPartFlav",      "b", read=True,  write=False, inData=False, inPlot=False ),
                              Variable( "genPartFlav",      "I", read=False, write=True,  inData=False, inPlot=False ),
                             ]

        self.JetVariables = [\
                             Variable( "pt",            "F", read=True,  write=True,  inData=True,  inPlot=True ),
                             Variable( "eta",           "F", read=True,  write=True,  inData=True,  inPlot=True ),
                             Variable( "phi",           "F", read=True,  write=True,  inData=True,  inPlot=True ),
                             Variable( "neEmEF",        "F", read=True,  write=True,  inData=True,  inPlot=True ),
                             Variable( "neHEF",         "F", read=True,  write=True,  inData=True,  inPlot=True ),
                             Variable( "chEmEF",        "F", read=True,  write=True,  inData=True,  inPlot=True ),
                             Variable( "chHEF",         "F", read=True,  write=True,  inData=True,  inPlot=True ),
                             Variable( "btagCSVV2",     "F", read=True,  write=True,  inData=True,  inPlot=True ),
                             Variable( "btagDeepB",     "F", read=True,  write=True,  inData=True,  inPlot=True ),
                             Variable( "nConstituents", "I", read=True,  write=True,  inData=True,  inPlot=True ),
                             Variable( "cleanmask",     "O", read=True,  write=True,  inData=True,  inPlot=True ),
                             Variable( "jetId",         "I", read=True,  write=True,  inData=True,  inPlot=True ),

                             Variable( "isGood",        "I", read=False, write=True,  inData=True,  inPlot=False ), #set to true after the next pp
                             Variable( "isBJet",        "I", read=False, write=True,  inData=True,  inPlot=False ), #set to true after the next pp

                             Variable( "area",          "F", read=True,  write=True,  inData=True,  inPlot=False ),
                             Variable( "btagCMVA",      "F", read=True,  write=False, inData=True,  inPlot=False ),
                             Variable( "btagDeepC",     "F", read=True,  write=False, inData=True,  inPlot=False ),
                             Variable( "mass",          "F", read=True,  write=True,  inData=True,  inPlot=False ),
                             Variable( "qgl",           "F", read=True,  write=False, inData=True,  inPlot=False ),
                             Variable( "rawFactor",     "F", read=True,  write=False, inData=True,  inPlot=False ),
                             Variable( "electronIdx1",  "I", read=True,  write=False, inData=True,  inPlot=False ),
                             Variable( "electronIdx2",  "I", read=True,  write=False, inData=True,  inPlot=False ),
                             Variable( "muonIdx1",      "I", read=True,  write=False, inData=True,  inPlot=False ),
                             Variable( "muonIdx2",      "I", read=True,  write=False, inData=True,  inPlot=False ),
                             Variable( "nElectrons",    "I", read=True,  write=True,  inData=True,  inPlot=False ),
                             Variable( "nMuons",        "I", read=True,  write=True,  inData=True,  inPlot=False ),
                             Variable( "puId",          "I", read=True,  write=True,  inData=True,  inPlot=False ),

                             Variable( "genJetIdx",     "I", read=True,  write=True,  inData=False, inPlot=False ),
                             Variable( "hadronFlavour", "I", read=True,  write=True,  inData=False, inPlot=False ),
                             Variable( "partonFlavour", "I", read=True,  write=True,  inData=False, inPlot=False ),
                            ]

        self.BJetVariables = [\
                              Variable( "pt",  "F", read=True,  write=True,  inData=True, inPlot=True ),
                              Variable( "eta", "F", read=True,  write=True,  inData=True, inPlot=True ),
                              Variable( "phi", "F", read=True,  write=True,  inData=True, inPlot=True ),
                             ]

        photonCutVarName = "cutBased" if year==2016 else "cutBasedBitmap"

        self.PhotonVariables = [\
                                Variable( "eta",               "F", read=True,  write=True,  inData=True,  inPlot=True ),
                                Variable( "hoe",               "F", read=True,  write=True,  inData=True,  inPlot=True ),
                                Variable( "pfRelIso03_all",    "F", read=True,  write=True,  inData=True,  inPlot=True ),
                                Variable( "pfRelIso03_chg",    "F", read=True,  write=True,  inData=True,  inPlot=True ),
                                Variable( "phi",               "F", read=True,  write=True,  inData=True,  inPlot=True ),
                                Variable( "pt",                "F", read=True,  write=True,  inData=True,  inPlot=True ),
                                Variable( "sieie",             "F", read=True,  write=True,  inData=True,  inPlot=True ),
                                Variable( photonCutVarName,    "I", read=True,  write=True,  inData=True,  inPlot=True ),
                                Variable( "electronVeto",      "O", read=True,  write=True,  inData=True,  inPlot=True ),
                                Variable( "pixelSeed",         "O", read=True,  write=True,  inData=True,  inPlot=True ),
                                Variable( "pdgId",             "I", read=True,  write=True,  inData=True,  inPlot=True ),
                                Variable( "vidNestedWPBitmap", "I", read=True,  write=True,  inData=True,  inPlot=True ),

                                Variable( "energyErr",         "F", read=True,  write=False, inData=True,  inPlot=False ),
                                Variable( "mass",              "F", read=True,  write=True,  inData=True,  inPlot=False ),
                                Variable( "mvaID",             "F", read=True,  write=False, inData=True,  inPlot=False ),
                                Variable( "r9",                "F", read=True,  write=True,  inData=True,  inPlot=False ),
                                Variable( "charge",            "I", read=True,  write=True,  inData=True,  inPlot=False ),
                                Variable( "electronIdx",       "I", read=True,  write=False, inData=True,  inPlot=False ),
                                Variable( "jetIdx",            "I", read=True,  write=False, inData=True,  inPlot=False ),
                                Variable( "mvaID_WP80",        "O", read=True,  write=False, inData=True,  inPlot=False ),
                                Variable( "mvaID_WP90",        "O", read=True,  write=False, inData=True,  inPlot=False ),
                                Variable( "cleanmask",         "O", read=True,  write=True,  inData=True,  inPlot=False ),
 
                                Variable( "genPartIdx",        "I", read=True,  write=True,  inData=False, inPlot=False ),

                                Variable( "genPartFlav",       "b", read=True,  write=False, inData=False, inPlot=False ),
                                Variable( "genPartFlav",       "I", read=False, write=True,  inData=False, inPlot=False ),
                                Variable( "photonCat",         "I", read=False, write=True,  inData=True,  inPlot=True ),
                               ]


        self.GenVariables = [\
                             Variable( "pt",               "F", read=True,  write=True,  inData=False,  inPlot=False ),
                             Variable( "eta",              "F", read=True,  write=True,  inData=False,  inPlot=False ),
                             Variable( "phi",              "F", read=True,  write=True,  inData=False,  inPlot=False ),
                             Variable( "mass",             "F", read=True,  write=True,  inData=False,  inPlot=False ),
                             Variable( "pdgId",            "I", read=True,  write=True,  inData=False,  inPlot=False ),
                             Variable( "genPartIdxMother", "I", read=True,  write=True,  inData=False,  inPlot=False ),
                             Variable( "status",           "I", read=True,  write=True,  inData=False,  inPlot=False ),
                             Variable( "statusFlags" ,     "I", read=True,  write=True,  inData=False,  inPlot=False ),
                            ]

        self.GenJetVariables = [\
                                Variable( "pt",            "F", read=True,  write=True,  inData=False,  inPlot=False ),
                                Variable( "eta",           "F", read=True,  write=True,  inData=False,  inPlot=False ),
                                Variable( "phi",           "F", read=True,  write=True,  inData=False,  inPlot=False ),
                                Variable( "mass",          "F", read=True,  write=True,  inData=False,  inPlot=False ),
                                Variable( "partonFlavour", "I", read=True,  write=True,  inData=False,  inPlot=False ),
                                Variable( "hadronFlavour", "I", read=True,  write=True,  inData=False,  inPlot=False ),
                               ]

    def getVariableObjects( self, particle, postprocessed=False, data=False, plot=False ):

        if particle not in self.knownParticleLists:
            raise Exception( "Variablelist not implemented for particle %s! Please use one of the following: %s"%( particle, ", ".join( self.knownParticleLists ) ) )

        if particle == "Lepton":
            varList = self.ElectronVariables + self.MuonVariables
        else:
            varList = getattr( self, "%sVariables"%particle )

        varList = filter( lambda var: var.write if postprocessed else var.read, varList ) 
        if data: varList = filter( lambda var: var.inData, varList )
        if plot: varList = filter( lambda var: var.inPlot, varList )

        return varList

    def getVariableNameList( self, particle, postprocessed=False, data=False, plot=False ):
        varList = self.getVariableObjects( particle, postprocessed=postprocessed, data=data, plot=plot )
        return list( set( map( lambda var: var.name, varList ) ) )


    def getVariables( self, particle, postprocessed=False, data=False, plot=False ):
        varList = self.getVariableObjects( particle, postprocessed=postprocessed, data=data, plot=plot )
        return list( set( map( lambda var: "/".join( [var.name, var.type] ), varList ) ) )


    def getVariableString( self, particle, postprocessed=False, data=False, plot=False ):
        return ','.join( self.getVariables( particle, postprocessed=postprocessed, data=data, plot=plot ) )


if __name__ == "__main__":
    Var = NanoVariables( 2017 )
    print Var.getVariableNameList( "Electron", postprocessed=True )
    print Var.getVariables( "Electron", postprocessed=True )
    print Var.getVariableString( "Electron", postprocessed=True )
    print
    print Var.getVariableNameList( "Muon", postprocessed=True )
    print Var.getVariables( "Muon", postprocessed=True )
    print Var.getVariableString( "Muon", postprocessed=True )
    print
    print Var.getVariableNameList( "Lepton", postprocessed=True )
    print Var.getVariables( "Lepton", postprocessed=True )
    print Var.getVariableString( "Lepton", postprocessed=True )
    print
    print Var.getVariableNameList( "Jet", postprocessed=True )
    print Var.getVariables( "Jet", postprocessed=True )
    print Var.getVariableString( "Jet", postprocessed=True )
    print
    print Var.getVariableNameList( "BJet", postprocessed=True )
    print Var.getVariables( "BJet", postprocessed=True )
    print Var.getVariableString( "BJet", postprocessed=True )
    print
    print Var.getVariableNameList( "Photon", postprocessed=True )
    print Var.getVariables( "Photon", postprocessed=True )
    print Var.getVariableString( "Photon", postprocessed=True )
    print

    print Var.getVariableNameList( "Gen", data=False )
    print Var.getVariables( "Gen", data=False )
    print Var.getVariableString( "Gen", data=False )
    print
    print Var.getVariableNameList( "GenJet", data=False )
    print Var.getVariables( "GenJet", data=False )
    print Var.getVariableString( "GenJet", data=False )
    print



