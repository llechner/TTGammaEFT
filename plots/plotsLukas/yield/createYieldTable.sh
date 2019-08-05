selections=(
            "nLepTight1-nLepVeto1-nJet3-nBTag1p-nPhoton1p","Signal Region 3 Jets"
            "nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p","Signal Region geq 4 Jets"

#            "nLepTight1-nLepVeto1-nJet3-nBTag1p-NoChgIsoNoSieiePhoton","Hadronic Fake CR 3 Jets"
#            "nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton","Hadronic Fake CR geq 4 Jets"

            "nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-offZeg","VGamma CR 3 Jets"
            "nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-offZeg","VGamma CR geq 4 Jets"

            "nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg","MisID DY CR 3 Jets"
            "nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-addDYSF-addMisIDSF","MisID DY CR 3 Jets + SF"
            "nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-onZeg","MisID DY CR geq 4 Jets"
            "nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-onZeg-addDYSF-addMisIDSF","MisID DY CR geq 4 Jets + SF"
            "nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg","MisID TT CR"
            "nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-addDYSF-addMisIDSF","MisID TT CR + SF"
)

noPhotonSelections=(
            "nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton0","W+Jets CR 3 Jets"
            "nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton0","W+Jets CR geq 4 Jets"

            "nLepTight1-nLepVeto1-nJet3-nBTag1p-nPhoton0","TT CR 3 Jets"
            "nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton0","TT CR geq 4 Jets"

            "nLepTight2-OStight-nLepVeto2-nJet3-nBTag1p-onZSFllTight","DY CR 3 Jets"
            "nLepTight2-OStight-nLepVeto2-nJet3-nBTag1p-onZSFllTight-addDYSF","DY CR 3 Jets + SF"
            "nLepTight2-OStight-nLepVeto2-nJet4p-nBTag1p-onZSFllTight","DY CR geq 4 Jets"
            "nLepTight2-OStight-nLepVeto2-nJet4p-nBTag1p-onZSFllTight-addDYSF","DY CR geq 4 Jets + SF"
)

leps=("all" "e" "mu")

cat header.dat > tables_2016.dat
echo " " >> tables_2016.dat

echo "\section{Yields - Semileptonic Channel 2016}" >> tables_2016.dat
echo " " >> tables_2016.dat

for seltuple in "${selections[@]}"; do 
    IFS=","; set -- ${seltuple};
    sel=$1;
    label=$2;
    for lep in "${leps[@]}"; do
        python createYieldTable.py --year 2016 --selection ${sel} --mode ${lep} --label $label --removeNegative --runOnNonValid
        cat logs/2016_${sel}-${lep}.log >> tables_2016.dat
    done
done


for seltuple in "${noPhotonSelections[@]}"; do 
    IFS=","; set -- ${seltuple};
    sel=$1;
    label=$2;
    python createYieldTable.py --year 2016 --selection ${sel} --label $label --removeNegative --runOnNonValid
    cat logs/2016_${sel}.log >> tables_2016.dat
done


echo " " >> tables_2016.dat

echo " " >> tables_2016.dat
echo "\end{document}" >> tables_2016.dat
