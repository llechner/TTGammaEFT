small=""

#python preFiring2017_2D.py ${small} --selection dilepOS-nLepVeto2-pTj50               --plot_directory 102X_TTG_ppv1_v7 &
#python preFiring2017_2D.py ${small} --selection dilepOS-nLepVeto2-pTj150              --plot_directory 102X_TTG_ppv1_v7 &
#python preFiring2017_2D.py ${small} --selection dilepOS-nLepVeto2-etaj1.8To3.5        --plot_directory 102X_TTG_ppv1_v7 &
#python preFiring2017_2D.py ${small} --selection dilepOS-nLepVeto2-pTj150-etaj1.8To3.5 --plot_directory 102X_TTG_ppv1_v7 &
#python preFiring2017_2D.py ${small} --selection dilepOS-nLepVeto2                     --plot_directory 102X_TTG_ppv1_v7

#python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2-pTj50               --plot_directory 102X_TTG_ppv1_v7 --normalize &
#python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2-pTj150              --plot_directory 102X_TTG_ppv1_v7 --normalize &
#python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2-etaj1.8To3.5        --plot_directory 102X_TTG_ppv1_v7 --normalize &
#python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2-pTj150-etaj1.8To3.5 --plot_directory 102X_TTG_ppv1_v7 --normalize &
#python preFiring2017_allJets.py ${small} --selection dilepOS-nLepVeto2                     --plot_directory 102X_TTG_ppv1_v7 --normalize

#python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-pTj50               --plot_directory 102X_TTG_ppv1_v7 --plotFile main --normalize &
#python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-pTj150              --plot_directory 102X_TTG_ppv1_v7 --plotFile main --normalize &
#python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-etaj1.8To3.5        --plot_directory 102X_TTG_ppv1_v7 --plotFile main --normalize &
#python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-pTj150-etaj1.8To3.5 --plot_directory 102X_TTG_ppv1_v7 --plotFile main --normalize &
#python preFiring2017.py ${small} --selection dilepOS-nLepVeto2                     --plot_directory 102X_TTG_ppv1_v7 --plotFile main --normalize


#python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40 --plot_directory 102X_TTG_ppv1_v7 --plotFile main --normalize
python preFiring2017.py ${small} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-trigger --plot_directory 102X_TTG_ppv1_v7 --plotFile main --normalize --triggerSelection
