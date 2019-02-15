#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
genPhoton0 = []
    
genPhoton0.append( Plot(
    name      = 'genPhoton0_pt',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = lambda event, sample: event.GenPhoton_pt[0],
    binning   = [ 19, 20, 115 ],
))

genPhoton0.append( Plot(
    name      = 'genPhoton0_pt_EFT',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 100 GeV',
    attribute = lambda event, sample: event.GenPhoton_pt[0],
    binning   = [ 5, 20, 520 ],
))

genPhoton0.append( Plot(
    name      = 'genPhoton0_eta',
    texX      = '#eta(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenPhoton_eta[0],
    binning   = [ 24, -1.8, 1.8 ],
))

genPhoton0.append( Plot(
    name      = 'genPhoton0_phi',
    texX      = '#phi(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenPhoton_phi[0],
    binning   = [ 10, -pi, pi ],
))

