#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                              import pi

# RootTools
from RootTools.core.standard           import *

from TTGammaEFT.plots.multiplicity     import multiplicity
from TTGammaEFT.plots.multiplicityGood import multiplicityGood

plotListData    = []
plotListData   += multiplicity
plotListData   += multiplicityGood
plotListDataMC  = plotListData
