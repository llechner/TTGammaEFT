small=""
#small="--small"
noData=""
#noData="--noData"

 # Base line selection
nohup krenew -t -K 10 -- bash -c "python analysisPlots.py ${small} ${noData} --year 2018 --selection dilepOS-nLepVeto2-offZSFll-nJet2p-nBTag1p-mll20 --plot_directory 102X_TTG_ppv4_v6 --plotFile all_noPhoton" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots.py ${small} ${noData} --year 2018 --selection dilepOS-nLepVeto2-onZll-nJet1p                  --plot_directory 102X_TTG_ppv4_v6 --plotFile all_noPhoton" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots.py ${small} ${noData} --year 2018 --selection dilepOS-nLepVeto2-onZll-met150                  --plot_directory 102X_TTG_ppv4_v6 --plotFile all_noPhoton" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots.py ${small} ${noData} --year 2018 --selection dilepOS-nLepVeto2-onZll-nJet1p-met150           --plot_directory 102X_TTG_ppv4_v6 --plotFile all_noPhoton" &

# DO NOT UNBLINED
noData="--noData"
#nohup krenew -t -K 10 -- bash -c "python analysisPlots.py ${small} ${noData} --year 2018 --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40 --plot_directory 102X_TTG_ppv4_v6 --plotFile all" &


