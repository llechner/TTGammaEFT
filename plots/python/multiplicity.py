#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
multiplicity = []
    
multiplicity.append( Plot(
    name      = 'nPhoton',
    texX      = 'N_{#gamma}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nPhoton,
    binning   = [ 4, 0, 4 ],
))

multiplicity.append( Plot(
    name      = 'nLepton',
    texX      = 'N_{l}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nLepton,
    binning   = [ 4, 0, 4 ],
))

multiplicity.append( Plot(
    name      = 'nElectron',
    texX      = 'N_{e}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nElectron,
    binning   = [ 4, 0, 4 ],
))

multiplicity.append( Plot(
    name      = 'nMuon',
    texX      = 'N_{#mu}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nMuon,
    binning   = [ 4, 0, 4 ],
))

multiplicity.append( Plot(
    name      = 'nJet',
    texX      = 'N_{jet}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nJet,
    binning   = [ 15, 0, 15 ],
))

multiplicity.append( Plot(
    name      = 'nBJet',
    texX      = 'N_{bJet}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nBTag,
    binning   = [ 4, 0, 4 ],
))
