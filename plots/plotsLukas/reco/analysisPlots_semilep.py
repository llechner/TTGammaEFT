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

# Internal Imports
from TTGammaEFT.Tools.user            import plot_directory
from TTGammaEFT.Tools.cutInterpreter  import cutInterpreter
from TTGammaEFT.Tools.TriggerSelector import TriggerSelector

from Samples.Tools.metFilters         import getFilterCut
from TTGammaEFT.Tools.objectSelection import nanoPlotElectronVars, nanoPlotMuonVars, nanoPlotLeptonVars, nanoPlotTauVars, nanoPlotPhotonVars, nanoPlotJetVars, nanoPlotBJetVars
from TTGammaEFT.Tools.objectSelection import nanoPlotElectronVarString, nanoPlotMuonVarString, nanoPlotLeptonVarString, nanoPlotTauVarString, nanoPlotPhotonVarString, nanoPlotJetVarString, nanoPlotBJetVarString

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
    for log in [False, True]:
        plot_directory_ = os.path.join( plot_directory, 'analysisPlots%i'%args.year, args.plot_directory, args.selection, mode, "log" if log else "lin" )

        for plot in plots:
            if not max(l[0].GetMaximum() for l in plot.histos): 
                continue # Empty plot
            postFix = " (legacy)"
            if not args.noData: 
                plot.histos[1][0].style          = styles.errorStyle( ROOT.kBlack )
                if mode == "all":
                    plot.histos[1][0].legendText = "data" + postFix
                if mode == "SF":
                    plot.histos[1][0].legendText = "data (SF)" + postFix
            extensions_ = ["pdf", "png", "root"] if mode in ['all', 'SF', 'mue'] else ['png']

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

# Read variables and sequences
read_variables  = ["weight/F", "ref_weight/F",
                   "PV_npvs/I", "PV_npvsGood/I",
                   "nJetGood/I", "nBTagGood/I",
                   "JetGood[%s]" %nanoPlotJetVarString,
                   "nLeptonTight/I", "nElectronTight/I", "nMuonTight/I",
                   "nLeptonVeto/I", "nElectronVeto/I", "nMuonVeto/I",
                   "nPhotonGood/I",
                   "MET_pt/F", "MET_phi/F", "METSig/F", "ht/F",
                   "mlltight/F", "mllgammatight/F",
                   "mLtight0Gamma/F",
                   "ltight0GammadR/F", "ltight0GammadPhi/F",
                   "m3/F", "m3wBJet/F",
                   "photonJetdR/F", "tightLeptonJetdR/F",
                  ]

read_variables += [ "PhotonGood0_"              + var for var in nanoPlotPhotonVarString.split(",") ]
read_variables += [ "PhotonNoChgIso0_"         + var for var in nanoPlotPhotonVarString.split(",") ]
read_variables += [ "PhotonNoChgIsoNoSieie0_"  + var for var in nanoPlotPhotonVarString.split(",") ]
read_variables += [ "LeptonTight0_" + var for var in nanoPlotLeptonVarString.split(",") ]
read_variables += [ "LeptonTight1_" + var for var in nanoPlotLeptonVarString.split(",") ]
read_variables += [ "Bj0_" + var for var in nanoPlotBJetVarString.split(",") ]
read_variables += [ "Bj1_" + var for var in nanoPlotBJetVarString.split(",") ]

read_variables_MC = ["isTTGamma/I", "isZWGamma/I", "isSingleTopTch/I",
                     "PhotonGood0_photonCat/I",
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
    if args.onlyTTG: mc = [ TTGLep_16 ]
    else:            mc = [ TT_pow_16, TTGLep_16, DY_LO_16, singleTop_16, ZGTo2LG_16, other_16 ]
elif args.year == 2017:
    if args.onlyTTG: mc = [ TTG_17 ]
    else:            mc = [ TTG_17, DY_LO_17, TT_pow_17, singleTop_17, other_17 ]
elif args.year == 2018:
    if args.onlyTTG: mc = [ ]
    else:            mc = [ DY_LO_18, TT_pow_18, other_18 ]

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
    sample.weight         = lambda event, sample: event.reweightDilepTriggerBackup*event.reweightPU*event.reweightLeptonSF*event.reweightLeptonTrackingSF*event.reweightPhotonSF*event.reweightPhotonElectronVetoSF*event.reweightBTag_SF

if args.small:
    for sample in stack.samples:
        sample.normalization=1.
        sample.reduceFiles( factor=15 )
        sample.scale /= sample.normalization

weight_ = lambda event, sample: event.weight
tr = TriggerSelector( args.year, None )

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
    plots += [ getYieldPlot( index ) ]

    # Define 2l selections
    leptonSelection = cutInterpreter.cutString( mode )

    if not args.noData:    data_sample.setSelectionString( [ getFilterCut( 2016, isData=True  ), leptonSelection ] )
    for sample in mc + signals: sample.setSelectionString( [ getFilterCut( 2016, isData=False ), leptonSelection, tr.getSelection( "MC" ) ] )

    # Overlap removal
    if any( x.name == "TTbar" or x.name == "TTLep_pow" for x in mc ) and any( x.name == "TTGLep" for x in mc ):
        if any( x.name == "TTbar" for x in mc ):     eval('TTbar_' + str(args.year)[-2:]).addSelectionString(  "isTTGamma==0" )
        if any( x.name == "TTLep_pow" for x in mc ): eval('TT_pow_' + str(args.year)[-2:]).addSelectionString( "isTTGamma==0" )
        eval('TTGLep_' + str(args.year)[-2:]).addSelectionString( "isTTGamma==1" )

    if any( x.name == "ZGTo2LG" or x.name == "ZGToLLG" for x in mc ) and any( x.name == "DY_LO" for x in mc ):
        if any( x.name == "ZGTo2LG" for x in mc ):   eval('ZGTo2LG_' + str(args.year)[-2:]).addSelectionString(   "isZWGamma==1" )
        if any( x.name == "ZGToLLG" for x in mc ):   eval('ZGToLLG_' + str(args.year)[-2:]).addSelectionString(   "isZWGamma==1" )
        eval('DY_LO_' + str(args.year)[-2:]).addSelectionString( "isZWGamma==0" )

    if any( x.name == "singleTop" for x in mc ) and any( x.name == "TGJets" for x in mc ):
        eval('singleTop_' + str(args.year)[-2:]).addSelectionString( "isSingleTopTch==1" )
        eval('TGJets_' + str(args.year)[-2:]).addSelectionString(    "isSingleTopTch==0" )

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

