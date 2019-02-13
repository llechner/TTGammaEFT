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
metSig = []
    
metSig.append( Plot(
    name      = 'MetSig',
    texX      = 'E_{T}^{miss}/#sqrt{H_{T}} (GeV^{1/2})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString('METSig/F'),
    binning   = [30,0,30],
))


