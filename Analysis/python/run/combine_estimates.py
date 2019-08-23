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
argParser.add_argument('--gammaCat',           action='store',      default='all')
argParser.add_argument('--ptBin',              action='store',      default='all')
argParser.add_argument('--mode',               action='store',      default='all')
argParser.add_argument('--sieie',              action='store',      default='all')
argParser.add_argument('--chgIso',             action='store',      default='all')
args = argParser.parse_args()


# Logging
if __name__=="__main__":
    import Analysis.Tools.logger as logger
    logger = logger.get_logger( args.logLevel, logFile=None)
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger( args.logLevel, logFile=None )
else:
    import logging
    logger = logging.getLogger(__name__)


cache_dir = os.path.join(cache_directory, "yields", str(args.year))
yield_dirDB = DirDB( cache_dir )
if not yield_dirDB: raise

res = {"sample":None, "selection":args.selection, "mode":args.mode, "ptBin":args.ptBin, "cat":args.gammaCat, "sieie":args.sieie, "chgIso":args.chgIso, "small":args.small}

if args.noQCD or "tight" in args.mode:
    mc = [ "TTG", "TT_pow", "DY_LO", "WJets", "WG", "ZG", "other" ]
elif args.QCDOnly:
    mc = [ "QCD" ]
else:
    mc = [ "TTG", "TT_pow", "DY_LO", "WJets", "WG", "ZG", "other", "QCD" ]

if args.QCDOnly or args.noData:
    allSamples = mc
else:
    allSamples = ["data"] + mc


# Helpers functions, combining yields
def getLowSieieLowChgIsoCache( resDict ):
    """ low sieie low chgIso region is the SR, just take the caches SR yields
    """

    resDict["selection"] = args.selection.replace("NoChgIsoNoSieiePhoton", "nPhoton1p")
    resDict["sieie"]     = "all"
    resDict["chgIso"]    = "all"
    resDict["cat"]       = args.gammaCat.replace("had", "")
    resDict["ptBin"]     = args.ptBin.replace("had", "")
    if yield_dirDB.contains( frozenset(resDict.items()) ):
        rate = float(yield_dirDB.get( frozenset(resDict.items()) ))    
    else:
        logger.info( "getLowSieieLowChgIsoCache: No cache found for low sieie and low chgIso: sample %s"%(sample) )
        return

    resDict["selection"] = args.selection
    resDict["sieie"]     = "lowSieie"
    resDict["chgIso"]    = "lowChgIso"
    resDict["cat"]       = args.gammaCat
    resDict["ptBin"]     = args.ptBin

    logger.info("Adding yield for sample %s: %s"%(sample, str(rate)) )
    yield_dirDB.add( frozenset(resDict.items()), str(rate), overwrite=args.overwrite )


def combineDilepSFCache( resDict ):
    """ combine dileptonic DY mumu and ee regions to SF regions
    """

    rate = 0
    for mode in ["eetight","mumutight"]:
        resDict["mode"] = mode
        if not yield_dirDB.contains( frozenset(resDict.items()) ):
            logger.info( "combineDilepSFCache: No cache found for mode %s: sample %s"%(mode, sample) )
            return
        rate += float(yield_dirDB.get( frozenset(resDict.items()) ))    

    logger.info("Adding yield for sample %s: %s"%(sample, str(rate)) )
    resDict["mode"] = "SFtight"
    yield_dirDB.add( frozenset(resDict.items()), str(rate), overwrite=args.overwrite )

def combinePtBins( resDict ):
    """ combine pt binned yields to inclusive yields
    """

    rate = 0
    for pt in allPT:
        resDict["ptBin"] = pt
        if not yield_dirDB.contains( frozenset(resDict.items()) ):
            logger.info( "combinePtBins: No cache found for pt bin %s: sample %s"%(pt, sample) )
            return
        rate += float(yield_dirDB.get( frozenset(resDict.items()) ))    

    logger.info("Adding yield for sample %s: %s"%(sample, str(rate)) )
    resDict["ptBin"] = "all"
    yield_dirDB.add( frozenset(resDict.items()), str(rate), overwrite=args.overwrite )

def combineModes( resDict ):
    """ combine lepton modes to "all"
    """

    rate = 0
    for mode in ["e","mu"]:
        resDict["mode"] = mode
        if not yield_dirDB.contains( frozenset(resDict.items()) ):
            logger.info( "combineModes: No cache found for mode %s: sample %s"%(mode, sample) )
            return
        rate += float(yield_dirDB.get( frozenset(resDict.items()) ))    

    logger.info("Adding yield for sample %s: %s"%(sample, str(rate)) )
    resDict["mode"] = "all"
    yield_dirDB.add( frozenset(resDict.items()), str(rate), overwrite=args.overwrite )

def combineJetBins( resDict ):
    """ combine =3 jet and >=4 jet regions to >=3 jet regions
    """

    rate = 0
    for mode in ["nJet3", "nJet4p"]:
        resDict["selection"] = args.selection.replace("nJet3p", mode)
        if not yield_dirDB.contains( frozenset(resDict.items()) ):
            logger.info( "combineJetBins: No cache found for jet bin %s: sample %s"%(mode, sample) )
            return
        rate += float(yield_dirDB.get( frozenset(resDict.items()) ))    
    
    resDict["selection"] = args.selection
    logger.info("Adding yield for sample %s: %s"%(sample, str(rate)) )
    yield_dirDB.add( frozenset(resDict.items()), str(rate), overwrite=args.overwrite )

def combineZRegions( resDict ):
    """ combine offZ and onZ regions to inclusive region
    """

    rate = 0
    for mode in ["-offZeg", "-onZeg"]:
        resDict["selection"] = args.selection + mode
        if not yield_dirDB.contains( frozenset(resDict.items()) ):
            logger.info( "combineZRegions: No cache found for Z region %s: sample %s"%(mode, sample) )
            return
        rate += float(yield_dirDB.get( frozenset(resDict.items()) ))    

    resDict["selection"] = args.selection
    logger.info("Adding yield for sample %s: %s"%(sample, str(rate)) )
    yield_dirDB.add( frozenset(resDict.items()), str(rate), overwrite=args.overwrite )



allPT = ["lowPT","medPT","highPT"] if not "NoChgIsoNoSieiePhoton" in args.selection else ['lowhadPT', 'medhadPT', 'highhadPT']
allModes = ["e","mu"] if not "nLepTight2" in args.selection else ["eetight", "mumutight"]

# Run over all loops
for sample in allSamples:
    for cat in ["all", "photonhadcat0", "photonhadcat1", "photonhadcat2", "photonhadcat3"]:

        if "nPhoton0" in args.selection and cat != "all": continue
        if sample=="data" and cat != "all": continue
        res["cat"] = cat.replace("had", "") if not "NoChgIsoNoSieiePhoton" in args.selection else cat
        res["sample"] = sample

        logger.info( "Combining sample %s and photon cat %s"%(sample, res["cat"]) )

        if not args.selection.endswith("-onZeg") and not args.selection.endswith("-offZeg") and not "nPhoton0" in args.selection:
            for mode in allModes:
                res["mode"] = mode
                for pt in allPT:
                    res["ptBin"] = pt
                    combineZRegions( copy.copy(res) )
            res["mode"]  = args.mode
            res["ptBin"] = args.ptBin

        if "nJet3p" in args.selection:
            for mode in allModes:
                res["mode"] = mode
                for pt in allPT:
                    res["ptBin"] = pt
                    combineJetBins( copy.copy(res) )

        if "NoChgIsoNoSieiePhoton" in args.selection and args.sieie == "lowSieie" and args.chgIso == "lowChgIso":
            for mode in allModes:
                res["mode"] = mode
                for pt in allPT:
                    res["ptBin"] = pt
                    getLowSieieLowChgIsoCache( copy.copy(res) )
            res["mode"]  = args.mode
            res["ptBin"] = args.ptBin

        if args.ptBin == "all" and not "nPhoton0" in args.selection:
            for mode in allModes:
                res["mode"] = mode
                combinePtBins( copy.copy(res) )
            res["mode"]  = args.mode

        if args.mode == "all" and not "nLepTight2" in args.selection:
            for pt in allPT:
                res["ptBin"] = pt
                combineModes( copy.copy(res) )
            res["ptBin"] = args.ptBin

        if args.mode == "SFtight" and "nLepTight2" in args.selection:
            combineDilepSFCache( copy.copy(res) )




