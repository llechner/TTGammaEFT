#nohup krenew -t -K 10 -- bash -c "python analysisPlots.py --year 2017 --selection dilepOS-nLepVeto2-offZSFll-nJet2p-nBTag1p-mll20 --plot_directory 102X_TTG_ppv12_v1 --plotFile all_noPhoton" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots.py --year 2017 --selection dilepOS-nLepVeto2-onZll-met150                  --plot_directory 102X_TTG_ppv12_v1 --plotFile all_noPhoton" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots.py --year 2017 --selection dilepOS-nLepVeto2-onZll-nJet1p                  --plot_directory 102X_TTG_ppv12_v1 --plotFile all_noPhoton" &

nohup krenew -t -K 10 -- bash -c "python analysisPlots.py --noData --year 2017 --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40 --plot_directory 102X_TTG_ppv12_v1 --plotFile all" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots.py --noData --year 2017 --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p --plot_directory 102X_TTG_ppv12_v1 --plotFile all" &

