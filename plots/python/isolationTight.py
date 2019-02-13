#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
isolationTight = []

isolationTight.append( Plot(
    name      = 'mindRJetTightLepton',
    texX      = 'min(#DeltaR(lep, jet))',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.tightLeptonJetdR if event.nJetGood >= 1 and event.nLeptonTight >= 1 else -999,
    binning   = [ 40, 0, 4 ],
))

# Lepton Photon    
isolationTight.append( Plot(
    name      = 'dRLTight0PhotonGood0',
    texX      = '#DeltaR(#gamma_{0},l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.ltight0GammadR if event.nPhotonGood >= 1 and event.nLeptonTight >= 1 else -999,
    binning   = [ 40, 0, 4 ],
))

isolationTight.append( Plot(
    name      = 'dPhiLTight0PhotonGood0',
    texX      = '#Delta#phi(#gamma_{0},l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.ltight0GammadPhi if event.nPhotonGood >= 1 and event.nLeptonTight >= 1 else -999,
    binning   = [ 40, 0, pi ],
))
