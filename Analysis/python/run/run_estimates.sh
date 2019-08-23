submitCondor.py $@ --dpm --maxRetries 10 --resubmitFailedJobs --execFile submit_estimates.sh --output /afs/cern.ch/work/l/llechner/public/condor_logs/est16/ --queue tomorrow allEstimates.sh
