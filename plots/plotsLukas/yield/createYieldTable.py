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

from TTGammaEFT.Tools.user               import cache_directory
from Analysis.Tools.DirDB               import DirDB

# Default Parameter
loggerChoices = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO', nargs='?', choices=loggerChoices,                  help="Log level for logging")
argParser.add_argument('--selection',          action='store',      default='dilepOS-nLepVeto2-offZSFll-mll40-nJet2p-nBTag1p-nPhoton1p')
argParser.add_argument('--small',              action='store_true',                                                                    help='Run only on a small subset of the data?', )
argParser.add_argument('--runOnNonValid',      action='store_true',                                                                    help='Skip missing cached yields?', )
argParser.add_argument('--removeNegative',     action='store_true',                                                                    help='Set negative values to 0?', )
argParser.add_argument('--noData',             action='store_true', default=False,                                                     help='also plot data?')
argParser.add_argument('--year',               action='store',      default=None,   type=int,  choices=[2016,2017,2018],               help="which year?")
args = argParser.parse_args()

# Logger
import Analysis.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

cache_dir = os.path.join(cache_directory, "yields", str(args.year))

os.environ["gammaSkim"]="False"
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

elif "nLepTight" in args.selection:
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


# Sample definition
if "dilep" in args.selection:
    if args.year == 2016:
            mc = [ TTG_priv_16, DY_LO_16, TT_pow_16, singleTop_16, ZG_16, other_16 ]
    elif args.year == 2017:
            mc = [ TTG_priv_17, DY_LO_17, TT_pow_17, singleTop_17, ZG_17, other_17 ]
    elif args.year == 2018:
            mc = [ TTG_priv_18, DY_LO_18, TT_pow_18, singleTop_18, ZG_18, other_18 ]

elif "nLepTight" in args.selection:
    #print "selection"
    if args.year == 2016:
        mc = [ TTG_priv_16, TT_pow_16, DY_LO_16, singleTop_16, WJets_16, TG_16, WG_NLO_16, ZG_16, other_16, QCD_16 ]
    elif args.year == 2017:
        mc = [ TTG_priv_17, TT_pow_17, DY_LO_17, singleTop_17, WJets_17, TG_17, WG_NLO_17, ZG_17, other_17, QCD_17 ]
    elif args.year == 2018:
        mc = [ TTG_priv_18, TT_pow_18, DY_LO_18, singleTop_18, WJets_18, TG_18, WG_NLO_18, ZG_18, other_18, QCD_18 ]


if args.noData:
    if args.year == 2016:   lumi_scale = 35.92
    elif args.year == 2017: lumi_scale = 41.86
    elif args.year == 2018: lumi_scale = 58.83
    allSamples = mc
else:
    if args.year == 2016:   data_sample = Run2016
    elif args.year == 2017: data_sample = Run2017
    elif args.year == 2018: data_sample = Run2018
    lumi_scale = data_sample.lumi * 0.001
    data_sample.name = "data"
    allSamples = [data_sample] + mc


ptSel     = ['lowPT', 'medPT', 'highPT']
pthadSel  = ['lowhadPT', 'medhadPT', 'highhadPT']
catSel    = ['photoncat0', 'photoncat1', 'photoncat2', 'photoncat3']
hadcatSel = ['photonhadcat0', 'photonhadcat1', 'photonhadcat2', 'photonhadcat3']
sieieSel  = ['lowSieie', 'highSieie']
chgSel    = ['lowChgIso', 'highChgIso']
noCat_sel = "(1)"
region    = "manual"

#for var in ptSel+pthadSel+catSel+hadcatSel+sieieSel+chgSel:
#    vars()[var] = cutInterpreter.cutString( var )

if "NoChgIsoNoSieiePhoton" in args.selection:
    allCats  = [noCat_sel] + hadcatSel
    allModes = []
    for sieie in sieieSel:
        for chg in chgSel:
            for pt in pthadSel:
                allModes.append( '-'.join( [ pt, sieie, chg ] ) )
    regions = { 
            "20To120":  [ mode for mode in allModes if "lowhadPT"  in mode],
            "120To220": [ mode for mode in allModes if "medhadPT"  in mode],
            "220To-1":  [ mode for mode in allModes if "highhadPT" in mode],
    }

else:
    allCats     = [noCat_sel] + catSel
    allModes    = ptSel

yields = {}
for i_mode, mode in enumerate(["incl"]+allModes):
    yields[mode] = {}
    for i_cat, cat in enumerate(allCats):
        yields[mode][cat] = {}
        yields[mode][cat]["MC"] = 0
        for sample in allSamples:
            yields[mode][cat][sample.name] = 0

yieldDB = DirDB( cache_dir )
if not yieldDB: raise

for sample in allSamples:

    for i_mode, mode in enumerate(allModes):
        for i_cat, cat in enumerate(allCats):
            if not args.noData and (sample.name == data_sample.name) and cat != noCat_sel:
                yields[mode][cat][sample.name] = -1
                yields["incl"][cat][sample.name] = -1
                continue

            # do not unblind 17 and 18
            if not args.noData and (sample.name == data_sample.name) and cat == noCat_sel and "NoChgIsoNoSieiePhoton" in args.selection and "lowSieie" in mode and "lowChgIso" in mode and args.year != 2016:
                yields[mode][cat][sample.name] = -1
                yields["incl"][cat][sample.name] = -1
                continue

            # do not unblind 17 and 18
            if not args.noData and (sample.name == data_sample.name) and cat == noCat_sel and "nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p" in args.selection and args.year != 2016:
                yields[mode][cat][sample.name] = -1
                yields["incl"][cat][sample.name] = -1
                continue

            if "QCD" in sample.name and ("all" in args.selection or "SFtight" in args.selection):
                leps = ["eetight", "mumutight", "muetight"] if "nLepTight2" in args.selection else ["e","mu"]
                yields[mode][cat][sample.name] = 0
                for lep in leps:
                    if "SFtight" in args.selection and lep == "muetight": continue
                    selection = "-".join( [args.selection.replace("all", lep), mode, cat] if cat != noCat_sel else [args.selection.replace("all", lep), mode] )
                    res = "_".join( [sample.name, selection, "small" if args.small else "full"] )

                    if not yieldDB.contains( res ):
                        print("Yield for sample %s and selection %s and year %i and mode %s and cat %s not cached!"%(sample.name, args.selection, args.year, mode, cat))
                        if args.runOnNonValid:
                            yields[mode][cat][sample.name] = -1
                            yields["incl"][cat][sample.name] = -1
                        continue
                        sys.exit(0)
                    yields[mode][cat][sample.name] += int(round(float(yieldDB.get( res ))))
            else:
                selection = "-".join( [args.selection, mode, cat] if cat != noCat_sel else [args.selection, mode] )
                res = "_".join( [sample.name, selection, "small" if args.small else "full"] )

                if not yieldDB.contains( res ):
                    print("Yield for sample %s and selection %s and year %i and mode %s and cat %s not cached!"%(sample.name, args.selection, args.year, mode, cat))
                    if args.runOnNonValid:
                        yields[mode][cat][sample.name] = -1
                        yields["incl"][cat][sample.name] = -1
                        continue
                    sys.exit(0)

                yields[mode][cat][sample.name] = int(round(float(yieldDB.get( res ))))

            if args.removeNegative and yields[mode][cat][sample.name] < 0: yields[mode][cat][sample.name] = 0 #could be for QCD estimation
#            print("Found yield for sample %s and selection %s and year %i: %i"%(sample.name, args.selection, args.year, yields[mode][cat][sample.name]))

            if sample.name != data_sample.name:
                yields[mode][cat]["MC"] += yields[mode][cat][sample.name]
                if not "NoChgIsoNoSieiePhoton" in args.selection:
                    yields["incl"][cat]["MC"] += yields[mode][cat][sample.name]

            if not "NoChgIsoNoSieiePhoton" in args.selection:
                yields["incl"][cat][sample.name] += yields[mode][cat][sample.name]


def printHadFakeYieldTable():

    with open("logs/%i_%s.log"%(args.year,args.selection), "w") as f:
        f.write("\\begin{frame}\n")
        f.write("\\frametitle{Yields - hadronic fake CR}\n\n")

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
                f.write("%s & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i \\\\ \n" %tuple( [s.name.replace("_","\_")] + [ int(yields[mode][cat][s.name]) for mode in regions["%iTo%i"%(lowPT, highPT)] for cat in allCats]) )
                f.write("\\hline\n")
            f.write("\\hline\n")
            f.write("MC total & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i \\\\ \n" %tuple( [int(yields[mode][cat]["MC"]) for mode in regions["%iTo%i"%(lowPT, highPT)] for cat in allCats] ))
            f.write("\\hline\n")
            if not args.noData:
                f.write("data total & \\textbf{%i} & \\multicolumn{4}{c||}{} & \\textbf{%i} & \\multicolumn{4}{c||}{} & \\textbf{%i} & \\multicolumn{4}{c||}{} & \\textbf{%i} & \\multicolumn{4}{c}{} \\\\ \n" %tuple( [int(yields[mode][noCat_sel][data_sample.name]) for mode in regions["%iTo%i"%(lowPT, highPT)]] ))
                f.write("\\hline\n")
            f.write("\\hline\n")
    
            if highPT == -1:
                f.write("\\multicolumn{21}{c}{}\\\\ \n")
                f.write("\\multicolumn{1}{c}{} & \\multicolumn{5}{c}{$\gamma$ = genuine photons} & \\multicolumn{5}{c}{had $\gamma$ = hadronic photons} & \\multicolumn{5}{c}{misID e = misID electrons} & \\multicolumn{5}{c}{fake = hadronic fakes} \\\\ \n")


            f.write("\\end{tabular}\n")
            f.write("}\n\n") #resizebox

        f.write("\\end{table}\n\n")
        f.write("\\end{frame}\n\n\n\n")




def printYieldTable():
    allSamples = [data_sample] + mc if not args.noData else mc

    with open("logs/%i_%s.log"%(args.year,args.selection), "w") as f:
    
        if "-e" in args.selection or "-all" in args.selection:
            f.write("\\begin{frame}\n")
            f.write("\\frametitle{Yields - CR}\n\n")

        f.write("\\begin{table}\n")
        f.write("\\centering\n")

        f.write("\\resizebox{0.9\\textwidth}{!}{\n")
        f.write("\\begin{tabular}{c||c||c|c|c|c||c||c|c|c|c||c||c|c|c|c||c||c|c|c|c}\n")
#        f.write("\\begin{tabular}{c||c||c|c|c|c||c||c|c|c|c||c||c|c|c|c}\n")

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
        f.write("Sample  & \\multicolumn{5}{c||}{inclusive} & \\multicolumn{5}{c||}{%i $\\leq$ \\pT($\\gamma$) $<$ %i GeV} & \\multicolumn{5}{c||}{%i $\\leq$ \\pT($\\gamma$) $<$ %i GeV} & \\multicolumn{5}{c}{\\pT($\\gamma$) $>$ %i GeV}\\\\ \n"%(20,120,120,220,220))
        f.write("\\hline\n")
        f.write("        & \\textbf{events} & $\gamma$ & had $\gamma$ & misID e & fake & \\textbf{events} & $\gamma$ & had $\gamma$ & misID e & fake & \\textbf{events} & $\gamma$ & had $\gamma$ & misID e & fake & \\textbf{events} & $\gamma$ & had $\gamma$ & misID e & fake \\\\ \n")
        f.write("\\hline\n")
        f.write("\\hline\n")
        for s in mc:
            f.write("%s & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i \\\\ \n" %tuple( [s.name.replace("_","\_")] + [ int(round(yields[mode][cat][s.name])) for mode in ["incl"] + allModes for cat in allCats]) )
            f.write("\\hline\n")
        f.write("\\hline\n")
        f.write("MC total & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i & \\textbf{%i} & %i & %i & %i & %i \\\\ \n" %tuple( [int(yields[mode][cat]["MC"]) for mode in ["incl"] + allModes for cat in allCats] ))
        f.write("\\hline\n")
        if not args.noData:
            f.write("data total & \\textbf{%i} & \\multicolumn{4}{c||}{} & \\textbf{%i} & \\multicolumn{4}{c||}{} & \\textbf{%i} & \\multicolumn{4}{c||}{} & \\textbf{%i} & \\multicolumn{4}{c}{} \\\\ \n" %tuple( [int(yields[mode][noCat_sel][data_sample.name]) for mode in ["incl"] + allModes] ))
            f.write("\\hline\n")
        f.write("\\hline\n")
    
        f.write("\\multicolumn{21}{c}{}\\\\ \n")
        f.write("\\multicolumn{1}{c}{} & \\multicolumn{5}{c}{$\gamma$ = genuine photons} & \\multicolumn{5}{c}{had $\gamma$ = hadronic photons} & \\multicolumn{5}{c}{misID e = misID electrons} & \\multicolumn{5}{c}{fake = hadronic fakes} \\\\ \n")


        f.write("\\end{tabular}\n")
        f.write("}\n\n") #resizebox

        f.write("\\end{table}\n\n")
        if "-mu" in args.selection or "-all" in args.selection:
            f.write("\\end{frame}\n")
        f.write("\n\n\n")



if "NoChgIsoNoSieiePhoton" in args.selection:
    printHadFakeYieldTable()
else:
    printYieldTable()
