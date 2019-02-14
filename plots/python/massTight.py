#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
massTight = []
    
massTight.append( Plot(
    name      = 'mL0PhotonTight',
    texX      = 'M(#gamma,l_{0}) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = TreeVariable.fromString( "mLtight0Gamma/F" ),
    binning   = [ 50, 0, 200 ],
))

massTight.append( Plot(
    name      = 'mllTight',
    texX      = 'M(ll) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = TreeVariable.fromString( "mlltight/F" ),
    binning   = [ 50, 0, 200 ],
))

massTight.append( Plot(
    name      = 'mllPhotonTight',
    texX      = 'M(ll#gamma) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = TreeVariable.fromString( "mllgammatight/F" ),
    binning   = [ 50, 0, 200 ],
))

