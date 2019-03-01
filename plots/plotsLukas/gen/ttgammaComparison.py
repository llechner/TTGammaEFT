#!/usr/bin/env python
''' Analysis script for standard plots
'''

# Standard imports
import ROOT, os, imp, sys, copy
ROOT.gROOT.SetBatch(True)
import itertools
import pickle
from math                                import isnan, ceil, pi

# RootTools
from RootTools.core.standard             import *

# Internal Imports
from TTGammaEFT.Tools.user               import plot_directory
from TTGammaEFT.Tools.genCutInterpreter  import cutInterpreter

from Analysis.Tools.WeightInfo           import WeightInfo

# Default Parameter
loggerChoices = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO', nargs='?', choices=loggerChoices,                                help="Log level for logging")
argParser.add_argument('--plot_directory',     action='store',      default='gen')
argParser.add_argument('--plotFile',           action='store',      default='all')
argParser.add_argument('--selection',          action='store',      default='dilepOS-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40')
argParser.add_argument('--small',              action='store_true',                                                                                  help='Run only on a small subset of the data?', )
argParser.add_argument('--normalize',          action='store_true', default=False,                                                                   help="Normalize yields" )
args = argParser.parse_args()

# Logger
import Analysis.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if args.small:     args.plot_directory += "_small"
if args.normalize: args.plot_directory += "_normalize"

# Samples
from TTGammaEFT.Samples.genTuples_TTGamma_postProcessed      import *

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
    scaling = { 0:i for i, _ in enumerate(comparisonSamples) }

# Plotting
def drawPlots( plots, mode ):
    for log in [False, True]:
        plot_directory_ = os.path.join( plot_directory, 'comparisonPlots', args.plot_directory, args.selection, mode, "log" if log else "lin" )

        for plot in plots:
            if not max(l[0].GetMaximum() for l in plot.histos): 
                continue # Empty plot
            postFix = " (legacy)"
            extensions_ = ["pdf", "png", "root"] if mode in ['all', 'SF', 'mue'] else ['png']

            plotting.draw( plot,
	                       plot_directory = plot_directory_,
                           extensions = extensions_,
                           ratio = {'yRange': (0.7, 1.3), 'histos':[(1,0)], 'texY':'Ratio'},
#	                       ratio = None,
	                       logX = False, logY = log, sorting = True,
	                       yRange = (0.03, "auto") if log else (0.001, "auto"),
	                       scaling = scaling if args.normalize else {},
	                       legend = [ (0.18,0.85-0.03*sum(map(len, plot.histos)),0.9,0.88), 2],
	                       drawObjects = drawObjects( lumi_scale ) if not args.normalize else drawObjects( lumi_scale ),
                           copyIndexPHP = True,
                         )

def getYieldPlot( index ):
    return Plot(
                name      = 'yield',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: 0.5 + index,
                binning   = [ 3, 0, 3 ],
                )

genJetVarString      = "pt/F,eta/F,phi/F,isMuon/I,isElectron/I,isPhoton/I,matchBParton/I"
genJetVars           = [ item.split("/")[0] for item in genJetVarString.split(",") ]

genTopVarString      = "pt/F,eta/F,phi/F,mass/F"
genTopVars           = [ item.split("/")[0] for item in genTopVarString.split(",") ]

genLeptonVarString   = "pt/F,eta/F,phi/F,pdgId/I,motherPdgId/I,grandmotherPdgId/I"
genLeptonVars        = [ item.split("/")[0] for item in genLeptonVarString.split(",") ]

genPhotonVarString   = "pt/F,phi/F,eta/F,mass/F,motherPdgId/I,relIso04_all/F,photonLepdR/F,photonJetdR/F"
genPhotonVars        = [ item.split("/")[0] for item in genPhotonVarString.split(",") ]

# Read variables and sequences
read_variables  = ["weight/F",
                   "nGenBJet/I",
                   "nGenMuon/I",
                   "nGenElectron/I",
                   "GenMET_pt/F", "GenMET_phi/F",
                   "nGenLepton/I",
                   "GenLepton[%s]"   %genLeptonVarString,
                   "nGenPhoton/I",
                   "GenPhoton[%s]"   %genPhotonVarString,
                   "nGenJet/I",
                   "GenJet[%s]"      %genJetVarString,
                   "nGenTop/I",
                   "GenTop[%s]"      %genTopVarString,
                   "mll/F", "mllgamma/F",
                   "minDRjj/F",
                   "minDRbb/F",
                   "minDRll/F",
                   "minDRaa/F",
                   "minDRbj/F",
                   "minDRaj/F",
                   "minDRjl/F",
                   "minDRab/F",
                   "minDRbl/F",
                   "minDRal/F",
                  ]

read_variables += [ "GenBj0_" + var for var in genJetVarString.split(",") ]
read_variables += [ "GenBj1_" + var for var in genJetVarString.split(",") ]

read_variables_EFT = [
                      "ref_weight/F",
                      VectorTreeVariable.fromString('p[C/F]', nMax=100)
                     ]

# Sequence
sequence = []

lumi_scale = 136.6

comparisonSamples = [ [TTG_SingleLeptFromT_3LPatched_SM], [TTG_SingleLeptFromT_1L_SM] ]
#comparisonSamples = [ [TTG_SingleLeptFromT_3LBuggy_SM], [TTG_SingleLeptFromT_3LPatched_SM], [TTG_SingleLeptFromT_1L_SM] ]
signals = []

stack      = Stack( *comparisonSamples )

for sample in stack.samples:
    sample.style = styles.lineStyle( sample.color, width=2  )
    sample.scale = lumi_scale
    sample.weight = lambda event, sample: event.weight

if args.small:
    for sample in stack.samples:
        sample.normalization=1.
        sample.reduceFiles( factor=10 )
        sample.scale /= sample.normalization

weight_ = lambda event, sample: 1

# Use some defaults (set defaults before you create/import list of Plots!!)
Plot.setDefaults( stack=stack, weight=staticmethod( weight_ ), selectionString=cutInterpreter.cutString( args.selection ) )#, addOverFlowBin='upper' )

# Import plots list (AFTER setDefaults!!)
plotListFile = os.path.join( os.path.dirname( os.path.realpath( __file__ ) ), 'plotLists', args.plotFile + '.py' )
if not os.path.isfile( plotListFile ):
    logger.info( "Plot file not found: %s", plotListFile )
    sys.exit(1)

plotModule = imp.load_source( "plotLists", os.path.expandvars( plotListFile ) )
from plotLists import plotListDataMC as plotList

# Loop over channels
yields   = {}
allPlots = {}
#allModes = [ 'mumu', 'mue', 'ee' ]
allModes = [ 'all' ]

for index, mode in enumerate( allModes ):
    logger.info( "Computing plots for mode %s", mode )

    yields[mode] = {}

    # always initialize with [], elso you get in trouble with pythons references!
    plots  = []
    plots += plotList
    if mode != 'all': plots += [ getYieldPlot( index ) ]

    # Define 2l selections
    leptonSelection = cutInterpreter.cutString( mode )

    for sample in signals: sample.setSelectionString( [ leptonSelection ] )

    plotting.fill( plots, read_variables=read_variables, sequence=sequence )

    # Get normalization yields from yield histogram
    for plot in plots:
        if plot.name != "yield": continue
        for i, l in enumerate( plot.histos ):
            for j, h in enumerate( l ):
                h.GetXaxis().SetBinLabel( 1, "#mu#mu" )
                h.GetXaxis().SetBinLabel( 2, "#mue" )
                h.GetXaxis().SetBinLabel( 3, "ee" )

    logger.info( "Plotting mode %s", mode )
    allPlots[mode] = copy.deepcopy(plots) # deep copy for creating SF/all plots afterwards!
    drawPlots( allPlots[mode], mode )

exit()

# Add the different channels into SF and all
for mode in [ "SF", "all" ]:
    yields[mode] = {}

    for plot in allPlots['mumu']:
        for pl in ( p for p in ( allPlots['ee'] if mode=="SF" else allPlots["mue"] ) if p.name == plot.name ):  #For SF add EE, second round add EMu for all
            for i, j in enumerate( list( itertools.chain.from_iterable( plot.histos ) ) ):
                j.Add( list( itertools.chain.from_iterable( pl.histos ) )[i] )

    drawPlots( allPlots['mumu'], mode )

