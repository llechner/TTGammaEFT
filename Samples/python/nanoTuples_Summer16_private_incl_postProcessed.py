# Standard Imports
import os, sys
import ROOT

# RootTools Imports
from RootTools.core.Sample import Sample

# Logging
if __name__=="__main__":
    import Analysis.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
else:
    import logging
    logger = logging.getLogger(__name__)

# Colors
from TTGammaEFT.Samples.color import color

# Data directory
from TTGammaEFT.Tools.user import dpm_directory as data_directory
data_directory += "postprocessed/"
from TTGammaEFT.Samples.default_locations import postprocessing_locations
postprocessing_directory = postprocessing_locations.MC2016_incl

# Redirector
try:
    redirector = sys.modules["__main__"].redirector
except:
    from TTGammaEFT.Tools.user import redirector as redirector

logger.info( "Loading MC samples from directory %s", os.path.join( data_directory, postprocessing_directory ) )

# Directories
dirs = {}
dirs["TTG_NoFullyHad_priv"] = ["TTGNoFullyHad_priv"]
dirs["TTG_NoFullyHad_fnal"] = ["TTGNoFullyHad_fnal"]

directories = { key : [ os.path.join( data_directory, postprocessing_directory, dir) for dir in dirs[key] ] for key in dirs.keys() }

# Samples
TTG_NoFullyHad_priv_16 = Sample.fromDPMDirectory(name="TTG",              treeName="Events", redirector=redirector, isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories["TTG_NoFullyHad_priv"], noCheckProxy=True)
TTG_NoFullyHad_fnal_16 = Sample.fromDPMDirectory(name="TTG",              treeName="Events", redirector=redirector, isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories["TTG_NoFullyHad_fnal"], noCheckProxy=True)


