#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
photonGood0 = []
    
photonGood0.append( Plot(
    name      = 'photonGood0_pt',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = TreeVariable.fromString( "PhotonGood0_pt/F" ),
    binning   = [ 19, 20, 115 ],
))

photonGood0.append( Plot(
    name      = 'photonGood0_pt_EFT',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 100 GeV',
    attribute = TreeVariable.fromString( "PhotonGood0_pt/F" ),
    binning   = [ 5, 20, 520 ],
))

photonGood0.append( Plot(
    name      = 'photonGood0_eta',
    texX      = '#eta(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "PhotonGood0_eta/F" ),
    binning   = [ 24, -1.5, 1.5 ],
))

photonGood0.append( Plot(
    name      = 'photonGood0_phi',
    texX      = '#phi(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "PhotonGood0_phi/F" ),
    binning   = [ 10, -pi, pi ],
))

photonGood0.append( Plot(
    name      = 'photonGood0_category',
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "PhotonGood0_photonCat/I" ),
    binning   = [ 4, 0, 4 ],
))

photonGood0.append( Plot(
    name      = 'photonGood0_category_0nPV20',
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_photonCat if event.PV_npvsGood < 20 else -999,
    binning   = [ 4, 0, 4 ],
))

photonGood0.append( Plot(
    name      = 'photonGood0_category_20nPV60',
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_photonCat if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 else -999,
    binning   = [ 4, 0, 4 ],
))


photonGood0.append( Plot(
    name      = 'photonGood0_category_60nPVinf',
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_photonCat if event.PV_npvsGood >= 60 else -999,
    binning   = [ 4, 0, 4 ],
))


photonGood0.append( Plot(
    name      = 'photonGood0_category_20ptG120',
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_photonCat if event.PhotonGood0_pt >= 20 and event.PhotonGood0_pt < 120 else -999,
    binning   = [ 4, 0, 4 ],
))

photonGood0.append( Plot(
    name      = 'photonGood0_category_120ptG220',
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_photonCat if event.PhotonGood0_pt >= 120 and event.PhotonGood0_pt < 220 else -999,
    binning   = [ 4, 0, 4 ],
))


photonGood0.append( Plot(
    name      = 'photonGood0_category_220ptGinf',
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_photonCat if event.PhotonGood0_pt >= 220 else -999,
    binning   = [ 4, 0, 4 ],
))

