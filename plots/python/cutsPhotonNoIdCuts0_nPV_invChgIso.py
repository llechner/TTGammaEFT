#!/usr/bin/env python
''' Define list of plots for plot script
'''
# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
cutsPhotonNoIdCuts0_nPV_invChgIso = []
    
cutsPhotonNoIdCuts0_nPV_invChgIso.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invChgIso_sieie_0nPV20',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_sieie if event.PV_npvsGood < 20 and event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt > 1.141 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_nPV_invChgIso.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invChgIso_sieie_20nPV60',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_sieie if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt > 1.141 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_nPV_invChgIso.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invChgIso_sieie_60nPVinf',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_sieie if event.PV_npvsGood >= 60 and event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt > 1.141 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))


cutsPhotonNoIdCuts0_nPV_invChgIso.append( Plot(
    name      = 'PhotonNoChgIso0_invChgIso_sieie_0nPV20',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_sieie if event.PV_npvsGood < 20 and event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt > 1.141 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_nPV_invChgIso.append( Plot(
    name      = 'PhotonNoChgIso0_invChgIso_sieie_20nPV60',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_sieie if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt > 1.141 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_nPV_invChgIso.append( Plot(
    name      = 'PhotonNoChgIso0_invChgIso_sieie_60nPVinf',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_sieie if event.PV_npvsGood >= 60 and event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt > 1.141 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))


