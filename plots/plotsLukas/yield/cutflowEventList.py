#!/usr/bin/env python
''' Analysis script for standard plots
'''

# Standard imports
import ROOT, os, imp, sys, copy
#ROOT.gROOT.SetBatch(True)
import itertools
from math                                import isnan, ceil, pi

# RootTools
from RootTools.core.standard             import *

# Internal Imports
from TTGammaEFT.Tools.user               import plot_directory
from TTGammaEFT.Tools.cutInterpreter     import cutInterpreter
from TTGammaEFT.Tools.TriggerSelector    import TriggerSelector

from Analysis.Tools.metFilters           import getFilterCut
from Analysis.Tools.u_float              import u_float

# Default Parameter
loggerChoices = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO', nargs='?', choices=loggerChoices,                  help="Log level for logging")
argParser.add_argument('--selection',          action='store',      default='dilepOS-nLepVeto2-offZSFll-mll40-nJet2p-nBTag1p-nPhoton1p')
argParser.add_argument('--small',              action='store_true',                                                                    help='Run only on a small subset of the data?', )
argParser.add_argument('--useCorrectedIsoVeto', action='store_true',                                                                    help='Use the leptonVeto with corrected Iso values?', )
#argParser.add_argument('--year',               action='store',      default=None,   type=int,  choices=[2016,2017,2018],               help="which year?")
args = argParser.parse_args()

# Logger
import Analysis.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

#os.environ["gammaSkim"]="True" if "hoton" in args.selection or "pTG" in args.selection else "False"
from TTGammaEFT.Samples.nanoTuples_Summer16_private_incl_postProcessed      import TTG_NoFullyHad_fnal_16 as TTG_16
from TTGammaEFT.Samples.nanoTuples_Fall17_private_incl_postProcessed        import TTG_NoFullyHad_fnal_17 as TTG_17
from TTGammaEFT.Samples.nanoTuples_Autumn18_private_incl_postProcessed      import TTG_NoFullyHad_fnal_18 as TTG_18
#from TTGammaEFT.Samples.nanoTuples_Summer16_private_incl_postProcessed      import TTG_NoFullyHad_priv_16 as TTG_16
#from TTGammaEFT.Samples.nanoTuples_Fall17_private_incl_postProcessed        import TTG_NoFullyHad_priv_17 as TTG_17
#from TTGammaEFT.Samples.nanoTuples_Autumn18_private_incl_postProcessed      import TTG_NoFullyHad_priv_18 as TTG_18


category = {
    "photoncat0":"genuine",
    "photoncat1":"hadronic",
    "photoncat2":"misID",
    "photoncat3":"fake",
}

for year in [2016,2017,2018]:
    if year == 2016:   ttg = TTG_16
    elif year == 2017: ttg = TTG_17
    elif year == 2018: ttg = TTG_18

    filterCutMc   = getFilterCut( year, isData=False )
    tr            = TriggerSelector( year, singleLepton=args.selection.count("nLepTight1") )
    triggerCutMc  = tr.getSelection( "MC" )

    selection = "&&".join( [ cutInterpreter.cutString( args.selection ), filterCutMc, triggerCutMc ] ) #, "overlapRemoval==1" ] )
    if not args.useCorrectedIsoVeto: selection = selection.replace("nLeptonVetoIsoCorr","nLeptonVeto")

    print selection
    
    # Define a reader
    r = ttg.treeReader( \
        variables = [ TreeVariable.fromString("event/l"), TreeVariable.fromString('run/i') ],
        selectionString = selection,
        )

#    r.activateAllBranches()
#    event_list = ttg.getEventList( ttg.selectionString )
#    r.SetEventList( event_list )

#    logger.info( "Found %i events in sample %s", event_list.GetN(), ttg.name )

    r.start()
    
    selection = args.selection
    for key, value in category.items():
        selection = selection.replace(key, value)

    with open("logs/%i_EventList_%s%s.dat"%(year,selection,"_corrIso" if args.useCorrectedIsoVeto else ""), "w") as f:
        while r.run():
            run, evt = r.event.run, r.event.event
            f.write(str(run) + ", " + str(evt) + "\n")

#    del r
