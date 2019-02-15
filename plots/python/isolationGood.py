#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
isolationGood = []

# Lepton Photon    
isolationGood.append( Plot(
    name      = 'dRL0PhotonGood0',
    texX      = '#DeltaR(#gamma_{0},l_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "l0GammadR/F" ),
    binning   = [ 40, 0, 4 ],
))

isolationGood.append( Plot(
    name      = 'dPhiL0PhotonGood0',
    texX      = '#Delta#phi(#gamma_{0},l_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "l0GammadPhi/F" ),
    binning   = [ 40, 0, pi ],
))

isolationGood.append( Plot(
    name      = 'dRL1PhotonGood0',
    texX      = '#DeltaR(#gamma_{0},l_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "l1GammadR/F" ),
    binning   = [ 40, 0, 4 ],
))

isolationGood.append( Plot(
    name      = 'dPhiL1PhotonGood0',
    texX      = '#Delta#phi(#gamma_{0},l_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "l1GammadPhi/F" ),
    binning   = [ 40, 0, pi ],
))

# Jet Photon    
isolationGood.append( Plot(
    name      = 'dRJ0PhotonGood0',
    texX      = '#DeltaR(#gamma_{0},j_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "j0GammadR/F" ),
    binning   = [ 40, 0, 4 ],
))

isolationGood.append( Plot(
    name      = 'dPhiJ0PhotonGood0',
    texX      = '#Delta#phi(#gamma_{0},j_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "j0GammadPhi/F" ),
    binning   = [ 40, 0, pi ],
))

isolationGood.append( Plot(
    name      = 'dRJ1PhotonGood0',
    texX      = '#DeltaR(#gamma_{0},j_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "j1GammadR/F" ),
    binning   = [ 40, 0, 4 ],
))

isolationGood.append( Plot(
    name      = 'dPhiJ1PhotonGood0',
    texX      = '#Delta#phi(#gamma_{0},j_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "j1GammadPhi/F" ),
    binning   = [ 40, 0, pi ],
))

# Min dR (for cuts)
isolationGood.append( Plot(
    name      = 'mindRJetPhoton',
    texX      = 'min(#DeltaR(#gamma, jet))',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "photonJetdR/F" ),
    binning   = [ 40, 0, 4 ],
))

isolationGood.append( Plot(
    name      = 'mindRJetLepton',
    texX      = 'min(#DeltaR(lep, jet))',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "leptonJetdR/F" ),
    binning   = [ 40, 0, 4 ],
))

isolationGood.append( Plot(
    name      = 'mindRLepPhoton',
    texX      = 'min(#DeltaR(#gamma, l))',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "photonLepdR/F" ),
    binning   = [ 40, 0, 4 ],
))

# ll
isolationGood.append( Plot(
    name      = 'dRll',
    texX      = '#DeltaR(ll)',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "lldR/F" ),
    binning   = [ 40, 0, 4 ],
))

isolationGood.append( Plot(
    name      = 'dPhill',
    texX      = '#Delta#phi(ll)',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "lldPhi/F" ),
    binning   = [ 40, 0, pi ],
))

# bb
isolationGood.append( Plot(
    name      = 'dRbb',
    texX      = '#DeltaR(bb)',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "bbdR/F" ),
    binning   = [ 40, 0, 4 ],
))

isolationGood.append( Plot(
    name      = 'dPhibb',
    texX      = '#Delta#phi(bb)',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "bbdPhi/F" ),
    binning   = [ 40, 0, pi ],
))
