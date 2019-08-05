import os
from math import sqrt

# Logging
import logging
logger = logging.getLogger(__name__)

from TTGammaEFT.Analysis.SystematicEstimator import SystematicEstimator
from TTGammaEFT.Analysis.SetupHelpers        import dilepChannels, lepChannels, default_DYSF, default_sampleList, QCD_updates
from TTGammaEFT.Tools.user                   import analysis_results, cache_directory

from Analysis.Tools.u_float                  import u_float

class DataDrivenQCDEstimate(SystematicEstimator):
    def __init__(self, name, cacheDir=None):
        super(DataDrivenQCDEstimate, self).__init__(name, cacheDir=cacheDir)

    #Concrete implementation of abstract method "estimate" as defined in Systematic
    def _estimate(self, region, channel, setup, overwrite=False):

        #Sum of all channels for "all"
        if channel=="all":
            estimate     = sum([ self.cachedEstimate(region, c, setup) for c in lepChannels])

        elif channel=="SFtight":
            estimate     = sum([ self.cachedEstimate(region, c, setup) for c in dilepChannels])

        else:

            # Skip QCD estimate for 2 lepton CR (QCD = 0)
            if channel in dilepChannels:
                logger.info("Estimate for QCD in dileptonic channels skipped: 0")
                return u_float(0, 0)

            weight_data  = setup.weightString( "Data" )
            weight_MC    = setup.weightString( "MC", addMisIDSF=False )
            weight_SF    = setup.weightString( "MC", addMisIDSF=True  )

            cut_MC_SR    = "&&".join([ region.cutString(setup.sys["selectionModifier"]), setup.selection("MC",   channel=channel, **setup.defaultParameters())["cut"] ])
            # QCD CR with 0 bjets and inverted lepton isolation +  SF for DY and MisIDSF
            # Attention: change region.cutstring to invLepIso and nBTag0 if there are leptons or btags in regions!!!
            cut_MC_CR    = "&&".join([ region.cutString(setup.sys["selectionModifier"]), setup.selection("MC",   channel=channel, **setup.defaultParameters( update=QCD_updates ))["cut"] ])
            cut_data_CR  = "&&".join([ region.cutString(),                               setup.selection("Data", channel=channel, **setup.defaultParameters( update=QCD_updates ))["cut"] ])

            print cut_MC_SR
            print weight_MC
            print
            print cut_MC_CR
            print weight_SF
            print
            print cut_data_CR
            print weight_data
            print

            # Calculate yields for CR (normalized to data lumi)
            yield_data    = self.yieldFromCache(setup, "Data",   channel, cut_data_CR, weight_data, overwrite=overwrite)
            print "yield_data", yield_data
            yield_other   = self.yieldFromCache(setup, "DY_LO",  channel, cut_MC_CR,   weight_SF,   overwrite=overwrite)*setup.dataLumi/1000.
            print "yield_DY", yield_other

            if setup.defaultParameters( update=QCD_updates )["nJet"][0] > 2: yield_other *= default_DYSF #add DY SF for >= 3 jet selections
            yield_other  += sum(self.yieldFromCache(setup, s,    channel, cut_MC_CR,   weight_SF,   overwrite=overwrite) for s in default_sampleList if s not in ["DY_LO", "QCD-DD", "QCD", "GJets", "Data"])*setup.dataLumi/1000.
            print "yield_other", yield_other

            # The QCD yield in the CR
            yield_QCD     = self.yieldFromCache(setup, "QCD",    channel, cut_MC_CR,   weight_MC,   overwrite=overwrite)*setup.dataLumi/1000.
            yield_QCD    += self.yieldFromCache(setup, "GJets",  channel, cut_MC_CR,   weight_MC,   overwrite=overwrite)*setup.dataLumi/1000.
            print "yield_QCD", yield_QCD

            # The QCD yield in the signal regions
            sr_QCD        = self.yieldFromCache(setup, "QCD",    channel, cut_MC_SR,   weight_MC,  overwrite=overwrite)*setup.lumi/1000.
            sr_QCD       += self.yieldFromCache(setup, "GJets",  channel, cut_MC_SR,   weight_MC,  overwrite=overwrite)*setup.lumi/1000.
            print "sr_QCD", sr_QCD

            normRegYield  = yield_data - yield_other
            transferFac   = sr_QCD/yield_QCD if yield_QCD > 0 else 0
            estimate      = normRegYield*transferFac

            logger.info("Calculating data-driven QCD normalization in channel " + channel + " using lumi " + str(setup.dataLumi) + ":")
            logger.info("yield QCD + GJets:         " + str(yield_QCD))
            logger.info("yield data:                " + str(yield_data))
            logger.info("yield other:               " + str(yield_other))
            logger.info("yield (data-other):        " + str(normRegYield))
            logger.info("transfer factor:           " + str(transferFac))

            print("Calculating data-driven QCD normalization in channel " + channel + " using lumi " + str(setup.dataLumi) + ":")
            print("yield QCD + GJets:         " + str(yield_QCD))
            print("yield data:                " + str(yield_data))
            print("yield other:               " + str(yield_other))
            print("yield (data-other):        " + str(normRegYield))
            print("transfer factor:           " + str(transferFac))
            if normRegYield < 0 and yield_data > 0: logger.warn("Negative normalization region yield!")

        logger.info("Estimate for QCD in " + channel + " channel" + (" (lumi=" + str(setup.lumi) + "/pb)" if channel != "all" else "") + ": " + str(estimate) + (" (negative estimated being replaced by 0)" if estimate < 0 else ""))
        return estimate if estimate > 0 else u_float(0, 0)

if __name__ == "__main__":
    from TTGammaEFT.Analysis.regions      import regionsTTG, noPhotonRegionTTG, inclRegionsTTG
    from TTGammaEFT.Analysis.SetupHelpers import VG3
    from TTGammaEFT.Analysis.Setup        import Setup

    print "lowPT"
    r = regionsTTG[0]

    setup = Setup(year=2016, photonSelection=True)
    setup = setup.sysClone(parameters=VG3["parameters"])

    estimate = DataDrivenQCDEstimate( "QCD-DD" )    
    estimate.initCache(setup.defaultCacheDir())

    print setup.defaultParameters()
    res = estimate._estimate( r, "e", setup, overwrite=False )
    print res



    print "medPT"
    r = regionsTTG[1]

    setup = Setup(year=2016, photonSelection=True)
    setup = setup.sysClone(parameters=VG3["parameters"])

    estimate = DataDrivenQCDEstimate( "QCD-DD" )    
    estimate.initCache(setup.defaultCacheDir())

    print setup.defaultParameters()
    res = estimate._estimate( r, "e", setup, overwrite=False )
    print res


    print "highPT"
    r = regionsTTG[2]

    setup = Setup(year=2016, photonSelection=True)
    setup = setup.sysClone(parameters=VG3["parameters"])

    estimate = DataDrivenQCDEstimate( "QCD-DD" )    
    estimate.initCache(setup.defaultCacheDir())

    print setup.defaultParameters()
    res = estimate._estimate( r, "e", setup, overwrite=False )
    print res
