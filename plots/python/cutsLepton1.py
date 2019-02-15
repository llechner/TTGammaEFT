#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
cutsLepton1 = []
    
cutsLepton1.append( Plot(
    name      = 'lepton1_hoe',
    texX      = 'H/E(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_hoe[1],
    binning   = [ 20, 0, 0.12 ],
))

cutsLepton1.append( Plot(
    name      = 'lepton1_eInvMinusPInv',
    texX      = '1/E - 1/p (l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_eInvMinusPInv[1],
    binning   = [ 50, -0.05, 0.05 ],
))

cutsLepton1.append( Plot(
    name      = 'lepton1_sieie',
    texX      = '#sigma_{i#etai#eta}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_sieie[1],
    binning   = [ 20, 0, 0.02 ],
))

cutsLepton1.append( Plot(
    name      = 'lepton1_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_pfRelIso03_chg[1],
    binning   = [ 20, 0, 0.12 ],
))

cutsLepton1.append( Plot(
    name      = 'lepton1_pfRelIso03_all',
    texX      = 'relIso_{0.3}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_pfRelIso03_all[1],
    binning   = [ 20, 0, 0.12 ],
))

