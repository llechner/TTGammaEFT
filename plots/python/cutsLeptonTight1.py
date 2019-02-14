#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
cutsLeptonTight1 = []
    
cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_hoe',
    texX      = 'H/E(l_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonTight1_hoe/F" ),
    binning   = [ 20, 0, 0.12 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_eInvMinusPInv',
    texX      = '1/E - 1/p (l_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonTight1_eInvMinusPInv/F" ),
    binning   = [ 50, -0.05, 0.05 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_sieie',
    texX      = '#sigma_{i#etai#eta}(l_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonTight1_sieie/F" ),
    binning   = [ 20, 0, 0.02 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(l_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonTight1_pfRelIso03_chg/F" ),
    binning   = [ 20, 0, 0.12 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_pfRelIso03_all',
    texX      = 'relIso_{0.3}(l_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonTight1_pfRelIso03_all/F" ),
    binning   = [ 20, 0, 0.12 ],
))
