#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
multiplicityNoPhoton = []
    
multiplicityNoPhoton.append( Plot(
    name      = 'nLepton',
    texX      = 'N_{l}',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "nLepton/I" ),
    binning   = [ 4, 0, 4 ],
))

multiplicityNoPhoton.append( Plot(
    name      = 'nElectron',
    texX      = 'N_{e}',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "nElectron/I" ),
    binning   = [ 4, 0, 4 ],
))

multiplicityNoPhoton.append( Plot(
    name      = 'nMuon',
    texX      = 'N_{#mu}',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "nMuon/I" ),
    binning   = [ 4, 0, 4 ],
))

multiplicityNoPhoton.append( Plot(
    name      = 'nJet',
    texX      = 'N_{jet}',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "nJet/I" ),
    binning   = [ 15, 0, 15 ],
))

multiplicityNoPhoton.append( Plot(
    name      = 'nBJet',
    texX      = 'N_{bJet}',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "nBTag/I" ),
    binning   = [ 4, 0, 4 ],
))
