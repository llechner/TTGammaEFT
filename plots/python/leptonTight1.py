#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
leptonTight1 = []

leptonTight1.append( Plot(
    name      = 'leptonTight1_pt',
    texX      = 'p_{T}(l_{1}) (GeV)',
    texY      = 'Number of Events / 15 GeV',
    attribute = TreeVariable.fromString( "LeptonTight1_pt/F" ),
    binning   = [ 20, 0, 300 ],
))

leptonTight1.append( Plot(
    name      = 'leptonTight1_eta',
    texX      = '#eta(l_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonTight1_eta/F" ),
    binning   = [ 30, -3, 3 ],
))

leptonTight1.append( Plot(
    name      = 'leptonTight1_absEta',
    texX      = '|#eta|(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.LeptonTight1_eta),
    binning   = [ 15, 0, 3 ],
))

leptonTight1.append( Plot(
    name      = 'leptonTight1_phi',
    texX      = '#phi(l_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonTight1_phi/F" ),
    binning   = [ 10, -pi, pi ],
))

