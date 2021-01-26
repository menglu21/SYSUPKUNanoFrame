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
### the command above run the sample locally, the output file will be at $CMSSW_BASE/..

# About the JEC/JER correction
The JECR part is using the existing module under the ``cms-nanoAOD/nanoAOD-tools``, but some modification is done and stored in ``https://github.com/menglu21/nanoAOD-tools``, the module is ``nanoAOD-tools/python/postprocessing/modules/jme/jetmetUncertainties.py``

## JEC 
The official twiki is ``https://twiki.cern.ch/twiki/bin/view/CMS/JECDataMC``
``files used for MC``: they are stored in ``nanoAOD-tools/data/jme/``
``2018``: Summer19UL18_V5_MC.tgz
``2017``: Summer19UL17_V5_MC.tgz
``2016``: Summer16_07Aug2017_V11_MC.tgz


