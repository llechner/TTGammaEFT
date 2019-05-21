#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
cutsPhotonMVA0 = []
    
cutsPhotonMVA0.append( Plot(
    name      = 'PhotonMVA0_hoe',
    texX      = 'H/E(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonMVA0_hoe,
    binning   = [ 20, 0, 0.05 ],
))

cutsPhotonMVA0.append( Plot(
    name      = 'PhotonMVA0_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonMVA0_pfRelIso03_chg,
    binning   = [ 20, 0, 0.03 ],
))

cutsPhotonMVA0.append( Plot(
    name      = 'PhotonMVA0_pfRelIso03_all',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonMVA0_pfRelIso03_all,
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonMVA0.append( Plot(
    name      = 'PhotonMVA0_sieie',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonMVA0_sieie,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonMVA0.append( Plot(
    name      = 'PhotonMVA0_pfIso03_all',
    texX      = 'Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonMVA0_pfRelIso03_all * event.PhotonMVA0_pt,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonMVA0.append( Plot(
    name      = 'PhotonMVA0_pfIso03_chg_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonMVA0_pfRelIso03_chg * event.PhotonMVA0_pt,
    binning   = [ 20, 0, 1.2 ],
))

cutsPhotonMVA0.append( Plot(
    name      = 'PhotonMVA0_pfIso03_chg',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonMVA0_pfRelIso03_chg * event.PhotonMVA0_pt,
    binning   = [ 50, 0, 1.2 ],
))

cutsPhotonMVA0.append( Plot(
    name      = 'PhotonMVA0_pfIso03_chg_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonMVA0_pfRelIso03_chg * event.PhotonMVA0_pt,
    binning   = [ 20, 0, 20 ],
))

cutsPhotonMVA0.append( Plot(
    name      = 'PhotonMVA0_pfIso03_n',
    texX      = 'neutral Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonMVA0_pfRelIso03_all - event.PhotonMVA0_pfRelIso03_chg) * event.PhotonMVA0_pt,
    binning   = [ 20, 0, 5 ],
))

