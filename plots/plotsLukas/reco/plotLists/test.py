#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                              import pi

# RootTools
from RootTools.core.standard           import *

from TTGammaEFT.plots.multiplicity     import multiplicity
from TTGammaEFT.plots.multiplicityGood import multiplicityGood
from TTGammaEFT.plots.jetGood0 import jetGood0
from TTGammaEFT.plots.jetGood1 import jetGood1

plotListData    = []
plotListData   += multiplicity
plotListData   += multiplicityGood
#plotListData   += jetGood0
#plotListData   += jetGood1
plotListDataMC  = plotListData
