#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
cutsLeptonGood1 = []
    
cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_hoe',
    texX      = 'H/E(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood1_hoe if event.nLeptonGood > 1 and abs(event.LeptonGood1_pdgId)==11 else -999,
    binning   = [ 20, 0, 0.12 ],
))

cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_eInvMinusPInv',
    texX      = '1/E - 1/p (l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood1_eInvMinusPInv if event.nLeptonGood > 1 and abs(event.LeptonGood1_pdgId)==11 else -999,
    binning   = [ 50, -0.05, 0.05 ],
))

cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_sip3d',
    texX      = 'sip3D(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood1_sip3d if event.nLeptonGood > 1 else -999,
    binning   = [ 20, 0, 4.5 ],
))

cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_sieie',
    texX      = '#sigma_{i#etai#eta}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood1_sieie if event.nLeptonGood > 1 and abs(event.LeptonGood1_pdgId)==11 else -999,
    binning   = [ 20, 0, 0.02 ],
))

cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood1_pfRelIso03_chg if event.nLeptonGood > 1 else -999,
    binning   = [ 20, 0, 0.12 ],
))

cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_pfRelIso03_all',
    texX      = 'relIso_{0.3}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood1_pfRelIso03_all if event.nLeptonGood > 1 else -999,
    binning   = [ 20, 0, 0.12 ],
))

