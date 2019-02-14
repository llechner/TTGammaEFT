#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
massGood = []
    
massGood.append( Plot(
    name      = 'mL0PhotonGood',
    texX      = 'M(#gamma,l_{0}) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = TreeVariable.fromString( "mL0Gamma/F" ),
    binning   = [ 50, 0, 200 ],
))

massGood.append( Plot(
    name      = 'mL1PhotonGood',
    texX      = 'M(#gamma,l_{1}) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = TreeVariable.fromString( "mL1Gamma/F" ),
    binning   = [ 50, 0, 200 ],
))

massGood.append( Plot(
    name      = 'mllPhotonGood',
    texX      = 'M(ll#gamma) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = TreeVariable.fromString( "mllgamma/F" ),
    binning   = [ 50, 0, 200 ],
))

massGood.append( Plot(
    name      = 'm3Good',
    texX      = 'M_{3} (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = TreeVariable.fromString( "m3/F" ),
    binning   = [ 50, 0, 250 ],
))

massGood.append( Plot(
    name      = 'm3wBJetGood',
    texX      = 'M_{3} w/ 1 BJet (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = TreeVariable.fromString( "m3wBJet/F" ),
    binning   = [ 50, 0, 250 ],
))
