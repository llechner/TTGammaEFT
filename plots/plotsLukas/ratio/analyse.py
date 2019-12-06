import os

with open( "matchingFakePi0.dat", "r" ) as f:
    output = f.readlines()

all     = len( output )
nMatch  = len( filter( lambda line: "match" in line, output ) )
nNoGen  = len( filter( lambda line: "no gen" in line, output ) )

gen     = map( lambda x: map( int, x.split("[")[1].split("]")[0].split(",")), filter( lambda line: "[" in line, output ) )
ptMatch = map( lambda x: x.split("[")[2].split("]")[0].split(","), filter( lambda line: "[" in line, output ) )
piParents = map( lambda x: x.split("[")[3].split("]")[0].split(","), filter( lambda line: "[" in line, output ) )
genMatch = [ (g,ptMatch[i],piParents[i]) for i, g in enumerate(gen) ]

noPtMatch = filter( lambda (gen,pdgList,par): not pdgList[0], genMatch )
ptMatch   = filter( lambda (gen,pdgList,par):     pdgList[0], genMatch )

noParMatch = filter( lambda (gen,pdgList,par): not par[0], ptMatch )
parMatch   = filter( lambda (gen,pdgList,par):     par[0], ptMatch )

print all
print len(gen)
print len(genMatch)
print len(ptMatch)
print len(parMatch)

nGen = len(gen)

for i, (gen, pt, par) in enumerate(parMatch):
    parMatch[i] = (gen,map(int,pt),map(abs,map(int,par)))

gen  = parMatch
nPi   = len( filter( lambda (pdgList,ptList,piPar): 111 in pdgList and 22 in pdgList, gen ) )
genPi = filter( lambda (pdgList,ptList,piPar): 111 in pdgList and 22 in pdgList, gen )

nPipt  = len( filter( lambda (pdgList,ptList,piPar): 111 in ptList, genPi ) )
genPi  = filter( lambda (pdgList,ptList,piPar): 111 in ptList, genPi )

nPibtau = len( filter( lambda (pdgList,ptList,piPar): 15 in piPar and (5 in piPar or max(piPar)>500), genPi ) )

nPitau = len( filter( lambda (pdgList,ptList,piPar): 15 in piPar, genPi ) )
#genPi  = filter( lambda (pdgList,ptList,piPar): not (15 in piPar), genPi )

nPib  = len( filter( lambda (pdgList,ptList,piPar): (5 in piPar or max(piPar)>500), genPi ) )
#genPi = filter( lambda (pdgList,ptList,piPar): not (5 in piPar), genPi )

#rest = filter( lambda (pdgList,ptList,piPar): not (5 in piPar or max(piPar)>500) and not (15 in piPar), genPi )

#for i, (gen, pt, par) in enumerate(rest):
#    print gen, pt, par

gen  = ptMatch
gen   = filter( lambda (pdgList,ptList,piPar): not (111 in pdgList and 22 in pdgList), gen )

nPhoMeson   = len( filter( lambda (pdgList,ptList,piPar): 22 in pdgList and max(map(abs,pdgList))>100, gen ) )
gen         = filter( lambda (pdgList,ptList,piPar): not (22 in pdgList and max(map(abs,pdgList))>100), gen )

nEMeson   = len( filter( lambda (pdgList,ptList,piPar): 11 in map(abs,pdgList) and max(map(abs,pdgList))>100, gen ) )
gen       = filter( lambda (pdgList,ptList,piPar): not (11 in map(abs,pdgList) and max(map(abs,pdgList))>100), gen )

nMuMeson   = len( filter( lambda (pdgList,ptList,piPar): 13 in map(abs,pdgList) and max(map(abs,pdgList))>100, gen ) )
gen        = filter( lambda (pdgList,ptList,piPar): not (13 in map(abs,pdgList) and max(map(abs,pdgList))>100), gen )

nq   = len( filter( lambda (pdgList,ptList,piPar): max(map(abs,pdgList))<10, gen ) )
gen  = filter( lambda (pdgList,ptList,piPar): not max(map(abs,pdgList))<10, gen )

nl   = len( filter( lambda (pdgList,ptList,piPar): max(map(abs,pdgList))<14, gen ) )
gen  = filter( lambda (pdgList,ptList,piPar): not max(map(abs,pdgList))<14, gen )

nERad = len( filter( lambda (pdgList,ptList,piPar): 22 in pdgList and not set(pdgList)-set([-11,11,24,-24,6,5,-6,-5,22,21]), gen ) )
gen   = filter( lambda (pdgList,ptList,piPar): not(22 in pdgList and not set(pdgList)-set([-11,11,13,-13,24,-24,6,5,-6,-5,22,21])), gen )

nSMTau  = len( filter( lambda (pdgList,ptList,piPar): 15 in map(abs,pdgList) and max(map(abs,pdgList))<30, gen ) )
gen     = filter( lambda (pdgList,ptList,piPar): not (15 in map(abs,pdgList) and max(map(abs,pdgList))<30), gen )

nSM  = len( filter( lambda (pdgList,ptList,piPar): (11 in map(abs,pdgList) or 13 in map(abs,pdgList)) and max(map(abs,pdgList))<30, gen ) )
gen  = filter( lambda (pdgList,ptList,piPar): not ((11 in map(abs,pdgList) or 13 in map(abs,pdgList)) and max(map(abs,pdgList))<30), gen )

nMeson  = len( filter( lambda (pdgList,ptList,piPar): min(filter(lambda x: x>6, map(abs,pdgList)))>100, gen ) )
gen     = filter( lambda (pdgList,ptList,piPar): not (min(filter(lambda x: x>6, map(abs,pdgList)))>100), gen )

nTau  = len( filter( lambda (pdgList,ptList,piPar): 15 in map(abs,pdgList), gen ) )
gen   = filter( lambda (pdgList,ptList,piPar): not (15 in map(abs,pdgList)), gen )

#for g in gen:
#    print g

print "total events: %i, %f%%"%(all, all/float(all)*100.)
print "with gen matching: %i, %f%%"%(nMatch, nMatch/float(all)*100.)
print "w close gen particles: %i, %f%%"%(nGen, nGen/float(nGen+nNoGen)*100.)
print "w/o close gen particles: %i, %f%%"%(nNoGen, nNoGen/float(nGen+nNoGen)*100.)

print "pion decay: %i, %f%%"%(nPi, nPi/float(nGen+nNoGen)*100.)
print "of those are"
print "pi0 pt close to gamma: %i, %f%%"%(nPipt, nPipt/float(nPi)*100.)
print "of those are"
print "tau and b parent: %i, %f%%"%(nPibtau, nPibtau/float(nPipt)*100.)
print "b parent: %i, %f%%"%(nPib, nPib/float(nPipt)*100.)
print "tau parent: %i, %f%%"%(nPitau, nPitau/float(nPipt)*100.)
print
print "photons+mesons: %i, %f%%"%(nPhoMeson, nPhoMeson/float(nGen+nNoGen)*100.)
print "e+mesons: %i, %f%%"%(nEMeson, nEMeson/float(nGen+nNoGen)*100.)
print "mu+mesons: %i, %f%%"%(nMuMeson, nMuMeson/float(nGen+nNoGen)*100.)
print "q only: %i, %f%%"%(nq, nq/float(nGen+nNoGen)*100.)
print "e/mu only: %i, %f%%"%(nl, nl/float(nGen+nNoGen)*100.)
print "e/mu radiation: %i, %f%%"%(nERad, nERad/float(nGen+nNoGen)*100.)
print "SM tau process only: %i, %f%%"%(nSMTau, nSMTau/float(nGen+nNoGen)*100.)
print "SM e/mu process only: %i, %f%%"%(nSM, nSM/float(nGen+nNoGen)*100.)
print "Mesons only: %i, %f%%"%(nMeson, nMeson/float(nGen+nNoGen)*100.)
print "contain tau: %i, %f%%"%(nTau, nTau/float(nGen+nNoGen)*100.)

print "rest: %i, %f%%"%(len(gen), len(gen)/float(nGen+nNoGen)*100.)
