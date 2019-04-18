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
from TTGammaEFT.Tools.user import postprocessing_directoryMC2017 as postprocessing_directory

logger.info( "Loading MC samples from directory %s", os.path.join( data_directory, postprocessing_directory ) )

dirs = {}
dirs['DY_LO']            = ["DYJetsToLL_M50_LO_comb", "DYJetsToLL_M10to50_LO"]
dirs['TT_pow']           = ["TTLep_pow", "TTSemiLep_pow"]

dirs['singleTop']        = ["TBar_tWch_ext", "T_tWch_ext", "T_tch_pow", "TBar_tch_pow", "TToLeptons_sch_amcatnlo" ]

dirs['TTGJets']          = ["TTGJets"]
dirs['TTG']              = ["TTGLep", "TTGSemiTbar", "TTGSemiT", "TTGHad"]

dirs['TG']               = ["TGJets"]
dirs['WJets']            = ["WJetsToLNu_comb"]
dirs['WG']               = ["WGToLNuG"]

dirs['TZQ']              = ["tZq_ll", "tZq_nunu"]
dirs['THQ']              = ["THQ"]
dirs['THW']              = ["THW"]

#dirs['TTW']              = ["TTW_LO_comb"]
dirs['TTW']              = ["TTWToLNu", "TTWToQQ"]
dirs['TTZ']              = ["TTZToQQ", "TTZToLLNuNu", "TTZToLLNuNu_m1to10"]

dirs['TTWZ']             = ["TTWZ"]
dirs['TTZZ']             = ["TTZZ"]
dirs['TTWW']             = ["TTWW"]
dirs['TTTT']             = ["TTTT"]

dirs['WWW']              = ["WWW_4F"]
dirs['WWZ']              = ["WWZ_4F"]
dirs['WZZ']              = ["WZZ"]
dirs['ZZZ']              = ["ZZZ"]

dirs['VV']               = ["VVTo2L2Nu"]
dirs['WW']               = ["WWToLNuQQ"] #, "WWTo1L1Nu2Q"] #"WWTo2L2Nu"
dirs['WZ']               = ["WZTo1L3Nu", "WZTo1L1Nu2Q", "WZTo2L2Q", "WZTo3LNu_amcatnlo"]
dirs['ZZ']               = ["ZZTo2L2Q"] #"ZZTo2L2Nu"

dirs['GluGlu']           = ["GluGluToContinToZZTo2e2mu", "GluGluToContinToZZTo2e2tau", "GluGluToContinToZZTo2mu2tau", "GluGluToContinToZZTo4e", "GluGluToContinToZZTo4mu"]

dirs['other']            = []
dirs['other']           += dirs['TZQ']  + dirs['THQ']  + dirs['THW']
dirs['other']           += dirs['TTW']  + dirs['TTZ']
dirs['other']           += dirs['TTWZ'] + dirs['TTZZ'] + dirs['TTWW'] + dirs['TTTT']
dirs['other']           += dirs['WWW']  + dirs['WWZ']  + dirs['WZZ']  + dirs['ZZZ']
dirs['other']           += dirs['VV']
dirs['other']           += dirs['WW']   + dirs['WZ']   + dirs['ZZ']
dirs['other']           += dirs['GluGlu']

dirs['all_noOther']      = dirs['TTG'] + dirs['TT_pow'] + dirs['DY_LO'] + dirs['singleTop']
dirs['all']              = dirs['all_noOther'] + dirs['other']

directories = { key : [ os.path.join( data_directory, postprocessing_directory, dir) for dir in dirs[key] ] for key in dirs.keys() }

# Samples
DY_LO_17           = Sample.fromDPMDirectory(name="DY_LO",            treeName="Events", isData=False, color=color.DY,              texName="DY (LO)",           directory=directories['DY_LO'])
TT_pow_17          = Sample.fromDPMDirectory(name="TT_pow",           treeName="Events", isData=False, color=color.TT,              texName="t#bar{t}",          directory=directories['TT_pow'])
singleTop_17       = Sample.fromDPMDirectory(name="singleTop",        treeName="Events", isData=False, color=color.T,               texName="single-t",          directory=directories['singleTop'])
TTG_17             = Sample.fromDPMDirectory(name="TTG",              treeName="Events", isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories['TTG'])
TG_17              = Sample.fromDPMDirectory(name="TG",               treeName="Events", isData=False, color=color.TGamma,          texName="t#gamma",           directory=directories['TG'])
WJets_17           = Sample.fromDPMDirectory(name="WJets",            treeName="Events", isData=False, color=color.W,               texName="W+jets",            directory=directories['WJets'])
WG_17              = Sample.fromDPMDirectory(name="WG",               treeName="Events", isData=False, color=color.WGamma,          texName="W#gamma",           directory=directories['WG'])
other_17           = Sample.fromDPMDirectory(name="other",            treeName="Events", isData=False, color=color.Other,           texName="other",             directory=directories['other'])
all_17             = Sample.fromDPMDirectory(name="all",              treeName="Events", isData=False, color=color.TT,              texName="all",               directory=directories['all'])
all_noOther_17     = Sample.fromDPMDirectory(name="all_noOther",      treeName="Events", isData=False, color=color.TT,              texName="all_noOther",       directory=directories['all_noOther'])

signals = []

if __name__ == "__main__":

    def get_parser():
        ''' Argument parser for post-processing module.
        '''
        import argparse
        argParser = argparse.ArgumentParser(description = "Argument parser for nanoPostProcessing")
        argParser.add_argument('--check',   action='store_true', help="check root files?")
        argParser.add_argument('--deepcheck',   action='store_true', help="check events of root files?")
        argParser.add_argument('--checkWeight', action='store_true', help="check weight?")
        argParser.add_argument('--remove',  action='store_true', help="remove corrupt root files?")
        argParser.add_argument('--log',         action='store_true', help="print each filename?")
        return argParser

    args = get_parser().parse_args()

    if not (args.check or args.deepcheck or args.checkWeight): sys.exit(0)

    # check Root Files
    from Analysis.Tools.helpers import checkRootFile, deepCheckRootFile, deepCheckWeight
    from multiprocessing        import Pool

    def checkFile( file ):
        if not file:
            logger.info( "File not found!" )
            return
        elif args.log: logger.info( "Checking filepath: %s"%file )
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
            sample = Sample.fromDPMDirectory(name="sample", treeName="Events", directory=path)
            files += sample.files
            del sample
        except:
            logger.info( "Sample not processed: %s"%path )

    pool = Pool( processes=16 )
    _ = pool.map( checkFile, files[::-1] )
    pool.close()
