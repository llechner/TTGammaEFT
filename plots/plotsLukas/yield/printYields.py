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

# Default Parameter
loggerChoices = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='CRITICAL', nargs='?', choices=loggerChoices,                  help="Log level for logging")
argParser.add_argument('--selection',          action='store',      default='dilepOS-nLepVeto2-offZSFll-mll40-nJet2p-nBTag1p-nPhoton1p')
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


os.environ["gammaSkim"]="True" if "hoton" in args.selection or "pTG" in args.selection else "False"
if "dilep" in args.selection:
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
            from TTGammaEFT.Samples.nanoTuples_Run2018_14Dec2018_postProcessed import *

elif "nLepTight1" in args.selection:
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



# Read variables and sequences
read_variables  = ["weight/F", 
                   "nJetGood/I", "nBTagGood/I",
                   "nLeptonGood/I", "nLeptonTight/I", "nLeptonVeto/I", "nElectronGood/I", "nMuonGood/I",
                   "nPhotonGood/I",
                   "mll/F", "mllgamma/F",
                  ]


read_variables_MC = ["isTTGamma/I", "isZWGamma/I", "isTGamma/I", "overlapRemoval/I",
                     "reweightPU/F", "reweightPUDown/F", "reweightPUUp/F", "reweightPUVDown/F", "reweightPUVUp/F",
                     "reweightLeptonTightSF/F", "reweightLeptonTightSFUp/F", "reweightLeptonTightSFDown/F",
                     "reweightLeptonTrackingTightSF/F",
                     "reweightLepton2lSF/F", "reweightLepton2lSFUp/F", "reweightLepton2lSFDown/F",
                     "reweightLeptonTracking2lSF/F",
                     "reweightDilepTrigger/F", "reweightDilepTriggerUp/F", "reweightDilepTriggerDown/F",
                     "reweightDilepTriggerBackup/F", "reweightDilepTriggerBackupUp/F", "reweightDilepTriggerBackupDown/F",
                     "reweightPhotonSF/F", "reweightPhotonSFUp/F", "reweightPhotonSFDown/F",
                     "reweightPhotonElectronVetoSF/F",
                     "reweightBTag_SF/F", "reweightBTag_SF_b_Down/F", "reweightBTag_SF_b_Up/F", "reweightBTag_SF_l_Down/F", "reweightBTag_SF_l_Up/F",
                     'reweightL1Prefire/F', 'reweightL1PrefireUp/F', 'reweightL1PrefireDown/F',
                    ]
# Sequence
sequence = []

# Sample definition
if "dilep" in args.selection:
    if args.year == 2016:
            mc = [ TTG_priv_16, DY_LO_16, TT_pow_16, singleTop_16, ZG_16 ]
    elif args.year == 2017:
            mc = [ TTG_priv_17, DY_LO_17, TT_pow_17, singleTop_17, ZG_17 ]
    elif args.year == 2018:
            mc = [ TTG_priv_18, DY_LO_18, TT_pow_18, singleTop_18, ZG_18 ]

    weightString   = "reweightL1Prefire*reweightPU*reweightLepton2lSF*reweightLeptonTracking2lSF*reweightPhotonSF*reweightPhotonElectronVetoSF*reweightBTag_SF"

elif "nLepTight1" in args.selection:
    if args.year == 2016:
            mc = [ TTG_priv_16, TT_pow_16, DY_LO_16, singleTop_16, WJets_16, TG_16, WG_16, ZG_16 ]
    elif args.year == 2017:
            mc = [ TTG_priv_17, TT_pow_17, DY_LO_17, singleTop_17, WJets_17, TG_17, WG_17, ZG_17 ]
    elif args.year == 2018:
            mc = [ TTG_priv_18, TT_pow_18, DY_LO_18, singleTop_18, WJets_18, TG_18, WG_18, ZG_18 ]

    weightString   = "reweightL1Prefire*reweightPU*reweightLeptonTightSF*reweightLeptonTrackingTightSF*reweightPhotonSF*reweightPhotonElectronVetoSF*reweightBTag_SF"


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

if args.small:
    for sample in stack.samples:
        sample.normalization=1.
        sample.reduceFiles( factor=15 )
        sample.scale /= sample.normalization

filterCutData = getFilterCut( args.year, isData=True )
filterCutMc   = getFilterCut( args.year, isData=False )
tr            = TriggerSelector( args.year )
triggerCutMc  = tr.getSelection( "MC" )

# Loop over channels
#allModes = [ 'mumu', 'mue', 'ee', 'SF', 'all' ]
#allModes = [ 'mue', 'SF' ]

lowSieie   = "PhotonNoChgIsoNoSieie0_sieie<0.01015"
highSieie  = "PhotonNoChgIsoNoSieie0_sieie>0.011"

lowChgIso   = "PhotonNoChgIsoNoSieie0_pfRelIso03_chg*PhotonNoChgIsoNoSieie0_pt<1.141"
highChgIso  = "PhotonNoChgIsoNoSieie0_pfRelIso03_chg*PhotonNoChgIsoNoSieie0_pt>1.141"

lowPT  = "PhotonNoChgIsoNoSieie0_pt>=20&&PhotonNoChgIsoNoSieie0_pt<120"
medPT  = "PhotonNoChgIsoNoSieie0_pt>=120&&PhotonNoChgIsoNoSieie0_pt<220"
highPT = "PhotonNoChgIsoNoSieie0_pt>=220"

noCat_sel = "(1)"
cat_sel0  = "PhotonNoChgIsoNoSieie0_photonCat==0"
cat_sel1  = "PhotonNoChgIsoNoSieie0_photonCat==1"
cat_sel2  = "PhotonNoChgIsoNoSieie0_photonCat==2"
cat_sel3  = "PhotonNoChgIsoNoSieie0_photonCat==3"

allCats  = [ noCat_sel, cat_sel0, cat_sel1, cat_sel2, cat_sel3 ]
allModes = [
            '&&'.join([lowSieie,lowChgIso,lowPT]),
            '&&'.join([lowSieie,lowChgIso,medPT]),
            '&&'.join([lowSieie,lowChgIso,highPT]),
            '&&'.join([highSieie,lowChgIso,lowPT]),
            '&&'.join([highSieie,lowChgIso,medPT]),
            '&&'.join([highSieie,lowChgIso,highPT]),
            '&&'.join([lowSieie,highChgIso,lowPT]),
            '&&'.join([lowSieie,highChgIso,medPT]),
            '&&'.join([lowSieie,highChgIso,highPT]),
            '&&'.join([highSieie,highChgIso,lowPT]),
            '&&'.join([highSieie,highChgIso,medPT]),
            '&&'.join([highSieie,highChgIso,highPT]),
 ]

yields = {}

for i_mode, mode in enumerate(allModes):
    yields[mode] = {}
    for i_cat, cat in enumerate(allCats):
        yields[mode][cat] = {}

        if not args.noData:    data_sample.setSelectionString( [ filterCutData, mode ] )
        for sample in mc + signals: sample.setSelectionString( [ filterCutMc, mode, cat, triggerCutMc, "overlapRemoval==1" ] )

        mcTotal = 0
        for i_s, s in enumerate(mc):
            if cat != noCat_sel and yields[mode][noCat_sel][s.name] < 0.5:
                yields[mode][cat][s.name] = 0
                continue
            y = s.getYieldFromDraw( selectionString=cutInterpreter.cutString( args.selection ), weightString="weight*%f*%s"%(s.scale,weightString) )['val']
            yields[mode][cat][s.name] = y
            mcTotal += y

        yields[mode][cat]["MC"] = mcTotal
        if not args.noData and cat==noCat_sel:
            y = data_sample.getYieldFromDraw( selectionString=cutInterpreter.cutString( args.selection ), weightString="weight" )['val']
            yields[mode][cat][data_sample.name] = y

allSamples = [data_sample] + mc if not args.noData else mc

regions = { 
            "20To120":  [ mode for mode in allModes if lowPT  in mode],
            "120To220": [ mode for mode in allModes if medPT  in mode],
            "220To-1":  [ mode for mode in allModes if highPT in mode],
          }

with open("logs/%s.log"%args.selection, "w") as f:
    f.write("\\begin{table}\n")
    f.write("\\centering\n")

    for lowPT, highPT in [ (20,120), (120,220), (220,-1) ]:
        f.write("\\resizebox{0.8\\textwidth}{!}{\n")
        f.write("\\begin{tabular}{c||c||c|c|c|c||c||c|c|c|c||c||c|c|c|c||c||c|c|c|c}\n")

        if lowPT == 20:
            f.write("\\hline\n")
            f.write("\\hline\n")
            f.write("\\multicolumn{21}{c}{%s}\\\\ \n"%( ", ".join( args.selection.split("-") ) ) )
            f.write("\\hline\n")
            f.write("\\multicolumn{21}{c}{%i: $\\mathcal{L}=%s$ fb$^{-1}$}\\\\ \n"%(args.year, "{:.2f}".format(lumi_scale)))
            f.write("\\hline\n")
            f.write("\\hline\n")
            f.write("\\multicolumn{21}{c}{}\\\\ \n")

        f.write("\\hline\n")
        f.write("\\hline\n")
        if highPT == -1:
            f.write("\\multicolumn{21}{c}{\\pT($\\gamma$) $>$ %i GeV}\\\\ \n"%(lowPT))
        else:
            f.write("\\multicolumn{21}{c}{%i $\\leq$ \\pT($\\gamma$) $<$ %i GeV}\\\\ \n"%(lowPT, highPT))
        f.write("\\hline\n")
        f.write("Sample  & \\multicolumn{5}{c||}{low $\\sigma_{i\\eta i\\eta}$, low chg Iso (SR)} & \\multicolumn{5}{c||}{high $\\sigma_{i\\eta i\\eta}$, low chg Iso  (NN2)}   & \\multicolumn{5}{c||}{low $\\sigma_{i\\eta i\\eta}$, high chg Iso (NN1)}   & \\multicolumn{5}{c}{high $\\sigma_{i\\eta i\\eta}$, high chg Iso  (CR)} \\\\ \n")
        f.write("\\hline\n")
        f.write("        & \\textbf{events} & $\gamma$ & had $\gamma$ & misID e & fake & \\textbf{events} & $\gamma$ & had $\gamma$ & misID e & fake & \\textbf{events} & $\gamma$ & had $\gamma$ & misID e & fake & \\textbf{events} & $\gamma$ & had $\gamma$ & misID e & fake \\\\ \n")
        f.write("\\hline\n")
        f.write("\\hline\n")
        for s in mc:
#            f.write("%s & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i \\\\ \n" %(s.name) + (int(yields[mode][cat][s.name] for mode in regions["%iTo%i"%(lowPT, highPT)] for cat in allCats) ))
            f.write("%s & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i \\\\ \n" %tuple( [s.name.replace("_","\_")] + [ int(yields[mode][cat][s.name]) for mode in regions["%iTo%i"%(lowPT, highPT)] for cat in allCats]) )
            f.write("\\hline\n")
        f.write("\\hline\n")
        f.write("MC total & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i \\\\ \n" %tuple( [int(yields[mode][cat]["MC"]) for mode in regions["%iTo%i"%(lowPT, highPT)] for cat in allCats] ))
        f.write("\\hline\n")
        f.write("data total & \\textbf{%i} & \\multicolumn{4}{c||}{} & \\textbf{%i} & \\multicolumn{4}{c||}{} & \\textbf{%i} & \\multicolumn{4}{c||}{} & \\textbf{%i} & \\multicolumn{4}{c}{} \\\\ \n" %tuple( [int(yields[mode][noCat_sel][data_sample.name]) for mode in regions["%iTo%i"%(lowPT, highPT)]] ))
        f.write("\\hline\n")
        f.write("\\hline\n")

        if highPT == -1:
            f.write("\\multicolumn{21}{c}{}\\\\ \n")
            f.write("\\multicolumn{1}{c}{} & \\multicolumn{5}{c}{$\gamma$ = genuine photons} & \\multicolumn{5}{c}{had $\gamma$ = hadronic photons} & \\multicolumn{5}{c}{misID e = misID electrons} & \\multicolumn{5}{c}{fake = hadronic fakes} \\\\ \n")


        f.write("\\end{tabular}\n")
        f.write("}\n\n") #resizebox

    f.write("\\end{table}\n")


