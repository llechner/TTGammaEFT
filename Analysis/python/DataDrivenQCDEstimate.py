import os
from math import sqrt

# Logging
import logging
logger = logging.getLogger(__name__)

from TTGammaEFT.Analysis.SystematicEstimator import SystematicEstimator
from TTGammaEFT.Analysis.SetupHelpers        import dilepChannels, lepChannels, default_DYSF, default_sampleList, QCD_CR_updates
from TTGammaEFT.Tools.user                   import analysis_results, cache_directory

from Analysis.Tools.u_float                  import u_float

class DataDrivenQCDEstimate(SystematicEstimator):
    def __init__(self, name, cacheDir=None):
        super(DataDrivenQCDEstimate, self).__init__(name, cacheDir=cacheDir)

    #Concrete implementation of abstract method "estimate" as defined in Systematic
    def _estimate(self, region, channel, setup):

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
            # Attention: change region.cutstring to invLepIso and nBTag0!!!
            cut_MC_CR    = "&&".join([ region.cutString(setup.sys["selectionModifier"]), setup.selection("MC",   channel=channel, **setup.defaultParameters( update=QCD_CR_updates ))["cut"] ])
            cut_data_CR  = "&&".join([ region.cutString(),                               setup.selection("Data", channel=channel, **setup.defaultParameters( update=QCD_CR_updates ))["cut"] ])

            # Calculate yields for CR (normalized to data lumi)
            yield_data    = self.yieldFromCache(setup, "Data",   channel, cut_data_CR, weight_data)
            yield_other   = self.yieldFromCache(setup,  "DY_LO", channel, cut_MC_CR,   weight_SF)*setup.dataLumi/1000.

            print yield_other
            if setup.defaultParameters()["nJet"][0] > 2: yield_other *= default_DYSF #add DY SF for >= 3 jet selections
            print yield_other
            yield_other  += sum(self.yieldFromCache(setup, s,    channel, cut_MC_CR,   weight_SF) for s in default_sampleList if s not in ["DY_LO", "QCD-DD", "QCD", "GJets", "Data"])*setup.dataLumi/1000.

            # The QCD yield in the CR
            yield_QCD     = self.yieldFromCache(setup, "QCD",    channel, cut_MC_CR,   weight_MC)*setup.dataLumi/1000.
            yield_QCD    += self.yieldFromCache(setup, "GJets",  channel, cut_MC_CR,   weight_MC)*setup.dataLumi/1000.

            # The QCD yield in the signal regions
            sr_QCD        = self.yieldFromCache(setup, "QCD",     channel, cut_MC_SR,   weight_MC)*setup.lumi/1000.
            sr_QCD       += self.yieldFromCache(setup, "GJets",   channel, cut_MC_SR,   weight_MC)*setup.lumi/1000.

            normRegYield  = yield_data - yield_other
            transferFac   = sr_QCD/yield_QCD if yield_QCD > 0 else 0
            estimate      = normRegYield*transferFac

            logger.info("Calculating data-driven QCD normalization in channel " + channel + " using lumi " + str(setup.dataLumi) + ":")
            logger.info("yield QCD + GJets:         " + str(yield_QCD))
            logger.info("yield data:                " + str(yield_data))
            logger.info("yield other:               " + str(yield_other))
            logger.info("yield (data-other):        " + str(normRegYield))
            logger.info("transfer factor:           " + str(transferFac))
            if normRegYield < 0 and yield_data > 0: logger.warn("Negative normalization region yield!")

        logger.info("Estimate for QCD in " + channel + " channel" + (" (lumi=" + str(setup.lumi) + "/pb)" if channel != "all" else "") + ": " + str(estimate) + (" (negative estimated being replaced by 0)" if estimate < 0 else ""))
        return estimate if estimate > 0 else u_float(0, 0)

