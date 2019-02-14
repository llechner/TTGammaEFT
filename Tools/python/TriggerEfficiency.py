import ROOT
import os
from Analysis.Tools.helpers import getObjFromFile

basedir = "$CMSSW_BASE/src/TTGammaEFT/Tools/data/triggerEff/"

#OR of all backput triggers
#2016
ee_trigger2016_SF   = basedir + 'Run2016BCDEFG_HLT_ee_DZ_None_measuredInMET_minLeadLepPt0.root'
mue_trigger2016_SF  = basedir + 'Run2016BCDEFG_HLT_mue_None_measuredInMET_minLeadLepPt0.root'
mumu_trigger2016_SF = basedir + 'Run2016BCDEFG_HLT_mumuIso_None_measuredInMET_minLeadLepPt0.root'

ee_trigger2016_SF_with_backup   = basedir + 'Run2016BCDEFGH_HLT_ee_DZ_OR_HLT_ee_33_OR_HLT_ee_33_MW_OR_HLT_SingleEle_noniso_None_measuredInMET_minLeadLepPt0.root'
mue_trigger2016_SF_with_backup  = basedir + 'Run2016BCDEFGH_HLT_mue_OR_HLT_mu30e30_OR_HLT_SingleEle_noniso_OR_HLT_SingleMu_noniso_None_measuredInMET_minLeadLepPt0.root'
mumu_trigger2016_SF_with_backup = basedir + 'Run2016BCDEFGH_HLT_mumuIso_OR_HLT_mumuNoiso_OR_HLT_SingleMu_noniso_None_measuredInMET_minLeadLepPt0.root'

#2017
# UPDATE WHEN AVAILABLE
ee_trigger2017_SF   = basedir + 'Run2016BCDEFG_HLT_ee_DZ_None_measuredInMET_minLeadLepPt0.root'
mue_trigger2017_SF  = basedir + 'Run2016BCDEFG_HLT_mue_None_measuredInMET_minLeadLepPt0.root'
mumu_trigger2017_SF = basedir + 'Run2016BCDEFG_HLT_mumuIso_None_measuredInMET_minLeadLepPt0.root'

ee_trigger2017_SF_with_backup   = basedir + 'Run2016BCDEFGH_HLT_ee_DZ_OR_HLT_ee_33_OR_HLT_ee_33_MW_OR_HLT_SingleEle_noniso_None_measuredInMET_minLeadLepPt0.root'
mue_trigger2017_SF_with_backup  = basedir + 'Run2016BCDEFGH_HLT_mue_OR_HLT_mu30e30_OR_HLT_SingleEle_noniso_OR_HLT_SingleMu_noniso_None_measuredInMET_minLeadLepPt0.root'
mumu_trigger2017_SF_with_backup = basedir + 'Run2016BCDEFGH_HLT_mumuIso_OR_HLT_mumuNoiso_OR_HLT_SingleMu_noniso_None_measuredInMET_minLeadLepPt0.root'

#2018
# UPDATE WHEN AVAILABLE
ee_trigger2018_SF   = basedir + 'Run2016BCDEFG_HLT_ee_DZ_None_measuredInMET_minLeadLepPt0.root'
mue_trigger2018_SF  = basedir + 'Run2016BCDEFG_HLT_mue_None_measuredInMET_minLeadLepPt0.root'
mumu_trigger2018_SF = basedir + 'Run2016BCDEFG_HLT_mumuIso_None_measuredInMET_minLeadLepPt0.root'

ee_trigger2018_SF_with_backup   = basedir + 'Run2016BCDEFGH_HLT_ee_DZ_OR_HLT_ee_33_OR_HLT_ee_33_MW_OR_HLT_SingleEle_noniso_None_measuredInMET_minLeadLepPt0.root'
mue_trigger2018_SF_with_backup  = basedir + 'Run2016BCDEFGH_HLT_mue_OR_HLT_mu30e30_OR_HLT_SingleEle_noniso_OR_HLT_SingleMu_noniso_None_measuredInMET_minLeadLepPt0.root'
mumu_trigger2018_SF_with_backup = basedir + 'Run2016BCDEFGH_HLT_mumuIso_OR_HLT_mumuNoiso_OR_HLT_SingleMu_noniso_None_measuredInMET_minLeadLepPt0.root'

class TriggerEfficiency:
    def __init__( self, with_backup_triggers=False, year=2016 ):

        if year not in [ 2016, 2017, 2018 ]:
            raise Exception("Lepton SF for year %i not known"%year)

        if year == 2016:
            if not with_backup_triggers:
                self.mumu_highEta   = getObjFromFile(os.path.expandvars(mumu_trigger2016_SF), "eff_pt1_pt2_highEta1_veryCoarse")
                self.mumu_lowEta    = getObjFromFile(os.path.expandvars(mumu_trigger2016_SF), "eff_pt1_pt2_lowEta1_veryCoarse")
                self.ee_highEta     = getObjFromFile(os.path.expandvars(ee_trigger2016_SF),   "eff_pt1_pt2_highEta1_veryCoarse")
                self.ee_lowEta      = getObjFromFile(os.path.expandvars(ee_trigger2016_SF),   "eff_pt1_pt2_lowEta1_veryCoarse")
                self.mue_highEta    = getObjFromFile(os.path.expandvars(mue_trigger2016_SF),  "eff_pt1_pt2_highEta1_veryCoarse")
                self.mue_lowEta     = getObjFromFile(os.path.expandvars(mue_trigger2016_SF),  "eff_pt1_pt2_lowEta1_veryCoarse")
            else:
                self.mumu_highEta   = getObjFromFile(os.path.expandvars(mumu_trigger2016_SF_with_backup), "eff_pt1_pt2_highEta1_veryCoarse")
                self.mumu_lowEta    = getObjFromFile(os.path.expandvars(mumu_trigger2016_SF_with_backup), "eff_pt1_pt2_lowEta1_veryCoarse")
                self.ee_highEta     = getObjFromFile(os.path.expandvars(ee_trigger2016_SF_with_backup),   "eff_pt1_pt2_highEta1_veryCoarse")
                self.ee_lowEta      = getObjFromFile(os.path.expandvars(ee_trigger2016_SF_with_backup),   "eff_pt1_pt2_lowEta1_veryCoarse")
                self.mue_highEta    = getObjFromFile(os.path.expandvars(mue_trigger2016_SF_with_backup),  "eff_pt1_pt2_highEta1_veryCoarse")
                self.mue_lowEta     = getObjFromFile(os.path.expandvars(mue_trigger2016_SF_with_backup),  "eff_pt1_pt2_lowEta1_veryCoarse")

        elif year == 2017:
            if not with_backup_triggers:
                self.mumu_highEta   = getObjFromFile(os.path.expandvars(mumu_trigger2016_SF), "eff_pt1_pt2_highEta1_veryCoarse")
                self.mumu_lowEta    = getObjFromFile(os.path.expandvars(mumu_trigger2016_SF), "eff_pt1_pt2_lowEta1_veryCoarse")
                self.ee_highEta     = getObjFromFile(os.path.expandvars(ee_trigger2016_SF),   "eff_pt1_pt2_highEta1_veryCoarse")
                self.ee_lowEta      = getObjFromFile(os.path.expandvars(ee_trigger2016_SF),   "eff_pt1_pt2_lowEta1_veryCoarse")
                self.mue_highEta    = getObjFromFile(os.path.expandvars(mue_trigger2016_SF),  "eff_pt1_pt2_highEta1_veryCoarse")
                self.mue_lowEta     = getObjFromFile(os.path.expandvars(mue_trigger2016_SF),  "eff_pt1_pt2_lowEta1_veryCoarse")
            else:
                self.mumu_highEta   = getObjFromFile(os.path.expandvars(mumu_trigger2016_SF_with_backup), "eff_pt1_pt2_highEta1_veryCoarse")
                self.mumu_lowEta    = getObjFromFile(os.path.expandvars(mumu_trigger2016_SF_with_backup), "eff_pt1_pt2_lowEta1_veryCoarse")
                self.ee_highEta     = getObjFromFile(os.path.expandvars(ee_trigger2016_SF_with_backup),   "eff_pt1_pt2_highEta1_veryCoarse")
                self.ee_lowEta      = getObjFromFile(os.path.expandvars(ee_trigger2016_SF_with_backup),   "eff_pt1_pt2_lowEta1_veryCoarse")
                self.mue_highEta    = getObjFromFile(os.path.expandvars(mue_trigger2016_SF_with_backup),  "eff_pt1_pt2_highEta1_veryCoarse")
                self.mue_lowEta     = getObjFromFile(os.path.expandvars(mue_trigger2016_SF_with_backup),  "eff_pt1_pt2_lowEta1_veryCoarse")

        elif year == 2018:
            if not with_backup_triggers:
                self.mumu_highEta   = getObjFromFile(os.path.expandvars(mumu_trigger2016_SF), "eff_pt1_pt2_highEta1_veryCoarse")
                self.mumu_lowEta    = getObjFromFile(os.path.expandvars(mumu_trigger2016_SF), "eff_pt1_pt2_lowEta1_veryCoarse")
                self.ee_highEta     = getObjFromFile(os.path.expandvars(ee_trigger2016_SF),   "eff_pt1_pt2_highEta1_veryCoarse")
                self.ee_lowEta      = getObjFromFile(os.path.expandvars(ee_trigger2016_SF),   "eff_pt1_pt2_lowEta1_veryCoarse")
                self.mue_highEta    = getObjFromFile(os.path.expandvars(mue_trigger2016_SF),  "eff_pt1_pt2_highEta1_veryCoarse")
                self.mue_lowEta     = getObjFromFile(os.path.expandvars(mue_trigger2016_SF),  "eff_pt1_pt2_lowEta1_veryCoarse")
            else:
                self.mumu_highEta   = getObjFromFile(os.path.expandvars(mumu_trigger2016_SF_with_backup), "eff_pt1_pt2_highEta1_veryCoarse")
                self.mumu_lowEta    = getObjFromFile(os.path.expandvars(mumu_trigger2016_SF_with_backup), "eff_pt1_pt2_lowEta1_veryCoarse")
                self.ee_highEta     = getObjFromFile(os.path.expandvars(ee_trigger2016_SF_with_backup),   "eff_pt1_pt2_highEta1_veryCoarse")
                self.ee_lowEta      = getObjFromFile(os.path.expandvars(ee_trigger2016_SF_with_backup),   "eff_pt1_pt2_lowEta1_veryCoarse")
                self.mue_highEta    = getObjFromFile(os.path.expandvars(mue_trigger2016_SF_with_backup),  "eff_pt1_pt2_highEta1_veryCoarse")
                self.mue_lowEta     = getObjFromFile(os.path.expandvars(mue_trigger2016_SF_with_backup),  "eff_pt1_pt2_lowEta1_veryCoarse")

        h_ = [self.mumu_highEta, self.mumu_lowEta, self.ee_highEta, self.ee_lowEta, self.mue_highEta, self.mue_lowEta]
        assert False not in [bool(x) for x in h_], "Could not load trigger SF: %r"%h_

        self.ptMax = self.mumu_highEta.GetXaxis().GetXmax()

    def __getSF(self, map_, pt1, pt2):
        if pt1 > self.ptMax: pt1 = self.ptMax - 1 
        if pt2 > self.ptMax: pt2 = self.ptMax - 1 
        val    = map_.GetBinContent( map_.FindBin(pt1, pt2) )
        valErr = map_.GetBinError(   map_.FindBin(pt1, pt2) )
        return (val, valErr)

    def getSF(self, p1, p2):

        if p1["pt"] < p2["pt"]:
            raise ValueError ( "Sort leptons wrt pt." )

        #Split in low/high eta of leading lepton for both, ee and mumu channel 
        if abs(p1["pdgId"]) == abs(p2["pdgId"]) == 13:
            if abs(p1["eta"]) < 1.5:
                return self.__getSF( self.mumu_lowEta, p1["pt"], p2["pt"] )
            else:
                return self.__getSF( self.mumu_highEta, p1["pt"], p2["pt"] )

        elif abs(p1["pdgId"]) == abs(p2["pdgId"]) == 11:
            if abs(p1["eta"]) < 1.5:
                return self.__getSF( self.ee_lowEta, p1["pt"], p2["pt"] )
            else:
                return self.__getSF( self.ee_highEta, p1["pt"], p2["pt"] )

        #Split in low/high eta of muon for emu channel 
        elif abs(p1["pdgId"]) == 13 and abs(p2["pdgId"]) == 11:
            if abs(p1["eta"]) < 1.5: 
                return self.__getSF( self.mue_lowEta, p1["pt"], p2["pt"] )
            else:
                return self.__getSF( self.mue_highEta, p1["pt"], p2["pt"] )

        elif abs(p1["pdgId"]) == 11 and abs(p2["pdgId"]) == 13:
            if abs(p2["eta"]) < 1.5: 
                return self.__getSF( self.mue_lowEta, p1["pt"], p2["pt"] )
            else:
                return self.__getSF( self.mue_highEta, p1["pt"], p2["pt"] )

        raise ValueError( "Did not find trigger SF for pt1 %3.2f eta %3.2f pdgId1 %i pt2 %3.2f eta2 %3.2f pdgId2 %i"%( p1["pt"], p1["eta"], p1["pdgId"], p2["pt"], p2["eta"], p2["pdgId"] ) )
        
