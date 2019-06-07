#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi
import copy

# RootTools
from RootTools.core.standard          import *

from TTGammaEFT.plots.cutsPhotonNoIdCuts0_invChgIso  import cutsPhotonNoIdCuts0_invChgIso
from TTGammaEFT.plots.cutsPhotonNoIdCuts0_nPV_invChgIso  import cutsPhotonNoIdCuts0_nPV_invChgIso
from TTGammaEFT.plots.cutsPhotonNoIdCuts0_pt_invChgIso   import cutsPhotonNoIdCuts0_pt_invChgIso

from TTGammaEFT.plots.cutsPhotonNoIdCuts0_invSieie  import cutsPhotonNoIdCuts0_invSieie
from TTGammaEFT.plots.cutsPhotonNoIdCuts0_nPV_invSieie  import cutsPhotonNoIdCuts0_nPV_invSieie
from TTGammaEFT.plots.cutsPhotonNoIdCuts0_pt_invSieie   import cutsPhotonNoIdCuts0_pt_invSieie

# plotList
plotListData  = []

plotListData += cutsPhotonNoIdCuts0_invChgIso
plotListData += cutsPhotonNoIdCuts0_nPV_invChgIso
plotListData += cutsPhotonNoIdCuts0_pt_invChgIso

plotListData += cutsPhotonNoIdCuts0_invSieie
plotListData += cutsPhotonNoIdCuts0_nPV_invSieie
plotListData += cutsPhotonNoIdCuts0_pt_invSieie

plotListDataMC  = copy.copy(plotListData)

