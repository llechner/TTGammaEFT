# Logging
import logging
logger = logging.getLogger(__name__)

from Setup import Setup
setup = Setup()

from TTGammaEFT.Analysis.MCBasedEstimate       import MCBasedEstimate
from TTGammaEFT.Analysis.DataDrivenQCDEstimate import DataDrivenQCDEstimate
from TTGammaEFT.Analysis.SetupHelpers          import default_sampleList

#from collections import OrderedDict
bkgEstimators = []
for sample in default_sampleList:
    if sample.count("DD"): bkgEstimators.append( DataDrivenDYEstimate( name=sample,                               cacheDir="analysis" ) )
    else:                  bkgEstimators.append( MCBasedEstimate(      name=sample, sample=setup.samples[sample], cacheDir="analysis" ) )

nList = [e.name for e in bkgEstimators]
assert len(list(set(nList))) == len(nList), "Names of bkgEstimators are not unique: %s"%",".join(nList)
