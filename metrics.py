# Obtaining metrics
#
#
#
#
#
#
import mobility as mob

AVERAGE_LINK_LIFETIME = float()
AVERAGE_DISTANCE = list()

def medium_distance(nodelist,output_file,MAX_TRANGE,sim_time):
    global AVERAGE_DISTANCE
    n_nodes = len(nodelist)

    for node in xrange(n_nodes):
          consumer = nodelist[str(node)]
          intervals = sorted(consumer.get_positionDict().keys())
          AVERAGE_dist = float()

          for t in intervals:
              if t != '-1' :
                  consumer_pos_at = consumer.get_positionAt(t)
                  n_neighbors = 0.0

                  for neighbor in xrange(n_nodes):
                      if node != neighbor:
                          producer = nodelist[str(neighbor)]
                          producer_pos_at = producer.get_positionAt(t)
                          if producer_pos_at:
                              distance_fromX = mob.euclidean_distance(a=consumer_pos_at,
                              b=producer_pos_at)
                              if distance_fromX <= MAX_TRANGE:
                                #   print "%s - %d is neighbor of %d" % (t,node,neighbor), consumer_pos_at, producer_pos_at,
                                #   print "distance = %.2f" % (distance_fromX)
                                AVERAGE_dist+=distance_fromX
                                n_neighbors+=1 # How many neighbors?

                #   print n_neighbors,"neighbors for node",node
                  AVERAGE_dist = AVERAGE_dist/n_neighbors if n_neighbors else 0.0
          AVERAGE_DISTANCE.append(AVERAGE_dist/float(sim_time))

    AVERAGE = 0.0
    for v in AVERAGE_DISTANCE:
        AVERAGE+=v
    print "%.2f" % (AVERAGE/n_nodes)
    output_file.write("%.2f\n" % (AVERAGE/n_nodes)) # Logging



# TODO: implement
def medin_lifetime():
    pass
