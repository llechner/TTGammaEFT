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
cutsJet0 = []
    
cutsJet0.append( Plot(
    name      = 'jet0_neHEF',
    texX      = 'neHEF(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_neHEF[0] if event.nJet > 0 else defaultValue,
    binning   = [ 30, 0., 1 ],
))

cutsJet0.append( Plot(
    name      = 'jet0_neEmEF',
    texX      = 'neEmEF(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_neEmEF[0] if event.nJet > 0 else defaultValue,
    binning   = [ 30, 0., 1 ],
))

cutsJet0.append( Plot(
    name      = 'jet0_chEmHEF',
    texX      = 'chEmEF(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_chEmEF[0] if event.nJet > 0 else defaultValue,
    binning   = [ 30, 0., 1 ],
))

cutsJet0.append( Plot(
    name      = 'jet0_chHEF',
    texX      = 'chHEF(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_chHEF[0] if event.nJet > 0 else defaultValue,
    binning   = [ 30, 0, 1 ],
))

