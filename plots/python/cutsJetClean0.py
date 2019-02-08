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
cutsJetClean0 = []
    
cutsJetClean0.append( Plot(
    name      = 'cleanJet0_nConstituents',
    texX      = 'nConstituents(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_nConstituents[0] if event.nJetClean > 0 else defaultValue,
    binning   = [ 5, 0, 5 ],
))

cutsJetClean0.append( Plot(
    name      = 'cleanJet0_neHEF',
    texX      = 'neHEF(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_neHEF[0] if event.nJetClean > 0 else defaultValue,
    binning   = [ 30, 0., 1 ],
))

cutsJetClean0.append( Plot(
    name      = 'cleanJet0_neEmEF',
    texX      = 'neEmEF(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_neEmEF[0] if event.nJetClean > 0 else defaultValue,
    binning   = [ 30, 0., 1 ],
))

cutsJetClean0.append( Plot(
    name      = 'cleanJet0_chEmHEF',
    texX      = 'chEmEF(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_chEmEF[0] if event.nJetClean > 0 else defaultValue,
    binning   = [ 30, 0., 1 ],
))

cutsJetClean0.append( Plot(
    name      = 'cleanJet0_chHEF',
    texX      = 'chHEF(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_chHEF[0] if event.nJetClean > 0 else defaultValue,
    binning   = [ 30, 0, 1 ],
))

cutsJetClean0.append( Plot(
    name      = 'cleanJet0_ID',
    texX      = 'ID(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_JetCleanId[0] if event.nJetClean > 0 else defaultValue,
    binning   = [ 4, 0, 4 ],
))

