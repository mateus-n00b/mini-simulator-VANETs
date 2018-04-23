#!/usr/bin/env python
# Mini-Simulator based on ns-2 mobility traces
#
# Author:  Mateus Sousa (mateus-n00b)
# Date: 12/04/2018 - Salvador, Brazil
#
# TODO: Develop a lot of things
#       -  simulate the mobility
#       - create/Destroy edges according to the distance among the nodes
#       - use the networkx to models the network
#       - create main function
#
#
import networkx as nx
import mobility as mob
import metrics
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t","--trace",dest="trace",type="str",default=None,
                 help="ns-2 mobility trace file")
parser.add_option("-o","--output",dest="results",type="str",default="statistics.dat",
                help="ns-2 mobility trace file",nargs=1)

opt, args = parser.parse_args()

# Global vars
MAX_TRANGE = 300.0 # maximum transmission range
try:
    STATISTICS_FILE = open(opt.results,"w")
    print "The output will be saved at => {}".format(STATISTICS_FILE.name)
except Exception as error:
    print error
    exit(-1)

# mob_files = ['/tmp/mobility25','/tmp/mobility50','/tmp/mobility75','/tmp/mobility100',
# '/tmp/highway25','/tmp/highway50','/tmp/highway75','/tmp/highway100']

if opt.trace:
    # for f in mob_files:
    nodelist,sim_time = mob.build_topo(trace=opt.trace)
    print "simulation time = {0}".format(sim_time)
    # print nodelist['1'].get_velocityAt('149.00') #
    # print nodelist['0'].get_positionAt('0.00') #
    # n_nodes = len(nodelist)
    STATISTICS_FILE.write("{} ".format(opt.trace))
    metrics.medium_distance(nodelist=nodelist,output_file=STATISTICS_FILE,
    MAX_TRANGE=MAX_TRANGE,sim_time=sim_time)
    STATISTICS_FILE.close() # Close statistics file
else:
    print "[-] Invalid entry! Try -h|--help for help."
    exit(-1)
