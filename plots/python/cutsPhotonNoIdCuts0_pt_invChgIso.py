#!/usr/bin/env python
''' Define list of plots for plot script
'''
# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
cutsPhotonNoIdCuts0_pt_invChgIso = []
    
cutsPhotonNoIdCuts0_pt_invChgIso.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invChgIso_sieie_20ptG120',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_sieie if event.PhotonNoChgIsoNoSieie0_pt >= 20 and event.PhotonNoChgIsoNoSieie0_pt < 120 and event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt > 1.141 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_pt_invChgIso.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invChgIso_sieie_120ptG220',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_sieie if event.PhotonNoChgIsoNoSieie0_pt >= 120 and event.PhotonNoChgIsoNoSieie0_pt < 220 and event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt > 1.141 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_pt_invChgIso.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invChgIso_sieie_220ptGinf',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_sieie if event.PhotonNoChgIsoNoSieie0_pt >= 220 and event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt > 1.141 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))


cutsPhotonNoIdCuts0_pt_invChgIso.append( Plot(
    name      = 'PhotonNoChgIso0_invChgIso_sieie_20ptG120',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_sieie if event.PhotonNoChgIso0_pt >= 20 and event.PhotonNoChgIso0_pt < 120 and event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt > 1.141 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_pt_invChgIso.append( Plot(
    name      = 'PhotonNoChgIso0_invChgIso_sieie_120ptG220',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_sieie if event.PhotonNoChgIso0_pt >= 120 and event.PhotonNoChgIso0_pt < 220 and event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt > 1.141 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_pt_invChgIso.append( Plot(
    name      = 'PhotonNoChgIso0_invChgIso_sieie_220ptGinf',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_sieie if event.PhotonNoChgIso0_pt >= 220 and event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt > 1.141 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

