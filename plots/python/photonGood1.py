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
photonGood1 = []
    
photonGood1.append( Plot(
    name      = 'photonGood1_pt',
    texX      = 'p_{T}(#gamma_{1}) (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = lambda event, sample: event.PhotonGood1_pt if event.nPhotonGood > 1 else defaultValue,
    binning   = [ 19, 20, 115 ],
))

photonGood1.append( Plot(
    name      = 'photonGood1_eta',
    texX      = '#eta(#gamma_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood1_eta if event.nPhotonGood > 1 else defaultValue,
    binning   = [ 24, -1.5, 1.5 ],
))

photonGood1.append( Plot(
    name      = 'photonGood1_absEta',
    texX      = '|#eta|(#gamma_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.PhotonGood1_eta) if event.nPhotonGood > 1 else defaultValue,
    binning   = [ 9, 0, 1.5 ],
))

photonGood1.append( Plot(
    name      = 'photonGood1_phi',
    texX      = '#phi(#gamma_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood1_phi if event.nPhotonGood > 1 else defaultValue,
    binning   = [ 20, -pi, pi ],
))

