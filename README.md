# SYSUPKUNanoFrame

## set-up, currently use release CMSSW_10_2_22

```cmsrel CMSSW_10_2_22

cd CMSSW_10_2_22/src``

cmsenv

git cms-init

git clone https://github.com/menglu21/nanoAOD-tools.git PhysicsTools/NanoAODTools

scram b

voms-proxy-init -voms cms # necessary for crab submission
```
## then this framework, 

``data_SF``: root file for ScaleFactor, currently only for electron recostruction ScaleFactor (for all three years)

``sysupku_framework``: modules to extend the official NanoAOD output for later use, currently only ScaleFactor and SF error for Electron reconstruction

``sysupku_nano``: executables

```
cd ~/

git clone https://github.com/menglu21/SYSUPKUNanoFrame.git

cd SYSUPKUNanoFrame

cp -rf sysupku_framework data_SF $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing

cp -rf sysupku_nano $CMSSW_BASE/src/PhysicsTools/NanoAODTools

cd $CMSSW_BASE/src/

scram b
```
## before run the executable, download a NanoAOD root file in $CMSSW_BASE/..
```
cd $CMSSW_BASE/src/PhysicsTools/NanoAODTools/sysupku_nano

sh run.sh -o LOCAL
```
## this command run the sample locally, the output file will be at $CMSSW_BASE/..
