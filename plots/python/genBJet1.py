#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
genBJet1 = []
    
genBJet1.append( Plot(
    name      = 'genBJet1_pt',
    texX      = 'p_{T}(gen b_{1}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = TreeVariable.fromString( "GenBj1_pt/F" ),
    binning   = [ 20, 0, 200 ],
))

genBJet1.append( Plot(
    name      = 'genBJet1_eta',
    texX      = '#eta(gen b_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "GenBj1_eta/F" ),
    binning   = [ 20, -5, 5 ],
))

genBJet1.append( Plot(
    name      = 'genBJet1_absEta',
    texX      = '|#eta|(gen b_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.GenBj1_eta),
    binning   = [ 10, 0, 5 ],
))

genBJet1.append( Plot(
    name      = 'genBJet1_phi',
    texX      = '#phi(gen b_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "GenBj1_phi/F" ),
    binning   = [ 10, -pi, pi ],
))
