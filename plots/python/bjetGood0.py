#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
bjetGood0 = []
    
bjetGood0.append( Plot(
    name      = 'bjetGood0_pt',
    texX      = 'p_{T}(b_{0}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.Bj0_pt if event.nBTagGood > 0 else -999,
    binning   = [ 20, 0, 200 ],
))

bjetGood0.append( Plot(
    name      = 'bjetGood0_eta',
    texX      = '#eta(b_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Bj0_eta if event.nBTagGood > 0 else -999,
    binning   = [ 20, -5, 5 ],
))

bjetGood0.append( Plot(
    name      = 'bjetGood0_absEta',
    texX      = '|#eta|(b_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.Bj0_eta) if event.nBTagGood > 0 else -999,
    binning   = [ 10, 0, 5 ],
))

bjetGood0.append( Plot(
    name      = 'bjetGood0_phi',
    texX      = '#phi(b_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Bj0_phi if event.nBTagGood > 0 else -999,
    binning   = [ 10, -pi, pi ],
))
