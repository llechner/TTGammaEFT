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
argParser.add_argument("--blinded",              action="store_true")
argParser.add_argument("--overwrite",            action="store_true",                            help="Overwrite existing output files, bool flag set to True  if used")
argParser.add_argument("--postFit",              action="store_true",                            help="Apply pulls?")
argParser.add_argument("--expected",             action="store_true",                            help="Run expected?")
argParser.add_argument("--preliminary",          action="store_true",                            help="Run expected?")
argParser.add_argument("--year",                 action="store",      type=int, default=2016,    help="Which year?")
argParser.add_argument("--carddir",              action='store',                default='limits/cardFiles/defaultSetup/observed',      help="which cardfile directory?")
argParser.add_argument("--cardfile",             action='store',                default='',      help="which cardfile?")
argParser.add_argument("--bkgOnly",              action='store_true',                            help="background fit?")
args = argParser.parse_args()

args.preliminary = True # fix label (change later)

# logger
import Analysis.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(    args.logLevel, logFile = None )
logger_rt = logger_rt.get_logger( args.logLevel, logFile = None )

isData = True if not args.expected else False

if args.year == 2016:   lumi_scale = 35.92
elif args.year == 2017: lumi_scale = 41.86
elif args.year == 2018: lumi_scale = 58.83

cardFile = os.path.join( cache_directory, "analysis", str(args.year), args.carddir, args.cardfile+".txt" )
logger.info("Plotting from cardfile %s"%cardFile)

labels   = [ tuple(label.split(" ")) for label in getAllBinLabels(cardFile) ]

if len(labels)>45:
    textsize = 40
    xlabelsize = 20
    ylabelsize = 30
    padwidth = 3000
    padheight = 1200
    padratio = 350
    hashcode = 3144
    legcolumns = 6
    legylower = 0.83
    textoffset = 0.8
    offsetfactor = 8
    ptlabelsize = 0.015
    heightFactor = 100
elif len(labels)>25:
    textsize = 40
    xlabelsize = 20
    ylabelsize = 30
    padwidth = 2500
    padheight = 1200
    padratio = 350
    hashcode = 3144
    legcolumns = 6
    legylower = 0.8
    textoffset = 1
    offsetfactor = 40
    ptlabelsize = 0.022
    heightFactor = 1000
else:
    textsize = 20
    xlabelsize = 16
    ylabelsize = 20
    padwidth = 1000
    padheight = 700
    padratio = 250
    hashcode = 3344
    legcolumns = 5
    legylower = 0.77
    textoffset = 1.5
    offsetfactor = 42
    ptlabelsize = 0.022
    heightFactor = 1000


def convPTLabel( lab ):
    # PhotonGood0_pt20To120_m370To140
    # PhotonNoChgIsoNoSieie0_pt20To120_(PhotonNoChgIsoNoSieie0_pfRelIso03_chg*PhotonNoChgIsoNoSieie0_pt)0To1
    rang = lab.split("_pt")[1].split("_")[0].split("To")
    if len(rang) > 1:
        low, high = rang[0], rang[1]
        return "%s #leq p_{T}(#gamma) < %s GeV"%(low, high)
    else:
        low = rang[0]
        return "p_{T}(#gamma) #geq %s GeV"%(low)

def convM3Label( lab ):
    # PhotonGood0_pt20To120_m370To140
    rang = lab.split("m3")[1].split("To")
    if len(rang) > 1:
        low, high = rang[0], rang[1]
        return "%s #leq M_{3} < %s GeV"%(low, high)
    else:
        low = rang[0]
        return "M_{3} #geq %s GeV"%(low)

def convChgIsoLabel( lab ):
    # PhotonNoChgIsoNoSieie0_pt20To120_(PhotonNoChgIsoNoSieie0_pfRelIso03_chg*PhotonNoChgIsoNoSieie0_pt)0To1
    rang = lab.split("(PhotonNoChgIsoNoSieie0_pfRelIso03_chg*PhotonNoChgIsoNoSieie0_pt)")[1].split("To")
    if len(rang) > 1:
        low, high = rang[0], rang[1]
        return "%s #leq chg.Iso(#gamma) < %s GeV"%(low, high)
    else:
        low = rang[0]
        return "chg.Iso(#gamma) #geq %s GeV"%(low)

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
        label = convPTLabel( lab )
        if "m3" in lab:
            label += ", " + convM3Label( lab )
        if "pfRelIso" in lab:
            label += ", " + convChgIsoLabel( lab )
        return label
    else:
        return ""

ptLabels = [ convLabel(reg) for lep, reg, cr in labels ]
crLabel  = [ ", ".join( [cr, lep.replace("mu","#mu").replace("tight","")] ) for lep, reg, cr in labels ]
crName   = [ cr for lep, reg, cr in labels ]

# get the results
postFitResults = getPrePostFitFromMLF(cardFile.replace(".txt","_shapeCard_FD.root"))

# get control regions from cardfile
controlRegions = {}
crList         = args.cardfile.split("_")
for cr in crList:
    if cr in allRegions.keys():
        controlRegions[cr] = allRegions[cr]

if args.postFit:
    hists = postFitResults["hists"]["shapes_fit_s" if not args.bkgOnly else "shapes_fit_b"]["Bin0"]
else:
    hists = postFitResults["hists"]["shapes_prefit"]["Bin0"]

histDict = processesMisIDPOI if "misIDPOI" in args.cardfile else controlRegions[controlRegions.keys()[0]]["processes"]
dataHist = hists[histDict.keys()[-1]].Clone()
dataHist.Reset()
dataHist.SetName("data")
dataHist.legendText = "data"

bkgHists = []
for p, p_dict in histDict.items():
    if p not in hists.keys():
        # some histograms are 0, still should be in the legend
        logger.info("Histogram for %s not found! Continuing..."%p)
        hists[p] = hists[histDict.keys()[-1]].Clone()
        hists[p].Scale(0.)
        hists[p].SetName(p)

    hists[p].style = styles.fillStyle( p_dict["color"], errors=False )
    hists[p].legendText = p_dict["texName"]
    if p != "signal":
        bkgHists.append(hists[p])
    
    for i in range( hists[p].GetNbinsX() ):
        hists[p].GetXaxis().SetBinLabel( i+1, crLabel[i] )
    hists[p].LabelsOption("v","X") #"vu" for 45 degree labels

for i in range(dataHist.GetNbinsX()):
    dataHist.SetBinContent(i+1, hists["data"].Eval(i+0.5))
    dataHist.SetBinError(i+1, math.sqrt(hists["data"].Eval(i+0.5)))
    for j in range( dataHist.GetNbinsX() ):
        dataHist.GetXaxis().SetBinLabel( j+1, crLabel[j] )
        dataHist.LabelsOption("v","X")


# Manipulate Signal Histos, clone histo, set one 0 in CR, the other 0 in SR
histSig = hists["signal"].Clone()
histSig.SetName("signalSR")
histSig.style = styles.fillStyle( histDict["signal"]["color"], errors=False )
histSig.notInLegend = True

for i_cr, cr in enumerate(crLabel):
    if "SR" in cr and not "Iso" in cr:
        hists["signal"].SetBinContent(i_cr+1, 0)
    else:
        histSig.SetBinContent(i_cr+1, 0)

    hists["signal"].GetXaxis().SetBinLabel( i_cr+1, crLabel[i_cr] )
    histSig.GetXaxis().SetBinLabel( i_cr+1, crLabel[i_cr] )

hists["signal"].LabelsOption("v","X") #"vu" for 45 degree labels
histSig.LabelsOption("v","X") #"vu" for 45 degree labels

bkgHists.append(hists["signal"])
hists["signalSR"] = histSig

# Data Histo
hists["data"]              = dataHist
hists["data"].style        = styles.errorStyle( ROOT.kBlack )
hists["data"].legendOption = "p"

boxes = []
ratio_boxes = []
for ib in range(1, 1 + hists["total"].GetNbinsX() ):
    val = hists["total"].GetBinContent(ib)
    if val<0: continue
    sys = hists["total"].GetBinError(ib)
    if val > 0:
        sys_rel = sys/val
    else:
        sys_rel = 1.
    
    # uncertainty box in main histogram
    box = ROOT.TBox( hists["total"].GetXaxis().GetBinLowEdge(ib),  max([0.006, val-sys]), hists["total"].GetXaxis().GetBinUpEdge(ib), max([0.006, val+sys]) )
    box.SetLineColor(ROOT.kGray+3)
    box.SetFillStyle(hashcode)
    box.SetFillColor(ROOT.kGray+3)
    
    # uncertainty box in ratio histogram
    r_box = ROOT.TBox( hists["total"].GetXaxis().GetBinLowEdge(ib),  max(0.11, 1-sys_rel), hists["total"].GetXaxis().GetBinUpEdge(ib), min(1.9, 1+sys_rel) )
    r_box.SetLineColor(ROOT.kGray+3)
    r_box.SetFillStyle(hashcode)
    r_box.SetFillColor(ROOT.kGray+3)

    boxes.append( box )
    hists["total"].SetBinError(ib, 0)
    ratio_boxes.append( r_box )

    #pt text in main histogram
    box = ROOT.TBox( hists["total"].GetXaxis().GetBinLowEdge(ib),  max([0.006, val-sys]), hists["total"].GetXaxis().GetBinUpEdge(ib), max([0.006, val+sys]) )
    box.SetLineColor(ROOT.kGray+3)
    box.SetFillStyle(hashcode)
    box.SetFillColor(ROOT.kGray+3)
    

def drawDivisions():
    min = 0.15
    max = 0.95
    diff = (max-min) / len(crLabel)
    line = ROOT.TLine()
    line.SetLineWidth(2)
    line.SetLineStyle(9)
    line2 = ROOT.TLine()
    line2.SetLineWidth(3)
    line2.SetLineStyle(1)
    lines  = []
    lines2 = []
    done = False
    for i_reg, reg in enumerate(crLabel):
        if i_reg != len(crLabel)-1 and "SR" in crLabel[i_reg+1] and not "Iso" in crLabel[i_reg+1] and not done:
            lines2.append( (min+(i_reg+1)*diff,  0., min+(i_reg+1)*diff, legylower) )
            done = True
        if i_reg != len(crLabel)-1 and reg.split(",")[0] != crLabel[i_reg+1].split(",")[0]:
            lines.append( (min+(i_reg+1)*diff,  0., min+(i_reg+1)*diff, legylower) )
    return [line.DrawLineNDC(*l) for l in lines] + [line2.DrawLineNDC(*l) for l in lines2]

def drawPTDivisions():
    min = 0.15
    max = 0.95
    diff = (max-min) / len(crLabel)
    lines = []
    lines2 = []
    line = ROOT.TLine()
#   line.SetLineColor(38)
    line.SetLineWidth(1)
    line.SetLineStyle(5)
    lines = []
    for i_pt, pt in enumerate(ptLabels):
        if i_pt != len(ptLabels)-1 and pt != ptLabels[i_pt+1] and crLabel[i_pt].split(",")[0] == crLabel[i_pt+1].split(",")[0]:
            lines.append( (min+(i_pt+1)*diff,  0., min+(i_pt+1)*diff, legylower) )
    return [line.DrawLineNDC(*l) for l in lines]

def drawObjects( isData, lumi_scale ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    addon = "post-fit" if args.postFit else "pre-fit"
    if "incl" in args.cardfile: addon += ", inclusive"
    lines = [
      (0.15, 0.945, "CMS Simulation (%s)"%addon) if not isData else ( (0.15, 0.945, "CMS (%s)"%addon) if not args.preliminary else (0.15, 0.945, "CMS #bf{#it{Preliminary}} #bf{(%s)}"%addon)),
      (0.84 if len(labels)>25 else legylower, 0.945, "#bf{%3.1f fb^{-1} (13 TeV)}"%lumi_scale )
    ]
    return [tex.DrawLatex(*l) for l in lines]

hMax = hists["total"].GetMaximum()
def setPTBinLabels( labels, fac=1. ):
    def setBinLabel( hist ):
        tex = ROOT.TLatex()
#        tex.SetNDC()
        tex.SetTextSize(ptlabelsize)
        tex.SetTextAlign(32)
        tex.SetTextAngle(90)
        dEntry = False
        for i in range(hist.GetNbinsX()):
            if dEntry:
                dEntry = False
                continue
            elif i == len(labels)-1 or labels[i] != labels[i+1] or crName[i] != crName[i+1]:
                x = 0.5 + hist.GetXaxis().GetBinUpEdge(i)#/hist.GetNbinsX()
                dEntry = False
            else:
                x = 0.5 + (hist.GetXaxis().GetBinUpEdge(i)+hist.GetXaxis().GetBinUpEdge(i+1))*0.5
                dEntry = True

            tex.DrawLatex( x, hMax*fac, labels[i] )
    return setBinLabel

drawObjects = drawObjects( isData=isData, lumi_scale=lumi_scale ) + boxes + drawDivisions() + drawPTDivisions()

# manual sorting
bkgHists.sort(key=lambda h: -h.Integral())
bkgHists.insert(0,histSig)

plots = [ bkgHists, [hists["data"]]]
plotName = "_".join( [ item for item in args.cardfile.split("_") if item not in ["addDYSF", "addMisIDSF", "misIDPOI"] ] )
add      = "_".join( [ item for item in args.cardfile.split("_") if item in ["addDYSF", "addMisIDSF", "misIDPOI"] ] )
fit      = "postFit" if args.postFit else "preFit"
if add: fit += "_"+add

for log in [True, False]:
    heightFactor = heightFactor if log else 1.5
    plotting.draw(
        Plot.fromHisto(plotName,
                plots,
                texX = "",
                texY = "Number of Events",
            ),
        plot_directory = os.path.join(plot_directory, "controlRegions", str(args.year), fit, "log" if log else "lin"),
        logX = False, logY = log, sorting = False, 
        #legend = (0.75,0.80-0.010*32, 0.95, 0.80),
        legend = [ (0.2,legylower,0.9,0.9), legcolumns ],
        widths = {"x_width":padwidth, "y_width":padheight, "y_ratio_width":padratio},
        yRange = (0.7,hMax*heightFactor),
        #yRange = (0.03, [0.001,0.5]),
        ratio = {"yRange": (0.11, 1.89), "texY":"Data/MC", "histos":[(1,0)], "drawObjects":ratio_boxes, #+ drawLabelsLower( regions ) +drawHeadlineLower( regions ) + drawDivisionsLower(regions),
                "histModifications": [lambda h: h.GetYaxis().SetTitleSize(textsize), lambda h: h.GetYaxis().SetLabelSize(ylabelsize), lambda h: h.GetYaxis().SetTitleOffset(textoffset), lambda h: h.GetXaxis().SetTitleSize(textsize), lambda h: h.GetXaxis().SetLabelSize(xlabelsize), lambda h: h.GetXaxis().SetLabelOffset(0.035)]} ,
        drawObjects = drawObjects,
        histModifications = [lambda h: h.GetYaxis().SetTitleSize(textsize), lambda h: h.GetYaxis().SetLabelSize(ylabelsize), lambda h: h.GetYaxis().SetTitleOffset(textoffset), setPTBinLabels(ptLabels,fac=offsetfactor if log else 1.2)],
        #canvasModifications = [ lambda c : c.SetLeftMargin(0.08), lambda c : c.GetPad(2).SetLeftMargin(0.08), lambda c : c.GetPad(1).SetLeftMargin(0.08), lambda c: c.GetPad(2).SetBottomMargin(0.60), lambda c : c.GetPad(1).SetRightMargin(0.03), lambda c: c.GetPad(2).SetRightMargin(0.03) ],
        copyIndexPHP = True,
    )

