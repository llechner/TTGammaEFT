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
    texX      = 'Flag_{Z#gamma}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.isZGamma,
    binning   = [ 2, 0, 2 ],
))

checksGood.append( Plot(
    name      = 'photonGood0_category',
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood_photonCat[0],
    binning   = [ 4, 0, 4 ],
))