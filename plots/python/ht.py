#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
ht = []
    
ht.append( Plot(
    name      = 'ht',
    texX      = 'H_{T} (GeV)',
    texY      = 'Number of Events / 30 GeV',
    attribute = lambda event, sample: event.ht,
    binning   = [ 20, 0, 600 ],
))
