from TTGammaEFT.Analysis.Region import Region

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

thresholds = [ 20, 120, 220, 320, 420, 520, -1 ]
genTTGammaRegions  = getRegionsFromThresholds( "GenPhoton_pt[0]", thresholds )
recoTTGammaRegions = getRegionsFromThresholds( "PhotonGood0_pt", thresholds )

thresholdsSmall = [ 420, 520 ]
genTTGammaRegionsSmall  = getRegionsFromThresholds( "GenPhoton_pt[0]", thresholdsSmall )
recoTTGammaRegionsSmall = getRegionsFromThresholds( "PhotonGood0_pt", thresholdsSmall )

#print genTTGammaRegions[0]
