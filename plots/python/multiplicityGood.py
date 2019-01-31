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
multiplicityGood = []
    
multiplicityGood.append( Plot(
    name      = 'nPhotonGood',
    texX      = 'N_{#gamma}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nPhotonGood,
    binning   = [ 4, 0, 4 ],
))

multiplicityGood.append( Plot(
    name      = 'nLeptonGood',
    texX      = 'N_{l}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nLeptonGood,
    binning   = [ 4, 0, 4 ],
))

multiplicityGood.append( Plot(
    name      = 'nElectronGood',
    texX      = 'N_{e}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nElectronGood,
    binning   = [ 4, 0, 4 ],
))

multiplicityGood.append( Plot(
    name      = 'nMuonGood',
    texX      = 'N_{#mu}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nMuonGood,
    binning   = [ 4, 0, 4 ],
))

multiplicityGood.append( Plot(
    name      = 'nLeptonTight',
    texX      = 'N_{l}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nLeptonTight,
    binning   = [ 4, 0, 4 ],
))

multiplicityGood.append( Plot(
    name      = 'nElectronTight',
    texX      = 'N_{e}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nElectronTight,
    binning   = [ 4, 0, 4 ],
))

multiplicityGood.append( Plot(
    name      = 'nMuonTight',
    texX      = 'N_{#mu}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nMuonTight,
    binning   = [ 4, 0, 4 ],
))

multiplicityGood.append( Plot(
    name      = 'nJetGood',
    texX      = 'N_{jet}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nJetGood,
    binning   = [ 15, 0, 15 ],
))

multiplicityGood.append( Plot(
    name      = 'nBJetGood',
    texX      = 'N_{bJet}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nBTagGood,
    binning   = [ 4, 0, 4 ],
))

