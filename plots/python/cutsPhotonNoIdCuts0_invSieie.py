#!/usr/bin/env python
''' Define list of plots for plot script
'''
# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
cutsPhotonNoIdCuts0_invSieie = []
    
cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pt',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_sieie > 0.011 else -999,
    binning   = [ 19, 20, 115 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_eta',
    texX      = '#eta(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_eta if event.PhotonNoChgIsoNoSieie0_sieie > 0.011 else -999,
    binning   = [ 24, -1.5, 1.5 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_phi',
    texX      = '#phi(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_phi if event.PhotonNoChgIsoNoSieie0_sieie > 0.011 else -999,
    binning   = [ 10, -pi, pi ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_category',
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_photonCat if event.PhotonNoChgIsoNoSieie0_sieie > 0.011 else -999,
    binning   = [ 4, 0, 4 ],
))



cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pt',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = lambda event, sample: event.PhotonNoSieie0_pt if event.PhotonNoSieie0_sieie > 0.011 else -999,
    binning   = [ 19, 20, 115 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_eta',
    texX      = '#eta(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_eta if event.PhotonNoSieie0_sieie > 0.011 else -999,
    binning   = [ 24, -1.5, 1.5 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_phi',
    texX      = '#phi(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_phi if event.PhotonNoSieie0_sieie > 0.011 else -999,
    binning   = [ 10, -pi, pi ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_category',
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_photonCat if event.PhotonNoSieie0_sieie > 0.011 else -999,
    binning   = [ 4, 0, 4 ],
))


cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_sieie',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_sieie if event.PhotonNoChgIsoNoSieie0_sieie > 0.011 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg if event.PhotonNoChgIsoNoSieie0_sieie > 0.011 else -999,
    binning   = [ 20, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfRelIso03_n',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIsoNoSieie0_pfRelIso03_all - event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg) if event.PhotonNoChgIsoNoSieie0_sieie > 0.011 else -999,
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfRelIso03_all',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_all if event.PhotonNoChgIsoNoSieie0_sieie > 0.011 else -999,
    binning   = [ 20, 0, 0.2 ],
))



cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_sieie',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_sieie if event.PhotonNoSieie0_sieie > 0.011 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg if event.PhotonNoSieie0_sieie > 0.011 else -999,
    binning   = [ 20, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfRelIso03_n',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoSieie0_pfRelIso03_all - event.PhotonNoSieie0_pfRelIso03_chg) if event.PhotonNoSieie0_sieie > 0.011 else -999,
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfRelIso03_all',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_all if event.PhotonNoSieie0_sieie > 0.011 else -999,
    binning   = [ 20, 0, 0.2 ],
))






cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_all',
    texX      = 'Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_all * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_sieie > 0.011 else -999,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_sieie > 0.011 else -999,
    binning   = [ 20, 0, 1.2 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_sieie > 0.011 else -999,
    binning   = [ 50, 0, 1.2 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_sieie > 0.011 else -999,
    binning   = [ 20, 0, 20 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg_wide_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_sieie > 0.011 else -999,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_n',
    texX      = 'neutral Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIsoNoSieie0_pfRelIso03_all - event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg) * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_sieie > 0.011 else -999,
    binning   = [ 20, 0, 5 ],
))






cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfIso03_all',
    texX      = 'Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_all * event.PhotonNoSieie0_pt if event.PhotonNoSieie0_sieie > 0.011 else -999,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfIso03_chg',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg * event.PhotonNoSieie0_pt if event.PhotonNoSieie0_sieie > 0.011 else -999,
    binning   = [ 50, 0, 1.2 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfIso03_chg_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg * event.PhotonNoSieie0_pt if event.PhotonNoSieie0_sieie > 0.011 else -999,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfIso03_chg_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg * event.PhotonNoSieie0_pt if event.PhotonNoSieie0_sieie > 0.011 else -999,
    binning   = [ 20, 0, 1.2 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfIso03_chg_wide_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg * event.PhotonNoSieie0_pt if event.PhotonNoSieie0_sieie > 0.011 else -999,
    binning   = [ 20, 0, 20 ],
))

cutsPhotonNoIdCuts0_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfIso03_n',
    texX      = 'neutral Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoSieie0_pfRelIso03_all - event.PhotonNoSieie0_pfRelIso03_chg) * event.PhotonNoSieie0_pt if event.PhotonNoSieie0_sieie > 0.011 else -999,
    binning   = [ 20, 0, 5 ],
))

