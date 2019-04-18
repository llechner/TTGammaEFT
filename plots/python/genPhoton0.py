#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
genPhoton0 = []
    
genPhoton0.append( Plot(
    name      = 'genPhoton0_pt',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenPhoton_pt[0],
    binning   = [ 40, 0, 120 ],
))

genPhoton0.append( Plot(
    name      = 'genPhoton0_pt_EFT',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenPhoton_pt[0],
    binning   = [ 5, 20, 520 ],
))

genPhoton0.append( Plot(
    name      = 'genPhoton0_eta',
    texX      = '#eta(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenPhoton_eta[0],
    binning   = [ 40, -4, 4 ],
))

genPhoton0.append( Plot(
    name      = 'genPhoton0_phi',
    texX      = '#phi(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenPhoton_phi[0],
    binning   = [ 20, -pi, pi ],
))

genPhoton0.append( Plot(
    name      = 'genPhoton0_motherPdgId',
    texX      = 'motherPdgId(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenPhoton_motherPdgId[0],
    binning   = [ 51, -25, 26 ],
))

genPhoton0.append( Plot(
    name      = 'genPhoton0_motherPdgId_mesons',
    texX      = 'motherPdgId(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.GenPhoton_motherPdgId[0],
    binning   = [ 300, -50, 251 ],
))

#genPhoton0.append( Plot(
#    name      = 'genPhoton0_ISR_motherPdgId',
#    texX      = 'motherPdgId(#gamma_{0})',
#    texY      = 'Number of Events',
#    attribute = lambda event, sample: event.GenPhoton_motherPdgId[0] if event.GenPhoton_isISR[0],
#    binning   = [ 51, -25, 26 ],
#))

#genPhoton0.append( Plot(
#    name      = 'genPhoton0_status',
#    texX      = 'status flag(#gamma_{0})',
#    texY      = 'Number of Events',
#    attribute = lambda event, sample: event.GenPhoton_status[0],
#    binning   = [ 60, 0, 60 ],
#))

#genPhoton0.append( Plot(
#    name      = 'genPhoton0_ISR_status',
#    texX      = 'status flag(#gamma_{0})',
#    texY      = 'Number of Events',
#    attribute = lambda event, sample: event.GenPhoton_status[0] if event.GenPhoton_isISR[0],
#    binning   = [ 60, 0, 60 ],
#))

