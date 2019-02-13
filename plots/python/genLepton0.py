#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
genLepton0 = []

genLepton0.append( Plot(
    name      = 'genLepton0_pt',
    texX      = 'p_{T}(l_{0}) (GeV)',
    texY      = 'Number of Events / 15 GeV',
    attribute = lambda event, sample: event.GenLepton_pt[0] if event.nGenLepton > 0 else -999,
    binning   = [ 20, 0, 300 ],
))

genLepton0.append( Plot(
    name      = 'genLepton0_eta',
    texX      = '#eta(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenLepton_eta[0] if event.nGenLepton > 0 else -999,
    binning   = [ 30, -3, 3 ],
))

genLepton0.append( Plot(
    name      = 'genLepton0_absEta',
    texX      = '|#eta|(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.GenLepton_eta[0]) if event.nGenLepton > 0 else -999,
    binning   = [ 15, 0, 3 ],
))

genLepton0.append( Plot(
    name      = 'genLepton0_phi',
    texX      = '#phi(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenLepton_phi[0] if event.nGenLepton > 0 else -999,
    binning   = [ 10, -pi, pi ],
))
