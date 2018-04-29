#!/usr/bin/env python
# Script for my master's degree thesis
#
# Author: Mateus Sousa (mateus-n00b), UFBA-Brazil (2018)
#
# License: GPLv3+
# TODO: Test the limits of Class car (i.e., how many objects it supports?)
import csv,sys
import car # Class car creates a representative object for every node in the tracefile
from optparse import OptionParser

add_ids = open("used_nodes.dat","a+")
file_1 = open("used_nodes.dat","r")
used_ids = str(file_1.read())
file_1.close()

nodecontainer = dict() # Store the nodes created

def parser(tracefile,max_vehicles): # Read the tracefile and fills nodecontainer with vehicles objects
    global nodecontainer # Structure: {'vehicle_id':object}
    node_id = int() # Var used to attribute a new id for each vehicle

    with open(tracefile, 'rb') as csvfile:
        fp =  csv.DictReader(csvfile)
        for row in fp:
            # if row['vehicle_type'] == 'Vehicle': # Just cars
            if row['vehicle_id'] not in used_ids:
                if not nodecontainer.has_key(row['vehicle_id']) and (node_id < max_vehicles): # how many nodes? Can I add one more?
                    m_car = car.Car(n_id=node_id)
                    nodecontainer[row['vehicle_id']] = m_car
                    node_id+=1 # Increments node_id for another Vehicle
                    add_ids.write(row['vehicle_id']+'\n')

                time = row['timestep_time']
                posX = row['vehicle_x']
                posY = row['vehicle_y']
                speed = row['vehicle_speed']

                try:
                    m_car = nodecontainer[row['vehicle_id']] # temporary object
                    m_car.setPositionAt(time,'X_',posX)
                    m_car.setPositionAt(time,'Y_',posY)
                    m_car.setVelocityAt(time,speed)
                except:
                    pass
    add_ids.close()

# NOTE: For debug purposes
# parser('vanet-trace-creteil-20130924-0700-0900.csv',2)
# car = nodecontainer['VehicleFlowEastToWest_0.0']
# print len(car.get_positionDict())

def createTracefile(output): # Read the mobility infos in nodecontainer and creates a ns2 mobility trace
    '''
      Valid trace files use the following ns2 statements:
      $node set X_ x1
      $node set Y_ y1
      $node set Z_ z1
      $ns at $time $node setdest x2 y2 speed
      $ns at $time $node set X_ x1
      $ns at $time $node set Y_ Y1
      $ns at $time $node set Z_ Z1
    '''
    with open(output,'w') as tracefile:
        tracefile.write("#number cars:{0}\n".format(len(nodecontainer)))

        for nodes in nodecontainer.values():
            node_id = nodes.get_id()
            positionDict = nodes.get_positionDict()
            velocityDict = nodes.get_velocityDict()

            for intervals in positionDict.keys():
                speed = velocityDict[intervals]
                posX = positionDict[intervals]['X_']
                posY = positionDict[intervals]['Y_']
                to_str = ""

                if intervals == '0.00' and speed == '0.00':
                    to_str = "$node_({0}) set X_ {1} ;#ref\n\
$node_({0}) set Y_ {2} ;#ref\n\
$ns_ at {3} \"$node_({0}) setdest {1} {2} {4}\"\n\
                              ".format(node_id,posX,posY,intervals,speed)
                else:
                    to_str = "$ns_ at {1} \"$node_({0}) setdest {2} {3} {4}\"\n".format(node_id,intervals,
                    posX,posY,speed)

                tracefile.write(to_str) # Writes in the tracefile
    tracefile.close()

def main():
    parser_ = OptionParser()
    parser_.add_option("-t","--trace",dest="tracefile",type="str",default=None,
                help="input trace file")
    parser_.add_option('-o','--output',dest="output",type="str",default="mobility_trace.tcl",
                    help="output file (ns-2 tracefile)")
    parser_.add_option("-n","--nodes",dest="n_nodes",type="int",default=0,
                    help="number number of nodes")
    opt,args = parser_.parse_args()

    if not opt.tracefile:
        print "[-] Invalid entry! Try {0} -h".format(sys.argv[0])
        exit(-1)

    print "*** Saving output in \"{0}\"".format(opt.output)
    parser(opt.tracefile,opt.n_nodes)
    createTracefile(output=opt.output)

if __name__ == '__main__':
    main()
