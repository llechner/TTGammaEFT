submitCondor.py $@ --dpm --maxRetries 10 --resubmitFailedJobs --execFile submit_QCDHistos.sh --output /afs/cern.ch/work/l/llechner/public/condor_logs/qcd16/ --queue tomorrow allQCDHistos.sh
