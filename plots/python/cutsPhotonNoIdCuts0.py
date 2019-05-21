#!/usr/bin/env python
''' Define list of plots for plot script
'''
# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
cutsPhotonNoIdCuts0 = []
    
cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_sieie',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_sieie,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg,
    binning   = [ 20, 0, 0.03 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_n',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIsoNoSieie0_pfRelIso03_all - event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg),
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_all',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_all,
    binning   = [ 20, 0, 0.2 ],
))



cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIso0_sieie',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_sieie,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg,
    binning   = [ 20, 0, 0.03 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_n',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIso0_pfRelIso03_all - event.PhotonNoChgIso0_pfRelIso03_chg),
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_all',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_all,
    binning   = [ 20, 0, 0.2 ],
))



cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoSieie0_sieie',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_sieie,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoSieie0_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg,
    binning   = [ 20, 0, 0.03 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoSieie0_pfRelIso03_n',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoSieie0_pfRelIso03_all - event.PhotonNoSieie0_pfRelIso03_chg),
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoSieie0_pfRelIso03_all',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_all,
    binning   = [ 20, 0, 0.2 ],
))






cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_all',
    texX      = 'Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_all * event.PhotonNoChgIsoNoSieie0_pt,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_all',
    texX      = 'Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_all * event.PhotonNoChgIso0_pt,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_chg_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt,
    binning   = [ 20, 0, 1.2 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_chg',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt,
    binning   = [ 50, 0, 1.2 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_chg_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt,
    binning   = [ 20, 0, 20 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_chg_wide_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_chg',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt,
    binning   = [ 50, 0, 1.2 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_chg_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt,
    binning   = [ 20, 0, 1.2 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_chg_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_chg_wide_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt,
    binning   = [ 20, 0, 20 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_n',
    texX      = 'neutral Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIsoNoSieie0_pfRelIso03_all - event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg) * event.PhotonNoChgIsoNoSieie0_pt,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_n',
    texX      = 'neutral Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIso0_pfRelIso03_all - event.PhotonNoChgIso0_pfRelIso03_chg) * event.PhotonNoChgIso0_pt,
    binning   = [ 20, 0, 5 ],
))







cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoSieie0_pfIso03_all',
    texX      = 'Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_all * event.PhotonNoSieie0_pt,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoSieie0_pfIso03_chg',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg * event.PhotonNoSieie0_pt,
    binning   = [ 50, 0, 1.2 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoSieie0_pfIso03_chg_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg * event.PhotonNoSieie0_pt,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoSieie0_pfIso03_chg_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg * event.PhotonNoSieie0_pt,
    binning   = [ 20, 0, 1.2 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoSieie0_pfIso03_chg_wide_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg * event.PhotonNoSieie0_pt,
    binning   = [ 20, 0, 20 ],
))

cutsPhotonNoIdCuts0.append( Plot(
    name      = 'PhotonNoSieie0_pfIso03_n',
    texX      = 'neutral Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoSieie0_pfRelIso03_all - event.PhotonNoSieie0_pfRelIso03_chg) * event.PhotonNoSieie0_pt,
    binning   = [ 20, 0, 5 ],
))

