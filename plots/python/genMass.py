#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# TTGammaEFT
from TTGammaEFT.Tools.constants       import defaultValue

# plotList
genMass = []
    
genMass.append( Plot(
    name      = 'mll',
    texX      = 'gen M(ll) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = lambda event, sample: event.mll if event.nGenLepton >= 2 else defaultValue,
    binning   = [ 50, 0, 200 ],
))

genMass.append( Plot(
    name      = 'mllPhoton',
    texX      = 'gen M(ll#gamma) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = lambda event, sample: event.mllgamma if event.nGenLepton >= 2 and event.nGenPhoton >= 1 else defaultValue,
    binning   = [ 50, 0, 200 ],
))
