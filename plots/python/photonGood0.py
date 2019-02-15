#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
photonGood0 = []
    
photonGood0.append( Plot(
    name      = 'photonGood0_pt',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = TreeVariable.fromString( "PhotonGood0_pt/F" ),
    binning   = [ 19, 20, 115 ],
))

photonGood0.append( Plot(
    name      = 'photonGood0_pt_EFT',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 100 GeV',
    attribute = TreeVariable.fromString( "PhotonGood0_pt/F" ),
    binning   = [ 6, 20, 620 ],
))

photonGood0.append( Plot(
    name      = 'photonGood0_eta',
    texX      = '#eta(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "PhotonGood0_eta/F" ),
    binning   = [ 24, -1.5, 1.5 ],
))

photonGood0.append( Plot(
    name      = 'photonGood0_absEta',
    texX      = '|#eta|(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.PhotonGood0_eta),
    binning   = [ 9, 0, 1.5 ],
))

photonGood0.append( Plot(
    name      = 'photonGood0_phi',
    texX      = '#phi(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString( "PhotonGood0_phi/F" ),
    binning   = [ 10, -pi, pi ],
))

