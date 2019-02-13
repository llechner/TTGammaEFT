#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
genBJet0 = []
    
genBJet0.append( Plot(
    name      = 'genBJet0_pt',
    texX      = 'p_{T}(gen b_{0}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.GenBj0_pt if event.nGenBJet > 0 else -999,
    binning   = [ 20, 0, 200 ],
))

genBJet0.append( Plot(
    name      = 'genBJet0_eta',
    texX      = '#eta(gen b_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenBj0_eta if event.nGenBJet > 0 else -999,
    binning   = [ 20, -5, 5 ],
))

genBJet0.append( Plot(
    name      = 'genBJet0_absEta',
    texX      = '|#eta|(gen b_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.GenBj0_eta) if event.nGenBJet > 0 else -999,
    binning   = [ 10, 0, 5 ],
))

genBJet0.append( Plot(
    name      = 'genBJet0_phi',
    texX      = '#phi(gen b_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenBj0_phi if event.nGenBJet > 0 else -999,
    binning   = [ 10, -pi, pi ],
))
