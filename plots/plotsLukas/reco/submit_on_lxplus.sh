#!/bin/bash

#
# Example of usage:
# submitCondor.py --execFile submit_on_lxplus.sh --queue nextweek nanoPostProcessing_Summer16_private.sh
# submitCondor.py --execFile THISFILE (setup for condor environment) --queue NAMEofCONDORQUEUE fileWithCommands.sh
#

export USER=$(whoami)
export HOME=/afs/cern.ch/user/l/llechner
initial="$(echo $USER | head -c 1)"
export SCRAM_ARCH=slc6_amd64_gcc630

echo "---------------------"
echo "Grid certificate 1"
voms-proxy-info --all
echo "---------------------"
echo "Current dir: `pwd`"
ls -l
echo "---------------------"

echo "---------------------"
echo "Changing dir to IWD:"
echo $IWD
cd $IWD
eval `scramv1 runtime -sh`
echo "---------------------"

echo "---------------------"
echo "Current dir: `pwd`"
ls -l
echo "---------------------"

echo "---------------------"
echo "Using hephy token: /afs/cern.ch/user/${initial}/${USER}/private/kerberos/krb5_token_hephy.at"
export KRB5CCNAME=/afs/cern.ch/user/${initial}/${USER}/private/kerberos/krb5_token_hephy.at
aklog -d hephy.at
echo "---------------------"

echo "Executing:"
echo ${@:2}
echo "---------------------"

${@:2}

