import subprocess, os
from Samples.miniAOD.Run2016_17Jul2018 import allSamples

exFiles = []
inFiles = os.listdir("dat/")
inFiles = filter(lambda file: file.count("EventList"), inFiles)

for i, inFile in enumerate(inFiles):
    os.system("cp dat/" + inFile + " " + inFile)
    outFile = inFile.rstrip(".dat")
    for j, sample in enumerate(allSamples):
        if not sample.name.startswith("SingleElectron") and not sample.name.startswith("SingleMuon"): continue
#        if not sample.name.startswith("SingleElectron"): continue
        if ((sample.name.startswith("SingleElectron") and outFile.endswith("-e")) or (sample.name.startswith("SingleMuon") and outFile.endswith("-mu"))) or ((sample.name.startswith("SingleElectron") and outFile.startswith("e")) or (sample.name.startswith("SingleMuon") and outFile.startswith("mu"))):
            print "Running on data sample %s with DAS path %s"%(sample.name, sample.DASname)
            cmd = ["edmPickEvents.py", "--output="+outFile+"_"+sample.name, sample.DASname, inFile, "--crab"]
            print "Executing command %s"%" ".join(cmd)
            subprocess.call( cmd )
    
            with open(outFile+"_"+sample.name+"_crab.py","r") as f:
                pyfile = f.readlines()
            with open(outFile+"_"+sample.name+"_crab.py","w") as f:
                for line in pyfile:
                    if "config.Data.unitsPerJob" in line:
                        line = line.replace("5", "10000")
                    if "config.General.workArea" in line:
                        workArea = line.split(" = ")[1].split("'")[1]
                        line = "config.General.workArea = '" + workArea + "_" + str(i) + "_" + str(j) + "'"
                    f.write(line.replace("US_Wisconsin","AT_Vienna"))
            exFiles.append(outFile+"_"+sample.name+"_crab.py")

            with open(outFile+"_"+sample.name+"_runEvents.txt","r") as f:
                pyfile = f.readlines()
            with open(outFile+"_"+sample.name+"_runEvents.txt","w") as f:
                for line in pyfile:
                    if line.count("-"): continue
                    f.write(line)

    
print "Please execute the following commands:"
for file in exFiles:
    print "crab submit -c " + file
