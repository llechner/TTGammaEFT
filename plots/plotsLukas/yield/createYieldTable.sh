cat header.dat > tables.dat
echo " " >> tables.dat

#python createYieldTable.py $@ --runOnNonValid --year 2016 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton-all
#python createYieldTable.py $@ --runOnNonValid --year 2016 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton-e
#python createYieldTable.py $@ --runOnNonValid --year 2016 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton-mu

#python createYieldTable.py $@ --runOnNonValid --year 2016 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p-all
#python createYieldTable.py $@ --runOnNonValid --year 2016 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p-e
#python createYieldTable.py $@ --runOnNonValid --year 2016 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p-mu

#python createYieldTable.py $@ --runOnNonValid --year 2016 --selection nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-all
#python createYieldTable.py $@ --runOnNonValid --year 2016 --selection nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-e
#python createYieldTable.py $@ --runOnNonValid --year 2016 --selection nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-mu

#python createYieldTable.py $@ --runOnNonValid --year 2016 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-all
#python createYieldTable.py $@ --runOnNonValid --year 2016 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-e
#python createYieldTable.py $@ --runOnNonValid --year 2016 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-mu

#python createYieldTable.py $@ --runOnNonValid --year 2016 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-all
#python createYieldTable.py $@ --runOnNonValid --year 2016 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-e
#python createYieldTable.py $@ --runOnNonValid --year 2016 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-mu

#python createYieldTable.py $@ --runOnNonValid --year 2016 --selection nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-all
#python createYieldTable.py $@ --runOnNonValid --year 2016 --selection nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-e
#python createYieldTable.py $@ --runOnNonValid --year 2016 --selection nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-mu

echo "\section{Yields - Semileptonic Channel 2016}" >> tables.dat
echo " " >> tables.dat
cat logs/2016_nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton-all.log >> tables.dat
cat logs/2016_nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton-e.log >> tables.dat
cat logs/2016_nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton-mu.log >> tables.dat

cat logs/2016_nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p-all.log >> tables.dat
cat logs/2016_nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p-e.log >> tables.dat
cat logs/2016_nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p-mu.log >> tables.dat

cat logs/2016_nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-all.log >> tables.dat
cat logs/2016_nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-e.log >> tables.dat
cat logs/2016_nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-mu.log >> tables.dat

cat logs/2016_nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-all.log >> tables.dat
cat logs/2016_nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-e.log >> tables.dat
cat logs/2016_nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-mu.log >> tables.dat

cat logs/2016_nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-all.log >> tables.dat
cat logs/2016_nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-e.log >> tables.dat
cat logs/2016_nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-mu.log >> tables.dat

cat logs/2016_nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-all.log >> tables.dat
cat logs/2016_nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-e.log >> tables.dat
cat logs/2016_nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-mu.log >> tables.dat
echo " " >> tables.dat

#python createYieldTable.py $@ --runOnNonValid --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton-all
#python createYieldTable.py $@ --runOnNonValid --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton-e
#python createYieldTable.py $@ --runOnNonValid --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton-mu

#python createYieldTable.py $@ --runOnNonValid --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p-all
#python createYieldTable.py $@ --runOnNonValid --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p-e
#python createYieldTable.py $@ --runOnNonValid --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p-mu

#python createYieldTable.py $@ --runOnNonValid --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-all
#python createYieldTable.py $@ --runOnNonValid --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-e
#python createYieldTable.py $@ --runOnNonValid --year 2017 --selection nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-mu

#python createYieldTable.py $@ --runOnNonValid --year 2017 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-all
#python createYieldTable.py $@ --runOnNonValid --year 2017 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-e
#python createYieldTable.py $@ --runOnNonValid --year 2017 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-mu

#python createYieldTable.py $@ --runOnNonValid --year 2017 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-all
#python createYieldTable.py $@ --runOnNonValid --year 2017 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-e
#python createYieldTable.py $@ --runOnNonValid --year 2017 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-mu

#python createYieldTable.py $@ --runOnNonValid --year 2017 --selection nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-all
#python createYieldTable.py $@ --runOnNonValid --year 2017 --selection nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-e
#python createYieldTable.py $@ --runOnNonValid --year 2017 --selection nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-mu

echo "\section{Yields - Semileptonic Channel 2017}" >> tables.dat
echo " " >> tables.dat
cat logs/2017_nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton-all.log >> tables.dat
cat logs/2017_nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton-e.log >> tables.dat
cat logs/2017_nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton-mu.log >> tables.dat

cat logs/2017_nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p-all.log >> tables.dat
cat logs/2017_nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p-e.log >> tables.dat
cat logs/2017_nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p-mu.log >> tables.dat

cat logs/2017_nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-all.log >> tables.dat
cat logs/2017_nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-e.log >> tables.dat
cat logs/2017_nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-mu.log >> tables.dat

cat logs/2017_nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-all.log >> tables.dat
cat logs/2017_nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-e.log >> tables.dat
cat logs/2017_nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-mu.log >> tables.dat

cat logs/2017_nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-all.log >> tables.dat
cat logs/2017_nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-e.log >> tables.dat
cat logs/2017_nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-mu.log >> tables.dat

cat logs/2017_nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-all.log >> tables.dat
cat logs/2017_nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-e.log >> tables.dat
cat logs/2017_nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-mu.log >> tables.dat

#python createYieldTable.py $@ --runOnNonValid --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton-all
#python createYieldTable.py $@ --runOnNonValid --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton-e
#python createYieldTable.py $@ --runOnNonValid --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton-mu

#python createYieldTable.py $@ --runOnNonValid --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p-all
#python createYieldTable.py $@ --runOnNonValid --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p-e
#python createYieldTable.py $@ --runOnNonValid --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p-mu

#python createYieldTable.py $@ --runOnNonValid --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-all
#python createYieldTable.py $@ --runOnNonValid --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-e
#python createYieldTable.py $@ --runOnNonValid --year 2018 --selection nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-mu

python createYieldTable.py $@ --runOnNonValid --year 2018 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-all
#python createYieldTable.py $@ --runOnNonValid --year 2018 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-e
python createYieldTable.py $@ --runOnNonValid --year 2018 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-mu

python createYieldTable.py $@ --runOnNonValid --year 2018 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-all
python createYieldTable.py $@ --runOnNonValid --year 2018 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-e
python createYieldTable.py $@ --runOnNonValid --year 2018 --selection nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-mu

python createYieldTable.py $@ --runOnNonValid --year 2018 --selection nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-all
python createYieldTable.py $@ --runOnNonValid --year 2018 --selection nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-e
python createYieldTable.py $@ --runOnNonValid --year 2018 --selection nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-mu

echo "\section{Yields - Semileptonic Channel 2018}" >> tables.dat
echo " " >> tables.dat
cat logs/2018_nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton-all.log >> tables.dat
cat logs/2018_nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton-e.log >> tables.dat
cat logs/2018_nLepTight1-nLepVeto1-nJet4p-nBTag1p-NoChgIsoNoSieiePhoton-mu.log >> tables.dat

cat logs/2018_nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p-all.log >> tables.dat
cat logs/2018_nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p-e.log >> tables.dat
cat logs/2018_nLepTight1-nLepVeto1-nJet4p-nBTag1p-nPhoton1p-mu.log >> tables.dat

cat logs/2018_nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-all.log >> tables.dat
cat logs/2018_nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-e.log >> tables.dat
cat logs/2018_nLepTight1-nLepVeto1-nJet4p-nBTag0-nPhoton1p-mu.log >> tables.dat

cat logs/2018_nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-all.log >> tables.dat
cat logs/2018_nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-mu.log >> tables.dat
cat logs/2018_nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-onZeg-e.log >> tables.dat

cat logs/2018_nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-all.log >> tables.dat
cat logs/2018_nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-e.log >> tables.dat
cat logs/2018_nLepTight1-nLepVeto1-nJet3-nBTag0-nPhoton1p-mu.log >> tables.dat

cat logs/2018_nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-all.log >> tables.dat
cat logs/2018_nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-e.log >> tables.dat
cat logs/2018_nLepTight1-nLepVeto1-nJet2-nBTag2-nPhoton1p-offZeg-mu.log >> tables.dat

echo " " >> tables.dat
echo "\end{document}" >> tables.dat
