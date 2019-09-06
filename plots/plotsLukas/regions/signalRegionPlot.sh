#cardfile="VG5_misDY5_addDYSF"
#cardfile="DY4p_VG4p_misDY4p"
carddir="2016/limits/cardFiles/defaultSetup/observed"
cachedir="/afs/hephy.at/data/llechner01/TTGammaEFT/cache"

cardpath=${cachedir}/${carddir}
for FILE in ${cardpath}/*.txt; do
    if [[ $FILE == *"shape"* ]]; then continue; fi
    card="$(basename -- $FILE)"
    card=${card%.txt}

    echo "python signalRegionPlot.py $@ --carddir ${carddir} --cardfile ${card} --year 2016 --postFit"
    python signalRegionPlot.py $@ --carddir ${carddir} --cardfile ${card} --year 2016 --postFit
    echo "python signalRegionPlot.py $@ --carddir ${carddir} --cardfile ${card} --year 2016"
    python signalRegionPlot.py $@ --carddir ${carddir} --cardfile ${card} --year 2016

    python covMatrixPlot.py $@ --carddir ${carddir} --cardfile ${card} --year 2016 --postFit
    python covMatrixPlot.py $@ --carddir ${carddir} --cardfile ${card} --year 2016

    python fitMatrixPlot.py $@ --carddir ${carddir} --cardfile ${card} --year 2016 --restrict
    python fitMatrixPlot.py $@ --carddir ${carddir} --cardfile ${card} --year 2016

done
