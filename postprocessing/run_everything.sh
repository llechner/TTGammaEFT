submitCondor.py $1 --dpm --execFile submit_on_lxplus.sh --output /afs/cern.ch/user/l/llechner/public/condor_logs/mc16/   --queue testmatch nanoPostProcessing_Summer16_private.sh
submitCondor.py $1 --dpm --execFile submit_on_lxplus.sh --output /afs/cern.ch/user/l/llechner/public/condor_logs/data16/ --queue testmatch nanoPostProcessing_Run2016_14Dec2018.sh

submitCondor.py $1 --dpm --execFile submit_on_lxplus.sh --output /afs/cern.ch/user/l/llechner/public/condor_logs/mc17/   --queue testmatch nanoPostProcessing_Fall17_private.sh
submitCondor.py $1 --dpm --execFile submit_on_lxplus.sh --output /afs/cern.ch/user/l/llechner/public/condor_logs/data17/ --queue testmatch nanoPostProcessing_Run2017_14Dec2018.sh

submitCondor.py $1 --dpm --execFile submit_on_lxplus.sh --output /afs/cern.ch/user/l/llechner/public/condor_logs/mc18/   --queue testmatch nanoPostProcessing_Autumn18_private.sh
submitCondor.py $1 --dpm --execFile submit_on_lxplus.sh --output /afs/cern.ch/user/l/llechner/public/condor_logs/data18/ --queue testmatch nanoPostProcessing_Run2018_14Dec2018.sh

submitCondor.py $1 --dpm --execFile submit_on_lxplus.sh --output /afs/cern.ch/user/l/llechner/public/condor_logs/mc16s/   --queue testmatch nanoPostProcessing_Summer16_private_semilep.sh
submitCondor.py $1 --dpm --execFile submit_on_lxplus.sh --output /afs/cern.ch/user/l/llechner/public/condor_logs/data16s/ --queue testmatch nanoPostProcessing_Run2016_14Dec2018_semilep.sh

submitCondor.py $1 --dpm --execFile submit_on_lxplus.sh --output /afs/cern.ch/user/l/llechner/public/condor_logs/mc17s/   --queue testmatch nanoPostProcessing_Fall17_private_semilep.sh
submitCondor.py $1 --dpm --execFile submit_on_lxplus.sh --output /afs/cern.ch/user/l/llechner/public/condor_logs/data17s/ --queue testmatch nanoPostProcessing_Run2017_14Dec2018_semilep.sh

submitCondor.py $1 --dpm --execFile submit_on_lxplus.sh --output /afs/cern.ch/user/l/llechner/public/condor_logs/mc18s/   --queue testmatch nanoPostProcessing_Autumn18_private_semilep.sh
submitCondor.py $1 --dpm --execFile submit_on_lxplus.sh --output /afs/cern.ch/user/l/llechner/public/condor_logs/data18s/ --queue testmatch nanoPostProcessing_Run2018_14Dec2018_semilep.sh

#submitCondor.py $1 --dpm --execFile submit_on_lxplus.sh --output /afs/cern.ch/user/l/llechner/public/condor_logs/pf17/    --queue nextweek nanoPostProcessing_preFiring2017.sh
