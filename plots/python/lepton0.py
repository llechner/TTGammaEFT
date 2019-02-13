#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
lepton0 = []

lepton0.append( Plot(
    name      = 'lepton0_pt_wide',
    texX      = 'p_{T}(l_{0}) (GeV)',
    texY      = 'Number of Events / 15 GeV',
    attribute = lambda event, sample: event.Lepton_pt[0] if event.nLepton > 0 else -999,
    binning   = [ 20, 0, 300 ],
))

lepton0.append( Plot(
    name      = 'lepton0_eta',
    texX      = '#eta(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_eta[0] if event.nLepton > 0 else -999,
    binning   = [ 30, -3, 3 ],
))

lepton0.append( Plot(
    name      = 'lepton0_eta',
    texX      = '#eta(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_eta[0] if event.nLepton > 0 else -999,
    binning   = [ 30, -4, 4 ],
))

lepton0.append( Plot(
    name      = 'lepton0_absEta',
    texX      = '|#eta|(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.Lepton_eta[0]) if event.nLepton > 0 else -999,
    binning   = [ 15, 0, 4 ],
))

lepton0.append( Plot(
    name      = 'lepton0_phi',
    texX      = '#phi(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_phi[0] if event.nLepton > 0 else -999,
    binning   = [ 10, -pi, pi ],
))
