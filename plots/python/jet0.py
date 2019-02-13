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
jet0 = []
    
jet0.append( Plot(
    name      = 'jet0_pt',
    texX      = 'p_{T}(jet_{0}) (GeV)',
    texY      = 'Number of Events / 30 GeV',
    attribute = lambda event, sample: event.Jet_pt[0] if event.nJet > 0 else defaultValue,
    binning   = [ 20, 0, 600 ],
))

jet0.append( Plot(
    name      = 'jet0_pt_wide',
    texX      = 'p_{T}(jet_{0}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.Jet_pt[0] if event.nJet > 0 else defaultValue,
    binning   = [ 20, 0, 200 ],
))

jet0.append( Plot(
    name      = 'jet0_eta',
    texX      = '#eta(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_eta[0] if event.nJet > 0 else defaultValue,
    binning   = [ 20, -5, 5 ],
))

jet0.append( Plot(
    name      = 'jet0_eta_fine',
    texX      = '#eta(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_eta[0] if event.nJet > 0 else defaultValue,
    binning   = [ 40, -5, 5 ],
))

jet0.append( Plot(
    name      = 'jet0_eta_veryFine',
    texX      = '#eta(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_eta[0] if event.nJet > 0 else defaultValue,
    binning   = [ 60, -5, 5 ],
))

jet0.append( Plot(
    name      = 'jet0_absEta',
    texX      = '|#eta|(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.Jet_eta[0]) if event.nJet > 0 else defaultValue,
    binning   = [ 10, 0, 5 ],
))

jet0.append( Plot(
    name      = 'jet0_absEta_fine',
    texX      = '|#eta|(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.Jet_eta[0]) if event.nJet > 0 else defaultValue,
    binning   = [ 20, 0, 5 ],
))

jet0.append( Plot(
    name      = 'jet0_absEta_veryFine',
    texX      = '|#eta|(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.Jet_eta[0]) if event.nJet > 0 else defaultValue,
    binning   = [ 30, 0, 5 ],
))

jet0.append( Plot(
    name      = 'jet0_phi',
    texX      = '#phi(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_phi[0] if event.nJet > 0 else defaultValue,
    binning   = [ 10, -pi, pi ],
))
