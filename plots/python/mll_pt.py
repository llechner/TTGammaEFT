#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
mll_pt = []
    
mll_pt.append( Plot(
    name      = 'mllGood_20ptG120',
    texX      = 'M(ll) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.mll if event.PhotonGood0_pt < 120 else -999,
    binning   = [ 50, 0, 200 ],
))

mll_pt.append( Plot(
    name      = 'mllGood_120ptG220',
    texX      = 'M(ll) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.mll if event.PhotonGood0_pt >= 120 and event.PhotonGood0_pt < 220 else -999,
    binning   = [ 50, 0, 200 ],
))

mll_pt.append( Plot(
    name      = 'mllGood_220ptGinf',
    texX      = 'M(ll) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.mll if event.PhotonGood0_pt >= 220 else -999,
    binning   = [ 50, 0, 200 ],
))



mll_pt.append( Plot(
    name      = 'mllTight_20ptG120',
    texX      = 'M(ll) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.mlltight if event.PhotonGood0_pt < 120 else -999,
    binning   = [ 50, 0, 200 ],
))

mll_pt.append( Plot(
    name      = 'mllTight_120ptG220',
    texX      = 'M(ll) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.mlltight if event.PhotonGood0_pt >= 120 and event.PhotonGood0_pt < 220 else -999,
    binning   = [ 50, 0, 200 ],
))

mll_pt.append( Plot(
    name      = 'mllTight_220ptGinf',
    texX      = 'M(ll) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.mlltight if event.PhotonGood0_pt >= 220 else -999,
    binning   = [ 50, 0, 200 ],
))

