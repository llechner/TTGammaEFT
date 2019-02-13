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
cutsLeptonGood0 = []
    
cutsLeptonGood0.append( Plot(
    name      = 'leptonGood0_hoe',
    texX      = 'H/E(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood0_hoe if event.nLeptonGood > 0 and abs(event.LeptonGood0_pdgId)==11 else defaultValue,
    binning   = [ 20, 0, 0.12 ],
))

cutsLeptonGood0.append( Plot(
    name      = 'leptonGood0_eInvMinusPInv',
    texX      = '1/E - 1/p (l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood0_eInvMinusPInv if event.nLeptonGood > 0 and abs(event.LeptonGood0_pdgId)==11 else defaultValue,
    binning   = [ 50, -0.05, 0.05 ],
))

cutsLeptonGood0.append( Plot(
    name      = 'leptonGood0_sip3d',
    texX      = 'sip3D(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood0_sip3d if event.nLeptonGood > 0 else defaultValue,
    binning   = [ 20, 0, 4.5 ],
))

cutsLeptonGood0.append( Plot(
    name      = 'leptonGood0_sieie',
    texX      = '#sigma_{i#etai#eta}(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood0_sieie if event.nLeptonGood > 0 and abs(event.LeptonGood0_pdgId)==11 else defaultValue,
    binning   = [ 20, 0, 0.02 ],
))

cutsLeptonGood0.append( Plot(
    name      = 'leptonGood0_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood0_pfRelIso03_chg if event.nLeptonGood > 0 else defaultValue,
    binning   = [ 20, 0, 0.12 ],
))

cutsLeptonGood0.append( Plot(
    name      = 'leptonGood0_pfRelIso03_all',
    texX      = 'relIso_{0.3}(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood0_pfRelIso03_all if event.nLeptonGood > 0 else defaultValue,
    binning   = [ 20, 0, 0.12 ],
))

