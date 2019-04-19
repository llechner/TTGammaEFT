''' Plot script pTG shape + WC
'''

# Standard imports 
import sys, os, pickle, copy, ROOT

# RootTools
from RootTools.core.standard   import *

# turn off graphics
ROOT.gROOT.SetBatch( True )

# TTGammaEFT
from TTGammaEFT.Tools.user              import plot_directory, cache_directory

from TTGammaEFT.Analysis.regions        import genTTGammaRegions  as genRegions
from TTGammaEFT.Analysis.regions        import recoTTGammaRegions as regions

from TTGammaEFT.Tools.TriggerSelector   import TriggerSelector
from TTGammaEFT.Tools.cutInterpreter    import cutInterpreter
from TTGammaEFT.Tools.genCutInterpreter import cutInterpreter as genCutInterpreter
from TTGammaEFT.Tools.Cache             import Cache

# get the reweighting function
from Analysis.Tools.WeightInfo          import WeightInfo
from Analysis.Tools.metFilters          import getFilterCut

# Default Parameter
loggerChoices = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO', nargs='?', choices=loggerChoices,                                help="Log level for logging")
argParser.add_argument('--genSelection',       action='store',      default='dilepOS-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p')
argParser.add_argument('--selection',          action='store',      default='nLepTight1-nLepVeto1-nJet4p-nBTag1p-pTG20-nPhoton1p')
argParser.add_argument('--small',              action='store_true',                                                                                  help='Run only on a small subset of the data?', )
argParser.add_argument('--normalize',          action='store_true', default=False,                                                                   help="Normalize yields" )
argParser.add_argument('--order',              action='store',      default=2,                                                                       help='Polynomial order of weight string (e.g. 2)')
argParser.add_argument('--parameters',         action='store',      default=['ctZI', '2', 'ctWI', '2', 'ctZ', '2', 'ctW', '2'], type=str, nargs='+', help = "argument parameters")
argParser.add_argument('--year',               action='store',      default=None,   type=int,  choices=[2016,2017,2018],                             help="Which year to plot?")
argParser.add_argument('--noData',             action='store_true', default=False,                                                                   help='also plot data?')
argParser.add_argument('--overwrite',          action='store_true',                                                                                  help='Overwrite Database entries?', )
args = argParser.parse_args()

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

# Gen Samples
from TTGammaEFT.Samples.genTuples_TTGamma_postProcessed                    import *

#signalSample = TTG_SingleLeptFromT_1L_test_EFT
signalSample = TTG_DiLept_1L_EFT #change that when available
subdir       = signalSample.name

# Logger
import Analysis.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if len(args.parameters) < 2: args.parameters = None

if args.small:     subdir += "_small"
if args.normalize: subdir += "_normalize"
if args.noData:    subdir += "_noData"

if args.parameters: wcString = "_".join(args.parameters).replace('.','p').replace('-','m')
else:               wcString = "SM"

# Text on the plots
colors = [ ROOT.kRed+1, ROOT.kGreen+2, ROOT.kOrange+1, ROOT.kViolet+9, ROOT.kSpring-7, ROOT.kRed+2 ]

params = []
if args.parameters:
    coeffs = args.parameters[::2]
    str_vals = args.parameters[1::2]
    vals = list( map( float, str_vals ) )
    for i_param, (coeff, val, str_val) in enumerate(zip(coeffs, vals, str_vals)):
        params.append( {
            'legendText': ' = '.join([coeff,str_val]).replace("c", "C_{").replace(" =", "} =").replace("I", "}^{[Im]"),
            'WC'        : { coeff:val },
            'color'     : colors[i_param],
            'name'      : coeff,
            })

params.append( {'legendText':'tt#gamma', 'WC':{}, 'color':ROOT.kBlack, 'name':'ttgamma'} )

def checkReferencePoint( sample ):
    ''' check if sample is simulated with a reference point
    '''
    return pickle.load(file(sample.reweight_pkl))['ref_point'] != {}

def drawObjects( lumi_scale ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS #bf{#it{Simulation Preliminary}}'), 
      (0.65, 0.95, '%3.1f fb{}^{-1} (13 TeV)' % lumi_scale)
    ]
    return [tex.DrawLatex(*l) for l in lines]

if args.normalize:
#    scaling = { i:len(params)-1 for i, _ in enumerate(params[:-1]) }
    scaling = { i:0 for i in range(1,len(params)) }

def legendmodification(l):
    l.SetTextSize(.035)

# Plotting
def drawPlots( plots ):
    extensions_ = ["pdf", "png", "root"]
    for log in [False, True]:
        plot_directory_ = os.path.join( plot_directory, 'regions', str(args.year), subdir, args.selection, wcString, "log" if log else "lin" )

        for plot in plots:
            if not max(l[0].GetMaximum() for l in plot.histos):
                continue # Empty plot

            plotting.draw( plot,
                           plot_directory = plot_directory_,
                           extensions = extensions_,
                           ratio = {'yRange':(0.1,1.9),'histos':[(len(params),0)]} if not args.noData else None,
                           logX = False, logY = log, sorting = True,
                           yRange = (0.03, "auto") if log else (0.001, "auto"),
                           scaling = scaling if args.normalize else {},
                           legend = [ (0.18,0.85-0.02*sum(map(len, plot.histos)),0.9,0.88), 2],
                           drawObjects = drawObjects( lumi_scale ),
#                           histModifications = [histmodification(logY)],
#                           ratioModifications = [ratiomodification],
#                           legendModifications = [legendmodification],
                           copyIndexPHP = True,
                         )

# Sample definition
if args.year == 2016:
    mc = [ TT_pow_16, DY_LO_16, singleTop_16, WJets_16, ZG_16, other_16 ]
    ttGammaSample = TTG_16

elif args.year == 2017:
    mc = [ DY_LO_17, TG_17, WJets_17, WG_17, TT_pow_17, singleTop_17, other_17 ]
    ttGammaSample = TTG_17

elif args.year == 2018:
    mc = [ TT_pow_18, DY_LO_18, singleTop_18, other_18 ]
    ttGammaSample = TTG_18

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
    data_sample.style          = styles.errorStyle( ROOT.kBlack )
    lumi_scale                 = data_sample.lumi * 0.001
    data_sample.setWeightString("weight")
    data_sample.setSelectionString( [ getFilterCut( args.year, isData=True ), cutInterpreter.cutString( args.selection ) ] )
    allSamples = [data_sample] + mc

w         = WeightInfo( signalSample.reweight_pkl )
w.set_order( int(args.order) )
variables = w.variables

tr = TriggerSelector( args.year, singleLepton=True )

signals = []
# Sample definition
for i, param in enumerate( params ):
    sample                = copy.deepcopy( signalSample )
    sample.params         = param
    if param["legendText"] == "tt#gamma":
        sample.style = styles.fillStyle( ttGammaSample.color )
    else:
        sample.style = styles.lineStyle( param["color"], width=2, dashed=True  )
    sample.texName        = param["legendText"]
    sample.name           = param["name"]
    sample.setWeightString("%f*ref_weight"%lumi_scale)
    sample.setSelectionString( genCutInterpreter.cutString( args.genSelection ) )
    signals.append( sample )

#stack.extend( [ [s] for s in signals ] )

for sample in [ttGammaSample] + mc:
    sample.style          = styles.fillStyle( sample.color )
    sample.setWeightString("weight*%f*reweightPU*reweightLeptonSF*reweightLeptonTrackingSF*reweightPhotonSF*reweightPhotonElectronVetoSF*reweightBTag_SF"%lumi_scale)
    sample.setSelectionString( [ getFilterCut( args.year, isData=False ), tr.getSelection( "MC" ), cutInterpreter.cutString( args.selection ) ] )
#reweightDilepTriggerBackup

if args.year == 2016:
    ttGammaSample.addSelectionString( "isTTGamma==1" )
    TT_pow_16.addSelectionString( "isTTGamma==0" )
    ZG_16.addSelectionString( "isZWGamma==1" )
    DY_LO_16.addSelectionString( "isZWGamma==0" )
if args.year == 2017:
    ttGammaSample.addSelectionString( "isTTGamma==1" )
    TT_pow_17.addSelectionString( "isTTGamma==0" )
#if args.year == 2018:
#    ttGammaSample.addSelectionString( "isTTGamma==1" )
#    TT_pow_18.addSelectionString( "isTTGamma==0" )

if args.small:

    for sample in [ttGammaSample] + allSamples + signals:
        sample.normalization=1.
        sample.reduceFiles( factor=50 )
        sample.addWeightString("%f"%(1./sample.normalization))

#    from TTGammaEFT.Analysis.regions import genTTGammaRegionsSmall  as genRegions
#    from TTGammaEFT.Analysis.regions import recoTTGammaRegionsSmall as regions



hists = {}
Nbins = len(regions)
minval = 20
maxval = 520
for sample in allSamples + signals:
    hists[sample.name] = ROOT.TH1F(sample.name,"", Nbins, minval, maxval)

rate = {}
for i_region, region in enumerate(regions):
    rate[region] = {}

cache_dir = os.path.join(cache_directory, "yields")
for i_sample, sample in enumerate( allSamples + [ttGammaSample]):

    logger.info( "Getting yield for sample %s", sample.name )

    dbFilename = "yields_%s.sql"%sample.name
    yieldDB = Cache( os.path.join( cache_dir, dbFilename ), "yields", [ "selection", "year", "small", "region", sample.name] )
    if not yieldDB: raise

    for i_region, region in enumerate(regions):

        logger.info( "At reco region %s", region )
        res = {"selection":args.selection, "year":args.year, "small":args.small, "region":str(region), sample.name:sample.name }

        if yieldDB.contains( res ):
            rate[region][sample.name] = float( yieldDB.getDicts( res )[0]["value"] )
            logger.info("Using yield for sample %s at region %s: %f"%(sample.name, region, rate[region][sample.name]))
        else:
            logger.info("Yield for sample %s at region %s not cached! Run caching script first"%(sample.name, region))
            sys.exit(1)

for i_region, region in enumerate(regions):

    genRegion = genRegions[i_region]
    logger.info( "At gen region %s", genRegion )

    coeffList   = w.getCoeffListFromDraw( signalSample, selectionString=genRegion.cutString() )
    genRateSM   = float( w.get_weight_yield( coeffList ) )

    for i_sample, sample in enumerate( signals ):
        genRateEFT = w.get_weight_yield( coeffList, **sample.params['WC'] )
        genKFactor = genRateEFT / genRateSM
        rate[region][sample.name] = rate[region][ttGammaSample.name] * genKFactor
        logger.info( "Calculated k-Factor for signal sample %s: %f! Signal yield: %s"%(sample.name, genKFactor, rate[region][sample.name]) )

    for i_sample, sample in enumerate( allSamples + signals ):
        hists[sample.name].SetBinContent(i_region+1, rate[region][sample.name])
#        hists[sample.name].SetBinError(i_region+1,0)
        hists[sample.name].legendText = sample.texName
        hists[sample.name].style      = sample.style



dataPlots = [ [ hists[data_sample.name] ] ] if not args.noData else []
plots     = [ [ hists[sample.name] ] for sample in signals[::-1] ] + dataPlots + [ [ hists[sample.name] for sample in mc ] ]
plot      = Plot.fromHisto( "regions", plots, texX="p_{T}(#gamma_{0}) (GeV)", texY="Number of Events / 100 GeV" )

for bgHisto in plot.histos[-1]:
    for signalHisto in plot.histos[:-1-int(not args.noData)]:
        signalHisto[-1].Add(bgHisto)

drawPlots( [plot] )
