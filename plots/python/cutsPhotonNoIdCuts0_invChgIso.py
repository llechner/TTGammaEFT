#!/usr/bin/env python
''' Define list of plots for plot script
'''
# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
cutsPhotonNoIdCuts0_invChgIso = []
    
cutsPhotonNoIdCuts0_invChgIso.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invChgIso_pt',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt > 1.141 else -999,
    binning   = [ 19, 20, 115 ],
))

cutsPhotonNoIdCuts0_invChgIso.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invChgIso_eta',
    texX      = '#eta(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_eta if event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt > 1.141 else -999,
    binning   = [ 24, -1.5, 1.5 ],
))

cutsPhotonNoIdCuts0_invChgIso.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invChgIso_phi',
    texX      = '#phi(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_phi if event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt > 1.141 else -999,
    binning   = [ 10, -pi, pi ],
))

cutsPhotonNoIdCuts0_invChgIso.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invChgIso_category',
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_photonCat if event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt > 1.141 else -999,
    binning   = [ 4, 0, 4 ],
))

cutsPhotonNoIdCuts0_invChgIso.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invChgIso_sieie',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_sieie if event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt > 1.141 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))



cutsPhotonNoIdCuts0_invChgIso.append( Plot(
    name      = 'PhotonNoChgIso0_invChgIso_pt',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt > 1.141 else -999,
    binning   = [ 19, 20, 115 ],
))

cutsPhotonNoIdCuts0_invChgIso.append( Plot(
    name      = 'PhotonNoChgIso0_invChgIso_eta',
    texX      = '#eta(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_eta if event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt > 1.141 else -999,
    binning   = [ 24, -1.5, 1.5 ],
))

cutsPhotonNoIdCuts0_invChgIso.append( Plot(
    name      = 'PhotonNoChgIso0_invChgIso_phi',
    texX      = '#phi(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_phi if event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt > 1.141 else -999,
    binning   = [ 10, -pi, pi ],
))

cutsPhotonNoIdCuts0_invChgIso.append( Plot(
    name      = 'PhotonNoChgIso0_invChgIso_category',
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_photonCat if event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt > 1.141 else -999,
    binning   = [ 4, 0, 4 ],
))


cutsPhotonNoIdCuts0_invChgIso.append( Plot(
    name      = 'PhotonNoChgIso0_invChgIso_sieie',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_sieie if event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt > 1.141 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))


