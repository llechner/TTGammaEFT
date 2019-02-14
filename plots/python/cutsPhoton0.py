#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
cutsPhoton0 = []
    
cutsPhoton0.append( Plot(
    name      = 'photon0_hoe',
    texX      = 'H/E(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_hoe[0],
    binning   = [ 50, 0, 0.05 ],
))

cutsPhoton0.append( Plot(
    name      = 'photon0_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_pfRelIso03_chg[0],
    binning   = [ 50, 0, 0.4 ],
))

cutsPhoton0.append( Plot(
    name      = 'photon0_pfRelIso03_all',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_pfRelIso03_all[0],
    binning   = [ 50, 0, 0.4 ],
))

