#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
photonGood1 = []
    
photonGood1.append( Plot(
    name      = 'photonGood1_pt',
    texX      = 'p_{T}(#gamma_{1}) (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = TreeVariable.fromString( "PhotonGood1_pt/F" ),
    binning   = [ 19, 20, 115 ],
))

photonGood1.append( Plot(
    name      = 'photonGood1_pt_EFT',
    texX      = 'p_{T}(#gamma_{1}) (GeV)',
    texY      = 'Number of Events / 100 GeV',
    attribute = TreeVariable.fromString( "PhotonGood1_pt/F" ),
    binning   = [ 6, 20, 620 ],
))

photonGood1.append( Plot(
    name      = 'photonGood1_eta',
    texX      = '#eta(#gamma_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "PhotonGood1_eta/F" ),
    binning   = [ 24, -1.5, 1.5 ],
))

photonGood1.append( Plot(
    name      = 'photonGood1_absEta',
    texX      = '|#eta|(#gamma_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.PhotonGood1_eta),
    binning   = [ 9, 0, 1.5 ],
))

photonGood1.append( Plot(
    name      = 'photonGood1_phi',
    texX      = '#phi(#gamma_{1})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "PhotonGood1_phi/F" ),
    binning   = [ 10, -pi, pi ],
))

