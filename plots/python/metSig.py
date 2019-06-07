#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
metSig = []
    
metSig.append( Plot(
    name      = 'METoverSqrtHT',
    texX      = 'E_{T}^{miss}/#sqrt{H_{T}} (GeV^{1/2})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString('METSig/F'),
    binning   = [30,0,30],
))


metSig.append( Plot(
    name      = 'MetSig',
    texX      = 'MET Significance',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString('MET_significance/F'),
    binning   = [30,0,30],
))


