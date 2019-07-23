# Logging
import logging
logger = logging.getLogger(__name__)

from TTGammaEFT.Analysis.DataDrivenQCDEstimate       import DataDrivenQCDEstimate
from TTGammaEFT.Analysis.MCBasedEstimate             import MCBasedEstimate
from TTGammaEFT.Analysis.SetupHelpers                import default_sampleList
from TTGammaEFT.Analysis.Region                      import *

class estimatorList:
    def __init__(self, setup, samples=default_sampleList):
        for s in samples:
            if "DD" in s:
                setattr(self, s, DataDrivenQCDEstimate(name=s) )
            else:
                setattr(self, s, MCBasedEstimate(name=s, sample=setup.samples[s]))


    def constructEstimatorList(self, samples):
        self.estimatorList = [ getattr(self, s) for s in samples ]
        return self.estimatorList
