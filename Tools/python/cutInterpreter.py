''' Class to interpret string based cuts
'''

# TTGamma Imports
from Analysis.Tools.CutInterpreter import CutInterpreter

mZ = 91.1876

special_cuts = {
    "OS":                "(LeptonGood0_pdgId*LeptonGood1_pdgId)<0",
    "OStight":           "(LeptonTight0_pdgId*LeptonTight1_pdgId)<0",
    "dilep":             "nLeptonGood==2&&nLeptonGoodLead>=1",
    "dilepOS":           "nLeptonGood==2&&nLeptonGoodLead>=1&&(LeptonGood0_pdgId*LeptonGood1_pdgId)<0",
    "dilepSS":           "nLeptonGood==2&&nLeptonGoodLead>=1&&(LeptonGood0_pdgId*LeptonGood1_pdgId)>0",
    "dilepOFOS":         "nLeptonGood==2&&nLeptonGoodLead>=1&&(LeptonGood0_pdgId*LeptonGood1_pdgId)<0&&nElectronGood==1&&nMuonGood==1",
    "dilepOFSS":         "nLeptonGood==2&&nLeptonGoodLead>=1&&(LeptonGood0_pdgId*LeptonGood1_pdgId)>0&&nElectronGood==1&&nMuonGood==1",
    "dilepSFOS":         "nLeptonGood==2&&nLeptonGoodLead>=1&&(LeptonGood0_pdgId*LeptonGood1_pdgId)<0&&(nElectronGood==2||nMuonGood==2)",
    "dilepSFSS":         "nLeptonGood==2&&nLeptonGoodLead>=1&&(LeptonGood0_pdgId*LeptonGood1_pdgId)>0&&(nElectronGood==2||nMuonGood==2)",
    "offZll":            "abs(mll-%s)>15"%(mZ),
    "offZllg":           "abs(mllgamma-%s)>15"%(mZ),

    "offZllgMVA":               "abs(mllgammaMVA-%s)>15"%(mZ),
    "offZllgNoChgIso":          "abs(mllgammaNoChgIso-%s)>15"%(mZ),
    "offZllgNoSieie":           "abs(mllgammaNoSieie-%s)>15"%(mZ),
    "offZllgNoChgIsoNoSieie":   "abs(mllgammaNoChgIsoNoSieie-%s)>15"%(mZ),

    "offZllTight":       "abs(mlltight-%s)>15"%(mZ),
    "offZllgTight":      "abs(mllgammatight-%s)>15"%(mZ),
    "offZSFll":          "((abs(mll-%s)>15&&(nElectronGood==2||nMuonGood==2))||(nElectronGood==1&&nMuonGood==1))"%(mZ),                      # Cut Z-Window only for SF dilep events
    "offZSFllg":         "((abs(mllgamma-%s)>15&&(nElectronGood==2||nMuonGood==2))||(nElectronGood==1&&nMuonGood==1))"%(mZ),                 # Cut Z-Window only for SF dilep events

    "offZSFllgMVA":             "((abs(mllgammaMVA-%s)>15&&(nElectronGood==2||nMuonGood==2))||(nElectronGood==1&&nMuonGood==1))"%(mZ),                 # Cut Z-Window only for SF dilep events
    "offZSFllgNoChgIso":        "((abs(mllgammaNoChgIso-%s)>15&&(nElectronGood==2||nMuonGood==2))||(nElectronGood==1&&nMuonGood==1))"%(mZ),                 # Cut Z-Window only for SF dilep events
    "offZSFllgNoSieie":         "((abs(mllgammaNoSieie-%s)>15&&(nElectronGood==2||nMuonGood==2))||(nElectronGood==1&&nMuonGood==1))"%(mZ),                 # Cut Z-Window only for SF dilep events
    "offZSFllgNoChgIsoNoSieie": "((abs(mllgammaNoChgIsoNoSieie-%s)>15&&(nElectronGood==2||nMuonGood==2))||(nElectronGood==1&&nMuonGood==1))"%(mZ),                 # Cut Z-Window only for SF dilep events

    "offZSFllTight":     "((abs(mlltight-%s)>15&&(nElectronTight==2||nMuonTight==2))||(nElectronTight==1&&nMuonTight==1))"%(mZ),             # Cut Z-Window only for SF dilep events
    "offZSFllgTight":    "((abs(mllgammatight-%s)>15&&(nElectronTight==2||nMuonTight==2))||(nElectronTight==1&&nMuonTight==1))"%(mZ),        # Cut Z-Window only for SF dilep events
    "onZll":             "abs(mll-%s)<=15"%(mZ),
    "onZllg":            "abs(mllgamma-%s)<=15"%(mZ),

    "onZllgMVA":               "abs(mllgammaMVA-%s)<=15"%(mZ),
    "onZllgNoChgIso":          "abs(mllgammaNoChgIso-%s)<=15"%(mZ),
    "onZllgNoSieie":           "abs(mllgammaNoSieie-%s)<=15"%(mZ),
    "onZllgNoChgIsoNoSieie":   "abs(mllgammaNoChgIsoNoSieie-%s)<=15"%(mZ),

    "onZllTight":        "abs(mlltight-%s)<=15"%(mZ),
    "onZllgTight":       "abs(mllgammatight-%s)<=15"%(mZ),
    "onZSFll":           "((abs(mll-%s)<=15&&(nElectronGood==2||nMuonGood==2))||(nElectronGood==1&&nMuonGood==1))"%(mZ),                     # Cut Z-Window only for SF dilep events
    "onZSFllg":          "((abs(mllgamma-%s)<=15&&(nElectronGood==2||nMuonGood==2))||(nElectronGood==1&&nMuonGood==1))"%(mZ),                # Cut Z-Window only for SF dilep events

    "onZSFllgMVA":             "((abs(mllgammaMVA-%s)<=15&&(nElectronGood==2||nMuonGood==2))||(nElectronGood==1&&nMuonGood==1))"%(mZ),                 # Cut Z-Window only for SF dilep events
    "onZSFllgNoChgIso":        "((abs(mllgammaNoChgIso-%s)<=15&&(nElectronGood==2||nMuonGood==2))||(nElectronGood==1&&nMuonGood==1))"%(mZ),                 # Cut Z-Window only for SF dilep events
    "onZSFllgNoSieie":         "((abs(mllgammaNoSieie-%s)<=15&&(nElectronGood==2||nMuonGood==2))||(nElectronGood==1&&nMuonGood==1))"%(mZ),                 # Cut Z-Window only for SF dilep events
    "onZSFllgNoChgIsoNoSieie": "((abs(mllgammaNoChgIsoNoSieie-%s)<=15&&(nElectronGood==2||nMuonGood==2))||(nElectronGood==1&&nMuonGood==1))"%(mZ),                 # Cut Z-Window only for SF dilep events

    "onZSFllTight":      "((abs(mlltight-%s)<=15&&(nElectronTight==2||nMuonTight==2))||(nElectronTight==1&&nMuonTight==1))"%(mZ),            # Cut Z-Window only for SF dilep events
    "onZSFllgTight":     "((abs(mllgammatight-%s)<=15&&(nElectronTight==2||nMuonTight==2))||(nElectronTight==1&&nMuonTight==1))"%(mZ),       # Cut Z-Window only for SF dilep events
    "mumu":              "nElectronGood==0&&nMuonGood==2",
    "mue":               "nElectronGood==1&&nMuonGood==1",
    "ee":                "nElectronGood==2&&nMuonGood==0",
    "all":               "(1)",
    "SF":                "(nElectronGood==2||nMuonGood==2)",
    "mu":                "nMuonTight==1",
    "e":                 "nElectronTight==1",
    "mumutight":         "nElectronTight==0&&nMuonTight==2",
    "muetight":          "nElectronTight==1&&nMuonTight==1",
    "eetight":           "nElectronTight==2&&nMuonTight==0",
    "SFtight":           "(nElectronTight==2||nMuonTight==2)",
    "trigger":           "(1)",

    "MVAPhoton":             "nPhotonMVA>=1",
    "NoSieiePhoton":         "nPhotonNoSieie>=1",
    "NoChgIsoPhoton":        "nPhotonNoChgIso>=1",
    "NoChgIsoNoSieiePhoton": "nPhotonNoChgIsoNoSieie>=1",

    "offZeg":               "((abs(mLtight0Gamma-%s)>15&&nElectronTight==1)||(nElectronTight==0))"%(mZ),             # Cut Z-Window only for egamma
    "onZeg":                "((abs(mLtight0Gamma-%s)<=15&&nElectronTight==1)||(nElectronTight==0))"%(mZ),             # Cut Z-Window only for egamma
    "phiGlt1p1":             "abs(PhotonGood0_phi)<1.1",
    "onZEphiGlt1p1":         "((abs(mLtight0Gamma-%s)<=15&&abs(PhotonGood0_phi)<1.1&&nElectronTight==1)||(abs(mLtight0Gamma-%s)>15&&nElectronTight==1)||(nElectronTight==0))"%(mZ,mZ),

    "n12Jet":               "nJetGood==1||nJetGood==2",

    "lowSieie":          "PhotonNoChgIsoNoSieie0_sieie<0.01015",
    "highSieie":         "PhotonNoChgIsoNoSieie0_sieie>0.011",
    "lowChgIso":         "PhotonNoChgIsoNoSieie0_pfRelIso03_chg*PhotonNoChgIsoNoSieie0_pt<1.141",
    "highChgIso":        "PhotonNoChgIsoNoSieie0_pfRelIso03_chg*PhotonNoChgIsoNoSieie0_pt>1.141",

    "lowPT":             "PhotonGood0_pt>=20&&PhotonGood0_pt<120",
    "medPT":             "PhotonGood0_pt>=120&&PhotonGood0_pt<220",
    "highPT":            "PhotonGood0_pt>=220",
    "incl":              "PhotonGood0_pt>=20",

    "lowhadPT":          "PhotonNoChgIsoNoSieie0_pt>=20&&PhotonNoChgIsoNoSieie0_pt<120",
    "medhadPT":          "PhotonNoChgIsoNoSieie0_pt>=120&&PhotonNoChgIsoNoSieie0_pt<220",
    "highhadPT":         "PhotonNoChgIsoNoSieie0_pt>=220",
    "inclhad":           "PhotonNoChgIsoNoSieie0_pt>=20",

    "photoncat0":        "PhotonGood0_photonCat==0",
    "photoncat1":        "PhotonGood0_photonCat==1",
    "photoncat2":        "PhotonGood0_photonCat==2",
    "photoncat3":        "PhotonGood0_photonCat==3",

    "photonhadcat0":        "PhotonNoChgIsoNoSieie0_photonCat==0",
    "photonhadcat1":        "PhotonNoChgIsoNoSieie0_photonCat==1",
    "photonhadcat2":        "PhotonNoChgIsoNoSieie0_photonCat==2",
    "photonhadcat3":        "PhotonNoChgIsoNoSieie0_photonCat==3",

  }

continous_variables = [ ("metSig", "METSig"), ("mll", "mll"), ("mllgamma", "mllgamma"), ("mlgamma", "mLtight0Gamma"), ("met", "MET_pt"), ("pTG","PhotonGood0_pt"), ("pTj","Jet_pt[0]"), ("etaj","abs(Jet_eta[0])") ]
discrete_variables  = [ ("nAllJet", "nJet"), ("nJet", "nJetGood"), ("nBTag", "nBTagGood"), ("nLepNoCorrVeto","nLeptonVeto"), ("nLepVeto","nLeptonVetoIsoCorr"), ("nInvLepTight","nLeptonTightInvIso"), ("nLepTight","nLeptonTight"), ("nLep","nLeptonGood"), ("nPhoton","nPhotonGood") ]

cutInterpreter = CutInterpreter( continous_variables, discrete_variables, special_cuts)

if __name__ == "__main__":
    print cutInterpreter.cutString("dilepOS-pTG20-nPhoton1p-offZSFllgNoChgIsoNoSieie-mll40")
#    print cutInterpreter.cutString("etaj2.25To3-pTj100")

