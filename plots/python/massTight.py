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
    attribute = TreeVariable.fromString( "mLtight0Gamma/F" ),
    binning   = [ 50, 0, 200 ],
))

massTight.append( Plot(
    name      = 'mllPhotonTight',
    texX      = 'M(ll#gamma) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = TreeVariable.fromString( "mllgammatight/F" ),
    binning   = [ 50, 0, 200 ],
))


massTight.append( Plot(
    name      = 'mL0PhotonTight_coarse',
    texX      = 'M(#gamma,l_{0}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = TreeVariable.fromString( "mLtight0Gamma/F" ),
    binning   = [ 17, 20, 190 ],
))

massTight.append( Plot(
    name      = 'mllPhotonTight_coarse',
    texX      = 'M(ll#gamma) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = TreeVariable.fromString( "mllgammatight/F" ),
    binning   = [ 17, 20, 190 ],
))


massTight.append( Plot(
    name      = 'm3',
    texX      = 'M_{3} (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = TreeVariable.fromString( "m3/F" ),
    binning   = [ 50, 0, 250 ],
))

massTight.append( Plot(
    name      = 'm3wBJet',
    texX      = 'M_{3} w/ 1 BJet (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = TreeVariable.fromString( "m3wBJet/F" ),
    binning   = [ 50, 0, 250 ],
))

massTight.append( Plot(
    name      = 'm3_coarse',
    texX      = 'M_{3} (GeV)',
    texY      = 'Number of Events / 20 GeV',
    attribute = TreeVariable.fromString( "m3/F" ),
    binning   = [ 22, 60, 500 ],
))

