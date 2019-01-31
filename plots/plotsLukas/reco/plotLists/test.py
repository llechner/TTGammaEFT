#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
import sys
from math                             import pi
import copy
# RootTools
from RootTools.core.standard          import *

from TTGammaEFT.plots.multiplicityGood import multiplicityGood

plotListData    = []
plotListData   += multiplicityGood
plotListDataMC  = plotListData
