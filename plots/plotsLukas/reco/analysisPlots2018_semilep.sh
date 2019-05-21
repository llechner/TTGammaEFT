nohup krenew -t -K 10 -- bash -c "python analysisPlots_semilep.py          --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p            --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l_noPhoton" &
#python analysisPlots_semilep.py          --addOtherBg --year 2018 --selection nLepTight2-OStight-nLepVeto2-nJet2p-nBTag1p    --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l_noPhoton
nohup krenew -t -K 10 -- bash -c "python analysisPlots_semilep.py          --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton0   --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l_noPhoton" &

nohup krenew -t -K 10 -- bash -c "python analysisPlots_semilep.py --noData --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nPhoton1p           --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots_semilep.py --noData --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p   --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots_semilep.py --noData --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-nPhoton1p    --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l" &

#python analysisPlots_semilep.py --noData --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-MVAPhoton  --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l
#python analysisPlots_semilep.py --noData --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-MVAPhoton   --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l

#python analysisPlots_semilep.py          --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoSieiePhoton  --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l_noPhoton
#python analysisPlots_semilep.py          --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-NoSieiePhoton   --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l_noPhoton

#python analysisPlots_semilep.py          --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoPhoton  --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l_noPhoton
#python analysisPlots_semilep.py          --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-NoChgIsoPhoton   --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l_noPhoton

#python analysisPlots_semilep.py          --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton  --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l_noPhoton
#python analysisPlots_semilep.py          --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-NoChgIsoNoSieiePhoton   --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l_noPhoton



#python analysisPlots_semilep.py --noData --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p  --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l --categoryPhoton PhotonGood0
#python analysisPlots_semilep.py --noData --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-nPhoton1p   --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l --categoryPhoton PhotonGood0

#python analysisPlots_semilep.py --noData --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-MVAPhoton  --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l --categoryPhoton PhotonMVA0
#python analysisPlots_semilep.py --noData --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-MVAPhoton   --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l --categoryPhoton PhotonMVA0

#python analysisPlots_semilep.py          --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoSieiePhoton  --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l_noPhoton --categoryPhoton PhotonNoSieie0
#python analysisPlots_semilep.py          --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-NoSieiePhoton   --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l_noPhoton --categoryPhoton PhotonNoSieie0

#python analysisPlots_semilep.py          --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoPhoton  --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l_noPhoton --categoryPhoton PhotonNoChgIso0
#python analysisPlots_semilep.py          --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-NoChgIsoPhoton   --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l_noPhoton --categoryPhoton PhotonNoChgIso0

#python analysisPlots_semilep.py          --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton  --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l_noPhoton --categoryPhoton PhotonNoChgIsoNoSieie0
#python analysisPlots_semilep.py          --addOtherBg --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-NoChgIsoNoSieiePhoton   --plot_directory 102X_TTG_ppv17_v2 --plotFile all_1l_noPhoton --categoryPhoton PhotonNoChgIsoNoSieie0
