#!/usr/bin/env python

import os, copy, time
import ROOT

from math                                import sqrt

from TTGammaEFT.Analysis.EstimatorList   import EstimatorList
from TTGammaEFT.Analysis.Setup           import Setup
from TTGammaEFT.Analysis.DataObservation import DataObservation
from TTGammaEFT.Analysis.MCBasedEstimate import MCBasedEstimate
from TTGammaEFT.Analysis.regions         import regionsTTG, noPhotonRegionTTG, inclRegionsTTG, regionsTTGfake, inclRegionsTTGfake
from TTGammaEFT.Analysis.SetupHelpers    import *

from TTGammaEFT.Tools.user               import cache_directory, combineReleaseLocation
from Analysis.Tools.DirDB                import DirDB
from Analysis.Tools.u_float              import u_float
from Analysis.Tools.cardFileWriter       import cardFileWriter
from Analysis.Tools.getPostFit           import getPrePostFitFromMLF

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
#argParser.add_argument( "--useChannel",         action="store",      default="all",   type=str, choices=["e", "mu", "all", "comb"], help="Which lepton channels to use?" )
argParser.add_argument( "--addDYSF",            action="store_true",                                                        help="add default DY scale factor" )
argParser.add_argument( "--addMisIDSF",         action="store_true",                                                        help="add default misID scale factor" )
argParser.add_argument( "--keepCard",           action="store_true",                                                        help="Overwrite existing output files" )
argParser.add_argument( "--expected",           action="store_true",                                                        help="Use sum of backgrounds instead of data." )
argParser.add_argument( "--useTxt",             action="store_true",                                                        help="Use txt based cardFiles instead of root/shape based ones?" )
argParser.add_argument( "--skipFitDiagnostics", action="store_true",                                                        help="Don't do the fitDiagnostics (this is necessary for pre/postfit plots, but not 2D scans)?" )
argParser.add_argument( "--significanceScan",   action="store_true",                                                        help="Calculate significance instead?")
argParser.add_argument( "--year",               action="store",      default=2016,   type=int,                              help="Which year?" )
args=argParser.parse_args()

# Logging
import Analysis.Tools.logger as logger
logger = logger.get_logger(       args.logLevel, logFile = None )
import RootTools.core.logger as logger_rt
logger_rt = logger_rt.get_logger( args.logLevel, logFile = None )

useCache = True
if args.keepCard:
    args.overwrite = False

# Define estimators for CR
default_setup            = Setup( year=args.year )
estimators               = EstimatorList( default_setup )
regionNames              = []
default_setup.data       = default_setup.processes["Data"]
default_setup.processes  = estimators.constructProcessDict( processDict=default_processes )
default_setup.addon      = ""
default_setup.regions    = inclRegionsTTG if args.inclRegion else regionsTTG

setups = []
if "SR3" in args.useRegions:
    signalSetup3             = default_setup.sysClone( parameters=signalRegions["SR3"]["parameters"] )
    signalSetup3.channels    = signalRegions["SR3"]["channels"] #default_setup.channels
    signalSetup3.regions     = signalRegions["SR3"]["inclRegions" if args.inclRegion else "regions"]
    signalSetup3.data        = default_setup.data
    signalSetup3.processes   = estimators.constructProcessDict( processDict=signalRegions["SR3"]["processes"] ) if "processes" in signalRegions["SR3"] else default_setup.processes
    signalSetup3.addon       = "_signal3"
    regionNames             += ["SR3"]
    setups.append(signalSetup3)

if "SR4p" in args.useRegions:
    signalSetup4p            = default_setup.sysClone( parameters=signalRegions["SR4p"]["parameters"] )
    signalSetup4p.channels   = signalRegions["SR4p"]["channels"] #default_setup.channels
    signalSetup4p.regions    = signalRegions["SR4p"]["inclRegions" if args.inclRegion else "regions"]
    signalSetup4p.data       = default_setup.data
    signalSetup4p.processes  = estimators.constructProcessDict( processDict=signalRegions["SR4p"]["processes"] ) if "processes" in signalRegions["SR4p"] else default_setup.processes
    signalSetup4p.addon      = "_signal4p"
    regionNames             += ["SR4p"]
    setups.append(signalSetup4p)


# Define CR, channels and regions
for key, val in controlRegions.items():
    if not key in args.useRegions: continue
    regionNames                     += [key]
    locals()["setup"+key]            = default_setup.sysClone( parameters=val["parameters"] )
    locals()["setup"+key].channels   = val["channels"] #default_setup.channels
    locals()["setup"+key].regions    = val["inclRegions" if args.inclRegion else "regions"]
    locals()["setup"+key].data       = default_setup.data
    locals()["setup"+key].processes  = estimators.constructProcessDict( processDict=val["processes"] ) if "processes" in val else default_setup.processes
    locals()["setup"+key].addon      = "_control%s"%key
    setups.append(locals()["setup"+key])

# use the regions as key for caches
regionNames.sort()
if args.addDYSF:    regionNames.append("addDYSF")
if args.addMisIDSF: regionNames.append("addMisIDSF")
if args.inclRegion: regionNames.append("incl")

baseDir       = os.path.join( cache_dir, str(args.year), "limits" )
limitDir      = os.path.join( baseDir, "cardFiles", args.label, "expected" if args.expected else "observed" )
if not os.path.exists( limitDir ): os.makedirs( limitDir )

cacheFileName   = os.path.join( limitDir, "calculatedLimits" )
limitCache      = DirDB( cacheFileName )

cacheFileName   = os.path.join( limitDir, "calculatedSignifs" )
signifCache     = DirDB( cacheFileName )

cacheFileName   = os.path.join( limitDir, "systematics", "systematics" )
scaleUncCache   = DirDB( cacheFileName )

cacheFileName   = os.path.join( limitDir, "systematics", "isr" )
isrUncCache     = DirDB( cacheFileName )

cacheFileName   = os.path.join( limitDir, "systematics", "scale" )
scaleUncCache   = DirDB( cacheFileName )

cacheFileName   = os.path.join( limitDir, "systematics", "pdf" )
pdfUncCache     = DirDB( cacheFileName )

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
        counter=0
        c.reset()
        c.setPrecision(3)
        shapeString = "lnN" if args.useTxt else "shape"
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
        c.addUncertainty( "scale",      shapeString)
        c.addUncertainty( "PDF",        shapeString)
        c.addUncertainty( "ISR",        shapeString)
        # only in SRs
        # all regions, lnN
        c.addUncertainty( "QCD",        "lnN" )
        c.addUncertainty( "TT",         "lnN" )
        if not args.addDYSF:
            c.addUncertainty( "DY",         "lnN" )
        if not args.addMisIDSF:
            c.addUncertainty( "misID",      "lnN" )

        for setup in setups:
            observation = DataObservation( name="Data", process=setup.data, cacheDir=setup.defaultCacheDir() )
            for pList in setup.processes.values():
                for e in pList:
                    e.initCache( setup.defaultCacheDir() )

            for r in setup.regions:
                for channel in setup.channels:
                    niceName      = " ".join( [ channel, str(r), setup.addon[1:] ] )
                    binname       = "Bin%i"%counter
                    counter      += 1
                    total_exp_bkg = 0

                    c.addBin( binname, [ pName for pName in setup.processes.keys() if pName != "signal" ], niceName)
    
                    mute = False
                    for pName, pList in setup.processes.items():

                        signal   = pName=="signal"
                        expected = 0

                        for e in pList:
                            exp_yield = e.cachedEstimate( r, channel, setup )
                            if e.name.count( "DY" ) and args.addDYSF:
                                exp_yield *= default_DYSF
                                logger.info( "Scaling DY background %s by %f"%(e.name,default_DYSF) )
                            if e.name.count( "misID" ) and args.addMisIDSF:
                                exp_yield *= default_misIDSF
                                logger.info( "Scaling misID background %s by %f"%(e.name,default_misIDSF) )
                            e.expYield = exp_yield
                            expected  += exp_yield

                        logger.info( "Expectation for process %s: %s", pName, expected.val )

                        c.specifyExpectation( binname, pName, expected.val )
                        if not signal: total_exp_bkg += expected.val
                        if signal and expected.val <= 0.01: mute = True

                        default_DY_unc    = 5.0
                        default_TT_unc    = 0.1
                        default_QCD_unc   = 1.0 # 100%
                        default_misID_unc = 5.0

                        pu, jec, jer, sfb, sfl, trigger, lepSF, lepTrSF, phSF, eVetoSF, pfSF = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
#                        scale, pdf, isr = 0, 0, 0
                        dyUnc, ttUnc, qcdUnc, misIDUnc = 0, 0, 0, 0
                        if expected.val:
                            for e in pList:
                                y_scale   = e.expYield.val / expected.val
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
                                if e.name.count( "DY" ) and not args.addDYSF:
                                    dyUnc    += y_scale * default_DY_unc
                                if e.name.count( "QCD" ):
                                    qcdUnc   += y_scale * default_QCD_unc
                                if e.name.count( "TT_pow" ):
                                    ttUnc    += y_scale * default_TT_unc
                                if e.name.count( "misID" ) and not args.addMisIDSF:
                                    misIDUnc += y_scale * default_misID_unc


                        c.specifyUncertainty( "PU",            binname, pName, 1 + pu )
                        c.specifyUncertainty( "JEC",           binname, pName, 1 + jec )
                        c.specifyUncertainty( "JER",           binname, pName, 1 + jer )
                        c.specifyUncertainty( "SFb",           binname, pName, 1 + sfb )
                        c.specifyUncertainty( "SFl",           binname, pName, 1 + sfl )
#                        c.specifyUncertainty( "trigger",       binname, pName, 1 + trigger )
                        c.specifyUncertainty( "leptonSF",      binname, pName, 1 + lepSF )
                        c.specifyUncertainty( "leptonTrackSF", binname, pName, 1 + lepTrSF )
                        c.specifyUncertainty( "photonSF",      binname, pName, 1 + phSF )
                        c.specifyUncertainty( "eVetoSF",       binname, pName, 1 + eVetoSF )
                        c.specifyUncertainty( "prefireSF",     binname, pName, 1 + pfSF )
                        
#                        c.specifyUncertainty( "scale",   binname, pName, 1 + scale )
#                        c.specifyUncertainty( "PDF",     binname, pName, 1 + pdf )
#                        c.specifyUncertainty( "ISR",     binname, pName, 1 + isr )

                        if dyUnc:
                            c.specifyUncertainty( "DY",    binname, pName, 1 + dyUnc )
                        if qcdUnc:
                            c.specifyUncertainty( "QCD",   binname, pName, 1 + qcdUnc )
                        if ttUnc:
                            c.specifyUncertainty( "TT",    binname, pName, 1 + ttUnc )
                        if misIDUnc:
                            c.specifyUncertainty( "misID", binname, pName, 1 + misIDUnc )

                        # MC bkg stat (some condition to neglect the smaller ones?)
                        uname = "Stat_%s_%s"%(binname,pName)
                        c.addUncertainty( uname, "lnN" )
                        c.specifyUncertainty( uname, binname, pName, 1 + (expected.sigma/expected.val) if expected.val > 0 else 1 )

                    if args.expected:
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

    else:
        logger.info( "File %s found. Reusing."%cardFileName )
        cardFileNameShape = cardFileNameShape.replace('.root', 'Card.txt')
        cardFileName      = cardFileNameTxt if args.useTxt else cardFileNameShape
    
    sConfig = "_".join(regionNames)

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
            res = c.calcLimit( cardFileName )
            if not args.skipFitDiagnostics:
                c.calcNuisances( cardFileName )
            limitCache.add( sConfig, res, overwrite=True )

    ###################
    # extract the SFs #
    ###################
    if not args.useTxt and not args.skipFitDiagnostics:
        # Would be a bit more complicated with the classical txt files, so only automatically extract the SF when using shape based datacards
        
        combineWorkspace = cardFileNameShape.replace( "shapeCard.txt","shapeCard_FD.root" )
        logger.info( "Extracting fit results from %s"%combineWorkspace )
        
        postFitResults = getPrePostFitFromMLF( combineWorkspace )
        
        try:
            DY_prefit  = postFitResults["results"]["shapes_prefit"]["Bin0"]["DY"]
            DY_postfit = postFitResults["results"]["shapes_fit_b"]["Bin0"]["DY"]
        except:
            logger.info("DY SF not found!")
            DY_prefit  = u_float(1.,0.)
            DY_postfit = u_float(1.,0.)

        try:
            TT_prefit  = postFitResults["results"]["shapes_prefit"]["Bin0"]["TT"]
            TT_postfit = postFitResults["results"]["shapes_fit_b"]["Bin0"]["TT"]
        except:
            logger.info("TT SF not found!")
            TT_prefit  = u_float(1.,0.)
            TT_postfit = u_float(1.,0.)

        try:
            QCD_prefit  = postFitResults["results"]["shapes_prefit"]["Bin0"]["QCD"]
            QCD_postfit = postFitResults["results"]["shapes_fit_b"]["Bin0"]["QCD"]
        except:
            logger.info("QCD SF not found!")
            QCD_prefit  = u_float(1.,0.)
            QCD_postfit = u_float(1.,0.)

        try:
            misID_prefit  = postFitResults["results"]["shapes_prefit"]["Bin0"]["misID"]
            misID_postfit = postFitResults["results"]["shapes_fit_b"]["Bin0"]["misID"]
        except:
            logger.info("misID SF not found!")
            misID_prefit  = u_float(1.,0.)
            misID_postfit = u_float(1.,0.)


        if not os.path.isdir("logs"): os.mkdir("logs")
        write_time  = time.strftime("%Y %m %d %H:%M:%S", time.localtime())

        with open("logs/scaleFactors.dat", "a") as f:
            print
            print "## Scale Factors for backgrounds: ##"

            sf = "{:20}{:4.2f}{:3}{:4.2f}".format( "Drell-Yan:",    (DY_postfit/DY_prefit).val,   "+/-",  DY_postfit.sigma/DY_postfit.val)
            print sf
            f.write( write_time + ": " + "_".join( regionNames ) + ": " + sf + "\n" )

            sf = "{:20}{:4.2f}{:3}{:4.2f}".format( "TT:",           (TT_postfit/TT_prefit).val,   "+/-",  TT_postfit.sigma/TT_postfit.val)
            print sf
            f.write( write_time + ": " + "_".join( regionNames ) + ": " + sf + "\n" )

            sf = "{:20}{:4.2f}{:3}{:4.2f}".format( "misID:",        (misID_postfit/misID_prefit).val,   "+/-",  misID_postfit.sigma/misID_postfit.val)
            print sf
            f.write( write_time + ": " + "_".join( regionNames ) + ": " + sf + "\n" )

#            sf = "{:20}{:4.2f}{:3}{:4.2f}".format( "QCD:",          (QCD_postfit/QCD_prefit).val,   "+/-",  QCD_postfit.sigma/QCD_postfit.val)
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

