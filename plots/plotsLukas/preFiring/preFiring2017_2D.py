''' Plot script pTG shape + WC
'''

# Standard imports 
import sys, os, pickle, copy, ROOT, itertools

from math import pi

# RootTools
from RootTools.core.standard   import *

# turn off graphics
ROOT.gROOT.SetBatch( True )

# TTGammaEFT
from TTGammaEFT.Tools.user              import plot_directory
from TTGammaEFT.Tools.cutInterpreter    import cutInterpreter

from Analysis.Tools.metFilters          import getFilterCut

# Default Parameter
loggerChoices = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO', nargs='?', choices=loggerChoices,                                help="Log level for logging")
argParser.add_argument('--plot_directory',     action='store',      default='80X_TTG_ppv1_v1')
argParser.add_argument('--selection',          action='store',      default='dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p')
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

# Text on the plots
def drawObjects( lumi_scale ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS #bf{#it{Preliminary}}'),
      (0.65, 0.95, '%3.1f fb{}^{-1} (13 TeV)' % lumi_scale),
    ]
    return [tex.DrawLatex(*l) for l in lines] 

#scaling = { 1:0 }
scaling = { 0:1 }

# 2017 Samples
from TTGammaEFT.Samples.nanoTuples_Run2017_preFiring_postProcessed import *

Run2017.texName = "data"
Run2017.name    = "data"
Run2017.style   = styles.errorStyle( ROOT.kBlue )#styles.fillStyle( ROOT.kOrange-3 )

Run2017_noPreFiring = copy.deepcopy(Run2017)
Run2017_noPreFiring.texName = "data (unprefirable)"
Run2017_noPreFiring.name    = "data_unprefireable"
Run2017_noPreFiring.style   = styles.errorStyle( ROOT.kBlack )

lumi_scale = Run2017.lumi * 0.001
allSamples = [ Run2017, Run2017_noPreFiring ]

eventNorm = 1
if args.small:
    for sample in [ Run2017_noPreFiring, Run2017 ]:
        sample.normalization=1.
        sample.reduceFiles( factor=15 )
        eventNorm = 1./sample.normalization



from TTGammaEFT.Analysis.regions import preFiringSumJetEta
from TTGammaEFT.Analysis.regions import preFiringSumJetPtLog
from TTGammaEFT.Analysis.Region  import texString

allRegions = [\
              ( preFiringSumJetEta, -5, 5 ), 
              ( preFiringSumJetPtLog,  30, 1000 ), 
             ]


allModes = [ 'mumu', 'mue', 'ee' ]
allPlots = {}

selection    = cutInterpreter.cutString( args.selection )
addSelection = "Jet_pt>30&&Jet_cleanmask"
metFilter    = getFilterCut( 2017, isData=True )

ptMinVal  = 30
ptMaxVal  = 1000
etaMinVal = -5
etaMaxVal = 5

variableString = "Jet_pt:Jet_eta"
ptBinning  = [ val0 for region in preFiringSumJetPtLog for val0, val1 in region.vals.values() ] + [ptMaxVal]
etaBinning = [ val0 for region in preFiringSumJetEta   for val0, val1 in region.vals.values() ] + [etaMaxVal]
binning = (etaBinning, ptBinning)

for index, mode in enumerate( allModes ):

    ratio = {}
    leptonSelection = cutInterpreter.cutString( mode )
    totalSelection  = [ metFilter, leptonSelection, selection, addSelection ]
    
    Run2017_noPreFiring.setSelectionString( totalSelection + [ "unPreFirableEvent==1"] )
    Run2017.setSelectionString( totalSelection )

#    r17      = Run2017.getEventList().GetN() * eventNorm
    npfHist = Run2017_noPreFiring.get2DHistoFromDraw( variableString, binning, weightString=str(eventNorm), binningIsExplicit = True )
    hist    = Run2017.get2DHistoFromDraw( variableString, binning, weightString=str(eventNorm), binningIsExplicit = True )

    cans = ROOT.TCanvas("can","",500,500)

    pads = ROOT.TPad("pad","",0.,0.,1.,1.)
    pads.SetRightMargin(0.20)
    pads.SetLeftMargin(0.14)
    pads.SetTopMargin(0.11)
    pads.Draw()
    pads.cd()

    npfHist.Draw()    
    hist.Draw()    

    plot_directory_ = os.path.join( plot_directory, "prefiring2017" )
    plotname = "test"
    for e in [".png",".pdf",".root"]:
        cans.Print( plot_directory_ + "/%s%s"%(plotname, e) )

