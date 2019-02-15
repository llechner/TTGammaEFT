#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
cutsJetGood0 = []
    
cutsJetGood0.append( Plot(
    name      = 'jetGood0_neHEF',
    texX      = 'neHEF(jet_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "JetGood0_neHEF/F" ),
    binning   = [ 30, 0., 1 ],
))

cutsJetGood0.append( Plot(
    name      = 'jetGood0_neEmEF',
    texX      = 'neEmEF(jet_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "JetGood0_neEmEF/F" ),
    binning   = [ 30, 0., 1 ],
))

cutsJetGood0.append( Plot(
    name      = 'jetGood0_chEmHEF',
    texX      = 'chEmEF(jet_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "JetGood0_chEmEF/F" ),
    binning   = [ 30, 0., 1 ],
))

cutsJetGood0.append( Plot(
    name      = 'jetGood0_chHEF',
    texX      = 'chHEF(jet_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "JetGood0_chHEF/F" ),
    binning   = [ 30, 0, 1 ],
))

