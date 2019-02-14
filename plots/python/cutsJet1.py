#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
cutsJet1 = []
    
cutsJet1.append( Plot(
    name      = 'jet1_neHEF',
    texX      = 'neHEF(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_neHEF[1],
    binning   = [ 30, 0., 1 ],
))

cutsJet1.append( Plot(
    name      = 'jet1_neEmEF',
    texX      = 'neEmEF(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_neEmEF[1],
    binning   = [ 30, 0., 1 ],
))

cutsJet1.append( Plot(
    name      = 'jet1_chEmHEF',
    texX      = 'chEmEF(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_chEmEF[1],
    binning   = [ 30, 0., 1 ],
))

cutsJet1.append( Plot(
    name      = 'jet1_chHEF',
    texX      = 'chHEF(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_chHEF[1],
    binning   = [ 30, 0, 1 ],
))

