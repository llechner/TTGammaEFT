#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
genJet0 = []
    
genJet0.append( Plot(
    name      = 'genJet0_pt',
    texX      = 'p_{T}(jet_{0}) (GeV)',
    texY      = 'Number of Events / 30 GeV',
    attribute = lambda event, sample: event.GenJet_pt[0] if event.nGenJet > 0 else -999,
    binning   = [ 20, 0, 600 ],
))

genJet0.append( Plot(
    name      = 'genJet0_pt_tight',
    texX      = 'p_{T}(jet_{0}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.GenJet_pt[0] if event.nGenJet > 0 else -999,
    binning   = [ 20, 0, 200 ],
))

genJet0.append( Plot(
    name      = 'genJet0_eta',
    texX      = '#eta(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenJet_eta[0] if event.nGenJet > 0 else -999,
    binning   = [ 20, -3, 3 ],
))

genJet0.append( Plot(
    name      = 'genJet0_absEta',
    texX      = '|#eta|(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.GenJet_eta[0]) if event.nGenJet > 0 else -999,
    binning   = [ 10, 0, 3 ],
))

genJet0.append( Plot(
    name      = 'genJet0_phi',
    texX      = '#phi(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenJet_phi[0] if event.nGenJet > 0 else -999,
    binning   = [ 10, -pi, pi ],
))
