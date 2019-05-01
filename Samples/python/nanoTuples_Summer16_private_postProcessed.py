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
from TTGammaEFT.Tools.user import postprocessing_directoryMC2016 as postprocessing_directory

# Redirector
try:
    redirector = sys.modules['__main__'].redirector
except:
    from TTGammaEFT.Tools.user import redirector as redirector

logger.info( "Loading MC samples from directory %s", os.path.join( data_directory, postprocessing_directory ) )

# Directories
dirs = {}

dirs['DY_LO']            = ["DYJetsToLL_M50_LO_ext1_comb", "DYJetsToLL_M10to50_NLO" ]

dirs['TT_pow']           = ["TTLep_pow", "TTSingleLep_pow" ] 

dirs['TTGJets']          = ["TTGJets_comb"]
dirs['TTG']              = ["TTGLep", "TTGSemiTbar", "TTGHad", "TTGSemiTbar"] #TTGSemiT

dirs['singleTop']        = ["TBar_tWch_ext", "T_tWch_ext", "T_tch_pow", "TBar_tch_pow" ]

dirs['ZGTo2LG']          = ["ZGTo2LG_ext"]

dirs['TG']               = ["TGJets"]
dirs['WJets']            = ["WJetsToLNu_comb"]
dirs['WG']               = ["WGToLNuG"]

# other
dirs['TZQ']              = ["tZq_ll_ext"]
dirs['THQ']              = ["THQ"]
dirs['THW']              = ["THW"]
dirs['TWZ']              = ["tWll", "tWnunu"]

dirs['TTW']              = ["TTWToLNu_ext2", "TTWToQQ"]
dirs['TTZ']              = ["TTZToLLNuNu_ext2_comb", "TTZToQQ"]

dirs['TTTT']             = ["TTTT"]

dirs['WWW']              = ["WWW_4F"]
dirs['WWZ']              = ["WWZ"]
dirs['WZZ']              = ["WZZ"]
dirs['ZZZ']              = ["ZZZ"]

dirs['VV']               = ["VVTo2L2Nu_comb"]
dirs['WW']               = ["WWTo1L1Nu2Q"]
dirs['WZ']               = ["WZTo1L3Nu", "WZTo1L1Nu2Q", "WZTo2L2Q", "WZTo3LNu_ext"]
dirs['ZZ']               = ["ZZTo2L2Q", "ZZTo2Q2Nu" ] #"ZZTo2L2Nu"

dirs['GluGlu']           = ["GluGluToContinToZZTo2e2mu", "GluGluToContinToZZTo2e2tau", "GluGluToContinToZZTo2mu2tau", "GluGluToContinToZZTo4e", "GluGluToContinToZZTo4mu", "GluGluToContinToZZTo4tau" ]

dirs['other']            = []
dirs['other']           += dirs['TZQ']  + dirs['THQ']  + dirs['TWZ'] + dirs['THW']
dirs['other']           += dirs['TTW']  + dirs['TTZ']
dirs['other']           += dirs['TTTT']
dirs['other']           += dirs['WWW']  + dirs['WWZ']  + dirs['WZZ']  + dirs['ZZZ']
dirs['other']           += dirs['VV']
dirs['other']           += dirs['WW']   + dirs['WZ']  + dirs['ZZ']
dirs['other']           += dirs['GluGlu']

dirs['all_noOther']      = dirs['TTG'] + dirs['TT_pow'] + dirs['DY_LO'] + dirs['singleTop'] + dirs['ZGTo2LG']
dirs['all']              = dirs['all_noOther'] + dirs['other']

directories = { key : [ os.path.join( data_directory, postprocessing_directory, dir) for dir in dirs[key] ] for key in dirs.keys() }

# Samples
DY_LO_16           = Sample.fromDPMDirectory(name="DY_LO",            treeName="Events", redirector=redirector, isData=False, color=color.DY,              texName="DY (LO)",           directory=directories['DY_LO'])
TT_pow_16          = Sample.fromDPMDirectory(name="TT_pow",           treeName="Events", redirector=redirector, isData=False, color=color.TT,              texName="t#bar{t}",          directory=directories['TT_pow'])
singleTop_16       = Sample.fromDPMDirectory(name="singleTop",        treeName="Events", redirector=redirector, isData=False, color=color.T,               texName="single-t",          directory=directories['singleTop'])
TTG_16             = Sample.fromDPMDirectory(name="TTG",              treeName="Events", redirector=redirector, isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories['TTG'])
WJets_16           = Sample.fromDPMDirectory(name="WJets",            treeName="Events", redirector=redirector, isData=False, color=color.W,               texName="W+jets",            directory=directories['WJets'])
ZG_16              = Sample.fromDPMDirectory(name="ZG",               treeName="Events", redirector=redirector, isData=False, color=color.ZGamma,          texName="Z#gamma",           directory=directories['ZGTo2LG'] )
TG_16              = Sample.fromDPMDirectory(name="TG",               treeName="Events", redirector=redirector, isData=False, color=color.TGamma,          texName="t#gamma",           directory=directories['TG'])
WG_16              = Sample.fromDPMDirectory(name="WG",               treeName="Events", redirector=redirector, isData=False, color=color.WGamma,          texName="W#gamma",           directory=directories['WG'])
#other_16           = Sample.fromDPMDirectory(name="other",            treeName="Events", redirector=redirector, isData=False, color=color.Other,           texName="other",             directory=directories['other'])
#all_16             = Sample.fromDPMDirectory(name="all",              treeName="Events", redirector=redirector, isData=False, color=color.TT,              texName="all",               directory=directories['all'])
all_noOther_16     = Sample.fromDPMDirectory(name="all_noOther",      treeName="Events", redirector=redirector, isData=False, color=color.TT,              texName="all_noOther",       directory=directories['all_noOther'])

signals = []

if __name__ == "__main__":

    def get_parser():
        ''' Argument parser for post-processing module.
        '''
        import argparse
        argParser = argparse.ArgumentParser(description = "Argument parser for nanoPostProcessing")
        argParser.add_argument('--check',       action='store_true', help="check root files?")
        argParser.add_argument('--deepcheck',   action='store_true', help="check events of root files?")
        argParser.add_argument('--checkWeight', action='store_true', help="check weight?")
        argParser.add_argument('--remove',      action='store_true', help="remove corrupt root files?")
        argParser.add_argument('--log',         action='store_true', help="print each filename?")
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
