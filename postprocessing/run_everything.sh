submitCondor.py $1 --execFile submit_on_lxplus.sh --queue workday nanoPostProcessing_Summer16_private.sh
submitCondor.py $1 --execFile submit_on_lxplus.sh --queue workday nanoPostProcessing_Run2016_14Dec2018.sh

submitCondor.py $1 --execFile submit_on_lxplus.sh --queue workday nanoPostProcessing_Fall17_private.sh
submitCondor.py $1 --execFile submit_on_lxplus.sh --queue workday nanoPostProcessing_Run2017_14Dec2018.sh

submitCondor.py $1 --execFile submit_on_lxplus.sh --queue workday nanoPostProcessing_Autumn18_private.sh
submitCondor.py $1 --execFile submit_on_lxplus.sh --queue workday nanoPostProcessing_Run2018_14Dec2018.sh

submitCondor.py $1 --execFile submit_on_lxplus.sh --queue tomorrow nanoPostProcessing_Summer16_private_semilep.sh
submitCondor.py $1 --execFile submit_on_lxplus.sh --queue tomorrow nanoPostProcessing_Run2016_14Dec2018_semilep.sh

submitCondor.py $1 --execFile submit_on_lxplus.sh --queue tomorrow nanoPostProcessing_Fall17_private_semilep.sh
submitCondor.py $1 --execFile submit_on_lxplus.sh --queue tomorrow nanoPostProcessing_Run2017_14Dec2018_semilep.sh

submitCondor.py $1 --execFile submit_on_lxplus.sh --queue tomorrow nanoPostProcessing_Autumn18_private_semilep.sh
submitCondor.py $1 --execFile submit_on_lxplus.sh --queue tomorrow nanoPostProcessing_Run2018_14Dec2018_semilep.sh

submitCondor.py $1 --execFile submit_on_lxplus.sh --queue nextweek nanoPostProcessing_preFiring2017.sh
