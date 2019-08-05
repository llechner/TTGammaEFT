from Analysis.Tools.u_float                  import u_float

# Logging
import logging
logger = logging.getLogger(__name__)

from TTGammaEFT.Analysis.SystematicEstimator import SystematicEstimator
from TTGammaEFT.Analysis.SetupHelpers        import dilepChannels, lepChannels
from TTGammaEFT.Analysis.Region              import Region

class MCBasedEstimate(SystematicEstimator):
    def __init__(self, name, sample, cacheDir=None):
        super(MCBasedEstimate, self).__init__(name, cacheDir=cacheDir)
        self.sample=sample
        
    def _estimate(self, region, channel, setup, overwrite=False):

        ''' Concrete implementation of abstract method 'estimate' as defined in Systematic
        '''

        logger.debug( "MC prediction for %s channel %s" %(self.name, channel) )

        if channel=='all':
            # 'all' is the total of all contributions
            return sum([self.cachedEstimate(region, c, setup) for c in lepChannels])

        elif channel=='SFtight':
            # 'all' is the total of all contributions
            return sum([self.cachedEstimate(region, c, setup) for c in dilepChannels])

        else:
            preSelection = setup.preselection('MC', channel=channel)
            cut = "&&".join([region.cutString(setup.sys['selectionModifier']), preSelection['cut']])
            weight = preSelection['weightStr']

            logger.debug( "Using cut %s and weight %s"%(cut, weight) )
            return setup.lumi/1000.*u_float(**self.sample.getYieldFromDraw(selectionString = cut, weightString = weight) )
