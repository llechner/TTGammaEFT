#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# TTGammaEFT
from TTGammaEFT.Tools.constants       import defaultValue

from TTGammaEFT.plots.photonGood0       import photonGood0
from TTGammaEFT.plots.leptonTight0      import leptonTight0
#from TTGammaEFT.plots.leptonTight1      import leptonTight1
from TTGammaEFT.plots.jet0              import jet0
from TTGammaEFT.plots.jetGood0          import jetGood0
#from TTGammaEFT.plots.jetGood1          import jetGood1
from TTGammaEFT.plots.bjetGood0         import bjetGood0
#from TTGammaEFT.plots.bjetGood1         import bjetGood1
from TTGammaEFT.plots.multiplicityGood  import multiplicityGood
from TTGammaEFT.plots.massTight         import massTight
from TTGammaEFT.plots.isolationTight    import isolationTight
from TTGammaEFT.plots.met               import met
from TTGammaEFT.plots.ht                import ht
from TTGammaEFT.plots.beam              import beam

#from TTGammaEFT.plots.cutsJet0                import cutsJet0
from TTGammaEFT.plots.cutsJetGood0            import cutsJetGood0
#from TTGammaEFT.plots.cutsJetGood1            import cutsJetGood1
from TTGammaEFT.plots.cutsLeptonTight0        import cutsLeptonTight0
#from TTGammaEFT.plots.cutsLeptonTight1        import cutsLeptonTight1
from TTGammaEFT.plots.cutsPhotonGood0         import cutsPhotonGood0
from TTGammaEFT.plots.cutsPhotonNoIdCuts0     import cutsPhotonNoIdCuts0
from TTGammaEFT.plots.cutsPhotonNoIdCuts0_nPV import cutsPhotonNoIdCuts0_nPV

# plotList
plotListData  = []
plotListData += photonGood0
plotListData += leptonTight0
#plotListData += leptonTight1
plotListData += jet0
plotListData += jetGood0
#plotListData += jetGood1
plotListData += bjetGood0
#plotListData += bjetGood1
plotListData += multiplicityGood
plotListData += massTight
plotListData += isolationTight
plotListData += met
plotListData += ht
plotListData += beam

#plotListData += cutsJet0
plotListData += cutsJetGood0
#plotListData += cutsJetGood1
plotListData += cutsLeptonTight0
#plotListData += cutsLeptonTight1
plotListData += cutsPhotonGood0
plotListData += cutsPhotonNoIdCuts0
plotListData += cutsPhotonNoIdCuts0_nPV

plotListDataMC = plotListData

