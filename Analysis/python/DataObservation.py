import os
import json

# Logging
import logging
logger = logging.getLogger(__name__)

from Analysis.Tools.u_float           import u_float
from Analysis.Tools.DirDB             import DirDB
from TTGammaEFT.Analysis.SetupHelpers import dilepChannels, lepChannels
from TTGammaEFT.Analysis.Region       import Region
from TTGammaEFT.Tools.user            import cache_directory

class DataObservation():

    def __init__(self, name, cacheDir=None):
        self.name = name
        self.sample = sample
        self.initCache(cacheDir)

    def initCache(self, cacheDir="dataObs"):
        if cacheDir:
            self.cacheDir = os.path.join(cache_directory, cacheDir)
            try:    os.makedirs(cacheDir)
            except: pass

            cacheDirName       = os.path.join(cacheDir, self.name)
            self.cache = DirDB(cacheDirName)
            if not self.cache: raise

        else:
            self.cache=None

    def uniqueKey(self, region, channel, setup):
        ## this is used in MCBasedEstimate
        if hasattr(setup, "blinding"): return str(region), channel, json.dumps(setup.sys, sort_keys=True), json.dumps(setup.parameters, sort_keys=True), json.dumps(setup.lumi, sort_keys=True), setup.blinding
        else:                          return str(region), channel, json.dumps(setup.sys, sort_keys=True), json.dumps(setup.parameters, sort_keys=True), json.dumps(setup.lumi, sort_keys=True)

    # alias for cachedObservation to make it easier to call the same function as for the mc"s
    def cachedEstimate(self, region, channel, setup, save=True, overwrite=False):
        return self.cachedObservation(region, channel, setup, overwrite=overwrite)

    def cachedObservation(self, region, channel, setup, save=True, overwrite=False):
        key =  self.uniqueKey(region, channel, setup)
        if self.cache and self.cache.contains(key) and not overwrite and channel != "all":
            res = self.cache.get(key)
            logger.debug( "Loading cached %s result for %r : %r"%(self.name, key, res) )
            return res
        elif self.cache:
            logger.debug( "Adding cached %s result for %r"%(self.name, key) )
            return self.cache.add( key, self.observation( region, channel, setup, overwrite), overwrite=True )
        else:
            return self.observation( region, channel, setup, overwrite )

    def observation(self, region, channel, setup, overwrite):

        if channel=="all":
            return sum([self.cachedEstimate(region, c, setup, overwrite=overwrite) for c in lepChannels ])

        elif channel=="SFtight":
            return sum([self.cachedEstimate(region, c, setup, overwrite=overwrite) for c in dilepChannels ])

        else:
            preSelection = setup.preselection("Data", channel=channel)
            cut = "&&".join([region.cutString(setup.sys["selectionModifier"]), preSelection["cut"]])

            logger.debug( "Using cut %s"% cut )

            if hasattr(setup, "blinding") and setup.blinding: weight = "weight*" + setup.blinding
            else:                                             weight = "weight"
            return u_float(**self.sample.getYieldFromDraw(selectionString = cut, weightString = weight) )
