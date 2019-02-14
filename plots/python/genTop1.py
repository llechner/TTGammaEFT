#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
genTop1 = []
    
genTop1.append( Plot(
    name      = 'genTop1_pt',
    texX      = 'p_{T}(gen t_{1}) (GeV)',
    texY      = 'Number of Events / 20 GeV',
    attribute = lambda event, sample: event.GenTop_pt[1],
    binning   = [ 20, 0, 400 ],
))

genTop1.append( Plot(
    name      = 'genTop1_eta',
    texX      = '#eta(gen t_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenTop_eta[1],
    binning   = [ 20, -5, 5 ],
))

genTop1.append( Plot(
    name      = 'genTop1_absEta',
    texX      = '|#eta|(gen t_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.GenTop_eta[1]),
    binning   = [ 10, 0, 5 ],
))

genTop1.append( Plot(
    name      = 'genTop1_phi',
    texX      = '#phi(gen t_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenTop_phi[1],
    binning   = [ 10, -pi, pi ],
))
