#SR4phighIso SR3lowIso WJets4p VG4p SR4poffM3 misDY2 DY5 SR4plowIso DY2 DY3 WJets3 SR3offM3 DY4p misDY5 SR4ponM3 misDY4 misTT2 TT4p SR3highIso SR3 SR4p misDY4p DY4 SR3onM3 misDY3 VG4 VG5 TT3 VG2 VG3

overwrite="--overwrite"
#overwrite=""

regions="SR3M3 SR3Iso"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="SR4pM3 SR4pIso"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="TT3 TT4p WJets3 WJets4p DY3 DY4p misTT2 misDY3 misDY4p VG3 VG4p SR3M3 SR4pM3 SR3Iso SR4pIso"
runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="TT3 TT4p WJets3 WJets4p DY3 DY4p misTT2 misDY3 misDY4p VG3 VG4p SR3Iso SR4pIso"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="TT3 TT4p WJets3 WJets4p DY3 DY4p misTT2 misDY3 misDY4p VG3 VG4p SR3lowIso SR4plowIso SR3highIso SR4phighIso SR3M3 SR4pM3 SR3Iso SR4pIso"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="DY2 DY3 DY4 DY5 DY4p misDY2 misDY3 misDY4 misDY5 misDY4p VG2 VG3 VG4 VG5 VG4p"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="TT3 TT4p WJets3 WJets4p DY3 DY4p misTT2 misDY3 misDY4p VG3 VG4p SR3onM3 SR4ponM3 SR3offM3 SR4poffM3 SR3lowIso SR4plowIso SR3highIso SR4phighIso SR3 SR4p"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="TT3 TT4p WJets3 WJets4p DY3 DY4p misTT2 misDY3 misDY4p VG3 VG4p SR3onM3 SR4ponM3 SR3offM3 SR4poffM3 SR4phighIso"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="TT3 TT4p DY3 DY4p misTT2 misDY3 misDY4p VG3 VG4p SR3onM3 SR4ponM3 SR3offM3 SR4poffM3 SR3lowIso SR4plowIso SR3highIso SR4phighIso"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="TT3 TT4p DY3 DY4p misTT2 misDY3 misDY4p VG3 VG4p SR3onM3 SR4ponM3 SR3offM3 SR4poffM3 SR4phighIso"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="TT3 TT4p DY3 DY4p misTT2 misDY3 misDY4p VG3 VG4p SR3onM3 SR4ponM3 SR3offM3 SR4poffM3 SR3lowIso SR4plowIso SR3highIso SR4phighIso"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="TT3 TT4p WJets3 WJets4p DY3 DY4p misTT2 misDY3 misDY4p VG3 VG4p SR3onM3 SR4ponM3 SR3offM3 SR4poffM3 SR3lowIso SR4plowIso SR3highIso SR4phighIso"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="TT3 TT4p DY3 DY4p misTT2 misDY3 misDY4p VG3 VG4p SR3onM3 SR4ponM3 SR3offM3 SR4poffM3"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="TT3 TT4p DY3 DY4p misTT2 misDY3 misDY4p VG3 VG4p SR3 SR4p"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="TT3 TT4p WJets3 WJets4p DY3 DY4p misTT2 misDY3 misDY4p VG3 VG4p SR3 SR4p"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="DY3 DY4p misTT2 misDY3 misDY4p VG3 VG4p SR3 SR4p"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="misDY3 VG3 DY3 misDY4p VG4p DY4p"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="misDY3 VG3 DY3 misDY4p VG4p DY4p misTT2"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

#WJets4p VG4p DY3 WJets3 DY4p misTT2 TT4p SR3 SR4p misDY4p misDY3 VG4 TT3 VG3
#SR4phighIso SR3lowIso WJets4p VG4p SR4poffM3 SR4plowIso DY3 WJets3 SR3offM3 DY4p SR4ponM3 misDY4 misTT2 TT4p SR3highIso SR3 SR4p misDY4p DY4 SR3onM3 misDY3 VG4 TT3 VG3

regions="misDY4p VG4p DY4p"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="misDY3 VG3 DY3"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="misDY4p VG4p"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="misDY3 VG3"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="misDY3 VG3 misDY4p VG4p misTT2"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

regions="misDY3 VG3 misDY4p VG4p"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions}"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addMisIDSF"
#runNotifier.sh "python run_limit.py $@ ${overwrite} --useRegions ${regions} --addDYSF --addMisIDSF"

