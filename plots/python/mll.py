#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
mll = []
    
mll.append( Plot(
    name      = 'mll_Zpeak',
    texX      = 'M(ll) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = TreeVariable.fromString( "mll/F" ),
    binning   = [ 50, 70, 110 ],
))

mll.append( Plot(
    name      = 'mllGood',
    texX      = 'M(ll) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = TreeVariable.fromString( "mll/F" ),
    binning   = [ 50, 0, 200 ],
))

mll.append( Plot(
    name      = 'mllTight',
    texX      = 'M(ll) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = TreeVariable.fromString( "mlltight/F" ),
    binning   = [ 50, 0, 200 ],
))

