#python analysisPlots.py $@ --year 2016 --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFll-mll40                          --plot_directory 102X_TTG_pp_v14_v3 --plotFile all
python analysisPlots.py $@ --year 2016 --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p --plot_directory 102X_TTG_pp_v14_v3 --plotFile all
python analysisPlots.py $@ --year 2016 --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40                --plot_directory 102X_TTG_pp_v14_v3 --plotFile all
python analysisPlots.py $@ --year 2016 --selection dilepOS-nLepVeto2-offZSFll-nJet2p-nBTag1p-mll20                           --plot_directory 102X_TTG_pp_v14_v3 --plotFile all
#python analysisPlots.py $@ --year 2016 --selection dilepOS-nLepVeto2-onZll-met150                                            --plot_directory 102X_TTG_pp_v14_v3 --plotFile all
python analysisPlots.py $@ --year 2016 --selection dilepOS-nLepVeto2-onZll-nJet1p                                            --plot_directory 102X_TTG_pp_v14_v3 --plotFile all

python analysisPlots.py $@ --year 2016 --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p --plot_directory 102X_TTG_pp_v14_v3 --plotFile all --categoryPlots
python analysisPlots.py $@ --year 2016 --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40                --plot_directory 102X_TTG_pp_v14_v3 --plotFile all --categoryPlots
