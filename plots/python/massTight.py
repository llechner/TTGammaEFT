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
    attribute = lambda event, sample: event.mLtight0Gamma if event.nLeptonTight >= 1 and event.nPhotonGood >= 1 else -999,
    binning   = [ 50, 0, 200 ],
))

massTight.append( Plot(
    name      = 'mllTight',
    texX      = 'M(ll) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = lambda event, sample: event.mlltight if event.nLeptonTight >= 2 else -999,
    binning   = [ 50, 0, 200 ],
))

massTight.append( Plot(
    name      = 'mllPhotonTight',
    texX      = 'M(ll#gamma) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = lambda event, sample: event.mllgammatight if event.nLeptonTight >= 2 and event.nPhotonGood >= 1 else -999,
    binning   = [ 50, 0, 200 ],
))

