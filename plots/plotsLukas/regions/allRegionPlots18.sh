year="2018"
carddir="limits/cardFiles/defaultSetup/observed"
cachedir="/afs/hephy.at/data/llechner01/TTGammaEFT/cache/analysis"

cardpath=${cachedir}/${year}/${carddir}
for FILE in ${cardpath}/*.txt; do
    if [[ $FILE == *"shape"* ]]; then continue; fi
    card="$(basename -- $FILE)"
    card=${card%.txt}

    echo ${card}

    python signalRegionPlot.py $@ --carddir ${carddir} --cardfile ${card} --year ${year} --postFit
    python signalRegionPlot.py $@ --carddir ${carddir} --cardfile ${card} --year ${year}
    python signalRegionPlot_sorted.py $@ --carddir ${carddir} --cardfile ${card} --year ${year} --postFit
    python signalRegionPlot_sorted.py $@ --carddir ${carddir} --cardfile ${card} --year ${year}

    python covMatrixPlot.py $@ --carddir ${carddir} --cardfile ${card} --year ${year} --postFit
    python covMatrixPlot.py $@ --carddir ${carddir} --cardfile ${card} --year ${year}

    python fitMatrixPlot.py $@ --carddir ${carddir} --cardfile ${card} --year ${year} --restrict
    python fitMatrixPlot.py $@ --carddir ${carddir} --cardfile ${card} --year ${year}
done


