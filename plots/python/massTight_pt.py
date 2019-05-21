#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
massTight_pt = []
    
massTight_pt.append( Plot(
    name      = 'mL0PhotonTight_20ptG120',
    texX      = 'M(#gamma,l_{0}) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.mLtight0Gamma if event.PhotonGood0_pt < 120 else -999,
    binning   = [ 50, 0, 200 ],
))

massTight_pt.append( Plot(
    name      = 'mL0PhotonTight_120ptG220',
    texX      = 'M(#gamma,l_{0}) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.mLtight0Gamma if event.PhotonGood0_pt > 120 and event.PhotonGood0_pt < 220 else -999,
    binning   = [ 50, 0, 200 ],
))

massTight_pt.append( Plot(
    name      = 'mL0PhotonTight_220ptGinf',
    texX      = 'M(#gamma,l_{0}) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.mLtight0Gamma if event.PhotonGood0_pt > 220 else -999,
    binning   = [ 50, 0, 200 ],
))

massTight_pt.append( Plot(
    name      = 'mllPhotonTight_20ptG120',
    texX      = 'M(ll#gamma) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.mllgammatight if event.PhotonGood0_pt < 120 else -999,
    binning   = [ 50, 0, 200 ],
))

massTight_pt.append( Plot(
    name      = 'mllPhotonTight_120ptG220',
    texX      = 'M(ll#gamma) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.mllgammatight if event.PhotonGood0_pt > 120 and event.PhotonGood0_pt < 220 else -999,
    binning   = [ 50, 0, 200 ],
))

massTight_pt.append( Plot(
    name      = 'mllPhotonTight_220ptGinf',
    texX      = 'M(ll#gamma) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.mllgammatight if event.PhotonGood0_pt > 220 else -999,
    binning   = [ 50, 0, 200 ],
))

massTight_pt.append( Plot(
    name      = 'm3_20ptG120',
    texX      = 'M_{3} (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.m3 if event.PhotonGood0_pt < 120 else -999,
    binning   = [ 50, 0, 250 ],
))

massTight_pt.append( Plot(
    name      = 'm3_120ptG220',
    texX      = 'M_{3} (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.m3 if event.PhotonGood0_pt > 120 and event.PhotonGood0_pt < 220 else -999,
    binning   = [ 50, 0, 250 ],
))

massTight_pt.append( Plot(
    name      = 'm3_220ptGinf',
    texX      = 'M_{3} (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.m3 if event.PhotonGood0_pt > 220 else -999,
    binning   = [ 50, 0, 250 ],
))


massTight_pt.append( Plot(
    name      = 'm3gamma_20ptG120',
    texX      = 'M_{3} (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.m3gamma if event.PhotonGood0_pt < 120 else -999,
    binning   = [ 100, 0, 500 ],
))

massTight_pt.append( Plot(
    name      = 'm3gamma_120ptG220',
    texX      = 'M_{3} (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.m3gamma if event.PhotonGood0_pt > 120 and event.PhotonGood0_pt < 220 else -999,
    binning   = [ 100, 0, 500 ],
))

massTight_pt.append( Plot(
    name      = 'm3gamma_220ptGinf',
    texX      = 'M_{3} (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.m3gamma if event.PhotonGood0_pt > 220 else -999,
    binning   = [ 100, 0, 500 ],
))








massTight_pt.append( Plot(
    name      = 'mL0PhotonTight_20ptG120_coarse',
    texX      = 'M(#gamma,l_{0}) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.mLtight0Gamma if event.PhotonGood0_pt < 120 else -999,
    binning   = [ 17, 20, 190 ],
))

massTight_pt.append( Plot(
    name      = 'mL0PhotonTight_120ptG220_coarse',
    texX      = 'M(#gamma,l_{0}) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.mLtight0Gamma if event.PhotonGood0_pt > 120 and event.PhotonGood0_pt < 220 else -999,
    binning   = [ 17, 20, 190 ],
))

massTight_pt.append( Plot(
    name      = 'mL0PhotonTight_220ptGinf_coarse',
    texX      = 'M(#gamma,l_{0}) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.mLtight0Gamma if event.PhotonGood0_pt > 220 else -999,
    binning   = [ 17, 20, 190 ],
))

massTight_pt.append( Plot(
    name      = 'mllPhotonTight_20ptG120_coarse',
    texX      = 'M(ll#gamma) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.mllgammatight if event.PhotonGood0_pt < 120 else -999,
    binning   = [ 17, 20, 190 ],
))

massTight_pt.append( Plot(
    name      = 'mllPhotonTight_120ptG220_coarse',
    texX      = 'M(ll#gamma) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.mllgammatight if event.PhotonGood0_pt > 120 and event.PhotonGood0_pt < 220 else -999,
    binning   = [ 17, 20, 190 ],
))

massTight_pt.append( Plot(
    name      = 'mllPhotonTight_220ptGinf_coarse',
    texX      = 'M(ll#gamma) (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.mllgammatight if event.PhotonGood0_pt > 220 else -999,
    binning   = [ 17, 20, 190 ],
))

massTight_pt.append( Plot(
    name      = 'm3_20ptG120_coarse',
    texX      = 'M_{3} (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.m3 if event.PhotonGood0_pt < 120 else -999,
    binning   = [ 22, 60, 500 ],
))

massTight_pt.append( Plot(
    name      = 'm3_120ptG220_coarse',
    texX      = 'M_{3} (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.m3 if event.PhotonGood0_pt > 120 and event.PhotonGood0_pt < 220 else -999,
    binning   = [ 22, 60, 500 ],
))

massTight_pt.append( Plot(
    name      = 'm3_220ptGinf_coarse',
    texX      = 'M_{3} (GeV)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.m3 if event.PhotonGood0_pt > 220 else -999,
    binning   = [ 22, 60, 500 ],
))
