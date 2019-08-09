# Standard Imports
import os, sys
import ROOT

# RootTools Imports
from RootTools.core.Sample import Sample

# Colors
from TTGammaEFT.Samples.color import color

# Data directory
from TTGammaEFT.Tools.user import dpm_directory as data_directory
data_directory += "postprocessed/"
from TTGammaEFT.Samples.default_locations import postprocessing_locations
postprocessing_directory = postprocessing_locations.MC2018_semilep
if "gammaSkim" in os.environ and os.environ["gammaSkim"] == "True": postprocessing_directory = postprocessing_directory.replace("/semilep/", "/semilepGamma/")

# Redirector
try:
    redirector = sys.modules["__main__"].redirector
except:
    from TTGammaEFT.Tools.user import redirector as redirector

# Logging
if __name__=="__main__":
    import Analysis.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
else:
    import logging
    logger = logging.getLogger(__name__)

logger.info( "Loading MC samples from directory %s", os.path.join( data_directory, postprocessing_directory ) )

dirs = {}
dirs["DY_LO"]            = ["DYJetsToLL_M50_LO", "DYJetsToLL_M10to50_LO"]

dirs["TT_pow"]           = ["TTLep_pow", "TTSingleLep_pow"]#, "TTHad_pow" ]

dirs["TTG"]              = ["TTGLep", "TTGSemiTbar", "TTGSemiT", "TTGHad"]
dirs["TTG_priv"]         = ["TTGLep_priv", "TTGSemi_priv", "TTGHad_priv"]
dirs["TTG_NoFullyHad_priv"] = ["TTGNoFullyHad_priv"]

dirs["singleTop"]        = ["T_tWch", "TBar_tWch", "TToLeptons_sch_amcatnlo", "T_tch_pow", "TBar_tch_pow"]

# other
dirs["TZQ"]              = ["tZq_ll"]
dirs["TWZ"]              = ["tWll"]

dirs["TTW"]              = ["TTWToLNu", "TTWToQQ"]
dirs["TTZ"]              = ["TTZToLLNuNu", "TTZToLLNuNu_m1to10"]

dirs["TTWZ"]             = ["TTWZ"]
dirs["TTZZ"]             = ["TTZZ"]
dirs["TTWW"]             = ["TTWW"]

dirs["WWZ"]              = ["WWZ"]
dirs["WZZ"]              = ["WZZ"]
dirs["ZZZ"]              = ["ZZZ"]

dirs["ZGToLLG"]          = ["ZGToLLG"]
dirs["TG"]               = ["TGJets"]
dirs["WJets"]            = ["WJetsToLNu"]
dirs["WG"]               = ["WGToLNuG"]
dirs["WG_NLO"]           = ["WGToLNuG_amcatnlo_ext1"]

dirs["VV"]               = ["VVTo2L2Nu"]

dirs["WW"]               = [] #["WWTo2L2Nu"]
dirs["ZZ"]               = ["ZZTo2L2Q", "ZZTo4L"] #"ZZTo2L2Nu"
dirs["WZ"]               = ["WZTo3LNu_amcatnlo"]

dirs["GluGlu"]           = ["GluGluToContinToZZTo2e2mu", "GluGluToContinToZZTo2e2tau"]

dirs["other"]            = []
dirs["other"]           += dirs["TZQ"]  + dirs["TWZ"]
dirs["other"]           += dirs["TTW"]  + dirs["TTZ"]
dirs["other"]           += dirs["TTWZ"] + dirs["TTZZ"] + dirs["TTWW"]
dirs["other"]           += dirs["WWZ"] + dirs["WZZ"]  + dirs["ZZZ"]
dirs["other"]           += dirs["VV"]
dirs["other"]           += dirs["WW"]   + dirs["WZ"]  + dirs["ZZ"]
dirs["other"]           += dirs["GluGlu"]

dirs["QCD"]              = [ "QCD_Mu_pt15to20", "QCD_Mu_pt20to30", "QCD_Mu_pt30to50", "QCD_Mu_pt50to80", "QCD_Mu_pt80to120", "QCD_Mu_pt120to170_comb", "QCD_Mu_pt170to300", "QCD_Mu_pt300to470_comb", "QCD_Mu_pt470to600", "QCD_Mu_pt600to800", "QCD_Mu_pt800to1000_ext", "QCD_Mu_pt1000toInf" ]
dirs["QCD"]             += [ "QCD_Ele_pt20to30", "QCD_Ele_pt30to50", "QCD_Ele_pt50to80", "QCD_Ele_pt80to120", "QCD_Ele_pt120to170", "QCD_Ele_pt170to300", "QCD_Ele_pt300toInf" ]

dirs["GJets"]            = ["GJets_HT40to100", "GJets_HT100to200", "GJets_HT200to400", "GJets_HT400to600", "GJets_HT600toInf_comb"]

dirs["all_noOther_noTT"] = dirs["DY_LO"] + dirs["singleTop"] + dirs["ZGToLLG"] + dirs["TG"] + dirs["WJets"] + dirs["WG"]# + dirs["QCD"] + dirs["GJets"]
dirs["all_noTT"]         = dirs["all_noOther_noTT"] + dirs["other"]

dirs["all_noOther"]      = dirs["TTG_priv"] + dirs["TT_pow"] + dirs["DY_LO"] + dirs["singleTop"] + dirs["ZGToLLG"] + dirs["TG"] + dirs["WJets"] + dirs["WG"] + dirs["QCD"] + dirs["GJets"]
dirs["all"]              = dirs["all_noOther"] + dirs["other"]

dirs["all_noQCD_noOther"] = dirs["TTG_priv"] + dirs["TT_pow"] + dirs["DY_LO"] + dirs["singleTop"] + dirs["ZGToLLG"] + dirs["TG"] + dirs["WJets"] + dirs["WG"]
dirs["all_noQCD"]         = dirs["all_noQCD_noOther"] + dirs["other"]

dirs["VG"]               = dirs["ZGToLLG"] + dirs["WG"]
dirs["rest"]             = dirs["singleTop"] + dirs["TG"] + dirs["other"]               

directories = { key : [ os.path.join( data_directory, postprocessing_directory, dir) for dir in dirs[key] ] for key in dirs.keys() }

# Samples
DY_LO_18            = Sample.fromDPMDirectory(name="DY_LO",            treeName="Events", redirector=redirector, isData=False, color=color.DY,              texName="DY (LO)",           directory=directories["DY_LO"], noCheckProxy=False)
TT_pow_18           = Sample.fromDPMDirectory(name="TT_pow",           treeName="Events", redirector=redirector, isData=False, color=color.TT,              texName="t#bar{t}",          directory=directories["TT_pow"], noCheckProxy=True)
singleTop_18        = Sample.fromDPMDirectory(name="singleTop",        treeName="Events", redirector=redirector, isData=False, color=color.T,               texName="single-t",          directory=directories["singleTop"], noCheckProxy=True)
#TTG_18              = Sample.fromDPMDirectory(name="TTG",              treeName="Events", redirector=redirector, isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories["TTG"], noCheckProxy=True)
#TTGSemiLep_18       = Sample.fromDPMDirectory(name="TTG",              treeName="Events", redirector=redirector, isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories["TTGSemiLep"], noCheckProxy=True)
TTG_priv_18         = Sample.fromDPMDirectory(name="TTG",              treeName="Events", redirector=redirector, isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories["TTG_priv"], noCheckProxy=True)

TTG_NoFullyHad_priv_18 = Sample.fromDPMDirectory(name="TTG",              treeName="Events", redirector=redirector, isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories["TTG_NoFullyHad_priv"], noCheckProxy=True)

WJets_18            = Sample.fromDPMDirectory(name="WJets",            treeName="Events", redirector=redirector, isData=False, color=color.W,               texName="W+jets",            directory=directories["WJets"], noCheckProxy=True)
ZG_18               = Sample.fromDPMDirectory(name="ZG",               treeName="Events", redirector=redirector, isData=False, color=color.ZGamma,          texName="Z#gamma",           directory=directories["ZGToLLG"], noCheckProxy=True)
TG_18               = Sample.fromDPMDirectory(name="TG",               treeName="Events", redirector=redirector, isData=False, color=color.TGamma,          texName="t#gamma",           directory=directories["TG"], noCheckProxy=True)
WG_18               = Sample.fromDPMDirectory(name="WG",               treeName="Events", redirector=redirector, isData=False, color=color.WGamma,          texName="W#gamma",           directory=directories["WG"], noCheckProxy=True)
WG_NLO_18           = Sample.fromDPMDirectory(name="WG",               treeName="Events", redirector=redirector, isData=False, color=color.WGamma,          texName="W#gamma",           directory=directories["WG_NLO"], noCheckProxy=True)
other_18            = Sample.fromDPMDirectory(name="other",            treeName="Events", redirector=redirector, isData=False, color=color.Other,           texName="other",             directory=directories["other"], noCheckProxy=True)
QCD_18             = Sample.fromDPMDirectory(name="QCD",              treeName="Events", redirector=redirector, isData=False, color=color.QCD,             texName="multijets",         directory=directories["QCD"], noCheckProxy=True)
GJets_18           = Sample.fromDPMDirectory(name="GJets",            treeName="Events", redirector=redirector, isData=False, color=color.GJets,           texName="#gamma+jets",       directory=directories["GJets"], noCheckProxy=True)

VG_18              = Sample.fromDPMDirectory(name="VG",               treeName="Events", redirector=redirector, isData=False, color=color.WGamma,          texName="V+#gamma",          directory=directories["VG"], noCheckProxy=True)
rest_18            = Sample.fromDPMDirectory(name="other",             treeName="Events", redirector=redirector, isData=False, color=color.Other,          texName="other",             directory=directories["rest"], noCheckProxy=True)

all_18              = Sample.fromDPMDirectory(name="all",              treeName="Events", redirector=redirector, isData=False, color=color.TT,              texName="all",               directory=directories["all"], noCheckProxy=True)
all_noOther_18      = Sample.fromDPMDirectory(name="all_noOther",      treeName="Events", redirector=redirector, isData=False, color=color.TT,              texName="all_noOther",       directory=directories["all_noOther"], noCheckProxy=True)
all_noQCD_18        = Sample.fromDPMDirectory(name="all",              treeName="Events", redirector=redirector, isData=False, color=color.TT,              texName="all",               directory=directories["all_noQCD"], noCheckProxy=True)
all_noTT_18         = Sample.fromDPMDirectory(name="all_noTT",         treeName="Events", redirector=redirector, isData=False, color=color.TT,              texName="all_noTT",          directory=directories["all_noTT"], noCheckProxy=True)
all_noOther_noTT_18 = Sample.fromDPMDirectory(name="all_noOther_noTT", treeName="Events", redirector=redirector, isData=False, color=color.TT,              texName="all_noOther_noTT",  directory=directories["all_noOther_noTT"], noCheckProxy=True)

signals = []


if __name__ == "__main__":

    def get_parser():
        """ Argument parser for post-processing module.
        """
        import argparse
        argParser = argparse.ArgumentParser(description = "Argument parser for nanoPostProcessing")
        argParser.add_argument("--check",   action="store_true", help="check root files?")
        argParser.add_argument("--deepcheck",   action="store_true", help="check events of root files?")
        argParser.add_argument("--checkWeight", action="store_true", help="check weight?")
        argParser.add_argument("--remove",  action="store_true", help="remove corrupt root files?")
        argParser.add_argument("--log",         action="store_true", help="print each filename?")
        return argParser

    args = get_parser().parse_args()

    if not (args.check or args.deepcheck or args.checkWeight): sys.exit(0)

    # check Root Files
    from Analysis.Tools.helpers import checkRootFile, deepCheckRootFile, deepCheckWeight
    from multiprocessing        import Pool

    def checkFile( file ):
                if args.log: logger.info( "Checking filepath: %s"%file )
                corrupt = False
                if args.check:
                    corrupt = not checkRootFile(file, checkForObjects=["Events"])
                if args.deepcheck and not corrupt:
                    corrupt = not deepCheckRootFile(file)
                if args.checkWeight and not corrupt:
                    corrupt = not deepCheckWeight(file)
                if corrupt:
                    if file.startswith("root://hephyse.oeaw.ac.at/"):
                        file = file.split("root://hephyse.oeaw.ac.at/")[1]
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
