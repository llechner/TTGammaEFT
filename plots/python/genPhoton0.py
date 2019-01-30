#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# TTGammaEFT
from TTGammaEFT.Tools.constants       import defaultValue

# plotList
genPhoton0 = []
    
genPhoton0.append( Plot(
    name      = 'genPhoton0_pt',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = lambda event, sample: event.GenPhoton_pt[0] if event.nGenPhoton > 0 else defaultValue,
    binning   = [ 19, 20, 115 ],
))

genPhoton0.append( Plot(
    name      = 'genPhoton0_pt_EFT40_wide',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 40 GeV',
    attribute = lambda event, sample: event.GenPhoton_pt[0] if event.nGenPhoton > 0 else defaultValue,
    binning   = [ 15, 20, 620 ],
))

genPhoton0.append( Plot(
    name      = 'genPhoton0_pt_EFT100_wide',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 100 GeV',
    attribute = lambda event, sample: event.GenPhoton_pt[0] if event.nGenPhoton > 0 else defaultValue,
    binning   = [ 6, 20, 620 ],
))

genPhoton0.append( Plot(
    name      = 'genPhoton0_pt_EFT40',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 40 GeV',
    attribute = lambda event, sample: event.GenPhoton_pt[0] if event.nGenPhoton > 0 else defaultValue,
    binning   = [ 10, 20, 420 ],
))

genPhoton0.append( Plot(
    name      = 'genPhoton0_pt_EFT100',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 100 GeV',
    attribute = lambda event, sample: event.GenPhoton_pt[0] if event.nGenPhoton > 0 else defaultValue,
    binning   = [ 4, 20, 420 ],
))

genPhoton0.append( Plot(
    name      = 'genPhoton0_eta',
    texX      = '#eta(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenPhoton_eta[0] if event.nGenPhoton > 0 else defaultValue,
    binning   = [ 24, -1.8, 1.8 ],
))

genPhoton0.append( Plot(
    name      = 'genPhoton0_absEta',
    texX      = '|#eta|(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.GenPhoton_eta[0]) if event.nGenPhoton > 0 else defaultValue,
    binning   = [ 9, 0, 1.5 ],
))

genPhoton0.append( Plot(
    name      = 'genPhoton0_phi',
    texX      = '#phi(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenPhoton_phi[0] if event.nGenPhoton > 0 else defaultValue,
    binning   = [ 10, -pi, pi ],
))

