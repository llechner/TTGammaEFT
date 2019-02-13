#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
jetGood0 = []
    
jetGood0.append( Plot(
    name      = 'jetGood0_pt_wide',
    texX      = 'p_{T}(jet_{0}) (GeV)',
    texY      = 'Number of Events / 30 GeV',
    attribute = lambda event, sample: event.JetGood_pt[0] if event.nJetGood > 0 else -999,
    binning   = [ 20, 0, 600 ],
))

jetGood0.append( Plot(
    name      = 'jetGood0_pt',
    texX      = 'p_{T}(jet_{0}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.JetGood_pt[0] if event.nJetGood > 0 else -999,
    binning   = [ 20, 0, 200 ],
))

jetGood0.append( Plot(
    name      = 'jetGood0_eta',
    texX      = '#eta(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetGood_eta[0] if event.nJetGood > 0 else -999,
    binning   = [ 20, -3, 3 ],
))

jetGood0.append( Plot(
    name      = 'jetGood0_absEta',
    texX      = '|#eta|(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.JetGood_eta[0]) if event.nJetGood > 0 else -999,
    binning   = [ 10, 0, 3 ],
))

jetGood0.append( Plot(
    name      = 'jetGood0_phi',
    texX      = '#phi(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetGood_phi[0] if event.nJetGood > 0 else -999,
    binning   = [ 10, -pi, pi ],
))
