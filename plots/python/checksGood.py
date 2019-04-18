#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
checksGood = []
    
checksGood.append( Plot(
    name      = 'isTTG',
    texX      = 'Flag_{tt#gamma}',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "isTTGamma/I" ),
    binning   = [ 2, 0, 2 ],
))

checksGood.append( Plot(
    name      = 'isZG',
    texX      = 'Flag_{Z/W#gamma}',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "isZWGamma/I" ),
    binning   = [ 2, 0, 2 ],
))

checksGood.append( Plot(
    name      = 'isZG',
    texX      = 'Flag_{single-t}',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "isTGamma/I" ),
    binning   = [ 2, 0, 2 ],
))

