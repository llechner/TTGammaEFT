# Problems with HLT_DoubleEle33_CaloIdL_GsfTrkIdVL, HLT_TkMu50 and HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL

class TriggerSelector:
    def __init__( self, year, singleLepton=False ):

        self.singleLepton = singleLepton

        # https://indico.cern.ch/event/718554/contributions/3027981/attachments/1667626/2674497/leptontriggerreview.pdf
        if year == 2016:
            if singleLepton:
                self.m  = [ "HLT_IsoMu24", "HLT_IsoTkMu24", "HLT_Mu50", "HLT_TkMu50" ]
                self.e  = [ "HLT_Ele27_WPTight_Gsf", "HLT_Ele115_CaloIdVT_GsfTrkIdT" ]
                self.mm = None
                self.em = None
                self.ee = None
            else:
                self.mm = [ "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL", "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ", "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL", "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ", "HLT_Mu30_TkMu11" ]
                self.m  = [ "HLT_IsoMu24", "HLT_IsoTkMu24", "HLT_Mu50", "HLT_TkMu50" ]
                self.ee = [ "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW" ]
                self.e  = [ "HLT_Ele27_WPTight_Gsf", "HLT_Ele115_CaloIdVT_GsfTrkIdT" ]
                self.em = [ "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL" ]

        elif year == 2017:
            if singleLepton:
                self.m  = [ "HLT_IsoMu27", "HLT_Mu50" ]
                self.e  = [ "HLT_Ele35_WPTight_Gsf", "HLT_Ele32_WPTight_Gsf_L1DoubleEG", "HLT_Ele115_CaloIdVT_GsfTrkIdT" ]
                self.mm = None
                self.em = None
                self.ee = None
            else:
                self.mm = [ "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ", "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8", "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8", "HLT_Mu37_TkMu27", "HLT_Mu37_TkMu27" ]
                self.m  = [ "HLT_IsoMu27", "HLT_Mu50" ]
                self.ee = [ "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL", "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_DoubleEle33_CaloIdL_MW" ]
                self.e  = [ "HLT_Ele35_WPTight_Gsf", "HLT_Ele32_WPTight_Gsf_L1DoubleEG", "HLT_Ele115_CaloIdVT_GsfTrkIdT" ]
                self.em = [ "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Mu27_Ele37_CaloIdL_MW", "HLT_Mu37_Ele27_CaloIdL_MW" ]

        elif year == 2018:
            if singleLepton:
                self.m  = [ "HLT_IsoMu24", "HLT_IsoMu27", "HLT_Mu50" ]
                self.e  = [ "HLT_Ele32_WPTight_Gsf", "HLT_Ele115_CaloIdVT_GsfTrkIdT", "HLT_Ele32_WPTight_Gsf_L1DoubleEG", "HLT_DoubleEle25_CaloIdL_MW" ]
                self.mm = None
                self.em = None
                self.ee = None
            else:
                self.mm = [ "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8", "HLT_Mu37_TkMu27" ]
                self.m  = [ "HLT_IsoMu24", "HLT_IsoMu27", "HLT_Mu50" ]
                self.ee = [ "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL", "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ" ]
                self.e  = [ "HLT_Ele32_WPTight_Gsf", "HLT_Ele115_CaloIdVT_GsfTrkIdT", "HLT_Ele32_WPTight_Gsf_L1DoubleEG", "HLT_DoubleEle25_CaloIdL_MW" ]
                self.em = [ "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Mu27_Ele37_CaloIdL_MW", "HLT_Mu37_Ele27_CaloIdL_MW" ]

        else:
            raise NotImplementedError( "Trigger selection %r not implemented" %year )

        # define which triggers should be used for which dataset
        self.DoubleMuon     = "(%s)"%"||".join( ["Alt$(%s,1<0)"%trigger for trigger in self.mm] ) if self.mm else None
        self.DoubleEG       = "(%s)"%"||".join( ["Alt$(%s,1<0)"%trigger for trigger in self.ee] ) if self.ee else None
        eGamma = []
        if self.e:  eGamma += ["Alt$(%s,1<0)"%trigger for trigger in self.e]
        if self.ee: eGamma += ["Alt$(%s,1<0)"%trigger for trigger in self.ee]
        self.EGamma         = "(%s)"%"||".join( eGamma  ) if eGamma  else None
        self.MuonEG         = "(%s)"%"||".join( ["Alt$(%s,1<0)"%trigger for trigger in self.em] ) if self.em else None
        self.SingleMuon     = "(%s)"%"||".join( ["Alt$(%s,1<0)"%trigger for trigger in self.m]  ) if self.m  else None
        self.SingleElectron = "(%s)"%"||".join( ["Alt$(%s,1<0)"%trigger for trigger in self.e]  ) if self.e  else None

        # define an arbitrary hierarchy
        if year == 2018:
            self.PDHierarchy = [ "DoubleMuon", "EGamma", "MuonEG", "SingleMuon" ]
        else:
            self.PDHierarchy = [ "DoubleMuon", "DoubleEG", "MuonEG", "SingleMuon", "SingleElectron" ]

    def __getVeto( self, cutString ):
        return "!%s" %cutString

    def getAllTrigger( self ):
        allTrigger = []
        if self.mm: allTrigger += self.mm
        if self.ee: allTrigger += self.ee
        if self.em: allTrigger += self.em
        if self.e:  allTrigger += self.e
        if self.m:  allTrigger += self.m
        return allTrigger

    def getSelection( self, PD ):
        found     = False
        cutString = ""

        if PD == "MC":
            triggerList = [ item for item in [ self.DoubleMuon, self.DoubleEG, self.MuonEG, self.SingleMuon, self.SingleElectron ] if item ]
            return "(%s)"%"||".join( triggerList )
        else:
            for x in reversed( self.PDHierarchy ):
                if not getattr( self, x ): continue # Trigger not included (singleLepton)
                if found:
                    cutString += "&&%s" %self.__getVeto( getattr( self, x ) )
                if x in PD:
                    found      = True
                    cutString  = getattr( self, x )

            if cutString == "":
                raise NotImplementedError( "Trigger selection for %s not implemented" %PD )

            return "(%s)" %cutString

