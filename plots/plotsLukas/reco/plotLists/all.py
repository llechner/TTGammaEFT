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
from TTGammaEFT.plots.jet0             import jet0
from TTGammaEFT.plots.jetGood0         import jetGood0
#from TTGammaEFT.plots.jetGood1         import jetGood1
from TTGammaEFT.plots.bjetGood0        import bjetGood0
#from TTGammaEFT.plots.bjetGood1        import bjetGood1
from TTGammaEFT.plots.multiplicity     import multiplicity
from TTGammaEFT.plots.multiplicityGood import multiplicityGood
from TTGammaEFT.plots.massGood         import massGood
from TTGammaEFT.plots.isolationGood    import isolationGood
from TTGammaEFT.plots.met              import met
from TTGammaEFT.plots.ht               import ht
from TTGammaEFT.plots.beam             import beam

#from TTGammaEFT.plots.cutsJet0         import cutsJet0
from TTGammaEFT.plots.cutsJetGood0     import cutsJetGood0
#from TTGammaEFT.plots.cutsJetGood1     import cutsJetGood1
from TTGammaEFT.plots.cutsLeptonGood0  import cutsLeptonGood0
#from TTGammaEFT.plots.cutsLeptonGood1  import cutsLeptonGood1
from TTGammaEFT.plots.cutsPhotonGood0  import cutsPhotonGood0

# plotList
plotListData  = []
plotListData += photonGood0
plotListData += leptonGood0
plotListData += leptonGood1
plotListData += jet0
plotListData += jetGood0
#plotListData += jetGood1
plotListData += bjetGood0
#plotListData += bjetGood1
plotListData += multiplicity
plotListData += multiplicityGood
plotListData += massGood
plotListData += isolationGood
plotListData += met
plotListData += ht
plotListData += beam

#plotListData += cutsJet0
plotListData += cutsJetGood0
#plotListData += cutsJetGood1
plotListData += cutsLeptonGood0
#plotListData += cutsLeptonGood1
plotListData += cutsPhotonGood0

plotListDataMC = plotListData

