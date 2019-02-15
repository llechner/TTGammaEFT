#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
leptonGood1 = []

leptonGood1.append( Plot(
    name      = 'leptonGood1_pt',
    texX      = 'p_{T}(l_{1}) (GeV)',
    texY      = 'Number of Events / 15 GeV',
    attribute = TreeVariable.fromString( "LeptonGood1_pt/F" ),
    binning   = [ 20, 0, 300 ],
))

leptonGood1.append( Plot(
    name      = 'leptonGood1_eta',
    texX      = '#eta(l_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonGood1_eta/F" ),
    binning   = [ 30, -3, 3 ],
))

leptonGood1.append( Plot(
    name      = 'leptonGood1_absEta',
    texX      = '|#eta|(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.LeptonGood1_eta),
    binning   = [ 15, 0, 3 ],
))

leptonGood1.append( Plot(
    name      = 'leptonGood1_phi',
    texX      = '#phi(l_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonGood1_phi/F" ),
    binning   = [ 10, -pi, pi ],
))
