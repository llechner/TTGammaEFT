#!/usr/bin/env python

""" 
Get a signal region plot from the cardfiles
"""

# Standard imports
import ROOT
ROOT.gROOT.SetBatch(True)
import os
import sys
import pickle
import math

# Analysis
from Analysis.Tools.u_float           import u_float
from Analysis.Tools.getPostFit        import *
from Analysis.Tools.cardFileHelpers   import *

from TTGammaEFT.Tools.user            import plot_directory, analysis_results, cache_directory
from TTGammaEFT.Samples.color         import color
#from TTGammaEFT.Analysis.Setup        import Setup
from TTGammaEFT.Analysis.SetupHelpers import allRegions, processesMisIDPOI

from RootTools.core.standard          import *

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument("--small",                action="store_true",                            help="small?")
argParser.add_argument("--logLevel",             action="store",                default="INFO",  help="log level?", choices=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "TRACE", "NOTSET"])
argParser.add_argument("--overwrite",            action="store_true",                            help="Overwrite existing output files, bool flag set to True  if used")
argParser.add_argument("--postFit",              action="store_true",                            help="Apply pulls?")
argParser.add_argument("--preliminary",          action="store_true",                            help="Run expected?")
argParser.add_argument("--year",                 action="store",      type=int, default=2016,    help="Which year?")
argParser.add_argument("--carddir",              action='store',                default='limits/cardFiles/defaultSetup/observed',      help="which cardfile directory?")
argParser.add_argument("--cardfile",             action='store',                default='',      help="which cardfile?")
args = argParser.parse_args()

args.preliminary = True # fix label (change later)

# logger
import Analysis.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(    args.logLevel, logFile = None )
logger_rt = logger_rt.get_logger( args.logLevel, logFile = None )

if args.year == 2016:   lumi_scale = 35.92
elif args.year == 2017: lumi_scale = 41.86
elif args.year == 2018: lumi_scale = 58.83


cardFile = os.path.join( cache_directory, "analysis", str(args.year), args.carddir, args.cardfile+".txt" )
logger.info("Plotting from cardfile %s"%cardFile)

def convPTLabel( lab ):
    rang      = lab.split("pt")[1].split("To")
    if len(rang) > 1:
        low, high = rang[0], rang[1]
        return "%s #leq p_{T}(#gamma) < %s GeV"%(low, high)
    else:
        low = rang[0]
        return "p_{T}(#gamma) #geq %s GeV"%(low)

def convNPhotonLabel( lab ):
    rang = lab.split("nPhotonGood")[1].split("To")
    if len(rang) > 1 and not (rang[0]=="0" and rang[1]=="1"):
        low, high = rang[0], rang[1]
        return "%s #leq N_{#gamma} < %s"%(low, high)
    else:
        low = rang[0]
        return "N_{#gamma} = %s"%(low)

def convLabel( lab ):
    if "nPhotonGood" in lab:
        return convNPhotonLabel( lab )
    elif "pt" in lab:
        return convPTLabel( lab )
    else:
        return ""

labels   = [ tuple(label.split(" ")) for label in getAllBinLabels(cardFile) ]
#ptLabels = [ convLabel(reg) for lep, reg, cr in labels ]
crLabel  = [ ", ".join( [cr, lep.replace("mu","#mu").replace("tight",""), convLabel(reg)]) for lep, reg, cr in labels ]
#crLabel  = [ ", ".join( [cr, convLabel(reg)] ) for cr in crLabel ]
#crName   = [ cr for lep, reg, cr in labels ]

# get the results
#postFitResults = getPrePostFitFromMLF(cardFile.replace(".txt","_shapeCard_FD.root"))
postFitResults = getCovHisto( cardFile.replace(".txt","_shapeCard_FD.root") )

# get control regions from cardfile
controlRegions = {}
crList         = args.cardfile.split("_")
for cr in crList:
    if cr in allRegions.keys():
        controlRegions[cr] = allRegions[cr]

if args.postFit:
    hist = postFitResults["shapes_fit_s"]
else:
    hist = postFitResults["shapes_prefit"]

hist.LabelsOption("v","X")
hist.Scale(1./hist.GetMaximum())
for i in range(hist.GetNbinsY()):
    hist.GetYaxis().SetBinLabel( i+1, crLabel[i] )
    hist.GetXaxis().SetBinLabel( i+1, crLabel[i] )


def drawObjects( lumi_scale ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.03)
    tex.SetTextAlign(11) # align right
    addon = "post-fit" if args.postFit else "pre-fit"
    if "incl" in args.cardfile: addon += ", inclusive"
    lines = [
      ( (0.25, 0.945, "CMS (%s)"%addon) if not args.preliminary else (0.25, 0.945, "CMS #bf{#it{Preliminary}} #bf{(%s)}"%addon)),
      (0.7 if len(labels)>25 else 0.7, 0.945, "#bf{%3.1f fb^{-1} (13 TeV)}"%lumi_scale )
    ]
    return [tex.DrawLatex(*l) for l in lines]

drawObjects = drawObjects( lumi_scale=lumi_scale )

plotName = "_".join( [ item for item in args.cardfile.split("_") if item not in ["addDYSF", "addMisIDSF", "misIDPOI"] ] )
add      = "_".join( [ item for item in args.cardfile.split("_") if item in ["addDYSF", "addMisIDSF", "misIDPOI"] ] )
fit      = "postFit" if args.postFit else "preFit"
if add: fit += "_"+add

for log in [True, False]:
    plotting.draw2D(
        Plot2D.fromHisto(plotName,
            [[hist]],
            texX = "",
            texY = "",
        ),
        plot_directory = os.path.join(plot_directory, "covRegions", str(args.year), fit, "log" if log else "lin"),
        logX = False, logY = False, logZ = log, 
#        legend = [ (0.2,0.78,0.9,0.9), 6 ],
        widths = {"x_width":800 if len(labels)>25 else 800, "y_width":800 if len(labels)>25 else 800},
#        yRange = (0.7,hMax*heightFactor),
        zRange = (0.000001,1) if log else (0,1),
        #yRange = (0.03, [0.001,0.5]),
#        ratio = {"yRange": (0.11, 1.89), "texY":"Data/MC", "histos":[(1,0)], "drawObjects":ratio_boxes, #+ drawLabelsLower( regions ) +drawHeadlineLower( regions ) + drawDivisionsLower(regions),
#                "histModifications": [lambda h: h.GetYaxis().SetTitleSize(20), lambda h: h.GetYaxis().SetLabelSize(20), lambda h: h.GetYaxis().SetTitleOffset(1.0 if len(labels)>25 else 1.5), lambda h: h.GetXaxis().SetTitleSize(20), lambda h: h.GetXaxis().SetLabelSize(16), lambda h: h.GetXaxis().SetLabelOffset(0.035)]} ,
        drawObjects = drawObjects,
        histModifications = [lambda h: h.GetYaxis().SetLabelSize(12), lambda h: h.GetXaxis().SetLabelSize(12), lambda h: h.GetZaxis().SetLabelSize(0.03)],
        canvasModifications = [ lambda c : c.SetLeftMargin(0.25), lambda c: c.SetBottomMargin(0.25) ],
        copyIndexPHP = True,
    )

