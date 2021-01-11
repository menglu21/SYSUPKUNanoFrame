import os
import sys
import optparse
import ROOT
import re

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.sysupku_framework.eleSFProducer import *

### main python file to run ###

def main():

  usage = 'usage: %prog [options]'
  parser = optparse.OptionParser(usage)
  parser.add_option('--year', dest='year', help='which year sample', default='2016', type='string')
  parser.add_option('--ismc', dest='ismc', help='to apply sf correction or not', default=False, action='store_true')
  parser.add_option('-i', '--in', dest='inputs', help='input directory with files', default=None, type='string')
  parser.add_option('-o', '--out', dest='output', help='output directory with files', default=None, type='string')
  (opt, args) = parser.parse_args()
  print 'year:', opt.year

  print 'inputs:', opt.inputs

  if opt.ismc:
	if opt.year == "2016":
	  p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[eleSF2016()], provenance=True)
	if opt.year == "2017":
	  p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[eleSF2017()], provenance=True)
	if opt.year == "2018":
	  p = PostProcessor(opt.output, [opt.inputs], cut="", branchsel=None, modules=[eleSF2018()], provenance=True)
  p.run()

if __name__ == "__main__":
    sys.exit(main())
