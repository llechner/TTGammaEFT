from math import pi

from TTGammaEFT.Analysis.Region import Region
from TTGammaEFT.Analysis.Region import texString

def getRegionsFromThresholds(var, vals, gtLastThreshold = True):
    return [Region(var, (vals[i], vals[i+1])) for i in range(len(vals)-1)]

def getRegions2D(varOne, varOneThresholds, varTwo, varTwoThresholds):
    regions_varOne  = getRegionsFromThresholds(varOne,  varOneThresholds)
    regions_varTwo  = getRegionsFromThresholds(varTwo, varTwoThresholds)

    regions2D = []
    for r1 in regions_varOne:
        for r2 in regions_varTwo:
            regions2D.append(r1+r2)

    return regions2D

#Put all sets of regions that are used in the analysis, closure, tables, etc.

#inclusive
thresholds = [ 20, -999 ]
genTTGammaRegionsIncl  = getRegionsFromThresholds( "GenPhoton_pt[0]", thresholds )
recoTTGammaRegionsIncl = getRegionsFromThresholds( "PhotonGood0_pt", thresholds )

#differencial EFT
thresholds = [ 20, 120, 220, 320, 420, -999 ]
genTTGammaRegionsEFT  = getRegionsFromThresholds( "GenPhoton_pt[0]", thresholds )
recoTTGammaRegionsEFT = getRegionsFromThresholds( "PhotonGood0_pt", thresholds )

#differencial
thresholds = [ 20, 120, 220, -999 ]
genTTGammaRegions  = getRegionsFromThresholds( "GenPhoton_pt[0]", thresholds )
recoTTGammaRegions = getRegionsFromThresholds( "PhotonGood0_pt", thresholds )

thresholdsSmall = [ 20, 120 ]
genTTGammaRegionsSmall  = getRegionsFromThresholds( "GenPhoton_pt[0]", thresholdsSmall )
recoTTGammaRegionsSmall = getRegionsFromThresholds( "PhotonGood0_pt", thresholdsSmall )

#prefiring plots sum(jets)
preFiringSumJetEta    = getRegionsFromThresholds( "Jet_eta", [-5., -4.5, -4., -3.5, -3., -2.5, -2., -1.5, -1., -0.5, 0., 0.5, 1., 1.5, 2., 2.5, 3., 3.5, 4., 4.5, 5.], gtLastThreshold=False )
preFiringSumJetPt     = getRegionsFromThresholds( "Jet_pt",  [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, -999] )
preFiringSumJetPtLog  = getRegionsFromThresholds( "Jet_pt",  [30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, -999] )
preFiringSumJet       = getRegionsFromThresholds( "Jet_phi", [-pi, -pi*(4./5), -pi*(3./5), -pi*(2./5), -pi*(1./5), 0., pi*(1./5), pi*(2./5), pi*(3./5), pi*(4./5), pi], gtLastThreshold=False )

pTG_thresh         = [ 20, 120, 220, -999 ]
regionsTTG         = getRegionsFromThresholds( "PhotonGood0_pt", pTG_thresh )
inclRegionsTTG     = [Region( "PhotonGood0_pt", (20,-999) )]
regionsTTGfake     = getRegionsFromThresholds( "PhotonNoChgIsoNoSieie0_pt", pTG_thresh )
inclRegionsTTGfake = [Region( "PhotonNoChgIsoNoSieie0_pt", (20,-999) )]
noPhotonRegionTTG  = [Region( "nPhotonGood", (0,1) )]

m3_thresh = [0, 140, 210, 280, 350, -999]
#m3_thresh = [0, 70, 140, 210, 280, -999]
m3Regions   = getRegionsFromThresholds( "m3", m3_thresh )
m3PtRegions = getRegions2D( "PhotonGood0_pt", pTG_thresh, "m3", m3_thresh )

chgIso_thresh = [0, 1.141, 4, 9, 16, -999]
chgIsoRegions   = getRegionsFromThresholds( "(PhotonNoChgIsoNoSieie0_pfRelIso03_chg*PhotonNoChgIsoNoSieie0_pt)", chgIso_thresh )
chgIsoPtRegions = getRegions2D( "PhotonNoChgIsoNoSieie0_pt", pTG_thresh, "(PhotonNoChgIsoNoSieie0_pfRelIso03_chg*PhotonNoChgIsoNoSieie0_pt)", chgIso_thresh )

chgIso_thresh = chgIso_thresh[1:]
chgIsoNoSRRegions   = getRegionsFromThresholds( "(PhotonNoChgIsoNoSieie0_pfRelIso03_chg*PhotonNoChgIsoNoSieie0_pt)", chgIso_thresh )
chgIsoNoSRPtRegions = getRegions2D( "PhotonNoChgIsoNoSieie0_pt", pTG_thresh, "(PhotonNoChgIsoNoSieie0_pfRelIso03_chg*PhotonNoChgIsoNoSieie0_pt)", chgIso_thresh )

pTG_thresh         = [ 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 150, 180, 210, -999 ]
photonBinRegions   = getRegionsFromThresholds( "PhotonGood0_pt", pTG_thresh )

if __name__ == "__main__":
#    print inclRegionsTTG[0].cutString()

    for region in m3PtRegions:
        print str(region)
        print region.cutString()
        print type(region.vals)
        for val0, val1 in region.vals.values():
            print val0, val1
        print val1
