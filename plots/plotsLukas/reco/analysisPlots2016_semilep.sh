small=""
#small="--small"
#noData=""
noData="--noData"

# Base line selection
nohup krenew -t -K 10 -- bash -c "python analysisPlots_semilep.py ${small} ${noData} --year 2016 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p                  --plot_directory 102X_TTG_ppv4_v1 --plotFile all_1l" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots_semilep.py ${small} ${noData} --year 2016 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-pTG20-nPhoton1p  --plot_directory 102X_TTG_ppv4_v1 --plotFile all_1l" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots_semilep.py ${small} ${noData} --year 2016 --selection nLepTight2-OStight-nLepVeto2-nJet4p-nBTag1p          --plot_directory 102X_TTG_ppv4_v1 --plotFile all_1l" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots_semilep.py ${small} ${noData} --year 2016 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-pTG20-nPhoton1p    --plot_directory 102X_TTG_ppv4_v1 --plotFile all_1l" &


