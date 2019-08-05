# Logging
import logging
logger = logging.getLogger(__name__)

from TTGammaEFT.Analysis.SystematicEstimator import SystematicEstimator
from TTGammaEFT.Analysis.Region              import Region
from TTGammaEFT.Analysis.SetupHelpers        import dilepChannels, lepChannels
from Analysis.Tools.u_float                  import u_float

class SumEstimate(SystematicEstimator):
    def __init__(self, name, cacheDir=None):
        super(SumEstimate, self).__init__(name, cacheDir=cacheDir)

    def _estimate(self, region, channel, setup, overwrite=False):
        if channel=='all':
            # 'all' is the total of all contributions
            return sum([self.cachedEstimate(region, c, setup) for c in lepChannels])
        if channel=='SFtight':
            return sum([self.cachedEstimate(region, c, setup) for c in dilepChannels])
        else:
            raise NotImplementedError("Run sum_estimates.py first")
