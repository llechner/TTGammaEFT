small=""
#small="--small"
noData=""
#noData="--noData"

# Base line selection
nohup krenew -t -K 10 -- bash -c "python analysisPlots2017.py ${small} ${noData} --selection dilepOS-nLepVeto2-offZSFll-nJet2p-nBTag1p-mll20 --plot_directory 94X_TTG_ppv1_v2 --plotFile allNoPhoton" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots2017.py ${small} ${noData} --selection dilepOS-nLepVeto2-onZll                         --plot_directory 94X_TTG_ppv1_v2 --plotFile allNoPhoton" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots2017.py ${small} ${noData} --selection dilepOS-nLepVeto2-onZll-nJet1p                  --plot_directory 94X_TTG_ppv1_v2 --plotFile allNoPhoton" &


# DO NOT UNBLINED
noData="--noData"
nohup krenew -t -K 10 -- bash -c "python analysisPlots2017.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40 --plot_directory 94X_TTG_ppv1_v2 --plotFile all" &
