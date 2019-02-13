#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
checksGood = []
    
checksGood.append( Plot(
    name      = 'isTTG',
    texX      = 'Flag_{tt#gamma}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.isTTGamma,
    binning   = [ 2, 0, 2 ],
))

checksGood.append( Plot(
    name      = 'isZG',
    texX      = 'Flag_{Z/W#gamma}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.isZWGamma,
    binning   = [ 2, 0, 2 ],
))

checksGood.append( Plot(
    name      = 'isZG',
    texX      = 'Flag_{single-t}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.isSingleTopTch,
    binning   = [ 2, 0, 2 ],
))

checksGood.append( Plot(
    name      = 'photonGood0_category',
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_photonCat if event.nPhotonGood > 0 else -999,
    binning   = [ 4, 0, 4 ],
))
