#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# TTGammaEFT
from TTGammaEFT.Tools.constants       import defaultValue

# plotList
cutsPhotonGood0 = []
    
cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_hoe',
    texX      = 'H/E(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_hoe if event.nPhotonGood > 0 else defaultValue,
    binning   = [ 50, 0, 0.05 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_pfRelIso03_chg if event.nPhotonGood > 0 else defaultValue,
    binning   = [ 50, 0, 0.4 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_pfRelIso03_all',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_pfRelIso03_all if event.nPhotonGood > 0 else defaultValue,
    binning   = [ 50, 0, 0.4 ],
))
