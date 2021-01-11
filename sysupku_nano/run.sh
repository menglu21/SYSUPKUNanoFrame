#!/bin/bash

#parse input arguments
YEAR=2018
while getopts "o:y:" opt; do
  case "$opt" in
	o) WHAT=$OPTARG
	  ;;
	y) YEAR=$OPTARG
	  ;;
  esac
done

#check an operation has been given
if [ -z "${WHAT}" ]; then
  echo "run.sh -o <LOCAL/SUBMIT> [ -y 2016/2017/2018 ] ";
  echo " LOCAL		- run locally";
  echo " SUBMIT 	- submit jobs";
  exit 1;
fi

case ${WHAT} in

  LOCAL)
	python $CMSSW_BASE/src/PhysicsTools/NanoAODTools/sysupku_nano/run.py --ismc True -i /afs/cern.ch/user/z/zhyuan/work/LuMeng_workspace/Nano_dev/DYJetsToLL_M50.root --year ${YEAR} -o /afs/cern.ch/user/z/zhyuan/work/LuMeng_workspace/Nano_dev/;
	;;

#  SUBMIT)
	
esac
