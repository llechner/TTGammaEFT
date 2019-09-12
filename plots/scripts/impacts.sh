path="${CMSSW_BASE}/src/TTGammaEFT/plots/plotsLukas/impactplots"
cdir="2016/limits/cardFiles/defaultSetup/observed"
runNotifier.sh "python ${path}/impactPlot.py --cores 4 --cardfile ${1} --carddir ${cdir} --year 2016"
