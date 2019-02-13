#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
photon1 = []
    
photon1.append( Plot(
    name      = 'photon1_pt',
    texX      = 'p_{T}(#gamma_{1}) (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = lambda event, sample: event.Photon_pt[1] if event.nPhoton > 1 else -999,
    binning   = [ 19, 20, 115 ],
))

photon1.append( Plot(
    name      = 'photon1_eta',
    texX      = '#eta(#gamma_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_eta[1] if event.nPhoton > 1 else -999,
    binning   = [ 24, -4, 4 ],
))

photon1.append( Plot(
    name      = 'photon1_absEta',
    texX      = '|#eta|(#gamma_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.Photon_eta[1]) if event.nPhoton > 1 else -999,
    binning   = [ 9, 0, 4 ],
))

photon1.append( Plot(
    name      = 'photon1_phi',
    texX      = '#phi(#gamma_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_phi[1] if event.nPhoton > 1 else -999,
    binning   = [ 20, -pi, pi ],
))

