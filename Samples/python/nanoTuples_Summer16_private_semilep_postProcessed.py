# Standard Imports
import os, sys
import ROOT

# RootTools Imports
from RootTools.core.Sample import Sample

# Logging
import logging
logger = logging.getLogger(__name__)

# Colors
from TTGammaEFT.Samples.color import color

# Data directory
#try:    data_directory = sys.modules['__main__'].data_directory
#except: from TTGammaEFT.Tools.user import data_directory2016 as data_directory
from TTGammaEFT.Tools.user import data_directory2016 as data_directory

# Take post processing directory if defined in main module
#try:    postprocessing_directory = sys.modules['__main__'].postprocessing_directory
#except: from TTGammaEFT.Tools.user import postprocessing_directory
from TTGammaEFT.Tools.user import postprocessing_directorySemiLep2016 as postprocessing_directory

logger.info( "Loading MC samples from directory %s", os.path.join( data_directory, postprocessing_directory ) )

# Directories
dirs = {}

dirs['DY_LO']            = ["DYJetsToLL_M10to50_LO", "DYJetsToLL_M50_LO_ext1_comb" ]

dirs['TTLep_pow']        = ["TTLep_pow"]
dirs['TT_pow']           = ["TTLep_pow", "TTSingleLep_pow", "TTSingleLep_pow"] #wrong x-sec in TTSingleLep_pow 2016, thus have to take twice for now
dirs['TTbar']            = ["TTbar"]

dirs['TTG']              = ["TTGJets_comb"]
dirs['TTGLep']           = ["TTGLep"]
dirs['TTG']              = ["TTGLep", "TTGSemiTbar", "TTGHad", "TTGSemiTbar" ] #TTGSemiT not available, thus taking TTGSemiTbar twice

dirs['singleTop']        = ["TBar_tWch_ext", "T_tWch_ext", "T_tch_pow", "TBar_tch_pow" ]#, "TToLeptons_sch_amcatnlo" ]

dirs['ZGTo2LG']          = ["ZGTo2LG_ext"]
#dirs['ZGToLLG']          = ["ZGToLLG"]

dirs['TZQ']              = ["tZq_ll_ext"]
dirs['THQ']              = ["THQ"]
dirs['THW']              = ["THW"]
dirs['TWZ']              = ["tWll", "tWnunu"]
dirs['TTW']              = ["TTWToLNu_ext2", "TTWToQQ"]
dirs['TTZ']              = ["TTZ_LO"]
dirs['TTH']              = ["TTHnobb_pow", "TTHbb"]

#dirs['TTWZ']             = ["TTWZ"]
#dirs['TTZZ']             = ["TTZZ"]
#dirs['TTWW']             = ["TTWW"]
dirs['TTTT']             = ["TTTT"]

dirs['WJets']            = ["WJetsToLNu_comb"]

dirs['WWW']              = ["WWW_4F"]
dirs['WWZ']              = ["WWZ"]
#dirs['WZG']              = ["WZG"]
dirs['WZZ']              = ["WZZ"]
dirs['ZZZ']              = ["ZZZ"]

dirs['VV']               = ["VVTo2L2Nu_comb"]
dirs['WW']               = ["WWTo1L1Nu2Q"]
#dirs['WW']               = ["WWToLNuQQ_comb", "WWTo2L2Nu", "WWTo1L1Nu2Q"]
#dirs['WZ']               = ["WZTo1L1Nu2Q", "WZTo3LNu_comb"]
dirs['WZ']               = ["WZTo1L3Nu", "WZTo1L1Nu2Q", "WZTo2L2Q", "WZTo3LNu_ext"]
dirs['ZZ']               = ["ZZTo2L2Q", "ZZTo2Q2Nu", "ZZTo4L"] #"ZZTo2L2Nu"
#dirs['ZZ']               = [ "ZZTo2L2Q", "ZZTo2Q2Nu", "ZZTo4L"]

dirs['GluGlu']           = ["GluGluToContinToZZTo2e2mu", "GluGluToContinToZZTo2e2tau", "GluGluToContinToZZTo2mu2tau", "GluGluToContinToZZTo4e", "GluGluToContinToZZTo4mu"] #GluGluToContinToZZTo4tau

dirs['other']            = []
dirs['other']           += dirs['TZQ']  + dirs['THQ']  + dirs['TWZ'] + dirs['THW']
dirs['other']           += dirs['TTW']  + dirs['TTZ']  + dirs['TTH']
#dirs['other']           += dirs['TTWZ'] + dirs['TTZZ'] + dirs['TTWW']
dirs['other']           += dirs['TTTT']
dirs['other']           += dirs['WWW']  + dirs['WWZ']  + dirs['WZZ']  + dirs['ZZZ'] #+ dirs['WZG']
dirs['other']           += dirs['VV']
dirs['other']           += dirs['WW']   + dirs['WZ']  + dirs['ZZ']
dirs['other']           += dirs['GluGlu']

directories = { key : [ os.path.join( data_directory, postprocessing_directory, dir) for dir in dirs[key] ] for key in dirs.keys() }

# Samples
DY_LO_16           = Sample.fromDirectory(name="DY_LO",            treeName="Events", isData=False, color=color.DY,              texName="DY (LO)",           directory=directories['DY_LO'])
TT_pow_16          = Sample.fromDirectory(name="TT_pow",           treeName="Events", isData=False, color=color.TT,              texName="t#bar{t}",          directory=directories['TT_pow'])
#TTbar_16           = Sample.fromDirectory(name="TTbar",            treeName="Events", isData=False, color=color.TT,              texName="t#bar{t}",          directory=directories['TTbar'])
singleTop_16       = Sample.fromDirectory(name="singleTop",        treeName="Events", isData=False, color=color.T,               texName="single-t",          directory=directories['singleTop'])
#TTGLep_16          = Sample.fromDirectory(name="TTG",              treeName="Events", isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories['TTGLep'])
TTG_16             = Sample.fromDirectory(name="TTG",              treeName="Events", isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories['TTG'])
#TG_16              = Sample.fromDirectory(name="TG",               treeName="Events", isData=False, color=color.TGamma,          texName="t#gamma",           directory=directories['TG'])
#WG_16              = Sample.fromDirectory(name="WG",               treeName="Events", isData=False, color=color.WGamma,          texName="W#gamma",           directory=directories['WG'])
WJets_16           = Sample.fromDirectory(name="WJets",            treeName="Events", isData=False, color=color.W,               texName="W+jets",            directory=directories['WJets'])
ZG_16              = Sample.fromDirectory(name="ZG",               treeName="Events", isData=False, color=color.ZGamma,         texName="Z#gamma",           directory=directories['ZGTo2LG'] )
#ZG_16              = Sample.fromDirectory(name="ZG",              treeName="Events", isData=False, color=color.ZGamma,          texName="Z#gamma",           directory=directories['ZGToLLG'] )
other_16           = Sample.fromDirectory(name="other",            treeName="Events", isData=False, color=color.Other,           texName="other",             directory=directories['other'])

signals = []
