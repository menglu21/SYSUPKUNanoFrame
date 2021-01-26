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
  parser.add_option('--ismc', dest='ismc', help='to apply sf correction or not', default=False, action='store_true')
  parser.add_option('-i', '--in', dest='inputs', help='input directory with files', default=None, type='string')
  parser.add_option('-o', '--out', dest='output', help='output directory with files', default=None, type='string')
  (opt, args) = parser.parse_args()
  print 'year:', opt.year

  print 'inputs:', opt.inputs

  if opt.ismc:
    if opt.year == "2016a":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonIDISOSF2016(),muonScaleRes2016a(),egammaRECOSF2016(),eleIDSF2016(),photonIDSF2016(),jetmetUncertainties2016()], provenance=True)
    if opt.year == "2016b":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonIDISOSF2016(),muonScaleRes2016b(),egammaRECOSF2016(),eleIDSF2016(),photonIDSF2016(),jetmetUncertainties2016()], provenance=True)
    if opt.year == "2017":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonIDISOSF2017(),muonScaleRes2017(),egammaRECOSF2017(),eleIDSF2017(),photonIDSF2017(),jetmetUncertainties2017()], provenance=True)
    if opt.year == "2018":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonIDISOSF2018(),muonScaleRes2018(),egammaRECOSF2018(),eleIDSF2018(),photonIDSF2018(),jetmetUncertainties2018()], provenance=True)
  if not (opt.ismc):
    if opt.year == "2016a":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonScaleRes2016a()], provenance=True)
    if opt.year == "2016b":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonScaleRes2016b()], provenance=True)
    if opt.year == "2017":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonScaleRes2017()], provenance=True)
    if opt.year == "2018":
      p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[muonScaleRes2018()], provenance=True)
  p.run()

if __name__ == "__main__":
    sys.exit(main())
