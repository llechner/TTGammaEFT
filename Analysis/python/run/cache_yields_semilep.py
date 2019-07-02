''' Plot script pTG shape + WC
'''

# Standard imports 
import sys, os, pickle, copy, ROOT

# RootTools
from RootTools.core.standard   import *

# turn off graphics
ROOT.gROOT.SetBatch( True )

# TTGammaEFT
from TTGammaEFT.Tools.user              import cache_directory
from TTGammaEFT.Tools.TriggerSelector   import TriggerSelector
from TTGammaEFT.Tools.cutInterpreter    import cutInterpreter
from TTGammaEFT.Tools.Cache             import Cache
from TTGammaEFT.Analysis.regions        import recoTTGammaRegions as regions
from Analysis.Tools.metFilters          import getFilterCut
from Analysis.Tools.DirDB               import DirDB

# Default Parameter
loggerChoices = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO', nargs='?', choices=loggerChoices,                                help="Log level for logging")
argParser.add_argument('--selection',          action='store',      default='nLepTight1-nLepVeto1-nJet4p-nBTag1p-pTG20-nPhoton1p')
argParser.add_argument('--small',              action='store_true',                                                                                  help='Run only on a small subset of the data?', )
argParser.add_argument('--year',               action='store',      default=None,   type=int,  choices=[2016,2017,2018],                             help="Which year to plot?")
argParser.add_argument('--noData',             action='store_true', default=False,                                                                   help='also plot data?')
argParser.add_argument('--overwrite',          action='store_true',                                                                                  help='Overwrite Database entries?', )
argParser.add_argument('--inclusive',          action='store_true',                                                                                  help='run inclusive regions', )
argParser.add_argument('--manual',             action='store_true',                                                                                  help='run no regions, but add it manually to the selection string', )
argParser.add_argument('--noQCD',              action='store_true',                                                                                  help='run w/o QCD', )
argParser.add_argument('--QCDOnly',            action='store_true',                                                                                  help='run only QCD estimate', )
argParser.add_argument('--checkOnly',          action='store_true',                                                                                  help='Just check if yield is already calculated', )
argParser.add_argument('--cores',              action='store',      default=1,                       type=int,                                       help='number of cpu cores for multicore processing')
args = argParser.parse_args()

if args.inclusive and not args.manual:
    from TTGammaEFT.Analysis.regions        import recoTTGammaRegionsIncl as regions
elif not args.manual:
    from TTGammaEFT.Analysis.regions        import recoTTGammaRegions     as regions
else:
    regions = ["manual"]


# Samples
if args.year == 2016:
    from TTGammaEFT.Samples.nanoTuples_Summer16_private_semilep_postProcessed      import *
    if not args.noData:
        from TTGammaEFT.Samples.nanoTuples_Run2016_14Dec2018_semilep_postProcessed import *

elif args.year == 2017:
    from TTGammaEFT.Samples.nanoTuples_Fall17_private_semilep_postProcessed        import *
    if not args.noData:
        from TTGammaEFT.Samples.nanoTuples_Run2017_14Dec2018_semilep_postProcessed import *

elif args.year == 2018:
    from TTGammaEFT.Samples.nanoTuples_Autumn18_private_semilep_postProcessed      import *
    if not args.noData:
        from TTGammaEFT.Samples.nanoTuples_Run2018_14Dec2018_semilep_postProcessed import *
# Logger
import Analysis.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

# Sample definition
if args.year == 2016:
    mc = [ TTG_priv_16, TT_pow_16, DY_LO_16, singleTop_16, WJets_16, TG_16, WG_NLO_16, ZG_16, other_16, QCD_16 ]
    if not args.noQCD:
#        all   = all_noQCD_16
        qcd   = QCD_16
        gjets = GJets_16

elif args.year == 2017:
    mc = [ TTG_priv_17, TT_pow_17, DY_LO_17, singleTop_17, WJets_17, TG_17, WG_NLO_17, ZG_17, other_17, QCD_17 ]
    if not args.noQCD:
#        all   = all_noQCD_17
        qcd   = QCD_17
        gjets = GJets_17

elif args.year == 2018:
    mc = [ TTG_priv_18, TT_pow_18, DY_LO_18, singleTop_18, WJets_18, TG_18, WG_NLO_18, ZG_18, other_18, QCD_18 ]
    if not args.noQCD:
#        all   = all_noQCD_18
        qcd   = QCD_18
        gjets = GJets_18



filterCutData = getFilterCut( args.year, isData=True )
filterCutMc   = getFilterCut( args.year, isData=False )
tr = TriggerSelector( args.year, singleLepton=True )
triggerCutMc  = tr.getSelection( "MC" )


if args.noData:
    if args.year == 2016:   lumi_scale = 35.92
    elif args.year == 2017: lumi_scale = 41.86
    elif args.year == 2018: lumi_scale = 58.83
    allSamples = mc
else:
    if args.year == 2016:   data_sample = Run2016
    elif args.year == 2017: data_sample = Run2017
    elif args.year == 2018: data_sample = Run2018
    data_sample.texName        = "data (legacy)"
    data_sample.name           = "data"
    lumi_scale                 = data_sample.lumi * 0.001
#    data_sample.setWeightString("weight")
#    data_sample.setSelectionString( [ filterCutData, cutInterpreter.cutString( args.selection ) ] )
    allSamples = [data_sample] + mc

weightString = "(weight*%f*reweightL1Prefire*reweightPU*reweightLeptonTightSF*reweightLeptonTrackingTightSF*reweightPhotonSF*reweightPhotonElectronVetoSF*reweightBTag_SF)"%lumi_scale
#try to create a weightString which gives a SF of 2.25 to misID photon events for QCD estimate
fancyWeightString = weightString + "+" + weightString + "*(PhotonGood0_photonCat==2)*1.25"

#for sample in mc:
#    sample.setWeightString(weightString)
#    if not "QCD" in sample.name:
#        sample.setSelectionString( [ filterCutMc, triggerCutMc, cutInterpreter.cutString( args.selection ), "overlapRemoval==1" ] )

#if not args.noQCD:
#    all.setWeightString(weightString)
#    qcd.setWeightString(weightString)
#    gjets.setWeightString(weightString)

if args.small:
    for sample in allSamples:
        sample.normalization=1.
        sample.reduceFiles( factor=15 )
#        sample.addWeightString("%f"%(1./sample.normalization))

cache_dir = os.path.join(cache_directory, "yields", str(args.year))

replaceSelection = {
    "nLeptonTight":    "nLeptonTightInvIso",
    "nMuonTight":      "nMuonTightInvIso",
    "nElectronTight":  "nElectronTightInvIso",
    "mLtight0Gamma":   "mLinvtight0Gamma",
}


def cacheYields( (i_region, i_sample) ):
#def cacheYields( i_sample ):

    region = regions[i_region]
    sample = allSamples[i_sample]

    if sample.name==data_sample.name and "cat" in args.selection: return
    if ("QCD" in sample.name and args.noQCD) or ("QCD" in sample.name and args.noData): return
    if not "QCD" in sample.name and args.QCDOnly: return

    logger.info( "At region %s for sample %s"%(region, sample.name) )

#    dbFilename = "yields_%s.sql"%sample.name
#    yieldDB = Cache( os.path.join( cache_dir, dbFilename ), "yields", [ "selection", "year", "small", "region", sample.name] )
#    if not yieldDB: raise

#    res = {"selection":args.selection, "year":args.year, "small":args.small, "region":str(region), sample.name:sample.name }
    yieldDB = DirDB( cache_dir )
    if not yieldDB: raise
    res = "_".join( [sample.name, args.selection, "small" if args.small else "full"] )

    if yieldDB.contains( res ) and not args.overwrite:
        if not args.checkOnly:
            logger.info( "Yield for sample %s at region %s already in database: %s" %(sample.name, region, yieldDB.get( res ) ) )
        return

    if args.checkOnly:
        logger.info( "Yield for sample %s at region %s not processed" %(sample.name, region) )
        return

    if "QCD" in sample.name:
        qcdSelection       = "-".join( [ item if not "nBTag" in item else "nBTag0" for item in args.selection.split("-") ] + ["nBTag0"] )
        qcdSelection       = "-".join( [ item for item in qcdSelection.split("-") if not "photoncat" in item and not "photonhadcat" in item and not "nLepVeto" in item ] )
        preSelectionSR     = [ cutInterpreter.cutString( args.selection ), "weight<15", filterCutMc, triggerCutMc, "overlapRemoval==1" ]
        preSelectionCR     = [ cutInterpreter.cutString( qcdSelection ),   "weight<15", filterCutMc, triggerCutMc, "overlapRemoval==1" ]
        preSelectionCRData = [ cutInterpreter.cutString( qcdSelection ),   "weight<15", filterCutData ]
        if region != "manual":
            preSelectionSR     += [ region.cutString() ]
            preSelectionCR     += [ region.cutString() ]
            preSelectionCRData += [ region.cutString() ]

        preSelectionSR     = "&&".join( preSelectionSR )
        preSelectionCR     = "&&".join( preSelectionCR )
        preSelectionCRData = "&&".join( preSelectionCRData )
        for key, val in replaceSelection.items():
            preSelectionCR     = preSelectionCR.replace(key, val)
            preSelectionCRData = preSelectionCRData.replace(key, val)

        print preSelectionSR
        print preSelectionCR
        print preSelectionCRData

        yield_QCD_CR  = qcd.getYieldFromDraw(   selectionString=preSelectionCR, weightString=weightString )["val"]
        yield_QCD_CR += gjets.getYieldFromDraw( selectionString=preSelectionCR, weightString=weightString )["val"]
        yield_QCD_SR  = qcd.getYieldFromDraw(   selectionString=preSelectionSR, weightString=weightString )["val"]
        yield_QCD_SR += gjets.getYieldFromDraw( selectionString=preSelectionSR, weightString=weightString )["val"]

        transFacQCD    = yield_QCD_SR / yield_QCD_CR if yield_QCD_CR != 0 else 0
        rate = 0

        if transFacQCD != 0:
            datCR        = data_sample.getYieldFromDraw( selectionString=preSelectionCRData, weightString="weight" )['val']

            mcNoQCDTotal = 0
            for s in mc:
                if "QCD" in s.name: continue
                y  = s.getYieldFromDraw( selectionString=preSelectionCR, weightString=fancyWeightString )['val']
                if "DY" in s.name: y *= 1.17 #hard coded DY Scale Factor for QCD estimate
                mcNoQCDTotal += y
            rate = int(round( (datCR - mcNoQCDTotal) * transFacQCD ))

    else:
        if sample.name == data_sample.name: 
            selection  = [ filterCutData, cutInterpreter.cutString( args.selection ) ]
        else:
            selection  = [ filterCutMc, triggerCutMc, cutInterpreter.cutString( args.selection ), "overlapRemoval==1" ]
        if region != "manual":
            selection += [ region.cutString() ]
        selectionString = "&&".join( selection )

        rate = sample.getYieldFromDraw( selectionString=selectionString, weightString=weightString if sample.name != data_sample.name else "weight")['val']

    logger.info("Adding yield for sample %s at region %s: %s"%(sample.name, str(region), str(rate)) )
    yieldDB.add( res, str(rate), overwrite=True )

# Multiprocessing
from multiprocessing import Pool

if not args.manual:
    for region in regions:
        region.name = str(region) # needed for Pool

# Objects can't be pickled, so args are indices of lists
input = [ (i_region, i_sample) for i_region, _ in enumerate(regions) for i_sample, _ in enumerate(allSamples) ]
#input = [ (i_region, 0) for i_region, _ in enumerate(regions) ]#for i_sample, _ in enumerate(allSamples) ]

logger.info( "Calculating %i yields for selection string %s"%(len(input), args.selection) )

pool = Pool( processes=args.cores )
_    = pool.map( cacheYields, input )
pool.close()

