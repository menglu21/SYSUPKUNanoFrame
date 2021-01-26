import os
import sys
import optparse
import ROOT
import re

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.sysupku_framework.egammaRECOSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.sysupku_framework.eleIDSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.sysupku_framework.photonIDSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.sysupku_framework.muonScaleResProducer import *
from PhysicsTools.NanoAODTools.postprocessing.sysupku_framework.muonIDISOSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *

### main python file to run ###

def main():

  usage = 'usage: %prog [options]'
  parser = optparse.OptionParser(usage)
  parser.add_option('--year', dest='year', help='which year sample', default='2018', type='string')
  parser.add_option('-m', dest='ismc', help='to apply sf correction or not', default=True, action='store_true')
  parser.add_option('-d', dest='ismc', help='to apply sf correction or not', action='store_false')
  parser.add_option('-i', '--in', dest='inputs', help='input directory with files', default=None, type='string')
  parser.add_option('-o', '--out', dest='output', help='output directory with files', default=None, type='string')
  (opt, args) = parser.parse_args()
  print 'year:', opt.year

  if opt.ismc:
    if opt.year == "2016a":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonIDISOSF2016(),muonScaleRes2016a(),egammaRECOSF2016(),eleIDSF2016(),photonIDSF2016(),jetmetUncertainties2016()], provenance=True)
    if opt.year == "2016b":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonIDISOSF2016(),muonScaleRes2016b(),egammaRECOSF2016(),eleIDSF2016(),photonIDSF2016(),jetmetUncertainties2016()], provenance=True)
    if opt.year == "2017":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonIDISOSF2017(),muonScaleRes2017(),egammaRECOSF2017(),eleIDSF2017(),photonIDSF2017(),jetmetUncertainties2017()], provenance=True)
    if opt.year == "2018":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonIDISOSF2018(),muonScaleRes2018(),egammaRECOSF2018(),eleIDSF2018(),photonIDSF2018(),jetmetUncertainties2018()], provenance=True)


# Sequence for data
  if not (opt.ismc):
    if opt.year == "2016b" or opt.year == "2016c" or opt.year == "2016d":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonScaleRes2016a(),jetmetUncertainties2016RunBCD()], provenance=True)
    if opt.year == "2016e" or opt.year == "2016f":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonScaleRes2016a(),jetmetUncertainties2016RunEF()], provenance=True)
    if opt.year == "2016g" or opt.year == "2016h":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonScaleRes2016b(),jetmetUncertainties2016RunGH()], provenance=True)
    if opt.year == "2017b":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonScaleRes2017(),jetmetUncertainties2017RunB()], provenance=True)
    if opt.year == "2017c":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonScaleRes2017(),jetmetUncertainties2017RunC()], provenance=True)
    if opt.year == "2017d":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonScaleRes2017(),jetmetUncertainties2017RunD()], provenance=True)
    if opt.year == "2017e":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonScaleRes2017(),jetmetUncertainties2017RunE()], provenance=True)
    if opt.year == "2017f":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonScaleRes2017(),jetmetUncertainties2017RunF()], provenance=True)
    if opt.year == "2018a":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonScaleRes2018(),jetmetUncertainties2018RunA()], provenance=True)
    if opt.year == "2018b":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonScaleRes2018(),jetmetUncertainties2018RunB()], provenance=True)
    if opt.year == "2018c":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonScaleRes2018(),jetmetUncertainties2018RunC()], provenance=True)
    if opt.year == "2018d":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonScaleRes2018(),jetmetUncertainties2018RunD()], provenance=True)
  p.run()

if __name__ == "__main__":
    sys.exit(main())
