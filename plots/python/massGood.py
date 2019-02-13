#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
massGood = []
    
massGood.append( Plot(
    name      = 'mL0PhotonGood',
    texX      = 'M(#gamma,l_{0}) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = lambda event, sample: event.mL0Gamma if event.nLeptonGood >= 1 and event.nPhotonGood >= 1 else -999,
    binning   = [ 50, 0, 200 ],
))

massGood.append( Plot(
    name      = 'mL1PhotonGood',
    texX      = 'M(#gamma,l_{1}) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = lambda event, sample: event.mL1Gamma if event.nLeptonGood >= 2 and event.nPhotonGood >= 1 else -999,
    binning   = [ 50, 0, 200 ],
))

massGood.append( Plot(
    name      = 'mllGood',
    texX      = 'M(ll) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = lambda event, sample: event.mll if event.nLeptonGood >= 2 else -999,
    binning   = [ 50, 0, 200 ],
))

massGood.append( Plot(
    name      = 'mllPhotonGood',
    texX      = 'M(ll#gamma) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = lambda event, sample: event.mllgamma if event.nLeptonGood >= 2 and event.nPhotonGood >= 1 else -999,
    binning   = [ 50, 0, 200 ],
))

massGood.append( Plot(
    name      = 'm3Good',
    texX      = 'M_{3} (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = lambda event, sample: event.m3 if event.nJetGood >= 3 else -999,
    binning   = [ 50, 0, 250 ],
))

massGood.append( Plot(
    name      = 'm3wBJetGood',
    texX      = 'M_{3} w/ 1 BJet (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = lambda event, sample: event.m3wBJet if event.nJetGood >= 3 and event.nBTagGood >= 1 else -999,
    binning   = [ 50, 0, 250 ],
))
