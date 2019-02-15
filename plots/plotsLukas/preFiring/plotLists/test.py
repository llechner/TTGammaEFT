#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

from TTGammaEFT.plots.multiplicity import multiplicity

plotListData    = []
plotListData   += multiplicity
plotListDataMC  = plotListData
