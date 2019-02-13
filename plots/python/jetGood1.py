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
jetGood1 = []
    
jetGood1.append( Plot(
    name      = 'jetGood1_pt_wide',
    texX      = 'p_{T}(jet_{1}) (GeV)',
    texY      = 'Number of Events / 30 GeV',
    attribute = lambda event, sample: event.JetGood_pt[1] if event.nJetGood > 1 else defaultValue,
    binning   = [ 20, 0, 600 ],
))

jetGood1.append( Plot(
    name      = 'jetGood1_pt',
    texX      = 'p_{T}(jet_{1}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.JetGood_pt[1] if event.nJetGood > 1 else defaultValue,
    binning   = [ 20, 0, 200 ],
))

jetGood1.append( Plot(
    name      = 'jetGood1_eta',
    texX      = '#eta(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetGood_eta[1] if event.nJetGood > 1 else defaultValue,
    binning   = [ 20, -3, 3 ],
))

jetGood1.append( Plot(
    name      = 'jetGood1_absEta',
    texX      = '|#eta|(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.JetGood_eta[1]) if event.nJetGood > 1 else defaultValue,
    binning   = [ 10, 0, 3 ],
))

jetGood1.append( Plot(
    name      = 'jetGood1_phi',
    texX      = '#phi(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetGood_phi[1] if event.nJetGood > 1 else defaultValue,
    binning   = [ 10, -pi, pi ],
))
