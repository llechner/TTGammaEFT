''' Plot script pTG shape + WC
'''

# Standard imports 
import sys, os, pickle, copy

# RootTools
from RootTools.core.standard   import *

# TTGammaEFT
from TTGammaEFT.Tools.user              import plot_directory

from TTGammaEFT.Analysis.regions        import genTTGammaRegions  as genRegions
from TTGammaEFT.Analysis.regions        import recoTTGammaRegions as regions

from Samples.Tools.metFilters           import getFilterCut
from TTGammaEFT.Tools.TriggerSelector   import TriggerSelector

from TTGammaEFT.Tools.cutInterpreter    import cutInterpreter
from TTGammaEFT.Tools.genCutInterpreter import cutInterpreter as genCutInterpreter

# get the reweighting function
from TTGammaEFT.Tools.WeightInfo        import WeightInfo

# Default Parameter
loggerChoices = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO', nargs='?', choices=loggerChoices,                                help="Log level for logging")
argParser.add_argument('--genSelection',       action='store',      default='dilepOS-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40')
argParser.add_argument('--selection',          action='store',      default='dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40')
argParser.add_argument('--small',              action='store_true',                                                                                  help='Run only on a small subset of the data?', )
argParser.add_argument('--normalize',          action='store_true', default=False,                                                                   help="Normalize yields" )
argParser.add_argument('--order',              action='store',      default=2,                                                                       help='Polynomial order of weight string (e.g. 2)')
argParser.add_argument('--parameters',         action='store',      default=['ctZI', '4', 'ctWI', '4', 'ctZ', '4', 'ctW', '4'], type=str, nargs='+', help = "argument parameters")
argParser.add_argument('--year',               action='store',      default=None,   type=int,  choices=[2016,2017,2018],               help="Which year to plot?")
argParser.add_argument('--onlyTTG',            action='store_true', default=False,                                                     help="Plot only ttG")
argParser.add_argument('--noData',             action='store_true', default=False,                                                     help='also plot data?')
args = argParser.parse_args()

# Samples
if args.year == 2016:
    from TTGammaEFT.Samples.nanoTuples_Summer16_private_postProcessed      import *
    if not args.noData:
        from TTGammaEFT.Samples.nanoTuples_Run2016_14Dec2018_postProcessed import *

elif args.year == 2017:
    from TTGammaEFT.Samples.nanoTuples_Fall17_private_postProcessed        import *
    if not args.noData:
        from TTGammaEFT.Samples.nanoTuples_Run2017_14Dec2018_postProcessed import *

elif args.year == 2018:
    from TTGammaEFT.Samples.nanoTuples_Autumn18_private_postProcessed      import *
    if not args.noData:
        from TTGammaEFT.Samples.nanoTuples_Run2018_14Sep2018_postProcessed import *

# Gen Samples
from TTGammaEFT.Samples.genTuples_TTGamma_postProcessed                    import *

#signalSample = TTG_SingleLeptFromT_1L_test_EFT
signalSample = TTG_DiLept_1L_small_EFT
subdir       = signalSample.name

# Logger
import TTGammaEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if len(args.parameters) < 2: args.parameters = None

if args.small:     subdir += "_small"
if args.normalize: subdir += "_normalize"
if args.noData:    subdir += "_noData"
if args.onlyTTG:   subdir += "_onlyTTG"

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
    scaling = { i:len(params)-1 for i, _ in enumerate(params) }

def legendmodification(l):
    l.SetTextSize(.035)

# Plotting
def drawPlots( plots ):
    for log in [False, True]:
        plot_directory_ = os.path.join( plot_directory, 'EFTPlots%i'%args.year, subdir, args.selection, wcString, "log" if log else "lin" )

        for plot in plots:
            if not max(l[0].GetMaximum() for l in plot.histos):
                continue # Empty plot
            extensions_ = ["pdf", "png", "root"]

            plotting.draw( plot,
                           plot_directory = plot_directory_,
                           extensions = extensions_,
                           ratio = None,
                           logX = False, logY = log, sorting = True,
                           yRange = (0.03, "auto") if log else (0.001, "auto"),
                           scaling = scaling if args.normalize else {},
                           legend = [ (0.18,0.85-0.02*sum(map(len, plot.histos)),0.9,0.88), 2],
                           drawObjects = drawObjects( lumi_scale ) if not args.normalize else drawObjects( lumi_scale ),
#                           histModifications = [histmodification(logY)],
#                           ratioModifications = [ratiomodification],
                           legendModifications = [legendmodification],
                           copyIndexPHP = True,
                         )

def get_reweight( param , sample_ ):

    def reweightRef( event, sample ):
        return w.get_weight_func( **param['WC'] )( event, sample ) * event.ref_weight

    def reweightNoRef( event, sample ):
        return event.weight

    return reweightRef if checkReferencePoint( sample_ ) else reweightNoRef


# Read variables and sequences
read_variables_GEN  = ["weight/F",
                       "nGenBJet/I",
                       "nGenMuon/I",
                       "nGenElectron/I",
                       "nGenLepton/I",
                       "nGenPhoton/I",
                       "GenPhoton[pt/F]",
                       "nGenJet/I",
                       "mll/F", "mllgamma/F",
                      ]

read_variables_EFT = [
                      "ref_weight/F",
                      VectorTreeVariable.fromString('p[C/F]', nMax=100)
                     ]

# Read variables and sequences
read_variables  = ["weight/F", 
                   "nJetGood/I", "nBTagGood/I",
                   "nLeptonGood/I","nElectronGood/I", "nMuonGood/I",
                   "nLeptonGoodLead/I","nElectronGoodLead/I", "nMuonGoodLead/I",
                   "nLeptonTight/I", "nElectronTight/I", "nMuonTight/I",
                   "nLeptonVeto/I", "nElectronVeto/I", "nMuonVeto/I",
                   "nPhotonGood/I",
                   "mll/F", "mllgamma/F",
                  ]

read_variables_MC = ["isTTGamma/I", "isZWGamma/I", "isSingleTopTch/I",
                     "reweightPU/F", "reweightPUDown/F", "reweightPUUp/F", "reweightPUVDown/F", "reweightPUVUp/F",
                     "reweightLeptonSF/F", "reweightLeptonSFUp/F", "reweightLeptonSFDown/F",
                     "reweightLeptonTrackingSF/F",
                     "reweightDilepTrigger/F", "reweightDilepTriggerUp/F", "reweightDilepTriggerDown/F",
                     "reweightDilepTriggerBackup/F", "reweightDilepTriggerBackupUp/F", "reweightDilepTriggerBackupDown/F",
                     "reweightPhotonSF/F", "reweightPhotonSFUp/F", "reweightPhotonSFDown/F",
                     "reweightPhotonElectronVetoSF/F",
                     "reweightBTag_SF/F", "reweightBTag_SF_b_Down/F", "reweightBTag_SF_b_Up/F", "reweightBTag_SF_l_Down/F", "reweightBTag_SF_l_Up/F",
                    ]

# Sequence
sequence = []

# Sample definition
if args.year == 2016:
    if args.onlyTTG: mc = []
    else:            mc = [ DY_LO_16, TT_pow_16, singleTop_16, ZG_16, other_16 ]
    ttGammaSample       = TTG_16

elif args.year == 2017:
    if args.onlyTTG: mc = []
    else:            mc = [ DY_LO_17, TT_pow_17, singleTop_17, other_17 ]
    ttGammaSample       = TTG_17

elif args.year == 2018:
    if args.onlyTTG: mc = []
    else:            mc = [ DY_LO_18, TT_pow_18, singleTop_18, other_18 ]
    ttGammaSample       = None

if args.noData:
    if args.year == 2016:   lumi_scale = 35.92
    elif args.year == 2017: lumi_scale = 41.86
    elif args.year == 2018: lumi_scale = 58.83
    allSamples = mc
#    stack = Stack( mc )
else:
    if args.year == 2016:   data_sample = Run2016
    elif args.year == 2017: data_sample = Run2017
    elif args.year == 2018: data_sample = Run2018
    data_sample.texName        = "data (legacy)"
    data_sample.name           = "data"
    data_sample.read_variables = read_variables + [ "event/I", "run/I" ]
    data_sample.scale          = 1
    data_sample.weight         = lambda event, sample: event.weight
    data_sample.style          = styles.errorStyle( ROOT.kBlack )
    lumi_scale                 = data_sample.lumi * 0.001
    data_sample.setSelectionString( [ getFilterCut( args.year, isData=True ), cutInterpreter.cutString( args.selection ) ] )
    allSamples = [data_sample] + mc
#    stack                      = Stack( mc, data_sample )

w         = WeightInfo( signalSample.reweight_pkl )
w.set_order( int(args.order) )
variables = w.variables

tr = TriggerSelector( args.year, None )

signals = []
# Sample definition
for i, param in enumerate( params ):
    sample                = copy.deepcopy( signalSample )
    sample.params         = param
    if param["legendText"] == "tt#gamma":
        sample.style = styles.fillStyle( ttGammaSample.color, lineWidth=3 )
#        sample.style = styles.lineStyle( param["color"], width=3  )
    else:
        sample.style = styles.lineStyle( param["color"], width=2, dashed=True  )
    sample.texName        = param["legendText"]
    sample.weight         = get_reweight( param, sample )
    sample.read_variables = read_variables_EFT + read_variables_GEN
    sample.scale          = lumi_scale
    sample.setSelectionString( genCutInterpreter.cutString( args.genSelection ) )
    sample.name           = param["name"]
    signals.append( sample )

#stack.extend( [ [s] for s in signals ] )

for sample in [ttGammaSample] + mc:
    sample.read_variables = read_variables + read_variables_MC
    sample.scale          = lumi_scale
    sample.style          = styles.fillStyle( sample.color )
    sample.weight         = lambda event, sample: event.weight*event.reweightDilepTriggerBackup*event.reweightPU*event.reweightLeptonSF*event.reweightLeptonTrackingSF*event.reweightPhotonSF*event.reweightPhotonElectronVetoSF*event.reweightBTag_SF
    sample.setSelectionString( [ getFilterCut( args.year, isData=False ), tr.getSelection( "MC" ), cutInterpreter.cutString( args.selection ) ] )

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

    from TTGammaEFT.Analysis.regions import genTTGammaRegionsSmall  as genRegions
    from TTGammaEFT.Analysis.regions import recoTTGammaRegionsSmall as regions

    for sample in [ttGammaSample] + allSamples + signals: #stack.samples:
        sample.normalization=1.
        sample.reduceFiles( factor=20 )
        sample.scale /= sample.normalization


hists = {}
Nbins = len(regions)
minval = 20
maxval = 620
for sample in allSamples + signals:
    hists[sample.name] = ROOT.TH1F(sample.name,"", Nbins, minval, maxval)

rate = {}

for i_region, region in enumerate(regions):
    # compute signal yield for this region (this is the final code)

    genRegion = genRegions[i_region]

    logger.info( "At reco region %s", region )
    logger.info( "At gen region %s", genRegion )

    rate[region] = {}

    for i_sample, sample in enumerate( allSamples ):
        rate[region][sample.name] = sample.getYieldFromDraw( selectionString=region.cutString() )['val']

        hists[sample.name].SetBinContent(i_region+1, rate[region][sample.name])
        hists[sample.name].SetBinError(i_region+1,0)
        hists[sample.name].legendText = sample.texName
        hists[sample.name].style      = sample.style

    ttgammaRate = ttGammaSample.getYieldFromDraw( selectionString=region.cutString() )['val']
    coeffList   = w.getCoeffListFromDraw( signalSample, selectionString=genRegion.cutString() )
    genRateSM   = float( w.get_weight_yield( coeffList ) )

    for i_sample, sample in enumerate( signals ):
        genRateEFT = w.get_weight_yield( coeffList, **sample.params['WC'] )
        genKFactor = genRateEFT / genRateSM

        print sample.name, genKFactor, ttgammaRate * genKFactor

        rate[region][sample.name] = ttgammaRate * genKFactor

        hists[sample.name].SetBinContent(i_region+1, rate[region][sample.name])
        hists[sample.name].SetBinError(i_region+1,0)
        hists[sample.name].legendText = sample.texName
        hists[sample.name].style      = sample.style

plots = [ [hists[sample.name]] for sample in signals ] +  [ [ hists[sample.name] for sample in allSamples ] ] 
plot  = Plot.fromHisto("photonGood0_pt_EFT100_wide", plots, texX="p_{T}(#gamma) (GeV)", texY="Number of Events / 100 GeV" )

for bgHisto in plot.histos[-1]:
    for signalHisto in plot.histos[:-1]:
        signalHisto[-1].Add(bgHisto)

drawPlots( [plot] )

