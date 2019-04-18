python analysisPlots.py $@ --year 2018 --selection dilepOS-nLepVeto2-offZSFll-nJet2p-nBTag1p-mll20 --plot_directory 102X_TTG_ppv15_v2 --plotFile all_noPhoton
python analysisPlots.py $@ --year 2018 --selection dilepOS-nLepVeto2-onZll-nJet1p                  --plot_directory 102X_TTG_ppv15_v2 --plotFile all_noPhoton
#python analysisPlots.py $@ --year 2018 --selection dilepOS-nLepVeto2-onZll-met150                  --plot_directory 102X_TTG_ppv15_v2 --plotFile all_noPhoton

python analysisPlots.py --noData $@ --year 2018 --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40                --plot_directory 102X_TTG_ppv15_v2 --plotFile all
python analysisPlots.py --noData $@ --year 2018 --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p --plot_directory 102X_TTG_ppv15_v2 --plotFile all

python analysisPlots.py --noData $@ --year 2018 --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40                --plot_directory 102X_TTG_ppv15_v2 --plotFile all --categoryPlots
python analysisPlots.py --noData $@ --year 2018 --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p --plot_directory 102X_TTG_ppv15_v2 --plotFile all --categoryPlots


