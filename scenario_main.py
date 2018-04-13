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

arr = mob.build_topo(trace='highway25')
print arr['1'].get_velocityAt('149.00')
