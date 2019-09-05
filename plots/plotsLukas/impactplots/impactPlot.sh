#cardfile="VG5_misDY5_addDYSF"
#cardfile="DY4p_VG4p_misDY4p"
carddir="2016/limits/cardFiles/defaultSetup/observed"
cachedir="/afs/hephy.at/data/llechner01/TTGammaEFT/cache"

cardpath=${cachedir}/${carddir}
for FILE in ${cardpath}/*.txt; do
    if [[ $FILE == *"shape"* ]]; then continue; fi
    card="$(basename -- $FILE)"
    card=${card%.txt}

    python impactPlot.py $@ --carddir ${carddir} --cardfile ${card} --year 2016 --cores 6
done
