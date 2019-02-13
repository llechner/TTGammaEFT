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
from TTGammaEFT.Tools.user import data_directory2                as data_directory
from TTGammaEFT.Tools.user import postprocessing_directoryMC2018 as postprocessing_directory

logger.info( "Loading MC samples from directory %s", os.path.join( data_directory, postprocessing_directory ) )

dirs = {}
dirs['DY_LO']            = ["DYJetsToLL_M50_LO"]#, "DYJetsToLL_M10to50_LO"]

dirs['TTLep_pow']        = ["TTLep_pow"]
#dirs['TTSemiLep_pow']    = ["TTSemiLep_pow"]
#dirs['TTHad_pow'    ]    = ["TTHad_pow"]
dirs['TT_pow']           = ["TTLep_pow"]#, "TTSemiLep_pow", "TTHad_pow" ]
#dirs['TTbar']            = ["TTbar"]

#dirs['TTG']              = ["TTGJets_ext"]
#dirs['TTGLep']           = ["TTGLep"]
dirs['TTG']              = ["TTGLep"]#, "TTGSemiTbar", "TTGSemiT", "TTGHad"]

#dirs['singleTop']        = ["TBar_tWch_ext", "T_tWch_ext", "T_tch_pow", "TBar_tch_pow", "TToLeptons_sch_amcatnlo" ]
dirs['singleTop']        = ["TBar_tWch", "T_tWch"]

#dirs['singleTop']        = ["TToLeptons_sch_amcatnlo" ]

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
#dirs['WW']               = ["WW"]
#dirs['ZZ']               = ["ZZ"]
#dirs['WW']               = ["WWToLNuQQ_comb", "WWTo2L2Nu", "WWTo1L1Nu2Q"]
#dirs['WZ']               = ["WZTo1L3Nu", "WZTo1L1Nu2Q", "WZTo2L2Q", "WZTo3LNu"]
#dirs['ZZ']               = ["ZZTo2L2Nu", "ZZTo2L2Q"]
#dirs['ZZ']               = ["ZZTo2L2Nu", "ZZTo2L2Q", "ZZTo2Q2Nu", "ZZTo4L"]

#dirs['GluGlu']           = ["GluGluToContinToZZTo2e2mu", "GluGluToContinToZZTo2e2tau", "GluGluToContinToZZTo2mu2tau", "GluGluToContinToZZTo4e", "GluGluToContinToZZTo4mu", "GluGluToContinToZZTo4tau"]
#dirs['GluGlu']           = ["GluGluToContinToZZTo2e2mu", "GluGluToContinToZZTo2e2tau"]

dirs['other']            = []
#dirs['other']           += dirs['TZQ']  + dirs['THQ']  + dirs['THW'] #+ dirs['TWZ']
#dirs['other']           += dirs['TTW']  + dirs['TTZ']  + dirs['TTH']
#dirs['other']           += dirs['TTWZ'] + dirs['TTZZ'] #+ dirs['TTWW']
#dirs['other']           += dirs['WWZ'] + dirs['WZZ']  + dirs['ZZZ']
#dirs['other']           += dirs['WWW']  + dirs['WWZ']  + dirs['WZG'] + dirs['WZZ']  + dirs['ZZZ']
#dirs['other']           += dirs['VV']   + dirs['WW']   + dirs['WZ']  + dirs['ZZ']
#dirs['other']           += dirs['WW']
#dirs['other']           += dirs['ZZ']
#dirs['other']           += dirs['GluGlu']

directories = { key : [ os.path.join( data_directory, postprocessing_directory, dir) for dir in dirs[key] ] for key in dirs.keys() }

# Samples
DY_LO_18           = Sample.fromDirectory(name="DY_LO",            treeName="Events", isData=False, color=color.DY,              texName="DY (LO)",           directory=directories['DY_LO'])
TT_pow_18          = Sample.fromDirectory(name="TT_pow",           treeName="Events", isData=False, color=color.TT,              texName="t#bar{t}",          directory=directories['TT_pow'])
#TTbar_18           = Sample.fromDirectory(name="TTbar",            treeName="Events", isData=False, color=color.TT,              texName="t#bar{t}",          directory=directories['TTbar'])
singleTop_18       = Sample.fromDirectory(name="singleTop",        treeName="Events", isData=False, color=color.T,               texName="single-t",          directory=directories['singleTop'])
#TTGLep_18          = Sample.fromDirectory(name="TTG",              treeName="Events", isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories['TTGLep'])
TTG_18             = Sample.fromDirectory(name="TTG",              treeName="Events", isData=False, color=color.TTG,             texName="t#bar{t}#gamma",    directory=directories['TTG'])
#ZG_18              = Sample.fromDirectory(name="ZG",               treeName="Events", isData=False, color=color.ZGamma,          texName="Z#gamma",           directory=directories['ZGTo2LG'] )
#ZG_18              = Sample.fromDirectory(name="ZG",               treeName="Events", isData=False, color=color.ZGamma,          texName="Z#gamma",           directory=directories['ZGToLLG'] )
#other_18           = Sample.fromDirectory(name="other",            treeName="Events", isData=False, color=color.Other,           texName="other",             directory=directories['other'])

signals = []
