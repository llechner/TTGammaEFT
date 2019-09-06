path="${CMSSW_BASE}/src/TTGammaEFT/plots/plotsLukas/regions"

runNotifier.sh "python ${path}/signalRegionPlot.py --cardfile ${1}"
runNotifier.sh "python ${path}/signalRegionPlot.py --cardfile ${1} --postFit"
runNotifier.sh "python ${path}/signalRegionPlot_sorted.py --cardfile ${1}"
runNotifier.sh "python ${path}/signalRegionPlot_sorted.py --cardfile ${1} --postFit"

runNotifier.sh "python ${path}/covMatrixPlot.py --cardfile ${1} --postFit"
runNotifier.sh "python ${path}/covMatrixPlot.py --cardfile ${1}"
runNotifier.sh "python ${path}/fitMatrixPlot.py --cardfile ${1} --restrict"
runNotifier.sh "python ${path}/fitMatrixPlot.py --cardfile ${1}"

