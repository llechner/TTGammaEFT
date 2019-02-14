#!/usr/bin/env python
''' Analysis script for standard plots
'''

# Standard imports
import ROOT, os, imp, sys, copy
ROOT.gROOT.SetBatch(True)
import itertools
from math                                import isnan, ceil, pi

# RootTools
from RootTools.core.standard             import *

# Internal Imports
from TTGammaEFT.Tools.user               import plot_directory
from TTGammaEFT.Tools.cutInterpreter     import cutInterpreter
from TTGammaEFT.Tools.TriggerSelector    import TriggerSelector

from Analysis.Tools.metFilters           import getFilterCut

# Default Parameter
loggerChoices = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='CRITICAL', nargs='?', choices=loggerChoices,                  help="Log level for logging")
argParser.add_argument('--selection',          action='store',      default='dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40')
argParser.add_argument('--small',              action='store_true',                                                                    help='Run only on a small subset of the data?', )
argParser.add_argument('--noData',             action='store_true', default=False,                                                     help='also plot data?')
argParser.add_argument('--signal',             action='store',      default=None,   nargs='?', choices=[None],                         help="Add signal to plot")
argParser.add_argument('--year',               action='store',      default=None,   type=int,  choices=[2016,2017,2018],               help="which year?")
argParser.add_argument('--onlyTTG',            action='store_true', default=False,                                                     help="Plot only ttG")
argParser.add_argument('--normalize',          action='store_true', default=False,                                                     help="Normalize yields" )
args = argParser.parse_args()

# Logger
import Analysis.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if args.year == 2016:
    from TTGammaEFT.Samples.nanoTuples_Summer16_postProcessed    import *
    if not args.noData:
        from TTGammaEFT.Samples.nanoTuples_Run2016_05Feb2018_postProcessed import *

elif args.year == 2017:
    from TTGammaEFT.Samples.nanoTuples_Summer16_postProcessed    import *
    if not args.noData:
        from TTGammaEFT.Samples.nanoTuples_Run2016_05Feb2018_postProcessed import *

elif args.year == 2018:
    from TTGammaEFT.Samples.nanoTuples_Summer16_postProcessed    import *
    if not args.noData:
        from TTGammaEFT.Samples.nanoTuples_Run2016_05Feb2018_postProcessed import *

# Read variables and sequences
read_variables  = ["weight/F", "ref_weight/F",
                   "nJetGood/I", "nBTagGood/I",
                   "nLeptonGood/I", "nLeptonTight/I", "nLeptonVeto/I", "nElectronGood/I", "nMuonGood/I",
                   "nPhotonGood/I",
                   "mll/F", "mllgamma/F",
                  ]


read_variables += [ 'Bj0_' + var for var in nanoPlotBJetVarString.split(',') ]
read_variables += [ 'Bj1_' + var for var in nanoPlotBJetVarString.split(',') ]

read_variables_MC = ["isTTGamma/I", "isZGamma/I",
                     "reweightPU36fb/F", "reweightPU36fbDown/F", "reweightPU36fbUp/F", "reweightPU36fbVDown/F", "reweightPU36fbVUp/F",
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
    if args.onlyTTG: mc = [ TTG_16 ]
    else:            mc = [ TT_pow_16, TTG_16, DY_LO_16, singleTop_16, ZGTo2LG_16, other_16 ]
elif args.year == 2017:
    if args.onlyTTG: mc = [ TTG_17 ]
    else:            mc = [ TTG_17, DY_LO_17, TT_pow_17, singleTop_17, other_17 ]
elif args.year == 2018:
    if args.onlyTTG: mc = [ TTG_18 ]
    else:            mc = [ TTG_18, DY_LO_18, TT_pow_18 ]#, singleTop_18, ZGTo2LG_18, other_18 ]

if args.noData:
    if args.year == 2016:   lumi_scale = 35.9
    elif args.year == 2017: lumi_scale = 
    elif args.year == 2018: lumi_scale = 
    stack      = Stack( mc )
else:
    if args.year == 2016:   data_sample = Run2016
    elif args.year == 2017: data_sample = Run2017
    elif args.year == 2018: data_sample = Run2018
    data_sample.texName        = "data (legacy)"
    data_sample.name           = "data"
    data_sample.read_variables = [ "event/I", "run/I" ]
    data_sample.scale          = 1

    lumi_scale                 = 35.9 #data_sample.lumi * 0.001
    stack                      = Stack( mc, data_sample )

stack.extend( [ [s] for s in signals ] )

for sample in mc + signals:
    sample.read_variables = read_variables_MC
    sample.scale          = lumi_scale
    sample.style          = styles.fillStyle( sample.color )
    sample.weight         = lambda event, sample: event.reweightDilepTriggerBackup*event.reweightPU36fb*event.reweightLeptonSF*event.reweightLeptonTrackingSF*event.reweightPhotonSF*event.reweightPhotonElectronVetoSF*event.reweightBTag_SF

weightString   = "reweightDilepTriggerBackup*reweightPU36fb*reweightLeptonSF*reweightLeptonTrackingSF*reweightPhotonSF*reweightPhotonElectronVetoSF*reweightBTag_SF"

if args.small:
    for sample in stack.samples:
        sample.normalization=1.
        sample.reduceFiles( factor=15 )
        sample.scale /= sample.normalization

tr = TriggerSelector( args.year )

# Loop over channels
allModes = [ 'mumu', 'mue', 'ee', 'SF', 'all' ]
#allModes = [ 'mue', 'SF' ]

#print args.selection
yields = {}
for index, mode in enumerate( allModes ):

    yields[mode] = {}
    # Define 2l selections
    leptonSelection = cutInterpreter.cutString( mode )

    if not args.noData:    data_sample.setSelectionString( [ getFilterCut( args.year, isData=True  ), leptonSelection ] )
    for sample in mc + signals: sample.setSelectionString( [ getFilterCut( args.year, isData=False ), leptonSelection, tr.getSelection( "MC" ) ] )

    # Overlap removal
    TTGLep_16.addSelectionString(    "isTTGamma==1" )
#    TTG_16.addSelectionString(    "isTTGamma==1" )
    TT_pow_16.addSelectionString( "isTTGamma==0" )
#    TTbar_16.addSelectionString(     "isTTGamma==0" )
    ZGTo2LG_16.addSelectionString(   "isZGamma==1"  )
#    ZGToLLG_16.addSelectionString(   "isZGamma==1"  )
    DY_LO_16.addSelectionString(  "isZGamma==0"  )

#    print mode

    mcTotal = 0
    for s in mc:
        y = s.getYieldFromDraw( selectionString=cutInterpreter.cutString( args.selection ), weightString="weight*%f*%s"%(s.scale,weightString) )['val']
        yields[mode][s.name] = y
        mcTotal += y
#        print s.name, "yield", y
#    print "MC Total:", mcTotal
    yields[mode]["MC"] = mcTotal
    if not args.noData:
        y = data_sample.getYieldFromDraw( selectionString=cutInterpreter.cutString( args.selection ), weightString="weight" )['val']
        yields[mode][data_sample.name] = y
#        print data_sample.name, "yield", y

    
    # Get yields from draw

allSamples = [data_sample] + mc if not args.noData else mc
with open("logs/%s.log"%args.selection, "w") as f:
    f.write(args.selection + "\n")
    for mode in allModes:
        f.write("\n Mode: " + mode + "\n")
        for s in mc:
            f.write(s.name + ":\t" + str(int(yields[mode][s.name])) + "\n")
        f.write("\nMC total:\t" + str(int(yields[mode]["MC"])) + "\n")
        if not args.noData:
            f.write("data:\t" + str(int(yields[mode][data_sample.name])) + "\n")
            r = yields[mode][data_sample.name] / yields[mode]["MC"]
            f.write("R:\t" + str(r) + "\n\n")

