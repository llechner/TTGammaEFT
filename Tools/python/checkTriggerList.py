import os

from TTGammaEFT.Tools.TriggerSelector import TriggerSelector

T16  = TriggerSelector(2016)
T16s = TriggerSelector(2016, singleLepton=True)

T17  = TriggerSelector(2017)
T17s = TriggerSelector(2017, singleLepton=True)

T18  = TriggerSelector(2018)
T18s = TriggerSelector(2018, singleLepton=True)

with open("availableTrigger_102X_2016.dat","r") as f:
    tr2016 = f.readlines()
tr2016 = [ "HLT_" + item.split("HLT_")[1].split(" ")[0] for item in tr2016]

with open("availableTrigger_102X_2017.dat","r") as f:
    tr2017 = f.readlines()
tr2017 = ["HLT_" + item.split("HLT_")[1].split(" ")[0] for item in tr2017]

with open("availableTrigger_102X_2018.dat","r") as f:
    tr2018 = f.readlines()
tr2018 = ["HLT_" + item.split("HLT_")[1].split(" ")[0] for item in tr2018]


print "2016"
print list(set(T16.getAllTrigger()) - set(tr2016))
print "2016, single"
print list(set(T16s.getAllTrigger()) - set(tr2016))

print "2017"
print list(set(T17.getAllTrigger()) - set(tr2017))
print "2017, single"
print list(set(T17s.getAllTrigger()) - set(tr2017))

print "2018"
print list(set(T18.getAllTrigger()) - set(tr2018))
print "2018, single"
print list(set(T18s.getAllTrigger()) - set(tr2018))

