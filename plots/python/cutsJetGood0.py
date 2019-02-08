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
cutsJetGood0 = []
    
cutsJetGood0.append( Plot(
    name      = 'jetGood0_nConstituents',
    texX      = 'nConstituents(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetGood_nConstituents[0] if event.nJetGood > 0 else defaultValue,
    binning   = [ 5, 0, 5 ],
))

cutsJetGood0.append( Plot(
    name      = 'jetGood0_neHEF',
    texX      = 'neHEF(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetGood_neHEF[0] if event.nJetGood > 0 else defaultValue,
    binning   = [ 30, 0., 1 ],
))

cutsJetGood0.append( Plot(
    name      = 'jetGood0_neEmEF',
    texX      = 'neEmEF(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetGood_neEmEF[0] if event.nJetGood > 0 else defaultValue,
    binning   = [ 30, 0., 1 ],
))

cutsJetGood0.append( Plot(
    name      = 'jetGood0_chEmHEF',
    texX      = 'chEmEF(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetGood_chEmEF[0] if event.nJetGood > 0 else defaultValue,
    binning   = [ 30, 0., 1 ],
))

cutsJetGood0.append( Plot(
    name      = 'jetGood0_chHEF',
    texX      = 'chHEF(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetGood_chHEF[0] if event.nJetGood > 0 else defaultValue,
    binning   = [ 30, 0, 1 ],
))

cutsJetGood0.append( Plot(
    name      = 'jetGood0_ID',
    texX      = 'ID(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetGood_jetId[0] if event.nJetGood > 0 else defaultValue,
    binning   = [ 4, 0, 4 ],
))

