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
    attribute = TreeVariable.fromString( "Bj1_pt/F" ),
    binning   = [ 20, 0, 200 ],
))

bjetGood1.append( Plot(
    name      = 'bjetGood1_eta',
    texX      = '#eta(b_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "Bj1_eta/F" ),
    binning   = [ 20, -5, 5 ],
))

bjetGood1.append( Plot(
    name      = 'bjetGood1_phi',
    texX      = '#phi(b_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "Bj1_phi/F" ),
    binning   = [ 10, -pi, pi ],
))
