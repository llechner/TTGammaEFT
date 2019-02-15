#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
jet1 = []
    
jet1.append( Plot(
    name      = 'jet1_pt_wide',
    texX      = 'p_{T}(jet_{1}) (GeV)',
    texY      = 'Number of Events / 30 GeV',
    attribute = lambda event, sample: event.Jet_pt[1],
    binning   = [ 20, 0, 600 ],
))

jet1.append( Plot(
    name      = 'jet1_pt',
    texX      = 'p_{T}(jet_{1}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.Jet_pt[1],
    binning   = [ 20, 0, 200 ],
))

jet1.append( Plot(
    name      = 'jet1_eta',
    texX      = '#eta(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_eta[1],
    binning   = [ 20, -5, 5 ],
))

jet1.append( Plot(
    name      = 'jet1_phi',
    texX      = '#phi(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_phi[1],
    binning   = [ 10, -pi, pi ],
))




jet1.append( Plot(
    name      = 'jet1_eta_fine',
    texX      = '#eta(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_eta[1],
    binning   = [ 40, -5, 5 ],
))

jet1.append( Plot(
    name      = 'jet1_eta_veryFine',
    texX      = '#eta(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_eta[1],
    binning   = [ 60, -5, 5 ],
))

