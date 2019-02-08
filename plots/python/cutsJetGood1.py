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
cutsJetGood1 = []
    
cutsJetGood1.append( Plot(
    name      = 'jetGood1_nConstituents',
    texX      = 'nConstituents(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetGood_nConstituents[1] if event.nJetGood > 1 else defaultValue,
    binning   = [ 5, 0, 5 ],
))

cutsJetGood1.append( Plot(
    name      = 'jetGood1_neHEF',
    texX      = 'neHEF(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetGood_neHEF[1] if event.nJetGood > 1 else defaultValue,
    binning   = [ 30, 0., 1 ],
))

cutsJetGood1.append( Plot(
    name      = 'jetGood1_neEmEF',
    texX      = 'neEmEF(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetGood_neEmEF[1] if event.nJetGood > 1 else defaultValue,
    binning   = [ 30, 0., 1 ],
))

cutsJetGood1.append( Plot(
    name      = 'jetGood1_chEmHEF',
    texX      = 'chEmEF(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetGood_chEmEF[1] if event.nJetGood > 1 else defaultValue,
    binning   = [ 30, 0., 1 ],
))

cutsJetGood1.append( Plot(
    name      = 'jetGood1_chHEF',
    texX      = 'chHEF(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetGood_chHEF[1] if event.nJetGood > 1 else defaultValue,
    binning   = [ 30, 0, 1 ],
))

cutsJetGood1.append( Plot(
    name      = 'jetGood1_ID',
    texX      = 'ID(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetGood_jetId[1] if event.nJetGood > 1 else defaultValue,
    binning   = [ 4, 0, 4 ],
))

