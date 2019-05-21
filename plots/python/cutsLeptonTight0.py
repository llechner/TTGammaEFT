#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
cutsLeptonTight0 = []
    
cutsLeptonTight0.append( Plot(
    name      = 'leptonTight0_hoe',
    texX      = 'H/E(l_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonTight0_hoe/F" ),
    binning   = [ 20, 0, 0.12 ],
))

cutsLeptonTight0.append( Plot(
    name      = 'leptonTight0_eInvMinusPInv',
    texX      = '1/E - 1/p (l_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonTight0_eInvMinusPInv/F" ),
    binning   = [ 50, -0.05, 0.05 ],
))

cutsLeptonTight0.append( Plot(
    name      = 'leptonTight0_convVeto',
    texX      = 'conversion veto (l_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonTight0_convVeto/I" ),
    binning   = [ 2, 0, 2 ],
))

cutsLeptonTight0.append( Plot(
    name      = 'leptonTight0_sieie',
    texX      = '#sigma_{i#etai#eta}(l_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonTight0_sieie/F" ),
    binning   = [ 20, 0, 0.02 ],
))

cutsLeptonTight0.append( Plot(
    name      = 'leptonTight0_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(l_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonTight0_pfRelIso03_chg/F" ),
    binning   = [ 20, 0, 0.12 ],
))

cutsLeptonTight0.append( Plot(
    name      = 'leptonTight0_pfRelIso03_all',
    texX      = 'relIso_{0.3}(l_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "LeptonTight0_pfRelIso03_all/F" ),
    binning   = [ 20, 0, 0.12 ],
))
