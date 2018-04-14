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
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t","--trace",dest="trace",type="str",default=None,
                help="ns-2 mobility trace file")
parser.add_option("-o","--output",dest="results",type="str",default="statistics.dat",
                help="ns-2 mobility trace file")

opt, args = parser.parse_args()

# Global vars
MAX_TRANGE = float() # maximum transmission range
MEAN_LINK_LIFETIME = float()
MEAN_DISTANCE = float()
try:
    STATISTICS_FILE = open(opt.results,"w")
    print "The output will be saved in file => {}".format(STATISTICS_FILE.name)
except Exception as error:
    print error
    exit(-1)

if opt.trace:
    nodelist = mob.build_topo(trace=opt.trace)
    # print nodelist['1'].get_velocityAt('149.00') #
    print nodelist['0'].get_positionAt('0.00') #
    n_nodes = len(nodelist)

    # posDict = nodelist['0'].get_positionDict()

    # for node in xrange(n_nodes):
    #     consumer = nodelist[node]
    #     for neighbor in xrange(n_nodes):
    #         if node != neighbor:
    #             producer = nodelist[neighbor]
    #             distance_fromX = mob.euclidian_distance(a=(consumer['X_'],consumer['']))
    #             if

else:
    print "[-] Invalid entry! Try -h|--help for help."
    exit(-1)
