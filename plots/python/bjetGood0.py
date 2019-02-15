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
    attribute = TreeVariable.fromString( "Bj0_pt/F" ),
    binning   = [ 20, 0, 200 ],
))

bjetGood0.append( Plot(
    name      = 'bjetGood0_eta',
    texX      = '#eta(b_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "Bj0_eta/F" ),
    binning   = [ 20, -5, 5 ],
))

bjetGood0.append( Plot(
    name      = 'bjetGood0_phi',
    texX      = '#phi(b_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "Bj0_phi/F" ),
    binning   = [ 10, -pi, pi ],
))
