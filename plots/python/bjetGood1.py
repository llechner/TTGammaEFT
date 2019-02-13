#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
bjetGood1 = []
    
bjetGood1.append( Plot(
    name      = 'bjetGood1_pt',
    texX      = 'p_{T}(b_{1}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.Bj1_pt if event.nBTagGood > 1 else -999,
    binning   = [ 20, 0, 200 ],
))

bjetGood1.append( Plot(
    name      = 'bjetGood1_eta',
    texX      = '#eta(b_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Bj1_eta if event.nBTagGood > 1 else -999,
    binning   = [ 20, -5, 5 ],
))

bjetGood1.append( Plot(
    name      = 'bjetGood1_absEta',
    texX      = '|#eta|(b_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.Bj1_eta) if event.nBTagGood > 1 else -999,
    binning   = [ 10, 0, 5 ],
))

bjetGood1.append( Plot(
    name      = 'bjetGood1_phi',
    texX      = '#phi(b_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Bj1_phi if event.nBTagGood > 1 else -999,
    binning   = [ 10, -pi, pi ],
))
