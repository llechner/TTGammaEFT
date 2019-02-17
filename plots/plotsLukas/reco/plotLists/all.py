#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

from TTGammaEFT.plots.beam import beam
from TTGammaEFT.plots.bjetGood0 import bjetGood0
from TTGammaEFT.plots.bjetGood1 import bjetGood1
from TTGammaEFT.plots.checksGood import checksGood
from TTGammaEFT.plots.cutsJet0 import cutsJet0
from TTGammaEFT.plots.cutsJet1 import cutsJet1
from TTGammaEFT.plots.cutsJetGood0 import cutsJetGood0
from TTGammaEFT.plots.cutsJetGood1 import cutsJetGood1
from TTGammaEFT.plots.cutsLepton0 import cutsLepton0
from TTGammaEFT.plots.cutsLepton1 import cutsLepton1
from TTGammaEFT.plots.cutsLeptonGood0 import cutsLeptonGood0
from TTGammaEFT.plots.cutsLeptonGood1 import cutsLeptonGood1
from TTGammaEFT.plots.cutsLeptonTight0 import cutsLeptonTight0
from TTGammaEFT.plots.cutsLeptonTight1 import cutsLeptonTight1
from TTGammaEFT.plots.cutsPhoton0 import cutsPhoton0
from TTGammaEFT.plots.cutsPhotonGood0 import cutsPhotonGood0
from TTGammaEFT.plots.cutsPhotonNoIdCuts0 import cutsPhotonNoIdCuts0
from TTGammaEFT.plots.cutsPhotonNoIdCuts0_nPV import cutsPhotonNoIdCuts0_nPV
from TTGammaEFT.plots.ht import ht
from TTGammaEFT.plots.isolationGood import isolationGood
from TTGammaEFT.plots.isolationTight import isolationTight
from TTGammaEFT.plots.jet0 import jet0
from TTGammaEFT.plots.jet1 import jet1
from TTGammaEFT.plots.jetGood0 import jetGood0
from TTGammaEFT.plots.jetGood1 import jetGood1
from TTGammaEFT.plots.lepton0 import lepton0
from TTGammaEFT.plots.lepton1 import lepton1
from TTGammaEFT.plots.leptonGood0 import leptonGood0
from TTGammaEFT.plots.leptonGood1 import leptonGood1
from TTGammaEFT.plots.leptonTight0 import leptonTight0
from TTGammaEFT.plots.leptonTight1 import leptonTight1
from TTGammaEFT.plots.massGood import massGood
from TTGammaEFT.plots.massTight import massTight
from TTGammaEFT.plots.met import met
from TTGammaEFT.plots.metSig import metSig
from TTGammaEFT.plots.mll import mll
from TTGammaEFT.plots.multiplicity import multiplicity
from TTGammaEFT.plots.multiplicityGood import multiplicityGood
from TTGammaEFT.plots.multiplicityGoodNoPhoton import multiplicityGoodNoPhoton
from TTGammaEFT.plots.multiplicityNoPhoton import multiplicityNoPhoton
from TTGammaEFT.plots.photon0 import photon0
from TTGammaEFT.plots.photon1 import photon1
from TTGammaEFT.plots.photonGood0 import photonGood0
from TTGammaEFT.plots.photonGood1 import photonGood1

# plotList
plotListData  = []

plotListData += beam
plotListData += bjetGood0
plotListData += bjetGood1
plotListData += checksGood
plotListData += cutsJet0
plotListData += cutsJet1
#plotListData += cutsJetGood0
#plotListData += cutsJetGood1
plotListData += cutsLepton0
plotListData += cutsLepton1
plotListData += cutsLeptonGood0
plotListData += cutsLeptonGood1
plotListData += cutsLeptonTight0
plotListData += cutsLeptonTight1
plotListData += cutsPhoton0
plotListData += cutsPhotonGood0
plotListData += cutsPhotonNoIdCuts0
plotListData += cutsPhotonNoIdCuts0_nPV
plotListData += ht
plotListData += isolationGood
plotListData += isolationTight
plotListData += jet0
plotListData += jet1
#plotListData += jetGood0
#plotListData += jetGood1
plotListData += lepton0
plotListData += lepton1
plotListData += leptonGood0
plotListData += leptonGood1
plotListData += leptonTight0
plotListData += leptonTight1
plotListData += massGood
plotListData += massTight
plotListData += met
plotListData += metSig
plotListData += mll
plotListData += multiplicity
plotListData += multiplicityGood
plotListData += multiplicityGoodNoPhoton
plotListData += multiplicityNoPhoton
plotListData += photon0
plotListData += photon1
plotListData += photonGood0
plotListData += photonGood1
plotListDataMC = plotListData
