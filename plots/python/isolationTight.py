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
    attribute = TreeVariable.fromString( "tightLeptonJetdR/F" ),
    binning   = [ 40, 0, 4 ],
))

# Lepton Photon    
isolationTight.append( Plot(
    name      = 'dRLTight0PhotonGood0',
    texX      = '#DeltaR(#gamma_{0},l_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "ltight0GammadR/F" ),
    binning   = [ 40, 0, 4 ],
))

isolationTight.append( Plot(
    name      = 'dPhiLTight0PhotonGood0',
    texX      = '#Delta#phi(#gamma_{0},l_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "ltight0GammadPhi/F" ),
    binning   = [ 40, 0, pi ],
))
