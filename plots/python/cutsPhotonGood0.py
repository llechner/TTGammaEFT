#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
cutsPhotonGood0 = []
    
cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_hoe',
    texX      = 'H/E(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "PhotonGood0_hoe/F" ),
    binning   = [ 20, 0, 0.05 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "PhotonGood0_pfRelIso03_chg/F" ),
    binning   = [ 20, 0, 0.03 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_pfRelIso03_all',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "PhotonGood0_pfRelIso03_all/F" ),
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_sieie',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "PhotonGood0_sieie/F" ),
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_r9',
    texX      = 'R9(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "PhotonGood0_r9/F" ),
    binning   = [ 80, 0, 1 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_r9_coarse',
    texX      = 'R9(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "PhotonGood0_r9/F" ),
    binning   = [ 20, 0, 1 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_pfIso03_all',
    texX      = 'Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_pfRelIso03_all * event.PhotonGood0_pt,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_pfIso03_chg',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_pfRelIso03_chg * event.PhotonGood0_pt,
    binning   = [ 20, 0, 1.2 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_pfIso03_chg_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_pfRelIso03_chg * event.PhotonGood0_pt,
    binning   = [ 20, 0, 20 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_pfIso03_n',
    texX      = 'neutral Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonGood0_pfRelIso03_all - event.PhotonGood0_pfRelIso03_chg) * event.PhotonGood0_pt,
    binning   = [ 20, 0, 5 ],
))

