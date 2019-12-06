#!/usr/bin/env python

import os, copy, time
import ROOT
from shutil                              import copyfile
from math                                import sqrt

from TTGammaEFT.Analysis.EstimatorList   import EstimatorList
from TTGammaEFT.Analysis.Setup           import Setup
from TTGammaEFT.Analysis.DataObservation import DataObservation
from TTGammaEFT.Analysis.MCBasedEstimate import MCBasedEstimate
from TTGammaEFT.Analysis.regions         import regionsTTG, noPhotonRegionTTG, inclRegionsTTG, regionsTTGfake, inclRegionsTTGfake, chgIso_thresh, chgIsoRegions
from TTGammaEFT.Analysis.SetupHelpers    import *

from TTGammaEFT.Tools.user               import cache_directory, combineReleaseLocation, cardfileLocation
from Analysis.Tools.MergingDirDB                import MergingDirDB
from Analysis.Tools.u_float              import u_float
from Analysis.Tools.cardFileWriter       import cardFileWriter
from Analysis.Tools.getPostFit           import getPrePostFitFromMLF, getFitResults

# Default Parameter
loggerChoices = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "TRACE", "NOTSET"]

# Arguments
import argparse
argParser=argparse.ArgumentParser(description="Argument parser" )
argParser.add_argument( "--logLevel",           action="store",      default="INFO",            choices=loggerChoices,      help="Log level for logging" )
argParser.add_argument( "--label",              action="store",      default="defaultSetup",    type=str,                   help="Label of results directory" )
argParser.add_argument( "--inclRegion",         action="store_true",                                                        help="use inclusive photon pt region" )
argParser.add_argument( "--overwrite",          action="store_true",                                                        help="Overwrite existing output files" )
argParser.add_argument( "--useRegions",         action="store",      nargs='*',       type=str, choices=allRegions.keys(),  help="Which regions to use?" )
argParser.add_argument( "--useChannels",        action="store",      nargs='*', default="all",   type=str, choices=["e", "mu", "all", "comb"], help="Which lepton channels to use?" )
argParser.add_argument( "--addDYSF",            action="store_true",                                                        help="add default DY scale factor" )
argParser.add_argument( "--addFakeSF",          action="store_true",                                                        help="add default fake scale factor" )
argParser.add_argument( "--addMisIDSF",         action="store_true",                                                        help="add default misID scale factor" )
argParser.add_argument( "--keepCard",           action="store_true",                                                        help="Overwrite existing output files" )
argParser.add_argument( "--expected",           action="store_true",                                                        help="Use sum of backgrounds instead of data." )
argParser.add_argument( "--useTxt",             action="store_true",                                                        help="Use txt based cardFiles instead of root/shape based ones?" )
argParser.add_argument( "--skipFitDiagnostics", action="store_true",                                                        help="Don't do the fitDiagnostics (this is necessary for pre/postfit plots, but not 2D scans)?" )
argParser.add_argument( "--significanceScan",   action="store_true",                                                        help="Calculate significance instead?")
argParser.add_argument( "--year",               action="store",      default=2016,   type=int,                              help="Which year?" )
argParser.add_argument( "--runOnLxPlus",        action="store_true",                                                        help="Change the global redirector of samples")
argParser.add_argument( "--misIDPOI",           action="store_true",                                                        help="Change POI to misID SF")
argParser.add_argument( "--vgPOI",              action="store_true",                                                        help="Change POI to misID SF")
argParser.add_argument( "--ttPOI",              action="store_true",                                                        help="Change POI to misID SF")
argParser.add_argument( "--wJetsPOI",           action="store_true",                                                        help="Change POI to misID SF")
argParser.add_argument( "--checkOnly",          action="store_true",                                                        help="Check the SF only")
argParser.add_argument( "--bkgOnly",            action="store_true",                                                        help="background only")
argParser.add_argument( "--unblind",            action="store_true",                                                        help="unblind 2017/2018")
args=argParser.parse_args()

# Logging
import Analysis.Tools.logger as logger
logger = logger.get_logger(       args.logLevel, logFile = None )
import RootTools.core.logger as logger_rt
logger_rt = logger_rt.get_logger( args.logLevel, logFile = None )

if "all" in args.useChannels: args.useChannels = None
useCache = True
if args.keepCard:
    args.overwrite = False

def replaceDictKey( dict, fromKey, toKey ):
    dict[toKey] = copy.copy(dict[fromKey])
    del dict[fromKey]
    return dict

regionNames = []
if not args.checkOnly:
    # Define estimators for CR
    default_setup            = Setup( year=args.year, runOnLxPlus=args.runOnLxPlus )
    default_setup.estimators = EstimatorList( default_setup )
    default_setup.data       = default_setup.processes["Data"]
#    default_setup.processes  = default_setup.estimators.constructProcessDict( processDict=default_processes )
    default_setup.processes["Data"] = default_setup.data
    default_setup.addon      = ""
    default_setup.regions    = inclRegionsTTG if args.inclRegion else regionsTTG

    default_photon_setup            = Setup( year=args.year, photonSelection=True, runOnLxPlus=args.runOnLxPlus )
    default_photon_setup.estimators = EstimatorList( default_photon_setup )
    default_photon_setup.data       = default_photon_setup.processes["Data"]
#    default_photon_setup.processes  = default_setup.estimators.constructProcessDict( processDict=default_processes )
    default_photon_setup.processes["Data"] = default_photon_setup.data
    default_photon_setup.addon      = ""
    default_photon_setup.regions    = inclRegionsTTG if args.inclRegion else regionsTTG

# Define SR, CR, channels and regions
setups = []
for key, val in allRegions.items():

    if not key in args.useRegions: continue
    if key not in limitOrdering:
        limitOrdering += [key]

    if args.checkOnly:
        locals()["setup"+key] = None
        continue

    locals()["setup"+key]              = default_setup.sysClone( parameters=val["parameters"] ) if val["noPhotonCR"] else default_photon_setup.sysClone( parameters=val["parameters"] )
    estimators                         = EstimatorList( locals()["setup"+key] )
    locals()["setup"+key].name         = key
    locals()["setup"+key].channels     = val["channels"] #default_setup.channels
    locals()["setup"+key].noPhotonCR   = val["noPhotonCR"]
    locals()["setup"+key].signalregion = "SR" in key and not "Iso" in key
    locals()["setup"+key].regions      = val["inclRegion" if args.inclRegion else "regions"]
    locals()["setup"+key].data         = default_setup.data if val["noPhotonCR"] else default_photon_setup.data
    locals()["setup"+key].processes    = estimators.constructProcessDict( processDict=val["processes"] ) if "processes" in val else default_setup.processes if val["noPhotonCR"] else default_photon_setup.processes
    locals()["setup"+key].processes["Data"] = locals()["setup"+key].data
    
#    locals()["setup"+key].processes["Data"] = locals()["setup"+key].data
#    if args.misIDPOI: replaceDictKey( locals()["setup"+key].processes, "signal", "TTG" )
    locals()["setup"+key].addon      = key

# sort regions accoring to ordering
for reg in limitOrdering:
    if "setup"+reg in locals():
        regionNames.append(reg)
        setups.append(locals()["setup"+reg])

# use the regions as key for caches
regionNames.sort()
if args.addDYSF:     regionNames.append("addDYSF")
if args.addMisIDSF:  regionNames.append("addMisIDSF")
if args.addFakeSF:   regionNames.append("addFakeSF")
if args.inclRegion:  regionNames.append("incl")
if args.misIDPOI:    regionNames.append("misIDPOI")
if args.vgPOI:       regionNames.append("vgPOI")
if args.wJetsPOI:    regionNames.append("wJetsPOI")
if args.ttPOI:       regionNames.append("ttPOI")
if args.useChannels: regionNames.append("_".join(args.useChannels))

baseDir       = os.path.join( cache_directory, "analysis",  str(args.year), "limits" )
limitDir      = os.path.join( baseDir, "cardFiles", args.label, "expected" if args.expected else "observed" )
if not os.path.exists( limitDir ): os.makedirs( limitDir )

cacheFileName   = os.path.join( limitDir, "calculatedLimits" )
limitCache      = MergingDirDB( cacheFileName )

cacheFileName   = os.path.join( limitDir, "calculatedSignifs" )
signifCache     = MergingDirDB( cacheFileName )

cacheFileName   = os.path.join( limitDir, "systematics", "systematics" )
scaleUncCache   = MergingDirDB( cacheFileName )

cacheFileName   = os.path.join( limitDir, "systematics", "isr" )
isrUncCache     = MergingDirDB( cacheFileName )

cacheFileName   = os.path.join( limitDir, "systematics", "scale" )
scaleUncCache   = MergingDirDB( cacheFileName )

cacheFileName   = os.path.join( limitDir, "systematics", "pdf" )
pdfUncCache     = MergingDirDB( cacheFileName )

def getScaleUnc( name, r, channel ):
    if scaleUncCache.contains( (name, r, channel) ): max( 0.01, scaleUncCache.get( (name, r, channel) ) )
    else:                                            return 0.01

def getPDFUnc( name, r, channel ):
    if pdfUncCache.contains( (name, r, channel) ): return max( 0.02, PDFUncCaches[process].get( (name, r, channel) ) )
    else:                                          return 0.02

def getISRUnc( name, r, channel ):
    if isrUncCache.contains( (name,r,channel) ): return abs( isrUncCache.get( (name, r, channel) ) )
    else:                                        return 0.02

def wrapper():
    c = cardFileWriter.cardFileWriter()
    c.releaseLocation = combineReleaseLocation

    cardFileNameTxt   = os.path.join( limitDir, "_".join( regionNames ) + ".txt" )
    cardFileNameShape = cardFileNameTxt.replace( ".txt", "_shape.root" )
    cardFileName      = cardFileNameTxt
    if ( not os.path.exists(cardFileNameTxt) or ( not os.path.exists(cardFileNameShape) and not args.useTxt ) ) or args.overwrite:

        if args.checkOnly:
            print cardFileNameShape
            logger.info("Combine Card not found. Please run without --checkOnly first!")
            return

        counter=0
        c.reset()
        c.setPrecision(3)
        shapeString     = "lnN" if args.useTxt else "shape"
        # experimental
        c.addUncertainty( "PU",            shapeString)
        c.addUncertainty( "JEC",           shapeString)
        c.addUncertainty( "JER",           shapeString)
        c.addUncertainty( "SFb",           shapeString)
        c.addUncertainty( "SFl",           shapeString)
#        c.addUncertainty( "trigger",       shapeString)
        c.addUncertainty( "leptonSF",      shapeString)
        c.addUncertainty( "leptonTrackSF", shapeString)
        c.addUncertainty( "photonSF",      shapeString)
        c.addUncertainty( "eVetoSF",       shapeString)
        c.addUncertainty( "prefireSF",     shapeString)
        # theory (PDF, scale, ISR)
#        c.addUncertainty( "scale",      shapeString)
#        c.addUncertainty( "PDF",        shapeString)
#        c.addUncertainty( "ISR",        shapeString)


        default_QCD_unc      = 0.5 if not args.inclRegion else 1.0 # 50%
#        c.addUncertainty( "QCD",        shapeString )
        c.addUncertainty( "QCD_0p",        shapeString )
        c.addUncertainty( "QCD_1p",        shapeString )
        if not args.inclRegion:
            c.addUncertainty( "QCD_TF",     shapeString )

        # Only if TT CR is used
        default_TT_unc       = 0.2
        addTTUnc = False
        if any( ["TT" in name for name in args.useRegions] ) and not args.ttPOI:
            addTTUnc = True
            c.addUncertainty( "TT_gen",        shapeString )
#            c.addRateParameter('TT', 1, '[0,2]')
            c.addUncertainty( "TT_0p",         shapeString )
                
        fakeLowUnc = 0.3
        c.addUncertainty( "fake",      shapeString )
        fakeHighUnc = 0.3
        c.addUncertainty( "fake_high",      shapeString )

        default_HadFakes_unc = 0.3
        default_HadCorr_unc = 0.3
        addFakeUnc = True
#        if any( ["fake" in name for name in args.useRegions] ):
#            addFakeUnc = True
        c.addUncertainty( "hadFakes",   shapeString )
#            for i_iso, iso in enumerate(chgIsoRegions):
#                c.addUncertainty( "fake_corr_%i"%i_iso,   shapeString )                

        default_VG_unc       = 0.35
        if not args.vgPOI:
#            c.addRateParameter('VG_gen', 1, '[0,2]')
            c.addUncertainty( "VG_gen",         shapeString )
#            c.addUncertainty( "VG_0p",         shapeString )

        default_Other_unc    = 0.35
        c.addUncertainty( "other_gen",      shapeString )
        c.addUncertainty( "other_0p",      shapeString )

        # Only if WJets CR is used
        default_WJets_unc    = 0.3
        addWJetsUnc = False
        if any( ["WJet" in name for name in args.useRegions] ) and not args.wJetsPOI:
            c.addUncertainty( "WJets_gen",      shapeString )
#            c.addRateParameter('WJets_gen', 1, '[0,2]')
            c.addUncertainty( "WJets_0p",      shapeString )
            addWJetsUnc = True

        default_DY_unc       = 0.1 if args.addDYSF else 0.3
        if any( ["DY3" in name or "DY4p" in name for name in args.useRegions] ):
            c.addUncertainty( "DY_gen",     shapeString )
#            c.addRateParameter('DY', 1, '[0,2]')
            c.addUncertainty( "DY_0p",     shapeString )

        default_misID_unc    = 0.1
        addMisIDUnc = False
        if not args.addMisIDSF and not args.misIDPOI:
             c.addFreeParameter( "misID" )
        else:
            c.addUncertainty( "misIDSF",    shapeString )
            addMisIDUnc = True

        for setup in setups:
            observation = DataObservation( name="Data", process=setup.data, cacheDir=setup.defaultCacheDir() )
            for pName, pList in setup.processes.items():
                if pName == "Data": continue
                for e in pList:
                    e.initCache( setup.defaultCacheDir() )

            if not setup.noPhotonCR:
                pt_Norm = float( sum( [1./r.vals.values()[0][0] if r.vals.values()[0][0] else 0. for r in setup.regions] ) )
            for r in setup.regions:
                if not setup.noPhotonCR:
                    # average photon pt in region for misID pt dependence scaling (misID from tracker). scale with 1/pt
                    # for simplicity take only lower value
                    av_pt = 1. / (pt_Norm * r.vals.values()[0][0]) if pt_Norm and r.vals.values()[0][0] else 0.
                else:
                    av_pt = 0

                for i_ch, channel in enumerate(setup.channels):

                    if args.useChannels and channel not in args.useChannels: continue

                    niceName      = " ".join( [ channel, str(r), setup.addon ] )
                    binname       = "Bin%i"%counter
                    counter      += 1
                    total_exp_bkg = 0

                    if args.misIDPOI:
                        c.addBin( binname, [ pName.replace("signal","TTG") for pName in setup.processes.keys() if not "misID" in pName and pName != "Data" ], niceName)
                    elif args.vgPOI:
                        c.addBin( binname, [ pName.replace("signal","TTG") for pName in setup.processes.keys() if not "WG" in pName and not "ZG" in pName and not "VG" in pName and pName != "Data" ], niceName)
                    elif args.ttPOI:
                        c.addBin( binname, [ pName.replace("signal","TTG") for pName in setup.processes.keys() if not "TT" in pName and pName != "Data" ], niceName)
                    elif args.wJetsPOI:
                        c.addBin( binname, [ pName.replace("signal","TTG") for pName in setup.processes.keys() if not "WJets" in pName and pName != "Data" ], niceName)
                    else:
                        c.addBin( binname, [ pName for pName in setup.processes.keys() if pName != "signal" and pName != "Data" ], niceName)
    
                    mute   = False
                    sigExp = u_float(0.,0.)
                    sigUnc = {}
                    for pName, pList in setup.processes.items():

                        if pName == "Data": continue
                        misIDPOI = "misID" in pName and args.misIDPOI
                        vgPOI    = ("WG" in pName or "ZG" in pName or "VG" in pName) and args.vgPOI
                        wJetsPOI = "WJets" in pName and args.wJetsPOI
                        ttPOI    = "TT"    in pName and args.ttPOI

                        newPOI_input = any( [args.misIDPOI, args.vgPOI, args.wJetsPOI, args.ttPOI] )
                        newPOI       = any( [misIDPOI, vgPOI, wJetsPOI, ttPOI] )
                        signal   = True if newPOI else pName == "signal"
                        expected = u_float(0.,0.)
                        
                        if newPOI_input and pName == "signal":
                            pName = "TTG"

                        for e in pList:
                            exp_yield = e.cachedEstimate( r, channel, setup )
                            if e.name.count( "DY" ) and args.addDYSF:
                                exp_yield *= DYSF_val[args.year]
                                logger.info( "Scaling DY background %s by %f"%(e.name,DYSF_val[args.year]) )
                            if e.name.count( "misID" ) and args.addMisIDSF:
                                exp_yield *= misIDSF_val[args.year]
                                logger.info( "Scaling misID background %s by %f"%(e.name,misIDSF_val[args.year]) )
                            if e.name.count( "had" ) and args.addFakeSF:
                                exp_yield *= fakeSF_val[args.year]
                                logger.info( "Scaling fake background %s by %f"%(e.name,fakeSF_val[args.year]) )
                            e.expYield = exp_yield
                            expected  += exp_yield

                        logger.info( "Expectation for process %s: %s", pName, expected.val )

                        if newPOI_input and signal:
                            sigExp += expected
                            logger.info( "Adding expectation for process %s to signal. Total signal now: %s", pName, sigExp )
                        else:
                            c.specifyExpectation( binname, pName, expected.val )

#                        if not signal: total_exp_bkg += expected.val
                        total_exp_bkg += expected.val
                        if signal and expected.val <= 0.01: mute = True

                        tf, pu, jec, jer, sfb, sfl, trigger, lepSF, lepTrSF, phSF, eVetoSF, pfSF = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
#                        scale, pdf, isr = 0, 0, 0
                        dyGenUnc, ttGenUnc, vgGenUnc, wjetsGenUnc, otherGenUnc, qcdUnc, misIDUnc, hadFakesUnc, misIDPtUnc = 0, 0, 0, 0, 0, 0, 0, 0, 0
                        dy0pUnc, tt0pUnc, wjets0pUnc, other0pUnc = 0, 0, 0, 0
                        fakeCorrUnc = []
                        for i_iso, iso in enumerate(chgIsoRegions):
                            fakeCorrUnc.append(0)
                        if expected.val:
                            for e in pList:
                                y_scale   = e.expYield.val / expected.val

                                if e.name.count( "QCD" ):
                                    qcdUnc   += y_scale * default_QCD_unc
                                    if not args.inclRegion:
                                        tf   += y_scale * e.TransferFactorStatistic( r, channel, setup ).val
                                    continue # no systematics for data-driven QCD

                                if e.name.count( "DY" ):
                                    if setup.noPhotonCR:
                                        dy0pUnc    += y_scale * default_DY_unc
                                    if e.name.count( "gen" ):
                                        dyGenUnc    += y_scale * default_DY_unc
                                if e.name.count( "TT_pow" ) or (args.ttPOI and signal):
                                    if setup.noPhotonCR:
                                        tt0pUnc    += y_scale * default_TT_unc
                                    if e.name.count( "gen" ):
                                        ttGenUnc    += y_scale * default_TT_unc
                                if (e.name.count( "ZG" ) or e.name.count("WG")) or (args.vgPOI and signal):
#                                    if setup.noPhotonCR:
#                                        vg0pUnc    += y_scale * default_VG_unc
                                    if e.name.count( "gen" ) or setup.noPhotonCR:
                                        vgGenUnc    += y_scale * default_VG_unc
                                if e.name.count( "WJets" ) or (args.wJetsPOI and signal):
                                    if setup.noPhotonCR:
                                        wjets0pUnc += y_scale * default_WJets_unc
                                    if e.name.count( "gen" ):
                                        wjetsGenUnc += y_scale * default_WJets_unc
                                if e.name.count( "other" ):
                                    if setup.noPhotonCR:
                                        other0pUnc += y_scale * default_Other_unc
                                    if e.name.count( "gen" ):
                                        otherGenUnc += y_scale * default_Other_unc
                                if e.name.count( "_had" ):
                                        hadFakesUnc += y_scale * default_HadFakes_unc
                                if e.name.count( "misID" ) or (args.misIDPOI and signal):
                                        misIDUnc += y_scale * default_misID_unc
#                                    misIDPtUnc += y_scale * default_misIDpt_unc * av_pt
#                                for i_iso, iso in enumerate(chgIsoRegions):
#                                    if iso.cutString() in r.cutString():
#                                        fakeCorrUnc[i_iso] += y_scale * default_HadCorr_unc
#                                    if "SR" in setup.name and i_iso == 0 and e.name.count( "_had" ):
#                                        fakeCorrUnc[i_iso] += y_scale * default_HadCorr_unc

                                pu       += y_scale * e.PUSystematic(                   r, channel, setup).val
                                jec      += y_scale * e.JECSystematic(                  r, channel, setup).val
                                jer      += y_scale * 0.03#e.JERSystematic(                  r, channel, setup).val
                                sfb      += y_scale * e.btaggingSFbSystematic(          r, channel, setup).val
                                sfl      += y_scale * e.btaggingSFlSystematic(          r, channel, setup).val
#                                trigger  += y_scale * e.triggerSystematic(              r, channel, setup).val
                                lepSF    += y_scale * e.leptonSFSystematic(             r, channel, setup).val
                                lepTrSF  += y_scale * e.leptonTrackingSFSystematic(     r, channel, setup).val
                                phSF     += y_scale * e.photonSFSystematic(             r, channel, setup).val
                                eVetoSF  += y_scale * e.photonElectronVetoSFSystematic( r, channel, setup).val
                                pfSF     += y_scale * e.L1PrefireSystematic(            r, channel, setup).val
#                                scale    += y_scale * getScaleUncBkg( e.name, r, channel )
#                                pdf      += y_scale * getPDFUnc(      e.name, r, channel )
#                                isr      += y_scale * getISRUnc(      e.name, r, channel )


#                        else:
#                                if pName.count( "QCD" ):
#                                    qcdUnc      += default_QCD_unc
#                                if pName.count( "DY" ):
#                                    dyUnc       += default_DY_unc
#                                if pName.count( "TT_pow" ):
#                                    ttUnc       += default_TT_unc
#                                if pName.count( "VG" ):
#                                    vgUnc       += default_VG_unc
#                                if pName.count( "WJets" ):
#                                    wjetsUnc    += default_WJets_unc
#                                if pName.count( "other" ):
#                                    otherUnc    += default_Other_unc
#                                if pName.count( "_had" ):
#                                    hadFakesUnc += default_HadFakes_unc

                        def addUnc( c, name, binname, pName, unc, unc_yield, signal ):
                            if newPOI_input and signal:
                                if name in sigUnc: sigUnc[name] += u_float(0,unc)*unc_yield
                                else:              sigUnc[name]  = u_float(0,unc)*unc_yield
                            else:
                                c.specifyUncertainty( name, binname, pName, 1 + unc )

                        addUnc( c, "PU",            binname, pName, pu,      expected.val, signal )
                        addUnc( c, "JEC",           binname, pName, jec,     expected.val, signal )
                        addUnc( c, "JER",           binname, pName, jer,     expected.val, signal )
                        addUnc( c, "SFb",           binname, pName, sfb,     expected.val, signal )
                        addUnc( c, "SFl",           binname, pName, sfl,     expected.val, signal )
#                        addUnc( c, "trigger",       binname, pName, trigger, expected.val, signal )
                        addUnc( c, "leptonSF",      binname, pName, lepSF,   expected.val, signal )
                        addUnc( c, "leptonTrackSF", binname, pName, lepTrSF, expected.val, signal )
                        addUnc( c, "photonSF",      binname, pName, phSF,    expected.val, signal )
                        addUnc( c, "eVetoSF",       binname, pName, eVetoSF, expected.val, signal )
                        addUnc( c, "prefireSF",     binname, pName, pfSF,    expected.val, signal )
                        

                        if qcdUnc:
                            if setup.noPhotonCR:
                                addUnc( c, "QCD_0p", binname, pName, qcdUnc, expected.val, signal )
#                                addUnc( c, "QCD", binname, pName, qcdUnc, expected.val, signal )
                            else:
#                                addUnc( c, "QCD", binname, pName, qcdUnc, expected.val, signal )
                                addUnc( c, "QCD_1p", binname, pName, qcdUnc, expected.val, signal )
                        if tf and not args.inclRegion:
                            addUnc( c, "QCD_TF", binname, pName, tf, expected.val, signal )

                        if dy0pUnc:
                            addUnc( c, "DY_0p", binname, pName, dy0pUnc, expected.val, signal )
                        if tt0pUnc and addTTUnc and not args.ttPOI:
                            addUnc( c, "TT_0p", binname, pName, tt0pUnc, expected.val, signal )
#                        if vg0pUnc:
#                            addUnc( c, "VG_0p", binname, pName, vg0pUnc, expected.val, signal )
                        if wjets0pUnc and addWJetsUnc and not args.wJetsPOI:
                            addUnc( c, "WJets_0p", binname, pName, wjets0pUnc, expected.val, signal )
                        if other0pUnc:
                            addUnc( c, "other_0p", binname, pName, other0pUnc, expected.val, signal )

                        if dyGenUnc:
                            addUnc( c, "DY_gen", binname, pName, dyGenUnc, expected.val, signal )
                        if ttGenUnc and addTTUnc:
                            addUnc( c, "TT_gen", binname, pName, ttGenUnc, expected.val, signal )
                        if vgGenUnc and not vgPOI:
                            addUnc( c, "VG_gen", binname, pName, vgGenUnc, expected.val, signal )
                        if wjetsGenUnc and addWJetsUnc:
                            addUnc( c, "WJets_gen", binname, pName, wjetsGenUnc, expected.val, signal )
                        if otherGenUnc:
                            addUnc( c, "other_gen", binname, pName, otherGenUnc, expected.val, signal )

#                        if "fake" in setup.name and "low" in setup.name:
#                            addUnc( c, "fake_low", binname, pName, fakeLowUnc, expected.val, signal )
#                        if "fake" in setup.name and "high" in setup.name:
#                            addUnc( c, "fake_low", binname, pName, fakeHighUnc, expected.val, signal )
                        if hadFakesUnc and addFakeUnc:
                            addUnc( c, "hadFakes", binname, pName, hadFakesUnc, expected.val, signal )
#                        if any(fakeCorrUnc) and addFakeUnc:
#                            for i_iso, iso in enumerate(chgIsoRegions):
#                                addUnc( c, "fake_corr_%i"%i_iso, binname, pName, fakeCorrUnc[i_iso], expected.val, signal )                

                        if misIDUnc and addMisIDUnc:
                            addUnc( c, "misIDSF", binname, pName, misIDUnc, expected.val, signal )

                        # MC bkg stat (some condition to neglect the smaller ones?)
                        uname = "Stat_%s_%s"%(binname, pName if not (newPOI_input and signal) else "signal")
                        if not (newPOI_input and signal):
                            c.addUncertainty( uname, "lnN" )
                        addUnc( c, uname, binname, pName, (expected.sigma/expected.val) if expected.val > 0 else 0.01, expected.val, signal )
#                        uname = "Stat_%s_%s"%(binname,"signal" if signal else pName)
#                        c.addUncertainty( uname, "lnN" )
#                        addUnc( c, uname, binname, pName, (expected.sigma/expected.val) if expected.val > 0 else 0.01, expected.val, signal )

                    if newPOI_input:
                        uname = "Stat_%s_%s"%(binname,"signal")
                        c.addUncertainty( uname, "lnN" )
                        c.specifyExpectation( binname, "signal", sigExp.val )
                        if sigExp.val:
                            for key, val in sigUnc.items():
                                c.specifyUncertainty( key, binname, "signal", 1 + val.sigma/sigExp.val )

                    if args.expected or (args.year in [2017,2018] and not args.unblind and setup.signalregion):
                        c.specifyObservation( binname, int( round( total_exp_bkg, 0 ) ) )
                        logger.info( "Expected observation: %s", int( round( total_exp_bkg, 0 ) ) )
                    else:
                        c.specifyObservation( binname,  int( observation.cachedObservation(r, channel, setup).val ) )
                        logger.info( "Observation: %s", int( observation.cachedObservation(r, channel, setup).val ) )

                    if mute and total_exp_bkg <= 0.01:
                        c.muted[binname] = True

        # Flat luminosity uncertainty
        c.addUncertainty( "Lumi", "lnN" )
        c.specifyFlatUncertainty( "Lumi", 1.026 )

        cardFileNameTxt     = c.writeToFile( cardFileNameTxt )
        cardFileNameShape   = c.writeToShapeFile( cardFileNameShape )
        cardFileName        = cardFileNameTxt if args.useTxt else cardFileNameShape
#        copycard            = cardFileNameTxt.replace(cache_directory,cardfileLocation)
#        if not os.path.exists( os.path.dirname(copycard) ): os.makedirs( os.path.dirname(copycard) )
#        copyfile( cardFileNameTxt, copycard )
#        logger.info( "Copying cardfile from %s to %s"%(cardFileNameTxt,copycard) )
#        copycard            = cardFileNameShape.replace(cache_directory,cardfileLocation)
#        copyfile( cardFileNameShape, copycard )
    else:
        logger.info( "File %s found. Reusing."%cardFileName )
        cardFileNameShape = cardFileNameShape.replace('.root', 'Card.txt')
        cardFileName      = cardFileNameTxt if args.useTxt else cardFileNameShape
    
    sConfig = "_".join(regionNames)
    res = None
    if args.significanceScan:
        if useCache and not args.overwrite and signifCache.contains( sConfig ):
            res = signifCache.get( sConfig )
        else:
            res = c.calcSignif( cardFileName )
            signifCache.add( sConfig, res, overwrite=True )
    
    else:
        if useCache and not args.overwrite and limitCache.contains( sConfig ):
            res = limitCache.get( sConfig )
        else:
#            if not args.bkgOnly:
            res = c.calcLimit( cardFileName )
            if not args.skipFitDiagnostics:
                c.calcNuisances( cardFileName, bonly=args.bkgOnly )
            if not args.bkgOnly:
                limitCache.add( sConfig, res, overwrite=True )

    ###################
    # extract the SFs #
    ###################
    if not args.useTxt and not args.skipFitDiagnostics:
        # Would be a bit more complicated with the classical txt files, so only automatically extract the SF when using shape based datacards
        
        combineWorkspace = cardFileNameShape.replace( "shapeCard.txt","shapeCard_FD.root" )
        logger.info( "Extracting fit results from %s"%combineWorkspace )

#        copycard = combineWorkspace.replace( cache_directory, cardfileLocation )
#        copyfile( combineWorkspace, copycard )
#        logger.info( "Copying cardfile from %s to %s"%(cardFileNameTxt,copycard) )
        
        postFitResults = getFitResults( combineWorkspace )
        postFit        = postFitResults["tree_fit_b" if args.bkgOnly else "tree_fit_sb"]
        preFit         = postFitResults["tree_prefit"]
        printSF        = ["QCD_0p", "QCD_1p", "QCD", "QCD_TF", "TT_0p", "TT_gen", "VG_gen", "other_0p",  "other_gen", "WJets_0p", "WJets_gen", "DY_0p",  "DY_gen", "hadFakes", "misID"]
        for i_iso, iso in enumerate(chgIsoRegions):
            printSF.append("fake_corr_%i"%i_iso)

#        postFitResults.update(getPrePostFitFromMLF( combineWorkspace ))

        if not os.path.isdir("logs"): os.mkdir("logs")
        write_time  = time.strftime("%Y %m %d %H:%M:%S", time.localtime())

        with open("logs/cardFiles.dat", "a") as f:
            f.write( cardFileNameTxt + "\n" )

        with open("logs/scaleFactors.dat", "a") as f:
            f.write( "\n\n" + cardFileNameTxt + ", Fit Status: %i\n"%postFit["fit_status"] )
            f.write( "\n\n POI: %f\n"%postFit["r"] )
            print
            print "## Scale Factors for backgrounds, fit status: %i ##"%postFit["fit_status"]
            print "POI: %f"%postFit["r"]

            for sf_name in printSF:
                if sf_name not in postFit.keys(): continue
                sf = "{:20}{:4.2f}".format( sf_name, 1+postFit[sf_name] )
                print sf
                f.write( write_time + ": " + "_".join( regionNames ) + ": " + sf + "\n" )

#            sf = "{:20}{:4.2f}{:3}{:4.2f}".format( "TT:",           (TT_postfit/TT_prefit).val,   " +/- ",  TT_postfit.sigma/TT_postfit.val)
#            print sf
#            f.write( write_time + ": " + "_".join( regionNames ) + ": " + sf + "\n" )

#            sf = "{:20}{:4.2f}{:3}{:4.2f}".format( "VG:",           (VG_postfit/VG_prefit).val,   " +/- ",  VG_postfit.sigma/VG_postfit.val)
#            print sf
#            f.write( write_time + ": " + "_".join( regionNames ) + ": " + sf + "\n" )

#            sf = "{:20}{:4.2f}{:3}{:4.2f}".format( "WJets:",           (WJets_postfit/WJets_prefit).val,   " +/- ",  WJets_postfit.sigma/WJets_postfit.val)
#            print sf
#            f.write( write_time + ": " + "_".join( regionNames ) + ": " + sf + "\n" )

#            sf = "{:20}{:4.2f}{:3}{:4.2f}".format( "QCD:",          (QCD_postfit/QCD_prefit).val,   " +/- ",  QCD_postfit.sigma/QCD_postfit.val)
#            print sf
#            f.write( write_time + ": " + "_".join( regionNames ) + ": " + sf + "\n" )

#            sf = "{:20}{:4.2f}{:3}{:4.2f}".format( "Other:",           (Other_postfit/Other_prefit).val,   " +/- ",  Other_postfit.sigma/Other_postfit.val)
#            print sf
#            f.write( write_time + ": " + "_".join( regionNames ) + ": " + sf + "\n" )

#            sf = "{:20}{:4.2f}{:3}{:4.2f}".format( "DY_misID:",        (DY_misID_postfit/DY_misID_prefit).val,   " +/- ",  DY_misID_postfit.sigma/DY_misID_postfit.val)
#            print sf
#            f.write( write_time + ": " + "_".join( regionNames ) + ": " + sf + "\n" )

#            sf = "{:20}{:4.2f}{:3}{:4.2f}".format( "TT_misID:",        (TT_misID_postfit/TT_misID_prefit).val,   " +/- ",  TT_misID_postfit.sigma/TT_misID_postfit.val)
#            print sf
#            f.write( write_time + ": " + "_".join( regionNames ) + ": " + sf + "\n" )

#            sf = "{:20}{:4.2f}{:3}{:4.2f}".format( "other_misID:",        (other_misID_postfit/other_misID_prefit).val,   " +/- ",  other_misID_postfit.sigma/other_misID_postfit.val)
#            print sf
#            f.write( write_time + ": " + "_".join( regionNames ) + ": " + sf + "\n" )

#            sf = "{:20}{:4.2f}{:3}{:4.2f}".format( "corr. DY_misID:",        ((DY_misID_postfit/DY_misID_prefit)/dySF).val,   " +/- ",  DY_misID_postfit.sigma/DY_misID_postfit.val)
#            print sf
#            f.write( write_time + ": " + "_".join( regionNames ) + ": " + sf + "\n" )

#            sf = "{:20}{:4.2f}{:3}{:4.2f}".format( "corr. TT_misID:",        ((TT_misID_postfit/TT_misID_prefit)/ttSF).val,   " +/- ",  TT_misID_postfit.sigma/TT_misID_postfit.val)
#            print sf
#            f.write( write_time + ": " + "_".join( regionNames ) + ": " + sf + "\n" )

#            sf = "{:20}{:4.2f}{:3}{:4.2f}".format( "corr. other_misID:",  ((other_misID_postfit/other_misID_prefit)/otSF).val,   " +/- ",  other_misID_postfit.sigma/other_misID_postfit.val)
#            print sf
#            f.write( write_time + ": " + "_".join( regionNames ) + ": " + sf + "\n" )

    if res: 
        sString = "-".join(regionNames)
        if args.significanceScan:
            try:   
                print "Result: %r significance %5.3f"%(sString, res["-1.000"])
                return sConfig, res
            except:
                print "Problem with limit: %r" + str(res)
                return None
        else:
            try:
                print "Result: %r obs %5.3f exp %5.3f -1sigma %5.3f +1sigma %5.3f"%(sString, res["-1.000"], res["0.500"], res["0.160"], res["0.840"])
                return sConfig, res
            except:
                print "Problem with limit: %r"%str(res)
                return None


######################################
# Load the signals and run the code! #
######################################

results = wrapper()


