#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

from TTGammaEFT.plots.photonGood0      import photonGood0
from TTGammaEFT.plots.leptonGood0      import leptonGood0
from TTGammaEFT.plots.leptonGood1      import leptonGood1
from TTGammaEFT.plots.jetGood0         import jetGood0
from TTGammaEFT.plots.jetGood1         import jetGood1
from TTGammaEFT.plots.bjetGood0        import bjetGood0
from TTGammaEFT.plots.bjetGood1        import bjetGood1
from TTGammaEFT.plots.multiplicityGood import multiplicityGood
from TTGammaEFT.plots.met              import met
from TTGammaEFT.plots.ht               import ht
from TTGammaEFT.plots.beam             import beam
#from TTGammaEFT.plots.metSig           import metSig

# plotList
plotListData  = []
plotListData += photonGood0
plotListData += leptonGood0
plotListData += leptonGood1
plotListData += jetGood0
plotListData += jetGood1
plotListData += bjetGood0
plotListData += bjetGood1
plotListData += multiplicityGood
plotListData += met
plotListData += ht
plotListData += beam
#plotListData += metSig

plotListDataMC  = plotListData
