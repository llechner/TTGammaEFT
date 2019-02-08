#cardfile="test"
cardfile="TTG_DiLept_1L_EFT_2016_ctZ_0_ctZI_0_dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p_small"
#cardfile="TTG_DiLept_1L_EFT_2016_ctZ_0_ctZI_0_dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40_full"

python impactPlot.py --removeDir --cardfile ${cardfile} --cores 6 --year 2016
