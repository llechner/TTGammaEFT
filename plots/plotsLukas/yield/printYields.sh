small=""
#small="--small"
noData=""
#noData="--noData"

year="2016"

nohup krenew -t -K 10 -- bash -c "python printYields.py ${small} ${noData} --year ${year} --selection dilepOS-nLepVeto2-pTG20-offZSFll-mll40-nJet0" &
nohup krenew -t -K 10 -- bash -c "python printYields.py ${small} ${noData} --year ${year} --selection dilepOS-nLepVeto2-pTG20-offZSFll-mll40-nJet1" &
nohup krenew -t -K 10 -- bash -c "python printYields.py ${small} ${noData} --year ${year} --selection dilepOS-nLepVeto2-pTG20-offZSFll-mll40-nJet2" &
nohup krenew -t -K 10 -- bash -c "python printYields.py ${small} ${noData} --year ${year} --selection dilepOS-nLepVeto2-pTG20-offZSFll-mll40-nJet3" &

nohup krenew -t -K 10 -- bash -c "python printYields.py ${small} ${noData} --year ${year} --selection dilepOS-nLepVeto2-pTG20-offZSFll-mll40-nBJet0" &
nohup krenew -t -K 10 -- bash -c "python printYields.py ${small} ${noData} --year ${year} --selection dilepOS-nLepVeto2-pTG20-offZSFll-mll40-nBJet1" &
nohup krenew -t -K 10 -- bash -c "python printYields.py ${small} ${noData} --year ${year} --selection dilepOS-nLepVeto2-pTG20-offZSFll-mll40-nBJet2" &

exit



# Base line selection
nohup krenew -t -K 10 -- bash -c "python printYields.py ${small} ${noData} --year ${year} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40" &
nohup krenew -t -K 10 -- bash -c "python printYields.py ${small} ${noData} --year ${year} --selection dilepOS-nLepVeto2-offZSFll-nJet2p-nBTag1p-mll20" &

nohup krenew -t -K 10 -- bash -c "python printYields.py ${small} ${noData} --year ${year} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet1-nBJet1" &
nohup krenew -t -K 10 -- bash -c "python printYields.py ${small} ${noData} --year ${year} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBJet0" &
nohup krenew -t -K 10 -- bash -c "python printYields.py ${small} ${noData} --year ${year} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBJet1" &
nohup krenew -t -K 10 -- bash -c "python printYields.py ${small} ${noData} --year ${year} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBJet2p" &

