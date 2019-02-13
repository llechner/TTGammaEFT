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
    attribute = lambda event, sample: event.LeptonTight1_hoe if event.nLeptonTight > 1 and abs(event.LeptonTight1_pdgId)==11 else -999,
    binning   = [ 20, 0, 0.12 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_eInvMinusPInv',
    texX      = '1/E - 1/p (l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight1_eInvMinusPInv if event.nLeptonTight > 1 and abs(event.LeptonTight1_pdgId)==11 else -999,
    binning   = [ 50, -0.05, 0.05 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_sieie',
    texX      = '#sigma_{i#etai#eta}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight1_sieie if event.nLeptonTight > 1 and abs(event.LeptonTight1_pdgId)==11 else -999,
    binning   = [ 20, 0, 0.02 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight1_pfRelIso03_chg if event.nLeptonTight > 1 else -999,
    binning   = [ 20, 0, 0.12 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_pfRelIso03_all',
    texX      = 'relIso_{0.3}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight1_pfRelIso03_all if event.nLeptonTight > 1 else -999,
    binning   = [ 20, 0, 0.12 ],
))

