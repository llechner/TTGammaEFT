nohup krenew -t -K 10 -- bash -c "python analysisPlots_semilep.py          --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p            --plot_directory 102X_TTG_ppv15_v3 --plotFile all_1l_noPhoton" &
#python analysisPlots_semilep.py          --year 2018 --selection nLepTight2-OStight-nLepVeto2-nJet4p-nBTag1p    --plot_directory 102X_TTG_ppv15_v3 --plotFile all_1l_noPhoton
nohup krenew -t -K 10 -- bash -c "python analysisPlots_semilep.py          --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton0   --plot_directory 102X_TTG_ppv15_v3 --plotFile all_1l_noPhoton" &

nohup krenew -t -K 10 -- bash -c "python analysisPlots_semilep.py --noData --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p  --plot_directory 102X_TTG_ppv15_v3 --plotFile all_1l" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots_semilep.py --noData --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-nPhoton1p    --plot_directory 102X_TTG_ppv15_v3 --plotFile all_1l" &

#python analysisPlots_semilep.py --noData --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhotonMVA1p  --plot_directory 102X_TTG_ppv15_v3 --plotFile all_1l
#python analysisPlots_semilep.py --noData --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-nPhotonMVA1p   --plot_directory 102X_TTG_ppv15_v3 --plotFile all_1l

#python analysisPlots_semilep.py          --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhotonNoSieie1p  --plot_directory 102X_TTG_ppv15_v3 --plotFile all_1l_noPhoton
#python analysisPlots_semilep.py          --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-nPhotonNoSieie1p   --plot_directory 102X_TTG_ppv15_v3 --plotFile all_1l_noPhoton

#python analysisPlots_semilep.py          --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhotonNoChgIso1p  --plot_directory 102X_TTG_ppv15_v3 --plotFile all_1l_noPhoton
#python analysisPlots_semilep.py          --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-nPhotonNoChgIso1p   --plot_directory 102X_TTG_ppv15_v3 --plotFile all_1l_noPhoton

#python analysisPlots_semilep.py          --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhotonNoChgIsoNoSieie1p  --plot_directory 102X_TTG_ppv15_v3 --plotFile all_1l_noPhoton
#python analysisPlots_semilep.py          --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-nPhotonNoChgIsoNoSieie1p   --plot_directory 102X_TTG_ppv15_v3 --plotFile all_1l_noPhoton



#python analysisPlots_semilep.py --noData --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p  --plot_directory 102X_TTG_ppv15_v3 --plotFile photonId --categoryPhoton PhotonGood0
#python analysisPlots_semilep.py --noData --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-nPhoton1p   --plot_directory 102X_TTG_ppv15_v3 --plotFile photonId --categoryPhoton PhotonGood0

#python analysisPlots_semilep.py --noData --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhotonMVA1p  --plot_directory 102X_TTG_ppv15_v3 --plotFile photonId --categoryPhoton PhotonMVA0
#python analysisPlots_semilep.py --noData --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-nPhotonMVA1p   --plot_directory 102X_TTG_ppv15_v3 --plotFile photonId --categoryPhoton PhotonMVA0

#python analysisPlots_semilep.py          --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhotonNoSieie1p  --plot_directory 102X_TTG_ppv15_v3 --plotFile photonId_noPhoton --categoryPhoton PhotonNoSieie0
#python analysisPlots_semilep.py          --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-nPhotonNoSieie1p   --plot_directory 102X_TTG_ppv15_v3 --plotFile photonId_noPhoton --categoryPhoton PhotonNoSieie0

#python analysisPlots_semilep.py          --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhotonNoChgIso1p  --plot_directory 102X_TTG_ppv15_v3 --plotFile photonId_noPhoton --categoryPhoton PhotonNoChgIso0
#python analysisPlots_semilep.py          --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-nPhotonNoChgIso1p   --plot_directory 102X_TTG_ppv15_v3 --plotFile photonId_noPhoton --categoryPhoton PhotonNoChgIso0

#python analysisPlots_semilep.py          --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhotonNoChgIsoNoSieie1p  --plot_directory 102X_TTG_ppv15_v3 --plotFile photonId_noPhoton --categoryPhoton PhotonNoChgIsoNoSieie0
#python analysisPlots_semilep.py          --year 2018 --selection nLepTight1-nLepVeto1-nJet3p-nBTag0-nPhotonNoChgIsoNoSieie1p   --plot_directory 102X_TTG_ppv15_v3 --plotFile photonId_noPhoton --categoryPhoton PhotonNoChgIsoNoSieie0
