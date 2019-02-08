small=""

nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-offZSFll         --plot_directory 102X_TTG_ppv1_v2 --plotFile main --normalize" &
nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-onZSFll          --plot_directory 102X_TTG_ppv1_v2 --plotFile main --normalize" &
nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2                  --plot_directory 102X_TTG_ppv1_v2 --plotFile main --normalize" &

nohup krenew -t -K 10 -- bash -c "python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2-offZSFll --plot_directory 102X_TTG_ppv1_v2 --normalize" &
nohup krenew -t -K 10 -- bash -c "python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2-onZSFll  --plot_directory 102X_TTG_ppv1_v2 --normalize" &
nohup krenew -t -K 10 -- bash -c "python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2          --plot_directory 102X_TTG_ppv1_v2 --normalize" &

#nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-offZSFll          --plot_directory 102X_TTG_ppv1_v2 --plotFile main" &
#nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-onZSFll           --plot_directory 102X_TTG_ppv1_v2 --plotFile main" &
#nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2                   --plot_directory 102X_TTG_ppv1_v2 --plotFile main" &

#nohup krenew -t -K 10 -- bash -c "python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2-offZSFll  --plot_directory 102X_TTG_ppv1_v2" &
#nohup krenew -t -K 10 -- bash -c "python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2-onZSFll   --plot_directory 102X_TTG_ppv1_v2" &
#nohup krenew -t -K 10 -- bash -c "python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2           --plot_directory 102X_TTG_ppv1_v2" &


