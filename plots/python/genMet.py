#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
genMet = []
    
genMet.append( Plot(
    name      = 'GenMET_pt',
    texX      = 'E^{miss}_{T} (GeV)',
    texY      = 'Number of Events / 20 GeV',
    attribute = lambda event, sample: event.GenMET_pt,
    binning   = [ 20, 0, 400 ],
))

genMet.append( Plot(
    name      = 'GenMET_pt_tight',
    texX      = 'E^{miss}_{T} (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.GenMET_pt,
    binning   = [ 20, 0, 200 ],
))

genMet.append( Plot(
    name      = 'GenMET_phi',
    texX      = '#phi(E^{miss}_{T})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenMET_phi,
    binning   = [ 10, -pi, pi ],
))

