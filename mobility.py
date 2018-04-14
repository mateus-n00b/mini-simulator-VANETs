import tracer_parser as tp
import car

trace_file = None

def build_topo(trace):
    parsed_tracer = tp.parser(trace)
    parsed_tracer = open(parsed_tracer,"r")

    try:
        number_cars = int(str(parsed_tracer.readline()).split("#number cars:")[1].split("avg")[0])
        # Dict structure == {ID:node_object}
        cars_in_sim = dict()

        for rows in parsed_tracer.readlines():
            rows = rows.rstrip()
            if not rows: break

            n_id = rows.split("node=")[1].split(")")[0]

            if not cars_in_sim.has_key(n_id):
                carX = car.Car(n_id) # Creates a new car/node
                cars_in_sim[n_id] = carX

            carX = cars_in_sim[n_id] # Temporary object

            if "set " in rows:
                XY_coord = rows.split(" ")[2]
                position =  rows.split(" ")[3]

                carX.setPositionAt('-1',XY_coord,position) # -1 because we're just placing the nodes before simulation starts

            elif "setdest" in rows:
                time = rows.split(" ")[2]
                X = rows.split(" ")[5]
                Y = rows.split(" ")[6]
                velocity = rows.split(" ")[7]
                # cars_mobility_infos[n_id]['time'] = "0.0"
                carX.setPositionAt(time,'X_',X)
                carX.setPositionAt(time,'Y_',Y)
                # print n_id,time,velocity
                carX.setVelocityAt(time,velocity)

        return cars_in_sim
    except Exception as error:
            print "[-] Error!\n-> {0}".format(error)
            exit(-1)

def euclidian_distance(a,b): # A = (px,qx), B = (qx,qy)
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

# NOTE: For debuging purposes
# trace_file = "highway25"
# arr = build_topo(trace_file)
# print arr['1'].get_velocityAt('149.00')
