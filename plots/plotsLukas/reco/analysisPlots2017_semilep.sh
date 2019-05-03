nohup krenew -t -K 10 -- bash -c "python analysisPlots_semilep.py          --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p            --plot_directory 102X_TTG_ppv16_v1 --plotFile all_1l_noPhoton" & #SPLIT3
#python analysisPlots_semilep.py          --year 2017 --selection nLepTight2-OStight-nLepVeto2-nJet4p-nBTag1p    --plot_directory 102X_TTG_ppv16_v1 --plotFile all_1l_noPhoton #SPLIT3
nohup krenew -t -K 10 -- bash -c "python analysisPlots_semilep.py          --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton0   --plot_directory 102X_TTG_ppv16_v1 --plotFile all_1l_noPhoton" & #SPLIT3

nohup krenew -t -K 10 -- bash -c "python analysisPlots_semilep.py --noData --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p  --plot_directory 102X_TTG_ppv16_v1 --plotFile all_1l" & #SPLIT3
nohup krenew -t -K 10 -- bash -c "python analysisPlots_semilep.py --noData --year 2017 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-nPhoton1p    --plot_directory 102X_TTG_ppv16_v1 --plotFile all_1l" & #SPLIT3

#python analysisPlots_semilep.py --noData --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-MVAPhoton  --plot_directory 102X_TTG_ppv16_v1 --plotFile all_1l #SPLIT3
#python analysisPlots_semilep.py --noData --year 2017 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-MVAPhoton   --plot_directory 102X_TTG_ppv16_v1 --plotFile all_1l #SPLIT3

#python analysisPlots_semilep.py          --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoSieiePhoton  --plot_directory 102X_TTG_ppv16_v1 --plotFile all_1l_noPhoton #SPLIT3
#python analysisPlots_semilep.py          --year 2017 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-NoSieiePhoton   --plot_directory 102X_TTG_ppv16_v1 --plotFile all_1l_noPhoton #SPLIT3

#python analysisPlots_semilep.py          --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoPhoton  --plot_directory 102X_TTG_ppv16_v1 --plotFile all_1l_noPhoton #SPLIT3
#python analysisPlots_semilep.py          --year 2017 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-NoChgIsoPhoton   --plot_directory 102X_TTG_ppv16_v1 --plotFile all_1l_noPhoton #SPLIT3

#python analysisPlots_semilep.py          --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton  --plot_directory 102X_TTG_ppv16_v1 --plotFile all_1l_noPhoton #SPLIT3
#python analysisPlots_semilep.py          --year 2017 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-NoChgIsoNoSieiePhoton   --plot_directory 102X_TTG_ppv16_v1 --plotFile all_1l_noPhoton #SPLIT3



#python analysisPlots_semilep.py --noData --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p  --plot_directory 102X_TTG_ppv16_v1 --plotFile all --categoryPhoton PhotonGood0 #SPLIT3
#python analysisPlots_semilep.py --noData --year 2017 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-nPhoton1p   --plot_directory 102X_TTG_ppv16_v1 --plotFile all --categoryPhoton PhotonGood0 #SPLIT3

#python analysisPlots_semilep.py --noData --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-MVAPhoton  --plot_directory 102X_TTG_ppv16_v1 --plotFile all --categoryPhoton PhotonMVA0 #SPLIT3
#python analysisPlots_semilep.py --noData --year 2017 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-MVAPhoton   --plot_directory 102X_TTG_ppv16_v1 --plotFile all --categoryPhoton PhotonMVA0 #SPLIT3

#python analysisPlots_semilep.py          --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoSieiePhoton  --plot_directory 102X_TTG_ppv16_v1 --plotFile all_noPhoton --categoryPhoton PhotonNoSieie0 #SPLIT3
#python analysisPlots_semilep.py          --year 2017 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-NoSieiePhoton   --plot_directory 102X_TTG_ppv16_v1 --plotFile all_noPhoton --categoryPhoton PhotonNoSieie0 #SPLIT3

#python analysisPlots_semilep.py          --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoPhoton  --plot_directory 102X_TTG_ppv16_v1 --plotFile all_noPhoton --categoryPhoton PhotonNoChgIso0 #SPLIT3
#python analysisPlots_semilep.py          --year 2017 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-NoChgIsoPhoton   --plot_directory 102X_TTG_ppv16_v1 --plotFile all_noPhoton --categoryPhoton PhotonNoChgIso0 #SPLIT3

#python analysisPlots_semilep.py          --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton  --plot_directory 102X_TTG_ppv16_v1 --plotFile all_noPhoton --categoryPhoton PhotonNoChgIsoNoSieie0 #SPLIT3
#python analysisPlots_semilep.py          --year 2017 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-NoChgIsoNoSieiePhoton   --plot_directory 102X_TTG_ppv16_v1 --plotFile all_noPhoton --categoryPhoton PhotonNoChgIsoNoSieie0 #SPLIT3

