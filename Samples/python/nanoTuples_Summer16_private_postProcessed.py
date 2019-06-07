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
postprocessing_directory = postprocessing_locations.MC2016
if "gammaSkim" in os.environ and os.environ["gammaSkim"] == "True": postprocessing_directory = postprocessing_directory.replace("/dilep/", "/dilepGamma/")

# Redirector
try:
    redirector = sys.modules["__main__"].redirector
except:
    from TTGammaEFT.Tools.user import redirector as redirector

logger.info( "Loading MC samples from directory %s", os.path.join( data_directory, postprocessing_directory ) )

# Directories
dirs = {}

dirs["DY_LO"]            = ["DYJetsToLL_M50_LO_ext1_comb", "DYJetsToLL_M10to50_NLO" ]

dirs["DY_HT"]            = ["DYJetsToLL_M50_HT70to100", "DYJetsToLL_M50_HT100to200_ext", "DYJetsToLL_M50_HT200to400_comb", "DYJetsToLL_M50_HT400to600_comb", "DYJetsToLL_M50_HT600to800", "DYJetsToLL_M50_HT800to1200", "DYJetsToLL_M50_HT1200to2500", "DYJetsToLL_M50_HT2500toInf" ]
dirs["DY_HT"]           += ["DYJetsToLL_M5to50_HT70to100", "DYJetsToLL_M5to50_HT100to200_comb", "DYJetsToLL_M5to50_HT200to400_comb", "DYJetsToLL_M5to50_HT400to600_comb", "DYJetsToLL_M5to50_HT600toInf"]

dirs["TT_pow"]           = ["TTLep_pow", "TTSingleLep_pow" ] 

dirs["TTGJets"]          = ["TTGJets_comb"]
dirs["TTGLep"]           = ["TTGLep"]
dirs["TTGSemiLep"]       = ["TTGSemiTbar", "TTGSemiT"] 
dirs["TTGLep_priv"]      = ["TTGLep_priv"]
dirs["TTGSemiLep_priv"]  = ["TTGSemi_priv"] 
dirs["TTG"]              = ["TTGLep", "TTGSemiTbar", "TTGHad", "TTGSemiT"] 
dirs["TTG_priv"]         = ["TTGLep_priv", "TTGSemi_priv", "TTGHad_priv"]

dirs["singleTop"]        = ["TBar_tWch_ext", "T_tWch_ext", "T_tch_pow", "TBar_tch_pow", "TToLeptons_sch_amcatnlo" ]

dirs["ZGTo2LG"]          = ["ZGTo2LG_ext"]
dirs["ZGToLLG"]          = ["ZGToLLG"]

dirs["TG"]               = ["TGJets"]
dirs["WJets"]            = ["WJetsToLNu_comb"]
dirs["WJets_HT"]         = ["WJetsToLNu_HT70to100", "WJetsToLNu_HT100to200", "WJetsToLNu_HT200to400_comb", "WJetsToLNu_HT400to600_comb", "WJetsToLNu_HT600to800_comb", "WJetsToLNu_HT800to1200_comb", "WJetsToLNu_HT1200to2500_comb", "WJetsToLNu_HT2500toInf_comb"]
dirs["WG"]               = ["WGToLNuG"]
dirs["WG_NLO"]           = ["WGToLNuG_amcatnlo"]

# other

dirs["TZQ"]              = ["tZq_ll_ext"]
dirs["THQ"]              = ["THQ"]
dirs["THW"]              = ["THW"]
dirs["TWZ"]              = ["tWll", "tWnunu"]

dirs["TTW"]              = ["TTWToLNu_ext2", "TTWToQQ"]
dirs["TTZ"]              = ["TTZToLLNuNu_ext2_comb", "TTZToQQ", "TTZToLLNuNu_m1to10"]
dirs["TTH"]              = ["TTHnobb_pow"] #"TTHbb"

dirs["TTTT"]             = ["TTTT"]
dirs["TTWW"]             = ["TTWW"]
dirs["TTWZ"]             = ["TTWZ"]
dirs["TTZZ"]             = ["TTZZ"]

dirs["WWW"]              = ["WWW_4F"]
dirs["WWZ"]              = ["WWZ"]
dirs["WZZ"]              = ["WZZ"]
dirs["ZZZ"]              = ["ZZZ"]

dirs["VV"]               = ["VVTo2L2Nu_comb"]
dirs["WW"]               = ["WWTo1L1Nu2Q"]
dirs["WZ"]               = ["WZTo1L3Nu", "WZTo1L1Nu2Q", "WZTo2L2Q", "WZTo3LNu_ext"]
dirs["ZZ"]               = ["ZZTo2L2Q", "ZZTo2Q2Nu", "ZZTo4L" ] #"ZZTo2L2Nu"

dirs["GluGlu"]           = ["GluGluToContinToZZTo2e2mu", "GluGluToContinToZZTo2e2tau", "GluGluToContinToZZTo2mu2tau", "GluGluToContinToZZTo4e", "GluGluToContinToZZTo4mu", "GluGluToContinToZZTo4tau" ]

dirs["other"]            = []
dirs["other"]           += dirs["TZQ"]  + dirs["THQ"]  + dirs["TWZ"] + dirs["THW"]
dirs["other"]           += dirs["TTW"]  + dirs["TTZ"]  + dirs["TTH"]
dirs["other"]           += dirs["TTTT"] + dirs["TTWW"] + dirs["TTWZ"] + dirs["TTZZ"]
dirs["other"]           += dirs["WWW"]  + dirs["WWZ"]  + dirs["WZZ"]  + dirs["ZZZ"]
dirs["other"]           += dirs["VV"]
dirs["other"]           += dirs["WW"]   + dirs["WZ"]   + dirs["ZZ"]
dirs["other"]           += dirs["WG_NLO"]
dirs["other"]           += dirs["GluGlu"]

dirs["all_noOther"]      = dirs["TTG_priv"] + dirs["TT_pow"] + dirs["DY_LO"] + dirs["singleTop"] + dirs["ZGToLLG"]
dirs["all"]              = dirs["all_noOther"] + dirs["other"]

dirs["W"]                = dirs["WJets"] + dirs["WG_NLO"]

directories = { key : [ os.path.join( data_directory, postprocessing_directory, dir) for dir in dirs[key] ] for key in dirs.keys() }

# Samples
DY_LO_16           = Sample.fromDPMDirectory(name="DY_LO",            treeName="Events", redirector=redirector, isData=False, color=color.DY,              texName="DY (LO)",           directory=directories["DY_LO"], noCheckProxy=False)
DY_HT_16           = Sample.fromDPMDirectory(name="DY_LO",            treeName="Events", redirector=redirector, isData=False, color=color.DY,              texName="DY (LO)",           directory=directories["DY_HT"], noCheckProxy=True)
TT_pow_16          = Sample.fromDPMDirectory(name="TT_pow",           treeName="Events", redirector=redirector, isData=False, color=color.TT,              texName="t#bar{t}",          directory=directories["TT_pow"], noCheckProxy=True)
singleTop_16       = Sample.fromDPMDirectory(name="singleTop",        treeName="Events", redirector=redirector, isData=False, color=color.T,               texName="single-t",          directory=directories["singleTop"], noCheckProxy=True)
TTG_16             = Sample.fromDPMDirectory(name="TTG",              treeName="Events", redirector=redirector, isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories["TTG"], noCheckProxy=True)
TTGLep_16          = Sample.fromDPMDirectory(name="TTGLep",           treeName="Events", redirector=redirector, isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories["TTGLep"], noCheckProxy=True)
TTGSemiLep_16      = Sample.fromDPMDirectory(name="TTGSemiLep",       treeName="Events", redirector=redirector, isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories["TTGSemiLep"], noCheckProxy=True)
TTGLep_priv_16     = Sample.fromDPMDirectory(name="TTGLep",           treeName="Events", redirector=redirector, isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories["TTGLep_priv"], noCheckProxy=True)
TTGSemiLep_priv_16 = Sample.fromDPMDirectory(name="TTGSemiLep",       treeName="Events", redirector=redirector, isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories["TTGSemiLep_priv"], noCheckProxy=True)
TTG_priv_16        = Sample.fromDPMDirectory(name="TTG",              treeName="Events", redirector=redirector, isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories["TTG_priv"], noCheckProxy=True)

WJets_16           = Sample.fromDPMDirectory(name="WJets",            treeName="Events", redirector=redirector, isData=False, color=color.W,               texName="W+jets",            directory=directories["WJets"], noCheckProxy=True)
WJets_HT_16        = Sample.fromDPMDirectory(name="WJets",            treeName="Events", redirector=redirector, isData=False, color=color.W,               texName="W+jets",            directory=directories["WJets_HT"], noCheckProxy=True)
ZG_16              = Sample.fromDPMDirectory(name="ZG",               treeName="Events", redirector=redirector, isData=False, color=color.ZGamma,          texName="Z#gamma",           directory=directories["ZGToLLG"], noCheckProxy=True)
TG_16              = Sample.fromDPMDirectory(name="TG",               treeName="Events", redirector=redirector, isData=False, color=color.TGamma,          texName="t#gamma",           directory=directories["TG"], noCheckProxy=True)
WG_16              = Sample.fromDPMDirectory(name="WG",               treeName="Events", redirector=redirector, isData=False, color=color.WGamma,          texName="W#gamma",           directory=directories["WG"], noCheckProxy=True)
WG_NLO_16          = Sample.fromDPMDirectory(name="WG",               treeName="Events", redirector=redirector, isData=False, color=color.WGamma,          texName="W#gamma",           directory=directories["WG_NLO"], noCheckProxy=True)
W_16               = Sample.fromDPMDirectory(name="W",                treeName="Events", redirector=redirector, isData=False, color=color.WGamma,          texName="W#gamma+Wjets",     directory=directories["W"], noCheckProxy=True)
other_16           = Sample.fromDPMDirectory(name="other",            treeName="Events", redirector=redirector, isData=False, color=color.Other,           texName="other",             directory=directories["other"], noCheckProxy=True)
all_16             = Sample.fromDPMDirectory(name="all",              treeName="Events", redirector=redirector, isData=False, color=color.TT,              texName="all",               directory=directories["all"], noCheckProxy=True)
all_noOther_16     = Sample.fromDPMDirectory(name="all_noOther",      treeName="Events", redirector=redirector, isData=False, color=color.TT,              texName="all_noOther",       directory=directories["all_noOther"], noCheckProxy=True)

signals = []

if __name__ == "__main__":

    def get_parser():
        """ Argument parser for post-processing module.
        """
        import argparse
        argParser = argparse.ArgumentParser(description = "Argument parser for nanoPostProcessing")
        argParser.add_argument("--check",       action="store_true", help="check root files?")
        argParser.add_argument("--deepcheck",   action="store_true", help="check events of root files?")
        argParser.add_argument("--checkWeight", action="store_true", help="check weight?")
        argParser.add_argument("--remove",      action="store_true", help="remove corrupt root files?")
        argParser.add_argument("--log",         action="store_true", help="print each filename?")
        return argParser

    args = get_parser().parse_args()

    redir="root://hephyse.oeaw.ac.at/"
    if not (args.check or args.deepcheck or args.checkWeight): sys.exit(0)

    # check Root Files
    from Analysis.Tools.helpers import checkRootFile, deepCheckRootFile, deepCheckWeight
    from multiprocessing        import Pool

    def checkFile( file ):
        print file
        if not file:
            logger.info( "File not found!" )
            return
#        elif args.log: logger.info( "Checking filepath: %s"%file )
        corrupt = False
        if args.check:
            corrupt = not checkRootFile(file, checkForObjects=["Events"])
        if args.deepcheck and not corrupt:
            corrupt = not deepCheckRootFile(file)
        if args.checkWeight and not corrupt:
            corrupt = not deepCheckWeight(file)
        if corrupt:
            if file.startswith(redir):
                file = file.split(redir)[1]
            logger.info( "File corrupt: %s"%file )
            if args.remove:
                logger.info( "Removing file: %s"%file )
                os.system( "/usr/bin/rfrm -f %s"%file )

    pathes = [ path for dirList in directories.values() for path in dirList ]

    files = []
    for path in pathes:
        try:
            sample = Sample.fromDPMDirectory(name="sample", treeName="Events", redirector=redirector, directory=path)
            files += sample.files
            del sample
        except:
            logger.info( "Sample not processed: %s"%path )

    pool = Pool( processes=16 )
    _ = pool.map( checkFile, files )
    pool.close()
