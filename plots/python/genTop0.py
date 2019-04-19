#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
genTop0 = []
    
genTop0.append( Plot(
    name      = 'genTop0_pt',
    texX      = 'p_{T}(gen t_{0}) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenTop_pt[0],
    binning   = [ 20, 0, 400 ],
))

genTop0.append( Plot(
    name      = 'genTop0_eta',
    texX      = '#eta(gen t_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenTop_eta[0],
    binning   = [ 20, -5, 5 ],
))

genTop0.append( Plot(
    name      = 'genTop0_phi',
    texX      = '#phi(gen t_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenTop_phi[0],
    binning   = [ 10, -pi, pi ],
))
