#!/usr/bin/env python
''' Analysis script for standard plots
'''

# Standard imports
import ROOT, os, imp, sys, copy
ROOT.gROOT.SetBatch(True)
import itertools
from math                             import isnan, ceil, pi

# RootTools
from RootTools.core.standard          import *

from TTGammaEFT.Tools.helpers         import getCollection

# Internal Imports
from TTGammaEFT.Tools.user            import plot_directory
from TTGammaEFT.Tools.cutInterpreter  import cutInterpreter
from TTGammaEFT.Tools.TriggerSelector import TriggerSelector

from Samples.Tools.metFilters         import getFilterCut

from TTGammaEFT.Tools.Variables       import NanoVariables
from TTGammaEFT.Tools.objectSelection import filterBJets

# Default Parameter
loggerChoices = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO', nargs='?', choices=loggerChoices,                  help="Log level for logging")
argParser.add_argument('--plot_directory',     action='store',      default='102X_TTG_ppv1_v1')
argParser.add_argument('--plotFile',           action='store',      default='all_noPhoton')
argParser.add_argument('--selection',          action='store',      default='dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40')
argParser.add_argument('--small',              action='store_true',                                                                    help='Run only on a small subset of the data?', )
argParser.add_argument('--noData',             action='store_true', default=False,                                                     help='also plot data?')
argParser.add_argument('--signal',             action='store',      default=None,   nargs='?', choices=[None],                         help="Add signal to plot")
argParser.add_argument('--year',               action='store',      default=None,   type=int,  choices=[2016,2017,2018],               help="Which year to plot?")
argParser.add_argument('--onlyTTG',            action='store_true', default=False,                                                     help="Plot only ttG")
argParser.add_argument('--normalize',          action='store_true', default=False,                                                     help="Normalize yields" )
args = argParser.parse_args()

# Logger
import TTGammaEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if args.small:           args.plot_directory += "_small"
if args.noData:          args.plot_directory += "_noData"
if args.signal:          args.plot_directory += "_signal_"+args.signal
if args.onlyTTG:         args.plot_directory += "_onlyTTG"
if args.normalize:       args.plot_directory += "_normalize"

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
        from TTGammaEFT.Samples.nanoTuples_Run2018_14Sep2018_semilep_postProcessed import *

# Text on the plots
def drawObjects( plotData, dataMCScale, lumi_scale ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS #bf{#it{Preliminary}}' if plotData else 'CMS #bf{#it{Simulation Preliminary}}'), 
      (0.45, 0.95, '%3.1f fb{}^{-1} (13 TeV) Scale %3.2f'% ( lumi_scale, dataMCScale ) ) if plotData else (0.65, 0.95, '%3.1f fb{}^{-1} (13 TeV)' % lumi_scale)
    ]
    return [tex.DrawLatex(*l) for l in lines] 

#scaling = { i+1:0 for i in range(len(signals)) }
scaling = { 1:0 }

# Plotting
def drawPlots( plots, mode, dataMCScale ):

    logger.info( "Plotting mode: %s"%mode )

    for log in [False, True]:
        plot_directory_ = os.path.join( plot_directory, 'analysisPlots', str(args.year), args.plot_directory, args.selection, mode, "log" if log else "lin" )

        for plot in plots:
            if not max(l[0].GetMaximum() for l in plot.histos):
                logger.info( "Empty plot!" )
                continue # Empty plot
            postFix = " (legacy)"
            if not args.noData: 
                plot.histos[1][0].style = styles.errorStyle( ROOT.kBlack )
                if mode == "all":
                    plot.histos[1][0].legendText = "data" + postFix
            extensions_ = ["pdf", "png", "root"]

            logger.info( "Plotting..." )

            plotting.draw( plot,
	                       plot_directory = plot_directory_,
                           extensions = extensions_,
	                       ratio = {'yRange':(0.1,1.9)} if not args.noData else None,
	                       logX = False, logY = log, sorting = True,
	                       yRange = (0.03, "auto") if log else (0.001, "auto"),
	                       scaling = scaling if args.normalize else {},
	                       legend = [ (0.15,0.9-0.03*sum(map(len, plot.histos)),0.9,0.9), 2],
	                       drawObjects = drawObjects( not args.noData, dataMCScale , lumi_scale ) if not args.normalize else drawObjects( not args.noData, 1.0 , lumi_scale ),
                           copyIndexPHP = True,
                         )

def getYieldPlot( index ):
    return Plot(
                name      = 'yield',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: 0.5 + index,
                binning   = [ 2, 0, 2 ],
                )

# get nano variable lists
NanoVars        = NanoVariables( args.year )

jetVarString     = NanoVars.getVariableString(   "Jet", postprocessed=True, data=(not args.noData), plot=True )
jetVariableNames = NanoVars.getVariableNameList( "Jet", postprocessed=True, data=(not args.noData), plot=True )
bJetVariables    = NanoVars.getVariables(        "BJet", postprocessed=True, data=(not args.noData), plot=True )
leptonVariables  = NanoVars.getVariables(        "Lepton", postprocessed=True, data=(not args.noData), plot=True )
photonVariables  = NanoVars.getVariables(        "Photon", postprocessed=True, data=(not args.noData), plot=True )

# Read variables and sequences
read_variables  = ["weight/F",
                   "PV_npvs/I", "PV_npvsGood/I",
                   "nJetGood/I", "nBTagGood/I",
                   "nJet/I", "nBTag/I",
                   "Jet[%s]" %jetVarString,
                   "JetGood[%s]" %jetVarString,
                   "nLepton/I", "nElectron/I", "nMuon/I",
                   "nLeptonGood/I", "nElectronGood/I", "nMuonGood/I",
                   "nLeptonTight/I", "nElectronTight/I", "nMuonTight/I",
                   "nLeptonVeto/I", "nElectronVeto/I", "nMuonVeto/I",
                   "nPhoton/I",
                   "nPhotonGood/I",
                   "MET_pt/F", "MET_phi/F", "METSig/F", "ht/F",
                   "mlltight/F", "mllgammatight/F",
                   "mLtight0Gamma/F",
                   "ltight0GammadR/F", "ltight0GammadPhi/F",
                   "m3/F", "m3wBJet/F",
                   "photonJetdR/F", "tightLeptonJetdR/F",
                  ]

read_variables += map( lambda var: "PhotonGood0_"             + var, photonVariables )
read_variables += map( lambda var: "PhotonNoChgIso0_"         + var, photonVariables )
read_variables += map( lambda var: "PhotonNoChgIsoNoSieie0_"  + var, photonVariables )
read_variables += map( lambda var: "LeptonGood0_"             + var, leptonVariables )
read_variables += map( lambda var: "LeptonGood1_"             + var, leptonVariables )
read_variables += map( lambda var: "LeptonTight0_"            + var, leptonVariables )
read_variables += map( lambda var: "LeptonTight1_"            + var, leptonVariables )
read_variables += map( lambda var: "Bj0_"                     + var, bJetVariables )
read_variables += map( lambda var: "Bj1_"                     + var, bJetVariables )

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

def clean_Jets( event, sample ):
    allJets    = getCollection( event, 'Jet', jetVariableNames, 'nJet' )
    allJets.sort( key = lambda j: -j['pt'] )
    allJets    = list( filter( lambda j: j['cleanmask'] and j['pt']>30, allJets ) )

    looseJets  = getCollection( event, 'JetGood', jetVariableNames, 'nJetGood' )
    looseJets.sort( key = lambda j: -j['pt'] )
    looseJets  = list( filter( lambda j: j['cleanmask'], looseJets ) )

    event.nJet      = len( allJets )
    event.nJetGood  = len( looseJets )
    event.nBTag     = len( filterBJets( allJets,   tagger="DeepCSV", year=args.year ) )
    event.nBTagGood = len( filterBJets( looseJets, tagger="DeepCSV", year=args.year ) )

    for var in jetVariableNames:
        for i, jet in enumerate( allJets[:2] ):
            getattr( event, "Jet_" + var )[i] = jet[var]
        for i, jet in enumerate ( looseJets[:2] ):
            getattr( event, "JetGood_" + var )[i] = jet[var]
# Sequence
sequence = [ clean_Jets ]

# Sample definition
if args.year == 2016:
    if args.onlyTTG: mc = [ TTGLep_16 ]
    else:            mc = [ TT_pow_16, TTG_16, DY_LO_16, singleTop_16, ZG_16, other_16 ]
elif args.year == 2017:
    if args.onlyTTG: mc = [ TTG_17 ]
    else:            mc = [ TTG_17, DY_LO_17, TG_17, WJets_17, WG_17, TT_pow_17, singleTop_17, other_17 ]
elif args.year == 2018:
    if args.onlyTTG: mc = [ TTG_18 ]
    else:            mc = [ TTG_18, TT_pow_18, singleTop_18]#, other_18 ]

if args.noData:
    if args.year == 2016:   lumi_scale = 35.92
    elif args.year == 2017: lumi_scale = 41.86
    elif args.year == 2018: lumi_scale = 58.83
    stack = Stack( mc )
else:
    if args.year == 2016:   data_sample = Run2016
    elif args.year == 2017: data_sample = Run2017
    elif args.year == 2018: data_sample = Run2018
    data_sample.texName        = "data (legacy)"
    data_sample.name           = "data"
    data_sample.read_variables = [ "event/I", "run/I" ]
    data_sample.scale          = 1
    lumi_scale                 = data_sample.lumi * 0.001
    stack                      = Stack( mc, data_sample )

stack.extend( [ [s] for s in signals ] )

for sample in mc + signals:
    sample.read_variables = read_variables_MC
    sample.scale          = lumi_scale
    sample.style          = styles.fillStyle( sample.color )
    sample.weight         = lambda event, sample: event.reweightPU*event.reweightLeptonSF*event.reweightLeptonTrackingSF*event.reweightPhotonSF*event.reweightPhotonElectronVetoSF*event.reweightBTag_SF
#event.reweightDilepTriggerBackup

if args.small:
    for sample in stack.samples:
        sample.normalization=1.
        sample.reduceFiles( factor=15 )
        sample.scale /= sample.normalization

weight_ = lambda event, sample: event.weight
tr = TriggerSelector( args.year, None, singleLepton=True )

# Use some defaults (set defaults before you create/import list of Plots!!)
Plot.setDefaults( stack=stack, weight=staticmethod( weight_ ), selectionString=cutInterpreter.cutString( args.selection ), addOverFlowBin='upper' )

# Import plots list (AFTER setDefaults!!)
plotListFile = os.path.join( os.path.dirname( os.path.realpath( __file__ ) ), 'plotLists', args.plotFile + '.py' )
if not os.path.isfile( plotListFile ):
    logger.info( "Plot file not found: %s", plotListFile )
    sys.exit(1)

plotModule = imp.load_source( "plotLists", os.path.expandvars( plotListFile ) )
if args.noData: from plotLists import plotListDataMC as plotList
else:           from plotLists import plotListData   as plotList

# Loop over channels
yields   = {}
allPlots = {}
allModes = [ 'mu', 'e' ]

for index, mode in enumerate( allModes ):
    logger.info( "Computing plots for mode %s", mode )

    yields[mode] = {}

    # always initialize with [], elso you get in trouble with pythons references!
    plots  = []
    plots += plotList
    if mode in [ "mu", "e" ]: plots += [ getYieldPlot( index ) ]

    # Define 2l selections
    leptonSelection = cutInterpreter.cutString( mode )

    if not args.noData:    data_sample.setSelectionString( [ getFilterCut( args.year, isData=True  ), leptonSelection ] )
    for sample in mc + signals: sample.setSelectionString( [ getFilterCut( args.year, isData=False ), leptonSelection, tr.getSelection( "MC" ) ] )
    
    # Overlap removal
    if any( x.name == "TTG" for x in mc ) and any( x.name == "TT_pow" for x in mc ):
        print "overlap removal TTgamma"
        eval('TTG_'    + str(args.year)[-2:]).addSelectionString( "isTTGamma==1" )
        eval('TT_pow_' + str(args.year)[-2:]).addSelectionString( "isTTGamma==0" )

    if any( x.name == "ZG" for x in mc ) and any( x.name == "DY_LO" for x in mc ):
        print "overlap removal Zgamma"
        eval('ZG_'    + str(args.year)[-2:]).addSelectionString( "isZWGamma==1" )
        eval('DY_LO_' + str(args.year)[-2:]).addSelectionString( "isZWGamma==0" )

    if any( x.name == "WG" for x in mc ) and any( x.name == "WJets" for x in mc ):
        print "overlap removal Wgamma"
        eval('WG_' + str(args.year)[-2:]).addSelectionString(    "isZWGamma==1" )
        eval('WJets_' + str(args.year)[-2:]).addSelectionString( "isZWGamma==0" )

    if any( x.name == "TG" for x in mc ) and any( x.name == "singleTop" for x in mc ):
        print "overlap removal singleTop"
        eval('TG_' + str(args.year)[-2:]).addSelectionString(        "isSingleTopTch==1" )
        eval('singleTop_' + str(args.year)[-2:]).addSelectionString( "isSingleTopTch==0" ) #ONLY IN THE T-channel!!!

    plotting.fill( plots, read_variables=read_variables, sequence=sequence )

    # Get normalization yields from yield histogram
    for plot in plots:
        if plot.name != "yield": continue
        for i, l in enumerate( plot.histos ):
            for j, h in enumerate( l ):
                yields[mode][plot.stack[i][j].name] = h.GetBinContent( h.FindBin( 0.5+index ) )
                h.GetXaxis().SetBinLabel( 1, "#mu" )
                h.GetXaxis().SetBinLabel( 2, "e" )

    if args.noData: yields[mode]["data"] = 0

    yields[mode]["MC"] = sum( yields[mode][s.name] for s in mc )
    dataMCScale        = yields[mode]["data"] / yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')

    logger.info( "Plotting mode %s", mode )
    allPlots[mode] = copy.deepcopy(plots) # deep copy for creating SF/all plots afterwards!
    drawPlots( allPlots[mode], mode, dataMCScale )


# Add the different channels into all
yields["all"] = {}

for y in yields["mu"]:
    try:    yields["all"][y] = sum( yields[c][y] for c in ['mu','e'] )
    except: yields["all"][y] = 0

dataMCScale = yields["all"]["data"] / yields["all"]["MC"] if yields["all"]["MC"] != 0 else float('nan')

for plot in allPlots['mu']:
    for pl in ( p for p in allPlots['e'] if p.name == plot.name ):  
        for i, j in enumerate( list( itertools.chain.from_iterable( plot.histos ) ) ):
            j.Add( list( itertools.chain.from_iterable( pl.histos ) )[i] )

drawPlots( allPlots['mu'], "all", dataMCScale )

