#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
PhotonMVA0 = []
    
PhotonMVA0.append( Plot(
    name      = 'PhotonMVA0_pt',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonMVA0_pt,
    binning   = [ 19, 20, 115 ],
))

PhotonMVA0.append( Plot(
    name      = 'PhotonMVA0_pt_EFT',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonMVA0_pt,
    binning   = [ 5, 20, 520 ],
))

PhotonMVA0.append( Plot(
    name      = 'PhotonMVA0_eta',
    texX      = '#eta(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonMVA0_eta,
    binning   = [ 24, -1.5, 1.5 ],
))

PhotonMVA0.append( Plot(
    name      = 'PhotonMVA0_phi',
    texX      = '#phi(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonMVA0_phi,
    binning   = [ 10, -pi, pi ],
))

PhotonMVA0.append( Plot(
    name      = 'PhotonMVA0_mvaID',
    texX      = 'MVA ID(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonMVA0_mvaID,
    binning   = [ 20, -1, 1 ],
))

