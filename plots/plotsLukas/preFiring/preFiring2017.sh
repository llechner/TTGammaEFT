small=""

#nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-offZSFll         --plot_directory 102X_TTG_ppv1_v6 --plotFile main --normalize" &
#nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-onZSFll          --plot_directory 102X_TTG_ppv1_v6 --plotFile main --normalize" &
#nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2                  --plot_directory 102X_TTG_ppv1_v6 --plotFile main --normalize" &

nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-offZSFll-pTj50         --plot_directory 102X_TTG_ppv1_v6 --plotFile main --normalize" &
nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-onZSFll-pTj50          --plot_directory 102X_TTG_ppv1_v6 --plotFile main --normalize" &
nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-pTj50                  --plot_directory 102X_TTG_ppv1_v6 --plotFile main --normalize" &

#nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-offZSFll-pTj150         --plot_directory 102X_TTG_ppv1_v6 --plotFile main --normalize" &
#nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-onZSFll-pTj150          --plot_directory 102X_TTG_ppv1_v6 --plotFile main --normalize" &
#nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-pTj150                  --plot_directory 102X_TTG_ppv1_v6 --plotFile main --normalize" &

#nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-offZSFll-pTj100-etaj2.25To3         --plot_directory 102X_TTG_ppv1_v6 --plotFile main --normalize" &
#nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-onZSFll-pTj100-etaj2.25To3          --plot_directory 102X_TTG_ppv1_v6 --plotFile main --normalize" &
#nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-pTj100-etaj2.25To3                  --plot_directory 102X_TTG_ppv1_v6 --plotFile main --normalize" &

#nohup krenew -t -K 10 -- bash -c "python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2-offZSFll --plot_directory 102X_TTG_ppv1_v6 --normalize" &
#nohup krenew -t -K 10 -- bash -c "python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2-onZSFll  --plot_directory 102X_TTG_ppv1_v6 --normalize" &
#nohup krenew -t -K 10 -- bash -c "python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2          --plot_directory 102X_TTG_ppv1_v6 --normalize" &

#nohup krenew -t -K 10 -- bash -c "python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2-offZSFll-pTj50 --plot_directory 102X_TTG_ppv1_v6 --normalize" &
#nohup krenew -t -K 10 -- bash -c "python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2-onZSFll-pTj50  --plot_directory 102X_TTG_ppv1_v6 --normalize" &
#nohup krenew -t -K 10 -- bash -c "python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2-pTj50          --plot_directory 102X_TTG_ppv1_v6 --normalize" &



# not normalized
#nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-offZSFll          --plot_directory 102X_TTG_ppv1_v6 --plotFile main" &
#nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-onZSFll           --plot_directory 102X_TTG_ppv1_v6 --plotFile main" &
#nohup krenew -t -K 10 -- bash -c "python preFiring2017.py ${small} --selection dilepOS-nLepVeto2                   --plot_directory 102X_TTG_ppv1_v6 --plotFile main" &

#nohup krenew -t -K 10 -- bash -c "python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2-offZSFll  --plot_directory 102X_TTG_ppv1_v6" &
#nohup krenew -t -K 10 -- bash -c "python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2-onZSFll   --plot_directory 102X_TTG_ppv1_v6" &
#nohup krenew -t -K 10 -- bash -c "python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2           --plot_directory 102X_TTG_ppv1_v6" &


