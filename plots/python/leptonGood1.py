y
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
leptonGood1 = []

leptonGood1.append( Plot(
    name      = 'leptonGood1_pt',
    texX      = 'p_{T}(l_{1}) (GeV)',
    texY      = 'Number of Events / 15 GeV',
    attribute = lambda event, sample: event.LeptonGood1_pt if event.nLeptonGood > 1 else defaultValue,
    binning   = [ 20, 0, 300 ],
))

leptonGood1.append( Plot(
    name      = 'leptonGood1_eta',
    texX      = '#eta(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood1_eta if event.nLeptonGood > 1 else defaultValue,
    binning   = [ 30, -3, 3 ],
))

leptonGood1.append( Plot(
    name      = 'leptonGood1_absEta',
    texX      = '|#eta|(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.LeptonGood1_eta) if event.nLeptonGood > 1 else defaultValue,
    binning   = [ 15, 0, 3 ],
))

leptonGood1.append( Plot(
    name      = 'leptonGood1_phi',
    texX      = '#phi(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood1_phi if event.nLeptonGood > 1 else defaultValue,
    binning   = [ 10, -pi, pi ],
))
