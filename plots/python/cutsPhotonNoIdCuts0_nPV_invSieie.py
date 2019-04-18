#!/usr/bin/env python
''' Define list of plots for plot script
'''
# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
cutsPhotonNoIdCuts0_nPV_invSieie = []
    
cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_sieie_0nPV20',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_sieie if event.PV_npvsGood < 20 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_sieie_20nPV60',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_sieie if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_sieie_60nPVinf',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_sieie if event.PV_npvsGood >= 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfRelIso03_n_0nPV20',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIsoNoSieie0_pfRelIso03_all - event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg) if event.PV_npvsGood < 20 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfRelIso03_n_20nPV60',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIsoNoSieie0_pfRelIso03_all - event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg) if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfRelIso03_n_60nPVinf',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIsoNoSieie0_pfRelIso03_all - event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg) if event.PV_npvsGood >= 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.2 ],
))



cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_sieie_0nPV20',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_sieie if event.PV_npvsGood < 20 and event.PhotonNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_sieie_20nPV60',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_sieie if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_sieie_60nPVinf',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_sieie if event.PV_npvsGood >= 60 and event.PhotonNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 40, 0.005, 0.025 ],
))



cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfRelIso03_n_0nPV20',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoSieie0_pfRelIso03_all - event.PhotonNoSieie0_pfRelIso03_chg) if event.PV_npvsGood < 20 and event.PhotonNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfRelIso03_n_20nPV60',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoSieie0_pfRelIso03_all - event.PhotonNoSieie0_pfRelIso03_chg) if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfRelIso03_n_60nPVinf',
    texX      = 'neutral relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoSieie0_pfRelIso03_all - event.PhotonNoSieie0_pfRelIso03_chg) if event.PV_npvsGood >= 60 and event.PhotonNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.2 ],
))


cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfRelIso03_chg_0nPV20_coarse',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg if event.PV_npvsGood < 20 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfRelIso03_chg_20nPV60_coarse',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfRelIso03_chg_60nPVinf_coarse',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg if event.PV_npvsGood >= 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfRelIso03_chg_0nPV20_coarse',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg if event.PV_npvsGood < 20 and event.PhotonNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfRelIso03_chg_20nPV60_coarse',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfRelIso03_chg_60nPVinf_coarse',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg if event.PV_npvsGood >= 60 and event.PhotonNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.03 ],
))


cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfRelIso03_chg_0nPV20',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg if event.PV_npvsGood < 20 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 50, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfRelIso03_chg_20nPV60',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 50, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfRelIso03_chg_60nPVinf',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg if event.PV_npvsGood >= 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 50, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfRelIso03_chg_0nPV20',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg if event.PV_npvsGood < 20 and event.PhotonNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 50, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfRelIso03_chg_20nPV60',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 50, 0, 0.03 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfRelIso03_chg_60nPVinf',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_chg if event.PV_npvsGood >= 60 and event.PhotonNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 50, 0, 0.03 ],
))


cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfRelIso03_all_0nPV20',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_all if event.PV_npvsGood < 20 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfRelIso03_all_20nPV60',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_all if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfRelIso03_all_60nPVinf',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_all if event.PV_npvsGood >= 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.2 ],
))


cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfRelIso03_all_0nPV20',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_all if event.PV_npvsGood < 20 and event.PhotonNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfRelIso03_all_20nPV60',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_all if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.2 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoSieie0_invSieie_pfRelIso03_all_60nPVinf',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoSieie0_pfRelIso03_all if event.PV_npvsGood >= 60 and event.PhotonNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.2 ],
))




cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_n_0nPV20',
    texX      = 'neutral Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIsoNoSieie0_pfRelIso03_all - event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg) * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood < 20 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_n_20nPV60',
    texX      = 'neutral Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIsoNoSieie0_pfRelIso03_all - event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg) * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_n_60nPVinf',
    texX      = 'neutral Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: (event.PhotonNoChgIsoNoSieie0_pfRelIso03_all - event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg) * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood >= 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 5 ],
))



cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg_0nPV20',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood < 20 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.5 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg_20nPV60',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.5 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg_60nPVinf',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood >= 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.5 ],
))




cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg_0nPV20_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood < 20 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg_20nPV60_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg_60nPVinf_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood >= 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 50, 0, 20 ],
))






cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg_0nPV20_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood < 20 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.5 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg_20nPV60_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.5 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg_60nPVinf_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood >= 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 0.5 ],
))



cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg_0nPV20_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood < 20 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg_20nPV60_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 50, 0, 20 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg_60nPVinf_wide',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood >= 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 50, 0, 20 ],
))



cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg_0nPV20_wide_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood < 20 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 20 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg_20nPV60_wide_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 20 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_chg_60nPVinf_wide_coarse',
    texX      = 'charged Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_chg * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood >= 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 20 ],
))



cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_all_0nPV20',
    texX      = 'Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_all * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood < 20 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_all_20nPV60',
    texX      = 'Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_all * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood >= 20 and event.PV_npvsGood < 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 5 ],
))

cutsPhotonNoIdCuts0_nPV_invSieie.append( Plot(
    name      = 'PhotonNoChgIsoNoSieie0_invSieie_pfIso03_all_60nPVinf',
    texX      = 'Iso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonNoChgIsoNoSieie0_pfRelIso03_all * event.PhotonNoChgIsoNoSieie0_pt if event.PV_npvsGood >= 60 and event.PhotonNoChgIsoNoSieie0_sieie > 0.01022 else -999,
    binning   = [ 20, 0, 5 ],
))

