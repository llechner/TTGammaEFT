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
cutsJetClean1 = []
    
cutsJetClean1.append( Plot(
    name      = 'cleanJet1_nConstituents',
    texX      = 'nConstituents(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_nConstituents[1] if event.nJetClean > 1 else defaultValue,
    binning   = [ 5, 0, 5 ],
))

cutsJetClean1.append( Plot(
    name      = 'cleanJet1_neHEF',
    texX      = 'neHEF(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_neHEF[1] if event.nJetClean > 1 else defaultValue,
    binning   = [ 30, 0., 1 ],
))

cutsJetClean1.append( Plot(
    name      = 'cleanJet1_neEmEF',
    texX      = 'neEmEF(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_neEmEF[1] if event.nJetClean > 1 else defaultValue,
    binning   = [ 30, 0., 1 ],
))

cutsJetClean1.append( Plot(
    name      = 'cleanJet1_chEmHEF',
    texX      = 'chEmEF(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_chEmEF[1] if event.nJetClean > 1 else defaultValue,
    binning   = [ 30, 0., 1 ],
))

cutsJetClean1.append( Plot(
    name      = 'cleanJet1_neHEF_detailed',
    texX      = 'neHEF(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_neHEF[1] if event.nJetClean > 1 else defaultValue,
    binning   = [ 80, 0., 1 ],
))

cutsJetClean1.append( Plot(
    name      = 'cleanJet1_neEmEF_detailed',
    texX      = 'neEmEF(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_neEmEF[1] if event.nJetClean > 1 else defaultValue,
    binning   = [ 80, 0., 1 ],
))

cutsJetClean1.append( Plot(
    name      = 'cleanJet1_chEmHEF_detailed',
    texX      = 'chEmEF(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_chEmEF[1] if event.nJetClean > 1 else defaultValue,
    binning   = [ 80, 0., 1 ],
))

cutsJetClean1.append( Plot(
    name      = 'cleanJet1_neHEF_tight',
    texX      = 'neHEF(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_neHEF[1] if event.nJetClean > 1 else defaultValue,
    binning   = [ 30, 0.8, 1 ],
))

cutsJetClean1.append( Plot(
    name      = 'cleanJet1_neEmEF_tight',
    texX      = 'neEmEF(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_neEmEF[1] if event.nJetClean > 1 else defaultValue,
    binning   = [ 30, 0.8, 1 ],
))

cutsJetClean1.append( Plot(
    name      = 'cleanJet1_chEmHEF_tight',
    texX      = 'chEmEF(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_chEmEF[1] if event.nJetClean > 1 else defaultValue,
    binning   = [ 30, 0.8, 1 ],
))

cutsJetClean1.append( Plot(
    name      = 'cleanJet1_chHEF',
    texX      = 'chHEF(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_chHEF[1] if event.nJetClean > 1 else defaultValue,
    binning   = [ 30, 0, 1 ],
))

cutsJetClean1.append( Plot(
    name      = 'cleanJet1_ID',
    texX      = 'ID(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_JetCleanId[1] if event.nJetClean > 1 else defaultValue,
    binning   = [ 4, 0, 4 ],
))

