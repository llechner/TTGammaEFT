#!/usr/bin/env python
''' Define list of plots for plot script
'''
# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
cutsPhotonNoIdCuts0_pt = []
    
cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_sieie_20ptG120',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_sieie if event.PhotonNoChgIsoNoSieie0_pt >= 20 and event.PhotonNoChgIsoNoSieie0_pt < 120 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_sieie_120ptG220',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_sieie if event.PhotonNoChgIsoNoSieie0_pt >= 120 and event.PhotonNoChgIsoNoSieie0_pt < 220 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_sieie_220ptGinf',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_sieie if event.PhotonNoChgIsoNoSieie0_pt >= 220 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_n_20ptG120',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIsoNoSieie0_pfRelIso03_all - event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg) if event.PhotonNoChgIsoNoSieie0_pt >= 20 and event.PhotonNoChgIsoNoSieie0_pt < 120 else -999,
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_n_120ptG220',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIsoNoSieie0_pfRelIso03_all - event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg) if event.PhotonNoChgIsoNoSieie0_pt >= 120 and event.PhotonNoChgIsoNoSieie0_pt < 220 else -999,
    binning   = [ 20, 0, 0.05 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_n_220ptGinf',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIsoNoSieie0_pfRelIso03_all - event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg) if event.PhotonNoChgIsoNoSieie0_pt >= 220 else -999,
    binning   = [ 20, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoSieie0_sieie_20ptG120',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_sieie if event.PhotonNoSieie0_pt >= 20 and event.PhotonNoSieie0_pt < 120 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoSieie0_sieie_120ptG220',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_sieie if event.PhotonNoSieie0_pt >= 120 and event.PhotonNoSieie0_pt < 220 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoSieie0_sieie_220ptGinf',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_sieie if event.PhotonNoSieie0_pt >= 220 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoSieie0_pfRelIso03_n_20ptG120',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoSieie0_pfRelIso03_all - event.PhotonNoSieie0_pfRelIso03_chg) if event.PhotonNoSieie0_pt < 120 else -999,
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoSieie0_pfRelIso03_n_120ptG220',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoSieie0_pfRelIso03_all - event.PhotonNoSieie0_pfRelIso03_chg) if event.PhotonNoSieie0_pt >= 120 and event.PhotonNoSieie0_pt < 220 else -999,
    binning   = [ 20, 0, 0.05 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoSieie0_pfRelIso03_n_220ptGinf',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoSieie0_pfRelIso03_all - event.PhotonNoSieie0_pfRelIso03_chg) if event.PhotonNoSieie0_pt >= 220 else -999,
    binning   = [ 20, 0, 0.03 ],
))


cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_n_20ptG120',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIso0_pfRelIso03_all - event.PhotonNoChgIso0_pfRelIso03_chg) if event.PhotonNoChgIso0_pt < 120 else -999,
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_n_120ptG220',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIso0_pfRelIso03_all - event.PhotonNoChgIso0_pfRelIso03_chg) if event.PhotonNoChgIso0_pt >= 120 and event.PhotonNoChgIso0_pt < 220 else -999,
    binning   = [ 20, 0, 0.05 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_n_220ptGinf',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIso0_pfRelIso03_all - event.PhotonNoChgIso0_pfRelIso03_chg) if event.PhotonNoChgIso0_pt >= 220 else -999,
    binning   = [ 20, 0, 0.03 ],
))





cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_chg_20ptG120_coarse',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg if event.PhotonNoChgIsoNoSieie0_pt >= 20 and event.PhotonNoChgIsoNoSieie0_pt < 120 else -999,
    binning   = [ 20, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_chg_120ptG220_coarse',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg if event.PhotonNoChgIsoNoSieie0_pt >= 120 and event.PhotonNoChgIsoNoSieie0_pt < 220 else -999,
    binning   = [ 20, 0, 0.005 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_chg_220ptGinf_coarse',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg if event.PhotonNoChgIsoNoSieie0_pt >= 220 else -999,
    binning   = [ 20, 0, 0.003 ],
))


cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoSieie0_pfRelIso03_chg_20ptG120_coarse',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg if event.PhotonNoSieie0_pt < 120 else -999,
    binning   = [ 20, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoSieie0_pfRelIso03_chg_120ptG220_coarse',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg if event.PhotonNoSieie0_pt >= 120 and event.PhotonNoSieie0_pt < 220 else -999,
    binning   = [ 20, 0, 0.005 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoSieie0_pfRelIso03_chg_220ptGinf_coarse',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg if event.PhotonNoSieie0_pt >= 220 else -999,
    binning   = [ 20, 0, 0.003 ],
))


cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_chg_20ptG120_coarse',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg if event.PhotonNoChgIso0_pt < 120 else -999,
    binning   = [ 20, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_chg_120ptG220_coarse',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg if event.PhotonNoChgIso0_pt >= 120 and event.PhotonNoChgIso0_pt < 220 else -999,
    binning   = [ 20, 0, 0.05 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_chg_220ptGinf_coarse',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg if event.PhotonNoChgIso0_pt >= 220 else -999,
    binning   = [ 20, 0, 0.003 ],
))













cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_chg_20ptG120',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg if event.PhotonNoChgIsoNoSieie0_pt >= 20 and event.PhotonNoChgIsoNoSieie0_pt < 120 else -999,
    binning   = [ 50, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_chg_120ptG220',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg if event.PhotonNoChgIsoNoSieie0_pt >= 120 and event.PhotonNoChgIsoNoSieie0_pt < 220 else -999,
    binning   = [ 50, 0, 0.005 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_chg_220ptGinf',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg if event.PhotonNoChgIsoNoSieie0_pt >= 220 else -999,
    binning   = [ 50, 0, 0.003 ],
))


cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoSieie0_pfRelIso03_chg_20ptG120',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg if event.PhotonNoSieie0_pt < 120 else -999,
    binning   = [ 50, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoSieie0_pfRelIso03_chg_120ptG220',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg if event.PhotonNoSieie0_pt >= 120 and event.PhotonNoSieie0_pt < 220 else -999,
    binning   = [ 50, 0, 0.005 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoSieie0_pfRelIso03_chg_220ptGinf',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg if event.PhotonNoSieie0_pt >= 220 else -999,
    binning   = [ 50, 0, 0.003 ],
))


cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_chg_20ptG120',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg if event.PhotonNoChgIso0_pt < 120 else -999,
    binning   = [ 50, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_chg_120ptG220',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg if event.PhotonNoChgIso0_pt >= 120 and event.PhotonNoChgIso0_pt < 220 else -999,
    binning   = [ 50, 0, 0.05 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_chg_220ptGinf',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg if event.PhotonNoChgIso0_pt >= 220 else -999,
    binning   = [ 50, 0, 0.003 ],
))












cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_all_20ptG120',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_all if event.PhotonNoChgIsoNoSieie0_pt >= 20 and event.PhotonNoChgIsoNoSieie0_pt < 120 else -999,
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_all_120ptG220',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_all if event.PhotonNoChgIsoNoSieie0_pt >= 120 and event.PhotonNoChgIsoNoSieie0_pt < 220 else -999,
    binning   = [ 20, 0, 0.05 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfRelIso03_all_220ptGinf',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_all if event.PhotonNoChgIsoNoSieie0_pt >= 220 else -999,
    binning   = [ 20, 0, 0.03 ],
))


cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_all_20ptG120',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_all if event.PhotonNoChgIso0_pt < 120 else -999,
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_all_120ptG220',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_all if event.PhotonNoChgIso0_pt >= 120 and event.PhotonNoChgIso0_pt < 220 else -999,
    binning   = [ 20, 0, 0.05 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfRelIso03_all_220ptGinf',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_all if event.PhotonNoChgIso0_pt >= 220 else -999,
    binning   = [ 20, 0, 0.03 ],
))











cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_n_20ptG120',
    texX      = 'neutral Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIsoNoSieie0_pfRelIso03_all - event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg) * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pt >= 20 and event.PhotonNoChgIsoNoSieie0_pt < 120 else -999,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_n_120ptG220',
    texX      = 'neutral Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIsoNoSieie0_pfRelIso03_all - event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg) * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pt >= 120 and event.PhotonNoChgIsoNoSieie0_pt < 220 else -999,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_n_220ptGinf',
    texX      = 'neutral Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIsoNoSieie0_pfRelIso03_all - event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg) * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pt >= 220 else -999,
    binning   = [ 20, 0, 5 ],
))


cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_n_20ptG120',
    texX      = 'neutral Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIso0_pfRelIso03_all - event.PhotonNoChgIso0_pfRelIso03_chg) * event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pt < 120 else -999,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_n_120ptG220',
    texX      = 'neutral Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIso0_pfRelIso03_all - event.PhotonNoChgIso0_pfRelIso03_chg) * event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pt >= 120 and event.PhotonNoChgIso0_pt < 220 else -999,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_n_220ptGinf',
    texX      = 'neutral Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIso0_pfRelIso03_all - event.PhotonNoChgIso0_pfRelIso03_chg) * event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pt >= 220 else -999,
    binning   = [ 20, 0, 5 ],
))





cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_chg_20ptG120',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pt >= 20 and event.PhotonNoChgIsoNoSieie0_pt < 120 else -999,
    binning   = [ 20, 0, 0.5 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_chg_120ptG220',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pt >= 120 and event.PhotonNoChgIsoNoSieie0_pt < 220 else -999,
    binning   = [ 20, 0, 0.5 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_chg_220ptGinf',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pt >= 220 else -999,
    binning   = [ 20, 0, 0.5 ],
))


cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_chg_20ptG120',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pt < 120 else -999,
    binning   = [ 20, 0, 0.5 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_chg_120ptG220',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pt >= 120 and event.PhotonNoChgIso0_pt < 220 else -999,
    binning   = [ 20, 0, 0.5 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_chg_220ptGinf',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pt >= 220 else -999,
    binning   = [ 20, 0, 0.5 ],
))






cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_chg_20ptG120_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pt >= 20 and event.PhotonNoChgIsoNoSieie0_pt < 120 else -999,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_chg_120ptG220_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pt >= 120 and event.PhotonNoChgIsoNoSieie0_pt < 220 else -999,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_chg_220ptGinf_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pt >= 220 else -999,
    binning   = [ 50, 0, 20 ],
))


cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_chg_20ptG120_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pt < 120 else -999,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_chg_120ptG220_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pt >= 120 and event.PhotonNoChgIso0_pt < 220 else -999,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_chg_220ptGinf_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pt >= 220 else -999,
    binning   = [ 50, 0, 20 ],
))





cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_chg_20ptG120',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pt >= 20 and event.PhotonNoChgIsoNoSieie0_pt < 120 else -999,
    binning   = [ 50, 0, 0.5 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_chg_120ptG220',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pt >= 120 and event.PhotonNoChgIsoNoSieie0_pt < 220 else -999,
    binning   = [ 50, 0, 0.5 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_chg_220ptGinf',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pt >= 220 else -999,
    binning   = [ 50, 0, 0.5 ],
))


cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_chg_20ptG120',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pt < 120 else -999,
    binning   = [ 50, 0, 0.5 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_chg_120ptG220',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pt >= 120 and event.PhotonNoChgIso0_pt < 220 else -999,
    binning   = [ 50, 0, 0.5 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_chg_220ptGinf',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pt >= 220 else -999,
    binning   = [ 50, 0, 0.5 ],
))






cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_chg_20ptG120_wide_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pt >= 20 and event.PhotonNoChgIsoNoSieie0_pt < 120 else -999,
    binning   = [ 20, 0, 20 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_chg_120ptG220_wide_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pt >= 120 and event.PhotonNoChgIsoNoSieie0_pt < 220 else -999,
    binning   = [ 20, 0, 20 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_chg_220ptGinf_wide_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pt >= 220 else -999,
    binning   = [ 20, 0, 20 ],
))


cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_chg_20ptG120_wide_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pt < 120 else -999,
    binning   = [ 20, 0, 20 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_chg_120ptG220_wide_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pt >= 120 and event.PhotonNoChgIso0_pt < 220 else -999,
    binning   = [ 20, 0, 20 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_chg_220ptGinf_wide_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_chg * event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pt >= 220 else -999,
    binning   = [ 20, 0, 20 ],
))





cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_all_20ptG120',
    texX      = 'Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_all * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pt >= 20 and event.PhotonNoChgIsoNoSieie0_pt < 120 else -999,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_all_120ptG220',
    texX      = 'Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_all * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pt >= 120 and event.PhotonNoChgIsoNoSieie0_pt < 220 else -999,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_pfIso03_all_220ptGinf',
    texX      = 'Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_all * event.PhotonNoChgIsoNoSieie0_pt if event.PhotonNoChgIsoNoSieie0_pt >= 220 else -999,
    binning   = [ 20, 0, 5 ],
))


cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_all_20ptG120',
    texX      = 'Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_all * event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pt < 120 else -999,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_all_120ptG220',
    texX      = 'Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_all * event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pt >= 120 and event.PhotonNoChgIso0_pt < 220 else -999,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonNoIdCuts0_pt.append( Plot(
    name      = 'PhotonNoChgIso0_pfIso03_all_220ptGinf',
    texX      = 'Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIso0_pfRelIso03_all * event.PhotonNoChgIso0_pt if event.PhotonNoChgIso0_pt >= 220 else -999,
    binning   = [ 20, 0, 5 ],
))


