#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
leptonTight0 = []

leptonTight0.append( Plot(
    name      = 'leptonTight0_pt',
    texX      = 'p_{T}(l_{0}) (GeV)',
    texY      = 'Number of Events / 15 GeV',
    attribute = lambda event, sample: event.LeptonTight0_pt if event.nLeptonTight > 0 else -999,
    binning   = [ 20, 0, 300 ],
))

leptonTight0.append( Plot(
    name      = 'leptonTight0_eta',
    texX      = '#eta(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight0_eta if event.nLeptonTight > 0 else -999,
    binning   = [ 30, -3, 3 ],
))

leptonTight0.append( Plot(
    name      = 'leptonTight0_absEta',
    texX      = '|#eta|(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.LeptonTight0_eta) if event.nLeptonTight > 0 else -999,
    binning   = [ 15, 0, 3 ],
))

leptonTight0.append( Plot(
    name      = 'leptonTight0_phi',
    texX      = '#phi(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight0_phi if event.nLeptonTight > 0 else -999,
    binning   = [ 10, -pi, pi ],
))
