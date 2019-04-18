python analysisPlots_semilep.py $@ --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p                   --plot_directory 102X_TTG_ppv15_v2 --plotFile all_1l_noPhoton
#python analysisPlots_semilep.py $@ --year 2018 --selection nLepTight2-OStight-nLepVeto2-nJet4p-nBTag1p          --plot_directory 102X_TTG_ppv15_v2 --plotFile all_1l_noPhoton

python analysisPlots_semilep.py --noData $@ --year 2018 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-pTG20-nPhoton1p    --plot_directory 102X_TTG_ppv15_v2 --plotFile all_1l
python analysisPlots_semilep.py --noData $@ --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-pTG20-nPhoton1p  --plot_directory 102X_TTG_ppv15_v2 --plotFile all_1l
#python analysisPlots_semilep.py --noData $@ --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag0-pTG20-nPhoton1p   --plot_directory 102X_TTG_ppv15_v2 --plotFile all_1l

python analysisPlots_semilep.py --noData $@ --year 2018 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-pTG20-nPhoton1p    --plot_directory 102X_TTG_ppv15_v2 --plotFile all_1l --categoryPlots
python analysisPlots_semilep.py --noData $@ --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-pTG20-nPhoton1p  --plot_directory 102X_TTG_ppv15_v2 --plotFile all_1l --categoryPlots
