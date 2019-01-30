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
#except: from TTGammaEFT.Tools.user import data_directory
from TTGammaEFT.Tools.user import data_directory2018 as data_directory

# Take post processing directory if defined in main module
#try:    postprocessing_directory = sys.modules['__main__'].postprocessing_directory
#except: from TTGammaEFT.Tools.user import postprocessing_directory2018
from TTGammaEFT.Tools.user import postprocessing_directory2018

logger.info( "Loading MC samples from directory %s", os.path.join( data_directory, postprocessing_directory2018 ) )

dirs = {}
dirs['DY_LO']            = ["DYJetsToLL_M50_LO"]#, "DYJetsToLL_M10to50_LO"]
dirs['TTLep_pow']        = ["TTLep_pow"]
#dirs['TTbar']            = ["TTbar"]

#dirs['TTG']              = ["TTGJets_ext"]
#dirs['TTGLep']           = ["TTGLep"]
#dirs['TTG']              = ["TTGLep", "TTGSemiTbar", "TTGSemiT", "TTGHad"]

#dirs['singleTop']        = ["TBar_tWch_ext", "T_tWch_ext", "T_tch_powheg", "TBar_tch_powheg", "TToLeptons_sch_amcatnlo" ]

#dirs['ZGTo2LG']          = ["ZGTo2LG_ext"]
#dirs['ZGToLLG']          = ["ZGToLLG"]

#dirs['TZQ']              = ["tZq_ll_ext"]
#dirs['THQ']              = ["THQ"]
#dirs['THW']              = ["THW"]
#dirs['TWZ']              = ["tWll", "tWnunu"]

#dirs['TTW']              = ["TTWToLNu"]
#dirs['TTZ']              = ["TTZToLLNuNu"]
#dirs['TTH']              = ["TTHnobb_pow"]


#dirs['TTWZ']             = ["TTWZ"]
#dirs['TTZZ']             = ["TTZZ"]
#dirs['TTWW']             = ["TTWW"]

#dirs['WWW']              = ["WWW_4F"]
#dirs['WWZ']              = ["WWZ"]
#dirs['WZG']              = ["WZG"]
#dirs['WZZ']              = ["WZZ"]
#dirs['ZZZ']              = ["ZZZ"]

#dirs['VV']               = ["VVTo2L2Nu"]
dirs['WW']               = ["WW"]
#dirs['WW']               = ["WWToLNuQQ_comb", "WWTo2L2Nu", "WWTo1L1Nu2Q"]
#dirs['WZ']               = ["WZTo1L3Nu", "WZTo1L1Nu2Q", "WZTo2L2Q", "WZTo3LNu"]
#dirs['ZZ']               = ["ZZTo2L2Nu", "ZZTo2L2Q"]
#dirs['ZZ']               = ["ZZTo2L2Nu", "ZZTo2L2Q", "ZZTo2Q2Nu", "ZZTo4L"]

#dirs['GluGlu']           = ["GluGluToContinToZZTo2e2mu", "GluGluToContinToZZTo2e2tau", "GluGluToContinToZZTo2mu2tau", "GluGluToContinToZZTo4e", "GluGluToContinToZZTo4mu", "GluGluToContinToZZTo4tau"]
dirs['GluGlu']           = ["GluGluToContinToZZTo2e2mu", "GluGluToContinToZZTo2e2tau"]

dirs['other']            = []
#dirs['other']           += dirs['TZQ']  + dirs['THQ']  + dirs['THW'] #+ dirs['TWZ']
#dirs['other']           += dirs['TTW']  + dirs['TTZ']  + dirs['TTH']
#dirs['other']           += dirs['TTWZ'] + dirs['TTZZ'] + dirs['TTWW']
#dirs['other']           += dirs['WWW']  + dirs['WWZ']  + dirs['WZG'] + dirs['WZZ']  + dirs['ZZZ']
#dirs['other']           += dirs['VV']   + dirs['WW']   + dirs['WZ']  + dirs['ZZ']
dirs['other']           += dirs['WW']
dirs['other']           += dirs['GluGlu']

directories = { key : [ os.path.join( data_directory, postprocessing_directory2018, dir) for dir in dirs[key] ] for key in dirs.keys() }

# Samples
DY_LO_18           = Sample.fromDirectory(name="DY_LO",            treeName="Events", isData=False, color=color.DY,              texName="DY (LO)",           directory=directories['DY_LO'])
TT_pow_18          = Sample.fromDirectory(name="TTLep_pow",        treeName="Events", isData=False, color=color.TT,              texName="t#bar{t}",          directory=directories['TTLep_pow'])
#TTbar_18           = Sample.fromDirectory(name="TTbar",            treeName="Events", isData=False, color=color.TT,              texName="t#bar{t}",          directory=directories['TTbar'])
#singleTop_18       = Sample.fromDirectory(name="singleTop",        treeName="Events", isData=False, color=color.T,               texName="single-t",          directory=directories['singleTop'])
#TTGLep_18          = Sample.fromDirectory(name="TTGLep",           treeName="Events", isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories['TTGLep'])
#TTG_18             = Sample.fromDirectory(name="TTGLep",           treeName="Events", isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories['TTG'])
#ZGTo2LG_18         = Sample.fromDirectory(name="ZGTo2LG",          treeName="Events", isData=False, color=color.ZGamma,          texName="Z#gamma",           directory=directories['ZGTo2LG'] )
#ZGToLLG_18         = Sample.fromDirectory(name="ZGToLLG",          treeName="Events", isData=False, color=color.ZGamma,          texName="Z#gamma",           directory=directories['ZGToLLG'] )
other_18           = Sample.fromDirectory(name="other",            treeName="Events", isData=False, color=color.Other,           texName="other",             directory=directories['other'])

signals = []
