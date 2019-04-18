#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi
import copy

# RootTools
from RootTools.core.standard          import *

from TTGammaEFT.plots.cutsPhotonGood0          import cutsPhotonGood0
from TTGammaEFT.plots.cutsPhotonNoIdCuts0      import cutsPhotonNoIdCuts0
from TTGammaEFT.plots.cutsPhotonNoIdCuts0_nPV  import cutsPhotonNoIdCuts0_nPV
from TTGammaEFT.plots.cutsPhotonNoIdCuts0_pt   import cutsPhotonNoIdCuts0_pt
from TTGammaEFT.plots.cutsPhotonNoIdCuts0_invSieie  import cutsPhotonNoIdCuts0_invSieie
from TTGammaEFT.plots.cutsPhotonNoIdCuts0_invSieie_nPV  import cutsPhotonNoIdCuts0_invSieie_nPV
from TTGammaEFT.plots.cutsPhotonNoIdCuts0_invSieie_pt   import cutsPhotonNoIdCuts0_invSieie_pt

# plotList
plotListData  = []

plotListData += cutsPhotonGood0
plotListData += cutsPhotonNoIdCuts0
plotListData += cutsPhotonNoIdCuts0_nPV
plotListData += cutsPhotonNoIdCuts0_pt
plotListData += cutsPhotonNoIdCuts0_invSieie
plotListData += cutsPhotonNoIdCuts0_invSieie_nPV
plotListData += cutsPhotonNoIdCuts0_invSieie_pt

plotListDataMC  = copy.copy(plotListData)

