import os
from math import sqrt

from TTGammaEFT.Analysis.SystematicEstimator import SystematicEstimator
from TTGammaEFT.Analysis.SetupHelpers        import dilepChannels, lepChannels, DYSF_val, default_sampleList, QCD_updates, default_photonSampleList
from TTGammaEFT.Tools.user                   import analysis_results, cache_directory

from Analysis.Tools.u_float                  import u_float

# Logging
if __name__=="__main__":
    import Analysis.Tools.logger as logger
    logger = logger.get_logger( "INFO", logFile=None)
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger( "INFO", logFile=None )
else:
    import logging
    logger = logging.getLogger(__name__)

class DataDrivenQCDEstimate(SystematicEstimator):
    def __init__(self, name, cacheDir=None):
        super(DataDrivenQCDEstimate, self).__init__(name, cacheDir=cacheDir)

    def _transferFactor(self, region, channel, setup, overwrite=False):

        selection_MC_SR   = setup.selection("MC",   channel=channel, **setup.defaultParameters())
        selection_MC_CR   = setup.selection("MC",   channel=channel, **setup.defaultParameters( update=QCD_updates ))

        cuts_MC_SR   = [ region.cutString(setup.sys["selectionModifier"]), selection_MC_SR["cut"] ]
        if self.processCut:
            cuts_MC_SR.append( self.processCut )
            logger.info( "Adding process specific cut %s"%self.processCut )
        cut_MC_SR    = "&&".join( cuts_MC_SR )


        weight_MC    = selection_MC_SR["weightStr"] # w/o misID SF

        # QCD CR with 0 bjets and inverted lepton isolation +  SF for DY and MisIDSF
        # Attention: change region.cutstring to invLepIso and nBTag0 if there are leptons or btags in regions!!!
        cut_MC_CR    = "&&".join([ region.cutString(setup.sys["selectionModifier"]), selection_MC_CR["cut"] ])

        # The QCD yield in the CR with SR weight (sic)
        yield_QCD_CR     = self.yieldFromCache(setup, "QCD",    channel, cut_MC_CR,   weight_MC,   overwrite=overwrite)*setup.dataLumi/1000.
        print "QCD, CR", channel, yield_QCD_CR
        yield_QCD_CR    += self.yieldFromCache(setup, "GJets",  channel, cut_MC_CR,   weight_MC,   overwrite=overwrite)*setup.dataLumi/1000.
        print "QCD+gjets, CR", channel, yield_QCD_CR

        # The QCD yield in the signal regions
        yield_QCD_SR     = self.yieldFromCache(setup, "QCD",    channel, cut_MC_SR,   weight_MC,  overwrite=overwrite)*setup.lumi/1000.
        print "QCD, SR", channel, yield_QCD_SR
        yield_QCD_SR    += self.yieldFromCache(setup, "GJets",  channel, cut_MC_SR,   weight_MC,  overwrite=overwrite)*setup.lumi/1000.
        print "QCD+gjets, SR", channel, yield_QCD_SR

        transferFac = yield_QCD_SR/yield_QCD_CR if yield_QCD_CR > 0 else u_float(0, 0)

        logger.info("yield QCD + GJets CR:         " + str(yield_QCD_CR))
        logger.info("yield QCD + GJets SR:         " + str(yield_QCD_CR))
        logger.info("transfer factor:              " + str(transferFac))

        return transferFac

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

            selection_MC_CR   = setup.selection("MC",   channel=channel, **setup.defaultParameters( update=QCD_updates ))
            selection_Data_CR = setup.selection("Data", channel=channel, **setup.defaultParameters( update=QCD_updates ))

            weight_Data_CR  = selection_Data_CR["weightStr"]
            weight_MC_CR    = selection_MC_CR["weightStr"] # w/ misID SF

            # QCD CR with 0 bjets and inverted lepton isolation +  SF for DY and MisIDSF
            # Attention: change region.cutstring to invLepIso and nBTag0 if there are leptons or btags in regions!!!
            cut_MC_CR    = "&&".join([ region.cutString(setup.sys["selectionModifier"]), selection_MC_CR["cut"] ])
            cut_Data_CR  = "&&".join([ region.cutString(),                               selection_Data_CR["cut"] ])

            # Calculate yields for CR (normalized to data lumi)
            yield_data    = self.yieldFromCache(setup, "Data",   channel, cut_Data_CR, weight_Data_CR, overwrite=overwrite)
#            full_sampleList = default_photonSampleList if setup.isPhotonSelection else default_sampleList
#            yield_other   = 0
#            for s in full_sampleList:
#                if "QCD" in s or "GJets" in s or "Data" in s: continue
#                y = self.yieldFromCache(setup, s,  channel, cut_MC_CR,   weight_MC_CR,   overwrite=overwrite)*setup.dataLumi/1000.
#                if "DY" in s: y *= DYSF_val[setup.year] #add DY SF
#                yield_other += y

            yield_other   = self.yieldFromCache(setup, "DY_LO",  channel, cut_MC_CR,   weight_MC_CR,   overwrite=overwrite)*setup.dataLumi/1000.
            yield_other  *= DYSF_val[setup.year] #add DY SF
            yield_other  += sum(self.yieldFromCache(setup, s,    channel, cut_MC_CR,   weight_MC_CR,   overwrite=overwrite) for s in default_sampleList if s not in ["DY_LO", "QCD-DD", "QCD", "GJets", "Data"])*setup.dataLumi/1000.

            normRegYield  = yield_data - yield_other
            transferFac   = self.cachedTransferFactor(region, channel, setup, save=True, overwrite=overwrite, checkOnly=False)
            estimate      = normRegYield*transferFac

            logger.info("Calculating data-driven QCD normalization in channel " + channel + " using lumi " + str(setup.dataLumi) + ":")
            logger.info("yield data:                " + str(yield_data))
            logger.info("yield other:               " + str(yield_other))
            logger.info("yield (data-other):        " + str(normRegYield))
            logger.info("transfer factor:           " + str(transferFac))

            if normRegYield < 0 and yield_data > 0: logger.warn("Negative normalization region yield!")

        logger.info("Estimate for QCD in " + channel + " channel" + (" (lumi=" + str(setup.lumi) + "/pb)" if channel != "all" else "") + ": " + str(estimate) + (" (negative estimated being replaced by 0)" if estimate < 0 else ""))
        return estimate if estimate > 0 else u_float(0, 0)

if __name__ == "__main__":
    from TTGammaEFT.Analysis.regions      import regionsTTG, noPhotonRegionTTG, inclRegionsTTG
    from TTGammaEFT.Analysis.SetupHelpers import allRegions
    from TTGammaEFT.Analysis.Setup        import Setup

    print "incl e"
    r = regionsTTG[0]

    setup = Setup(year=2016, photonSelection=False)
    setup = setup.sysClone(parameters=allRegions["VG3"]["parameters"])

    estimate = DataDrivenQCDEstimate( "QCD-DD" )    
    estimate.initCache(setup.defaultCacheDir())

    res = estimate._transferFactor( r, "mu", setup, overwrite=True )
#    res = estimate._estimate( r, "mu", setup, overwrite=True )
#    res = estimate._estimate( r, "e", setup, overwrite=True )
    print res



    print "lowPT"
    r = regionsTTG[0]

    setup = Setup(year=2016, photonSelection=True)
    setup = setup.sysClone(parameters=allRegions["VG3"]["parameters"])

    estimate = DataDrivenQCDEstimate( "QCD-DD" )    
    estimate.initCache(setup.defaultCacheDir())

    res = estimate._estimate( r, "e", setup, overwrite=True )
    print res



    print "medPT"
    r = regionsTTG[1]

    setup = Setup(year=2016, photonSelection=True)
    setup = setup.sysClone(parameters=allRegions["VG3"]["parameters"])

    estimate = DataDrivenQCDEstimate( "QCD-DD" )    
    estimate.initCache(setup.defaultCacheDir())

    print setup.defaultParameters()
    res = estimate._estimate( r, "e", setup, overwrite=True )
    print res


    print "highPT"
    r = regionsTTG[2]

    setup = Setup(year=2016, photonSelection=True)
    setup = setup.sysClone(parameters=allRegions["VG3"]["parameters"])

    estimate = DataDrivenQCDEstimate( "QCD-DD" )    
    estimate.initCache(setup.defaultCacheDir())

    print setup.defaultParameters()
    res = estimate._estimate( r, "e", setup, overwrite=True )
    print res
