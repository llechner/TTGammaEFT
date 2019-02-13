#!/usr/bin/env python
''' Define list of plots for plot script
'''
# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
cutsPhotonNoIdCuts0_nPV = []
    
cutsPhotonNoIdCuts0_nPV.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_chg_0nPV10',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg if event.PV_npvsGood >= 0 and event.PV_npvsGood < 10 else -999,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0_nPV.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_chg_10nPV20',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg if event.PV_npvsGood >= 10 and event.PV_npvsGood < 20 else -999,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0_nPV.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_chg_20nPV30',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg if event.PV_npvsGood >= 20 and event.PV_npvsGood < 30 else -999,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0_nPV.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_chg_30nPV40',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg if event.PV_npvsGood >= 30 and event.PV_npvsGood < 40 else -999,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0_nPV.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_chg_40nPVinf',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg if event.PV_npvsGood >= 40 else -999,
    binning   = [ 50, 0, 20 ],
))



cutsPhotonNoIdCuts0_nPV.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_chg_0nPV10',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg if event.PV_npvsGood >= 0 and event.PV_npvsGood < 10 else -999,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0_nPV.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_chg_10nPV20',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg if event.PV_npvsGood >= 10 and event.PV_npvsGood < 20 else -999,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0_nPV.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_chg_20nPV30',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg if event.PV_npvsGood >= 20 and event.PV_npvsGood < 30 else -999,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0_nPV.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_chg_30nPV40',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg if event.PV_npvsGood >= 30 and event.PV_npvsGood < 40 else -999,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0_nPV.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_chg_40nPVinf',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg if event.PV_npvsGood >= 40 else -999,
    binning   = [ 50, 0, 20 ],
))


