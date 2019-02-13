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
cutsLeptonTight0 = []
    
cutsLeptonTight0.append( Plot(
    name      = 'leptonTight0_hoe',
    texX      = 'H/E(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight0_hoe if event.nLeptonTight > 0 and abs(event.LeptonTight0_pdgId)==11 else defaultValue,
    binning   = [ 20, 0, 0.12 ],
))

cutsLeptonTight0.append( Plot(
    name      = 'leptonTight0_eInvMinusPInv',
    texX      = '1/E - 1/p (l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight0_eInvMinusPInv if event.nLeptonTight > 0 and abs(event.LeptonTight0_pdgId)==11 else defaultValue,
    binning   = [ 50, -0.05, 0.05 ],
))

cutsLeptonTight0.append( Plot(
    name      = 'leptonTight0_sieie',
    texX      = '#sigma_{i#etai#eta}(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight0_sieie if event.nLeptonTight > 0 and abs(event.LeptonTight0_pdgId)==11 else defaultValue,
    binning   = [ 20, 0, 0.02 ],
))

cutsLeptonTight0.append( Plot(
    name      = 'leptonTight0_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight0_pfRelIso03_chg if event.nLeptonTight > 0 else defaultValue,
    binning   = [ 20, 0, 0.12 ],
))

cutsLeptonTight0.append( Plot(
    name      = 'leptonTight0_pfRelIso03_all',
    texX      = 'relIso_{0.3}(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight0_pfRelIso03_all if event.nLeptonTight > 0 else defaultValue,
    binning   = [ 20, 0, 0.12 ],
))

