nohup krenew -t -K 10 -- bash -c "python analysisPlots.py --year 2018 --selection dilepOS-nLepVeto2-offZSFll-nJet2p-nBTag1p-mll20 --plot_directory 102X_TTG_ppv16_v1 --plotFile all_noPhoton" & #SPLIT5
nohup krenew -t -K 10 -- bash -c "python analysisPlots.py --year 2018 --selection dilepOS-nLepVeto2-onZll-nJet1p                  --plot_directory 102X_TTG_ppv16_v1 --plotFile all_noPhoton" & #SPLIT5
#python analysisPlots.py --year 2018 --selection dilepOS-nLepVeto2-onZll-met150                  --plot_directory 102X_TTG_ppv16_v1 --plotFile all_noPhoton #SPLIT5

nohup krenew -t -K 10 -- bash -c "python analysisPlots.py --noData --year 2018 --selection dilepOS-nLepVeto2-nPhoton1p-offZSFllg-offZSFll-mll40                --plot_directory 102X_TTG_ppv16_v1 --plotFile all" & #SPLIT5
nohup krenew -t -K 10 -- bash -c "python analysisPlots.py --noData --year 2018 --selection dilepOS-nLepVeto2-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p --plot_directory 102X_TTG_ppv16_v1 --plotFile all" & #SPLIT5

#python analysisPlots.py --noData --year 2018 --selection dilepOS-nLepVeto2-MVAPhoton-offZSFllgMVA-offZSFll-mll40-nJet2p-nBTag1p                --plot_directory 102X_TTG_pp_v16_v1 --plotFile all #SPLIT5
#python analysisPlots.py --noData --year 2018 --selection dilepOS-nLepVeto2-MVAPhoton-offZSFllgMVA-offZSFll-mll40                               --plot_directory 102X_TTG_pp_v16_v1 --plotFile all #SPLIT5

#python analysisPlots.py --year 2018 --selection dilepOS-nLepVeto2-NoChgIsoPhoton-offZSFllgNoChgIso-offZSFll-mll40-nJet2p-nBTag1p               --plot_directory 102X_TTG_pp_v16_v1 --plotFile all #SPLIT5
#python analysisPlots.py --year 2018 --selection dilepOS-nLepVeto2-NoChgIsoPhoton-offZSFllgNoChgIso-offZSFll-mll40                              --plot_directory 102X_TTG_pp_v16_v1 --plotFile all #SPLIT5

#python analysisPlots.py --year 2018 --selection dilepOS-nLepVeto2-NoSieiePhoton-offZSFllgNoSieie-offZSFll-mll40-nJet2p-nBTag1p                 --plot_directory 102X_TTG_pp_v16_v1 --plotFile all #SPLIT5
#python analysisPlots.py --year 2018 --selection dilepOS-nLepVeto2-NoSieiePhoton-offZSFllgNoSieie-offZSFll-mll40                                --plot_directory 102X_TTG_pp_v16_v1 --plotFile all #SPLIT5

#python analysisPlots.py --year 2018 --selection dilepOS-nLepVeto2-NoChgIsoNoSieiePhoton-offZSFllgNoChgIsoNoSieie-offZSFll-mll40-nJet2p-nBTag1p --plot_directory 102X_TTG_pp_v16_v1 --plotFile all #SPLIT5
#python analysisPlots.py --year 2018 --selection dilepOS-nLepVeto2-NoChgIsoNoSieiePhoton-offZSFllgNoChgIsoNoSieie-offZSFll-mll40                --plot_directory 102X_TTG_pp_v16_v1 --plotFile all #SPLIT5



#python analysisPlots.py --noData --year 2018 --selection dilepOS-nLepVeto2-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p                      --plot_directory 102X_TTG_pp_v16_v1 --plotFile photonId --categoryPhoton PhotonGood0 #SPLIT5
#python analysisPlots.py --noData --year 2018 --selection dilepOS-nLepVeto2-nPhoton1p-offZSFllg-offZSFll-mll40                                     --plot_directory 102X_TTG_pp_v16_v1 --plotFile photonId --categoryPhoton PhotonGood0 #SPLIT5

#python analysisPlots.py --noData --year 2018 --selection dilepOS-nLepVeto2-MVAPhoton-offZSFllgMVA-offZSFll-mll40-nJet2p-nBTag1p                --plot_directory 102X_TTG_pp_v16_v1 --plotFile photonId --categoryPhoton PhotonMVA0 #SPLIT5
#python analysisPlots.py --noData --year 2018 --selection dilepOS-nLepVeto2-MVAPhoton-offZSFllgMVA-offZSFll-mll40                               --plot_directory 102X_TTG_pp_v16_v1 --plotFile photonId --categoryPhoton PhotonMVA0 #SPLIT5

#python analysisPlots.py --year 2018 --selection dilepOS-nLepVeto2-NoChgIsoPhoton-offZSFllgNoChgIso-offZSFll-mll40-nJet2p-nBTag1p               --plot_directory 102X_TTG_pp_v16_v1 --plotFile photonId --categoryPhoton PhotonNoChgIso0 #SPLIT5
#python analysisPlots.py --year 2018 --selection dilepOS-nLepVeto2-NoChgIsoPhoton-offZSFllgNoChgIso-offZSFll-mll40                              --plot_directory 102X_TTG_pp_v16_v1 --plotFile photonId --categoryPhoton PhotonNoChgIso0 #SPLIT5

#python analysisPlots.py --year 2018 --selection dilepOS-nLepVeto2-NoSieiePhoton-offZSFllgNoSieie-offZSFll-mll40-nJet2p-nBTag1p                 --plot_directory 102X_TTG_pp_v16_v1 --plotFile photonId --categoryPhoton PhotonNoSieie0 #SPLIT5
#python analysisPlots.py --year 2018 --selection dilepOS-nLepVeto2-NoSieiePhoton-offZSFllgNoSieie-offZSFll-mll40                                --plot_directory 102X_TTG_pp_v16_v1 --plotFile photonId --categoryPhoton PhotonNoSieie0 #SPLIT5

#python analysisPlots.py --year 2018 --selection dilepOS-nLepVeto2-NoChgIsoNoSieiePhoton-offZSFllgNoChgIsoNoSieie-offZSFll-mll40-nJet2p-nBTag1p --plot_directory 102X_TTG_pp_v16_v1 --plotFile photonId --categoryPhoton PhotonNoChgIsoNoSieie0 #SPLIT5
#python analysisPlots.py --year 2018 --selection dilepOS-nLepVeto2-NoChgIsoNoSieiePhoton-offZSFllgNoChgIsoNoSieie-offZSFll-mll40                --plot_directory 102X_TTG_pp_v16_v1 --plotFile photonId --categoryPhoton PhotonNoChgIsoNoSieie0 #SPLIT5

