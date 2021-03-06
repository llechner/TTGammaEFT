#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
lepton1 = []

lepton1.append( Plot(
    name      = 'lepton1_pt_wide',
    texX      = 'p_{T}(l_{1}) (GeV)',
    texY      = 'Number of Events / 15 GeV',
    attribute = lambda event, sample: event.Lepton_pt[1],
    binning   = [ 20, 0, 300 ],
))

lepton1.append( Plot(
    name      = 'lepton1_eta',
    texX      = '#eta(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_eta[1],
    binning   = [ 30, -4, 4 ],
))

lepton1.append( Plot(
    name      = 'lepton1_phi',
    texX      = '#phi(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_phi[1],
    binning   = [ 10, -pi, pi ],
))
