path="${CMSSW_BASE}/src/TTGammaEFT/plots/plotsLukas/impactplots"
runNotifier.sh "python ${path}/impactPlot.py --cores 4 --cardfile ${1}"
