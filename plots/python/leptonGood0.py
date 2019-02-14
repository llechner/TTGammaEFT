#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
leptonGood0 = []

leptonGood0.append( Plot(
    name      = 'leptonGood0_pt',
    texX      = 'p_{T}(l_{0}) (GeV)',
    texY      = 'Number of Events / 15 GeV',
    attribute = TreeVariable.fromString( "LeptonGood0_pt/F" ),
    binning   = [ 20, 0, 300 ],
))

leptonGood0.append( Plot(
    name      = 'leptonGood0_eta',
    texX      = '#eta(l_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonGood0_eta/F" ),
    binning   = [ 30, -3, 3 ],
))

leptonGood0.append( Plot(
    name      = 'leptonGood0_absEta',
    texX      = '|#eta|(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.LeptonGood0_eta),
    binning   = [ 15, 0, 3 ],
))

leptonGood0.append( Plot(
    name      = 'leptonGood0_phi',
    texX      = '#phi(l_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonGood0_phi/F" ),
    binning   = [ 10, -pi, pi ],
))
