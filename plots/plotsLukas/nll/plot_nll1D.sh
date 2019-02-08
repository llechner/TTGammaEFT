python plot_nll1D.py $1 --skipMissingPoints --year 2016 --variables ctZ ctZI --zRange 0 5 --xyRange -0.7 0.7 -0.7 0.7 --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p
python plot_nll1D.py $1 --skipMissingPoints --year 2017 --variables ctZ ctZI --zRange 0 5 --xyRange -0.7 0.7 -0.7 0.7 --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p

python plot_nll1D.py $1 --skipMissingPoints --year 2016 --variables ctW ctWI --zRange 0 5 --xyRange -0.3 0.3 -0.7 0.7 --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p
python plot_nll1D.py $1 --skipMissingPoints --year 2017 --variables ctW ctWI --zRange 0 5 --xyRange -0.3 0.3 -0.7 0.7 --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p

#SemiLep
python plot_nll1D.py --semilep $1 --skipMissingPoints --year 2016 --variables ctZ ctZI --zRange 0 5 --xyRange -0.5 0.5 -0.5 0.5 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-pTG20-nPhoton1p
python plot_nll1D.py --semilep $1 --skipMissingPoints --year 2017 --variables ctZ ctZI --zRange 0 5 --xyRange -0.5 0.5 -0.5 0.5 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-pTG20-nPhoton1p

python plot_nll1D.py --semilep $1 --skipMissingPoints --year 2016 --variables ctW ctWI --zRange 0 5 --xyRange -0.25 0.25 -0.5 0.5 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-pTG20-nPhoton1p
python plot_nll1D.py --semilep $1 --skipMissingPoints --year 2017 --variables ctW ctWI --zRange 0 5 --xyRange -0.25 0.25 -0.5 0.5 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-pTG20-nPhoton1p

#Combined
python plot_nll1D.py $1 --skipMissingPoints --year combined --variables ctZ ctZI --zRange 0 5 --xyRange -0.6 0.6 -0.6 0.6 --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p
python plot_nll1D.py $1 --skipMissingPoints --year combined --variables ctW ctWI --zRange 0 5 --xyRange -0.6 0.6 -0.6 0.6 --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p

#SemiLep combined
python plot_nll1D.py --semilep $1 --skipMissingPoints --year combined --variables ctZ ctZI --zRange 0 5 --xyRange -0.4 0.4 -0.4 0.4 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-pTG20-nPhoton1p
python plot_nll1D.py --semilep $1 --skipMissingPoints --year combined --variables ctW ctWI --zRange 0 5 --xyRange -0.25 0.25 -0.4 0.4 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-pTG20-nPhoton1p
