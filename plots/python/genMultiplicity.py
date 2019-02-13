#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
genMultiplicity = []
    
genMultiplicity.append( Plot(
    name      = 'nGenPhoton',
    texX      = 'N_{#gamma}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nGenPhoton,
    binning   = [ 4, 0, 4 ],
))

genMultiplicity.append( Plot(
    name      = 'nGenLepton',
    texX      = 'N_{l}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nGenLepton,
    binning   = [ 4, 0, 4 ],
))

genMultiplicity.append( Plot(
    name      = 'nGenMuon',
    texX      = 'N_{#mu}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nGenMuon,
    binning   = [ 4, 0, 4 ],
))

genMultiplicity.append( Plot(
    name      = 'nGenElectron',
    texX      = 'N_{e}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nGenElectron,
    binning   = [ 4, 0, 4 ],
))

genMultiplicity.append( Plot(
    name      = 'nGenJet',
    texX      = 'N_{jet}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nGenJet,
    binning   = [ 10, 0, 10 ],
))

genMultiplicity.append( Plot(
    name      = 'nGenBJet',
    texX      = 'N_{bJet}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nGenBJet,
    binning   = [ 4, 0, 4 ],
))

