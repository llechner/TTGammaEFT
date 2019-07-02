qcd="--noQCD"
year="2016"
cores="1"
lepSel=('e' 'mu' 'all')
lepSel2=('eetight' 'mumutight' 'all')
ptSel=('lowPT' 'medPT' 'highPT')
pthadSel=('lowhadPT' 'medhadPT' 'highhadPT')
catSel=('photoncat0' 'photoncat1' 'photoncat2' 'photoncat3')
hadcatSel=('photonhadcat0' 'photonhadcat1' 'photonhadcat2' 'photonhadcat3')
sieieSel=('lowSieie' 'highSieie')
chgSel=('lowChgIso' 'highChgIso')

# had fake CR
selection="nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton"
for sieie in "${sieieSel[@]}"; do
    for chg in "${chgSel[@]}"; do
        for pt in "${pthadSel[@]}"; do
            for lep in "${lepSel[@]}"; do
                echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}-${pt}-${sieie}-${chg}"
                for pcat in "${hadcatSel[@]}"; do
                    echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}-${pt}-${sieie}-${chg}-${pcat}"
                done
            done
            echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${pt}-${sieie}-${chg}"
        done

        echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${sieie}-${chg}"

        # inclusive
        for lep in "${lepSel[@]}"; do
            echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}-${sieie}-${chg}"
            for pcat in "${hadcatSel[@]}"; do
                echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}-${sieie}-${chg}-${pcat}"
            done
        done

    done
done

# SR
selection="nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p"
for pt in "${ptSel[@]}"; do
    for lep in "${lepSel[@]}"; do
        for pcat in "${catSel[@]}"; do
            echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}-${pt}-${pcat}"
        done
        echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}-${pt}"
    done
    echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${pt}"
done
echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}"

# inclusive
for lep in "${lepSel[@]}"; do
    for pcat in "${catSel[@]}"; do
        echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}-${pcat}"
    done
    echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}"
done


# VG CR
selection="nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p"
for pt in "${ptSel[@]}"; do
    for lep in "${lepSel[@]}"; do
        for pcat in "${catSel[@]}"; do
            echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}-${pt}-${pcat}"
        done
        echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}-${pt}"
    done
done
echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}"

# WG CR
selection="nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p"
for pt in "${ptSel[@]}"; do
    for lep in "${lepSel[@]}"; do
        for pcat in "${catSel[@]}"; do
            echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}-${pt}-${pcat}"
        done
        echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}-${pt}"
    done
done
echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}"

# inclusive
for lep in "${lepSel[@]}"; do
    for pcat in "${catSel[@]}"; do
        echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}-${pcat}"
    done
    echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}"
done


# DY SF
selection="nLepTight2-OStight-nLepVeto2-nJet4p-nBTag1p-onZSFllTight"
for lep in "${lepSel2[@]}"; do
    echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}"
done
echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}"

selection="nLepTight2-OStight-nLepVeto2-nJet2p-nBTag1p-onZSFllTight"
for lep in "${lepSel2[@]}"; do
    echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}"
done
echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}"

# misID SF DY
selection="nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg"
for pt in "${ptSel[@]}"; do
    for lep in "${lepSel[@]}"; do
        for pcat in "${catSel[@]}"; do
            echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}-${pt}-${pcat}"
        done
        echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}-${pt}"
    done
    echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${pt}"
done
echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}"

# inclusive
for lep in "${lepSel[@]}"; do
    for pcat in "${catSel[@]}"; do
        echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}-${pcat}"
    done
    echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}"
done


# misID SF ttbar
selection="nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg"
for pt in "${ptSel[@]}"; do
    for lep in "${lepSel[@]}"; do
        for pcat in "${catSel[@]}"; do
            echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}-${pt}-${pcat}"
        done
        echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}-${pt}"
    done
    echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${pt}"
done
echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}"

# inclusive
for lep in "${lepSel[@]}"; do
    for pcat in "${catSel[@]}"; do
        echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}-${pcat}"
    done
    echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}"
done


# ttbar CR
selection="nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton0"
for lep in "${lepSel[@]}"; do
    echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}"
done

# WJets CR
selection="nLepTight1-nLepVeto1-nJet3p-nPhoton0"
for lep in "${lepSel[@]}"; do
    echo "python cache_yields_semilep.py $@ --manual ${qcd} --year ${year} --cores ${cores} --selection ${selection}-${lep}"
done

