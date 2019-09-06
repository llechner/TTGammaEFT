runNotifier.sh "python signalRegionPlot.py --cardfile ${1}"
runNotifier.sh "python signalRegionPlot.py --cardfile ${1} --postFit"
runNotifier.sh "python signalRegionPlot_sorted.py --cardfile ${1}"
runNotifier.sh "python signalRegionPlot_sorted.py --cardfile ${1} --postFit"

runNotifier.sh "python covMatrixPlot.py --cardfile ${1} --postFit"
runNotifier.sh "python covMatrixPlot.py --cardfile ${1}"
runNotifier.sh "python fitMatrixPlot.py --cardfile ${1} --restrict"
runNotifier.sh "python fitMatrixPlot.py --cardfile ${1}"

