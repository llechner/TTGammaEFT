#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
beam = []
    
beam.append(Plot(
    name = 'PV_npvs',
    texX = 'N_{PV} (total)',
    texY = 'Number of Events',
    attribute = TreeVariable.fromString( "PV_npvs/I" ),
    binning=[100,0,100],
))

beam.append(Plot(
    name = 'PV_npvs_good',
    texX = 'N_{PV} (good)',
    texY = 'Number of Events',
    attribute = TreeVariable.fromString( "PV_npvsGood/I" ),
    binning=[100,0,100],
))

