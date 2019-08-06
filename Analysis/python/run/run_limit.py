#!/usr/bin/env python

import os, copy
import ROOT

from math                                import sqrt

from TTGammaEFT.Analysis.EstimatorList   import EstimatorList
from TTGammaEFT.Analysis.Setup           import Setup
from TTGammaEFT.Analysis.DataObservation import DataObservation
from TTGammaEFT.Analysis.MCBasedEstimate import MCBasedEstimate
from TTGammaEFT.Analysis.regions         import regionsTTG, noPhotonRegionTTG, inclRegionsTTG
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
argParser.add_argument( "--logLevel",           action="store",      default="INFO",            choices=loggerChoices,  help="Log level for logging" )
argParser.add_argument( "--label",              action="store",      default="defaultSetup",    type=str,               help="Label of results directory" )
argParser.add_argument( "--inclRegion",         action="store_true",                                                    help="use inclusive photon pt region" )
argParser.add_argument( "--overwrite",          action="store_true",                                                    help="Overwrite existing output files" )
argParser.add_argument( "--addDYSF",            action="store_true",                                                    help="add default DY scale factor" )
argParser.add_argument( "--keepCard",           action="store_true",                                                    help="Overwrite existing output files" )
argParser.add_argument( "--expected",           action="store_true",                                                    help="Use sum of backgrounds instead of data." )
argParser.add_argument( "--useTxt",             action="store_true",                                                    help="Use txt based cardFiles instead of root/shape based ones?" )
argParser.add_argument( "--skipFitDiagnostics", action="store_true",                                                    help="Don't do the fitDiagnostics (this is necessary for pre/postfit plots, but not 2D scans)?" )
argParser.add_argument( "--significanceScan",   action="store_true",                                                    help="Calculate significance instead?")
argParser.add_argument( "--year",               action="store",      default=2016,   type=int,                          help="Which year?" )
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

default_setup.channels   = lepChannels
#default_setup.estimators = estimators.constructEstimatorList( samples=["TTG", "WG"] )
default_setup.estimators = estimators.constructEstimatorList( samples=default_sampleList )
default_setup.addon      = ""
default_setup.regions    = inclRegionsTTG if args.inclRegion else regionsTTG

signalSetup3             = default_setup.sysClone( parameters=signalRegions["SR3"]["parameters"] )
signalSetup3.channels    = default_setup.channels
signalSetup3.estimators  = default_setup.estimators
signalSetup3.addon       = "_signal3"
signalSetup3.regions     = default_setup.regions
regionNames             += ["SR3"]

signalSetup4p            = default_setup.sysClone( parameters=signalRegions["SR4p"]["parameters"] )
signalSetup4p.channels   = default_setup.channels
signalSetup4p.estimators = default_setup.estimators
signalSetup4p.addon      = "_signal4p"
signalSetup4p.regions    = default_setup.regions
regionNames             += ["SR4p"]


# Define CR, channels and regions
for key, val in controlRegions.items():
    regionNames                     += [key]
    noPhotonCR                       = "nPhoton" in val["parameters"] and val["parameters"]["nPhoton"][1] == 0
    locals()["setup"+key]            = default_setup.sysClone( parameters=val["parameters"] )
    locals()["setup"+key].channels   = dilepChannels if key.startswith( "DY" ) else default_setup.channels
    locals()["setup"+key].estimators = default_setup.estimators
    locals()["setup"+key].addon      = "_control%s"%key
    locals()["setup"+key].regions    = noPhotonRegionTTG if noPhotonCR else default_setup.regions

# use the regions as key for caches
regionNames.sort()

# Define the regions that should be used
setups = [ locals()["setup"+key] for key in controlRegions.keys() ] + [ signalSetup3, signalSetup4p ]
#setups = [ setupVG3 ]


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
    c.releaseLocation = combineReleaseLocation #os.path.abspath( "/tmp/llechner/limits/" ) 

    cardFileName = os.path.join(limitDir, "_".join(regionNames)+".txt" )
    if not os.path.exists(cardFileName) or args.overwrite:
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
        c.addUncertainty( "DY",         "lnN" )
#        c.addUncertainty( "misID",      "lnN" )

        for setup in setups:
            observation = DataObservation( name="Data", sample=setup.samples["Data"], cacheDir=setup.defaultCacheDir() )
            for e in setup.estimators: e.initCache( setup.defaultCacheDir() )

            for r in setup.regions:
              for channel in setup.channels:
                  niceName      = " ".join( [ channel, str(r), setup.addon ] )
                  binname       = "Bin%i"%counter
                  counter      += 1
                  total_exp_bkg = 0

                  c.addBin( binname, [ e.name.split("-")[0] for e in setup.estimators if e.name != "TTG" ], niceName)
    
                  mute = False
                  for e in setup.estimators:

                      signal = False
                      if e.name == "TTG": signal = True

                      name           = e.name.split( "-" )[0] if not signal else "signal"
                      print e.name
                      print r, channel, setup
                      expected       = e.cachedEstimate( r, channel, setup, save=True ) 

                      logger.info( "Expectation for process %s: %s", e.name, expected.val )

                      y = expected.val
                      if e.name.count( "DY" ) and args.addDYSF:
                          y *= default_DYSF
                          logger.info( "Scaling DY background by %f", default_DYSF )

                      c.specifyExpectation( binname, name, y )
                      if not signal: total_exp_bkg += y
                      if signal and y <= 0.01: mute = True

                      c.specifyUncertainty( "PU",            binname, name, 1 + e.PUSystematic(                   r, channel, setup).val )
                      c.specifyUncertainty( "JEC",           binname, name, 1 + e.JECSystematic(                  r, channel, setup).val )
                      c.specifyUncertainty( "JER",           binname, name, 1 + 0.03 )#e.JERSystematic(                   r, channel, setup).val )
                      c.specifyUncertainty( "SFb",           binname, name, 1 + e.btaggingSFbSystematic(          r, channel, setup).val )
                      c.specifyUncertainty( "SFl",           binname, name, 1 + e.btaggingSFlSystematic(          r, channel, setup).val )
#                      c.specifyUncertainty( "trigger",       binname, name, 1 + e.triggerSystematic(              r, channel, setup).val )
                      c.specifyUncertainty( "leptonSF",      binname, name, 1 + e.leptonSFSystematic(             r, channel, setup).val )
                      c.specifyUncertainty( "leptonTrackSF", binname, name, 1 + e.leptonTrackingSFSystematic(     r, channel, setup).val )
                      c.specifyUncertainty( "photonSF",      binname, name, 1 + e.photonSFSystematic(             r, channel, setup).val )
                      c.specifyUncertainty( "eVetoSF",       binname, name, 1 + e.photonElectronVetoSFSystematic( r, channel, setup).val )
                      c.specifyUncertainty( "prefireSF",     binname, name, 1 + e.L1PrefireSystematic(            r, channel, setup).val )
                        
#                      c.specifyUncertainty( "scale",   binname, name, 1 + getScaleUncBkg( e.name, r, channel ) )
#                      c.specifyUncertainty( "PDF",     binname, name, 1 + getPDFUnc(      e.name, r, channel ) )
#                      c.specifyUncertainty( "ISR",     binname, name, 1 + getISRUnc(      e.name, r, channel ) )

                      if e.name.count( "DY" ):
                          c.specifyUncertainty( "DY",         binname, name, 1.5 )

                      # MC bkg stat (some condition to neglect the smaller ones?)
                      uname = "Stat_%s_%s"%(binname,name)
                      c.addUncertainty( uname, "lnN" )
                      c.specifyUncertainty( uname, binname, name, 1 + (expected.sigma/expected.val) if expected.val > 0 else 1 )

                  if args.expected:
                      c.specifyObservation( binname, int( round( total_exp_bkg, 0 ) ) )
                      logger.info( "Expected observation: %s", int( round( total_exp_bkg, 0 ) ) )
                  else:
                      c.specifyObservation( binname,  int( observation.cachedObservation(r, channel, setup).val ) )
                      logger.info( "Observation: %s", int( observation.cachedObservation(r, channel, setup).val ) )

                  if mute and total_exp_bkg <= 0.01:
                      c.muted[binname] = True

        c.addUncertainty( "Lumi", "lnN" )
        c.specifyFlatUncertainty( "Lumi", 1.026 )
        cardFileNameTxt     = c.writeToFile( cardFileName )
        cardFileNameShape   = c.writeToShapeFile( cardFileName.replace( ".txt", "_shape.root" ) )
        cardFileName        = cardFileNameTxt if args.useTxt else cardFileNameShape

    else:
        print "File %s found. Reusing."%cardFileName
    
    sConfig = "_".join(regionNames)

    if args.significanceScan:
        if useCache and not args.overwrite and signifCache.contains( sConfig ):
            res = signifCache.get( sConfig )
        else:
            res = c.calcSignif( cardFileName )
            signifCache.add( sConfig, res )
    
    else:
        if useCache and not args.overwrite and limitCache.contains( sConfig ):
            res = limitCache.get( sConfig )
        else:
            res = c.calcLimit( cardFileName )
            if not args.skipFitDiagnostics:
                c.calcNuisances( cardFileName )
            limitCache.add( sConfig, res )

    ###################
    # extract the SFs #
    ###################
    if not args.useTxt and not args.skipFitDiagnostics:
        # Would be a bit more complicated with the classical txt files, so only automatically extract the SF when using shape based datacards
        
        print cardFileName
        combineWorkspace = cardFileName.replace( "shapeCard.txt","shapeCard_FD.root" )
        print "Extracting fit results from %s"%combineWorkspace
        
        postFitResults = getPrePostFitFromMLF( combineWorkspace )
        
        DY_prefit  = postFitResults["results"]["shapes_prefit"]["Bin0"]["DY"]
        DY_postfit = postFitResults["results"]["shapes_fit_b"]["Bin0"]["DY"]

        print
        print "## Scale Factors for backgrounds: ##"
        print "{:20}{:4.2f}{:3}{:4.2f}".format( "Drell-Yan:",    (DY_postfit/DY_prefit).val,   "+/-",  DY_postfit.sigma/DY_postfit.val)

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

