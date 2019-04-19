python analysisPlots.py $@ --year 2018 --selection dilepOS-nLepVeto2-offZSFll-nJet2p-nBTag1p-mll20 --plot_directory 102X_TTG_ppv15_v3 --plotFile all_noPhoton
python analysisPlots.py $@ --year 2018 --selection dilepOS-nLepVeto2-onZll-nJet1p                  --plot_directory 102X_TTG_ppv15_v3 --plotFile all_noPhoton
#python analysisPlots.py $@ --year 2018 --selection dilepOS-nLepVeto2-onZll-met150                  --plot_directory 102X_TTG_ppv15_v3 --plotFile all_noPhoton

python analysisPlots.py --noData $@ --year 2018 --selection dilepOS-nLepVeto2-nPhoton1p-offZSFllg-offZSFll-mll40                --plot_directory 102X_TTG_ppv15_v3 --plotFile all
python analysisPlots.py --noData $@ --year 2018 --selection dilepOS-nLepVeto2-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p --plot_directory 102X_TTG_ppv15_v3 --plotFile all

python analysisPlots.py --noData $@ --year 2018 --selection dilepOS-nLepVeto2-nPhotonMVA1p-offZSFllgMVA-offZSFll-mll40-nJet2p-nBTag1p                --plot_directory 102X_TTG_pp_v15_v3 --plotFile all
python analysisPlots.py --noData $@ --year 2018 --selection dilepOS-nLepVeto2-nPhotonMVA1p-offZSFllgMVA-offZSFll-mll40                               --plot_directory 102X_TTG_pp_v15_v3 --plotFile all

python analysisPlots.py $@ --year 2018 --selection dilepOS-nLepVeto2-nPhotonNoChgIso1p-offZSFllgNoChgIso-offZSFll-mll40-nJet2p-nBTag1p               --plot_directory 102X_TTG_pp_v15_v3 --plotFile all
python analysisPlots.py $@ --year 2018 --selection dilepOS-nLepVeto2-nPhotonNoChgIso1p-offZSFllgNoChgIso-offZSFll-mll40                              --plot_directory 102X_TTG_pp_v15_v3 --plotFile all

python analysisPlots.py $@ --year 2018 --selection dilepOS-nLepVeto2-nPhotonNoSieie1p-offZSFllgNoSieie-offZSFll-mll40-nJet2p-nBTag1p                 --plot_directory 102X_TTG_pp_v15_v3 --plotFile all
python analysisPlots.py $@ --year 2018 --selection dilepOS-nLepVeto2-nPhotonNoSieie1p-offZSFllgNoSieie-offZSFll-mll40                                --plot_directory 102X_TTG_pp_v15_v3 --plotFile all

python analysisPlots.py $@ --year 2018 --selection dilepOS-nLepVeto2-nPhotonNoChgIsoNoSieie1p-offZSFllgNoChgIsoNoSieie-offZSFll-mll40-nJet2p-nBTag1p --plot_directory 102X_TTG_pp_v15_v3 --plotFile all
python analysisPlots.py $@ --year 2018 --selection dilepOS-nLepVeto2-nPhotonNoChgIsoNoSieie1p-offZSFllgNoChgIsoNoSieie-offZSFll-mll40                --plot_directory 102X_TTG_pp_v15_v3 --plotFile all



python analysisPlots.py --noData $@ --year 2018 --selection dilepOS-nLepVeto2-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p                      --plot_directory 102X_TTG_pp_v15_v3 --plotFile all --categoryPhoton PhotonGood0
python analysisPlots.py --noData $@ --year 2018 --selection dilepOS-nLepVeto2-nPhoton1p-offZSFllg-offZSFll-mll40                                     --plot_directory 102X_TTG_pp_v15_v3 --plotFile all --categoryPhoton PhotonGood0

python analysisPlots.py --noData $@ --year 2018 --selection dilepOS-nLepVeto2-nPhotonMVA1p-offZSFllgMVA-offZSFll-mll40-nJet2p-nBTag1p                --plot_directory 102X_TTG_pp_v15_v3 --plotFile all --categoryPhoton PhotonMVA0
python analysisPlots.py --noData $@ --year 2018 --selection dilepOS-nLepVeto2-nPhotonMVA1p-offZSFllgMVA-offZSFll-mll40                               --plot_directory 102X_TTG_pp_v15_v3 --plotFile all --categoryPhoton PhotonMVA0

python analysisPlots.py $@ --year 2018 --selection dilepOS-nLepVeto2-nPhotonNoChgIso1p-offZSFllgNoChgIso-offZSFll-mll40-nJet2p-nBTag1p               --plot_directory 102X_TTG_pp_v15_v3 --plotFile all --categoryPhoton PhotonNoChgIso0
python analysisPlots.py $@ --year 2018 --selection dilepOS-nLepVeto2-nPhotonNoChgIso1p-offZSFllgNoChgIso-offZSFll-mll40                              --plot_directory 102X_TTG_pp_v15_v3 --plotFile all --categoryPhoton PhotonNoChgIso0

python analysisPlots.py $@ --year 2018 --selection dilepOS-nLepVeto2-nPhotonNoSieie1p-offZSFllgNoSieie-offZSFll-mll40-nJet2p-nBTag1p                 --plot_directory 102X_TTG_pp_v15_v3 --plotFile all --categoryPhoton PhotonNoSieie0
python analysisPlots.py $@ --year 2018 --selection dilepOS-nLepVeto2-nPhotonNoSieie1p-offZSFllgNoSieie-offZSFll-mll40                                --plot_directory 102X_TTG_pp_v15_v3 --plotFile all --categoryPhoton PhotonNoSieie0

python analysisPlots.py $@ --year 2018 --selection dilepOS-nLepVeto2-nPhotonNoChgIsoNoSieie1p-offZSFllgNoChgIsoNoSieie-offZSFll-mll40-nJet2p-nBTag1p --plot_directory 102X_TTG_pp_v15_v3 --plotFile all --categoryPhoton PhotonNoChgIsoNoSieie0
python analysisPlots.py $@ --year 2018 --selection dilepOS-nLepVeto2-nPhotonNoChgIsoNoSieie1p-offZSFllgNoChgIsoNoSieie-offZSFll-mll40                --plot_directory 102X_TTG_pp_v15_v3 --plotFile all --categoryPhoton PhotonNoChgIsoNoSieie0

