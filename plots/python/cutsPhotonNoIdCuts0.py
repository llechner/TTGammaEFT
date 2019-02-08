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
cutsPhotonNoIdCuts0 = []
    
cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_sieie',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_sieie,
    binning   = [ 50, 0, 0.025 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_chg_coarse',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg,
    binning   = [ 20, 0, 20 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_chg_coarse',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg,
    binning   = [ 20, 0, 20 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_chg_low',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg,
    binning   = [ 20, 0, 2 ],
))
