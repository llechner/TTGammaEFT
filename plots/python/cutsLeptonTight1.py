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
cutsLeptonTight1 = []
    
cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_hoe',
    texX      = 'H/E(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight1_hoe if event.nLeptonTight > 1 and abs(event.LeptonTight1_pdgId)==11 else defaultValue,
    binning   = [ 20, 0, 0.12 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_hoe_tight',
    texX      = 'H/E(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight1_hoe if event.nLeptonTight > 1 and abs(event.LeptonTight1_pdgId)==11 else defaultValue,
    binning   = [ 20, 0, 0.05 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_eInvMinusPInv',
    texX      = '1/E - 1/p (l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight1_eInvMinusPInv if event.nLeptonTight > 1 and abs(event.LeptonTight1_pdgId)==11 else defaultValue,
    binning   = [ 50, -0.05, 0.05 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_sip3d',
    texX      = 'sip3D(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight1_sip3d if event.nLeptonTight > 1 else defaultValue,
    binning   = [ 20, 0, 4.5 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_sieie',
    texX      = '#sigma_{i#etai#eta}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight1_sieie if event.nLeptonTight > 1 and abs(event.LeptonTight1_pdgId)==11 else defaultValue,
    binning   = [ 20, 0, 0.02 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight1_pfRelIso03_chg if event.nLeptonTight > 1 else defaultValue,
    binning   = [ 20, 0, 0.2 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_pfRelIso03_chg_tight',
    texX      = 'charged relIso_{0.3}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight1_pfRelIso03_chg if event.nLeptonTight > 1 else defaultValue,
    binning   = [ 20, 0, 0.05 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_pfRelIso03_all',
    texX      = 'relIso_{0.3}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight1_pfRelIso03_all if event.nLeptonTight > 1 else defaultValue,
    binning   = [ 20, 0, 0.2 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_pfRelIso03_all_tight',
    texX      = 'relIso_{0.3}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight1_pfRelIso03_all if event.nLeptonTight > 1 else defaultValue,
    binning   = [ 20, 0, 0.05 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_convVeto',
    texX      = 'convVeto(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight1_convVeto if event.nLeptonTight > 1 and abs(event.LeptonTight1_pdgId)==11 else defaultValue,
    binning   = [ 2, 0, 2 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_lostHits',
    texX      = 'lost hits(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight1_lostHits if event.nLeptonTight > 1 and abs(event.LeptonTight1_pdgId)==11 else defaultValue,
    binning   = [ 5, 0, 5 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_cutBasedId',
    texX      = 'cut-based ID(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight1_cutBased if event.nLeptonTight > 1 and abs(event.LeptonTight1_pdgId)==11 else defaultValue,
    binning   = [ 5, 0, 5 ],
))

cutsLeptonTight1.append( Plot(
    name      = 'leptonTight1_mediumID',
    texX      = 'medium ID(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonTight1_mediumId if event.nLeptonTight > 1 and abs(event.LeptonTight1_pdgId)==13 else defaultValue,
    binning   = [ 2, 0, 2 ],
))

