#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
met = []
    
met.append( Plot(
    name      = 'MET_pt_800',
    texX      = 'E^{miss}_{T} (GeV)',
    texY      = 'Number of Events / 40 GeV',
    attribute = TreeVariable.fromString( "MET_pt/F" ),
    binning   = [ 20, 0, 800 ],
))

met.append( Plot(
    name      = 'MET_pt_400',
    texX      = 'E^{miss}_{T} (GeV)',
    texY      = 'Number of Events / 20 GeV',
    attribute = TreeVariable.fromString( "MET_pt/F" ),
    binning   = [ 20, 0, 400 ],
))

met.append( Plot(
    name      = 'MET_pt_200',
    texX      = 'E^{miss}_{T} (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = TreeVariable.fromString( "MET_pt/F" ),
    binning   = [ 20, 0, 200 ],
))

met.append( Plot(
    name      = 'MET_phi',
    texX      = '#phi(E^{miss}_{T})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "MET_phi/F" ),
    binning   = [ 10, -pi, pi ],
))

