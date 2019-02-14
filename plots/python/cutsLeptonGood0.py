#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
cutsLeptonGood0 = []
    
cutsLeptonGood0.append( Plot(
    name      = 'leptonGood0_hoe',
    texX      = 'H/E(l_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonGood0_hoe/F" ),
    binning   = [ 20, 0, 0.12 ],
))

cutsLeptonGood0.append( Plot(
    name      = 'leptonGood0_eInvMinusPInv',
    texX      = '1/E - 1/p (l_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonGood0_eInvMinusPInv/F" ),
    binning   = [ 50, -0.05, 0.05 ],
))

cutsLeptonGood0.append( Plot(
    name      = 'leptonGood0_sieie',
    texX      = '#sigma_{i#etai#eta}(l_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonGood0_sieie/F" ),
    binning   = [ 20, 0, 0.02 ],
))

cutsLeptonGood0.append( Plot(
    name      = 'leptonGood0_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(l_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonGood0_pfRelIso03_chg/F" ),
    binning   = [ 20, 0, 0.12 ],
))

cutsLeptonGood0.append( Plot(
    name      = 'leptonGood0_pfRelIso03_all',
    texX      = 'relIso_{0.3}(l_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonGood0_pfRelIso03_all/F" ),
    binning   = [ 20, 0, 0.12 ],
))

