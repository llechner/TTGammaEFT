import ROOT

from TTGammaEFT.Samples.helpers import singleton as singleton

@singleton
class color():
  pass

color.data           = ROOT.kBlack
color.DY             = ROOT.kCyan+2
color.ZGamma         = ROOT.kBlue+2
color.WGamma         = ROOT.kBlue
color.TTG            = ROOT.kOrange
color.Other          = ROOT.kViolet
color.TT             = ROOT.kRed+1
color.T              = ROOT.kOrange+1
color.TGamma         = ROOT.kGray
color.W              = ROOT.kCyan+1
color.QCD            = ROOT.kGreen+3
color.GJets          = ROOT.kGreen+4

color.TTG1L          = ROOT.kBlue+2
color.TTG3LBuggy     = ROOT.kRed+1
color.TTG3LPatched   = ROOT.kGreen+3
color.TTG1           = ROOT.kOrange+1
color.TTG2           = ROOT.kGray
color.TTG3           = ROOT.kCyan+1
color.TTG4           = ROOT.kViolet
color.TTG5           = ROOT.kBlue
color.TTG6           = ROOT.kBlack
