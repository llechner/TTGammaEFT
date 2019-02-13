import ROOT
import os

preFiringPath = '$CMSSW_BASE/src/TTGammaEFT/postprocessing/L1Prefiring/'
preFiringFile = 'UnprefirableEventList_SingleMuon_Run2017BtoF.root'

class PreFiring:

    def __init__( self ):

        self.preFiringFile = os.path.expandvars( os.path.join( preFiringPath, preFiringFile ) )

    def getUnPreFirableEvents( self ):
        # Read Prefiring File
        f = ROOT.TFile.Open( self.preFiringFile )
        return [ ( int(event.event), int(event.run), int(event.lumi) ) for event in f.tree ]

