# Obtaining metrics
#
# Author: mateus Sousa (mateus-n00b)
# Institution: UFBA - Salvador, Brazil
# Date: 30/04/2018
import mobility as mob

# Globas lists
AVERAGE_LINK_LIFETIME = float()
AVERAGE_DISTANCE = list()
AVERAGE_NEIGHBORS = list()
AVERAGE_VELOCITY = list()

def average_distance(nodelist,output_file,MAX_TRANGE,sim_time):
    global AVERAGE_DISTANCE
    global AVERAGE_NEIGHBORS
    global AVERAGE_VELOCITY

    n_nodes = len(nodelist) # number of nodes

    for node in xrange(n_nodes):
          consumer = nodelist[str(node)]
          intervals = sorted(consumer.get_positionDict().keys())
          average_distance_temp = float()
          average_neighbors_temp = float()
          average_node_velocity = float()

          for t in intervals:
              if t != '-1' :
                  consumer_pos_at = consumer.get_positionAt(t)
                  consumer_vel_at = consumer.get_velocityAt(t)
                  n_neighbors = 0.0
                  temp_var = 0.0
                  for neighbor in xrange(n_nodes):
                      if node != neighbor:
                          producer = nodelist[str(neighbor)]
                          producer_pos_at = producer.get_positionAt(t)
                          if producer_pos_at:
                              distance_fromX = mob.euclidean_distance(a=consumer_pos_at,
                              b=producer_pos_at)

                              if distance_fromX <= MAX_TRANGE:
                                # print "at %ss - %d is neighbor of %d" % (t,node,neighbor), consumer_pos_at, producer_pos_at,
                                # print "distance = %.2f" % (distance_fromX)
                                temp_var+=distance_fromX # Wrong?
                                n_neighbors+=1.0 # How many neighbors?

                #   print n_neighbors,"neighbors for node",node
                  average_distance_temp += temp_var/n_neighbors if n_neighbors else 0.0
                  average_neighbors_temp += n_neighbors if n_neighbors else 0.0
                  average_node_velocity += float(consumer_vel_at)

          AVERAGE_DISTANCE.append(average_distance_temp/float(sim_time))
          AVERAGE_NEIGHBORS.append(average_neighbors_temp/float(sim_time))
          AVERAGE_VELOCITY.append(average_node_velocity/float(sim_time))

    # Temp vars
    average_distance_temp = float()
    average_neighbors_temp = float()
    average_node_velocity = float()
    # Files to statistical
    distance_file = open(output_file.name+"_distance_file","w")
    neighbors_file = open(output_file.name+"_neighbors_file","w")
    velocity_file = open(output_file.name+"_velocity_file","w")

    # Saving data for statistical analysis
    for v in xrange(len(AVERAGE_DISTANCE)):
        # print AVERAGE_DISTANCE[v],AVERAGE_NEIGHBORS[v]
        average_distance_temp+=AVERAGE_DISTANCE[v]
        average_neighbors_temp+=AVERAGE_NEIGHBORS[v]
        average_node_velocity+=AVERAGE_VELOCITY[v]
        # Saving Statistics
        distance_file.write("%.3f\n" % AVERAGE_DISTANCE[v])
        neighbors_file.write("%.3f\n" % AVERAGE_NEIGHBORS[v])
        velocity_file.write("%.3f\n" % AVERAGE_VELOCITY[v])

    print "Average distance = %.2f" % (average_distance_temp/n_nodes)
    print "Average neighbors = %.2f" % (average_neighbors_temp/n_nodes)
    print "Average velocity = %.3f" % (average_node_velocity/n_nodes)

    # General Averages
    output_file.write("Average distance = %.3f\n" % (average_distance_temp/n_nodes)) # Logging
    output_file.write("Average neighbors = %.3f\n" % (average_neighbors_temp/n_nodes)) # Logging
    output_file.write("Average velocity = %.3f\n" % (average_node_velocity/n_nodes)) # Logging

    distance_file.close()
    neighbors_file.close()
    velocity_file.close()



# TODO: implement
def average_lifetime():
    pass
