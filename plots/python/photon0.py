#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
photon0 = []
    
photon0.append( Plot(
    name      = 'photon0_pt',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = lambda event, sample: event.Photon_pt[0],
    binning   = [ 19, 20, 115 ],
))

photon0.append( Plot(
    name      = 'photon0_eta',
    texX      = '#eta(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_eta[0],
    binning   = [ 24, -4, 4 ],
))

photon0.append( Plot(
    name      = 'photon0_phi',
    texX      = '#phi(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_phi[0],
    binning   = [ 10, -pi, pi ],
))

