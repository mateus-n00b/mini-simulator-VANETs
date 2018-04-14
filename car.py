class Car(object):
    def __init__(self,n_id):
        '''Creates a new node and set its mobility informations'''
        self.n_id = n_id
        # Dict format: {time:'values'}
        self.velocity_at = {'0.0':'0.0'} # time:velocity
        self.position_at = {
        "0.0":
        {"X_":"0.0",
        "Y_":"0.0"}
        }


    def get_id(self):
        return self.n_id

    def get_positionAt(self,t):
        return (float(self.position_at[t]['X_']),
        float(self.position_at[t]['Y_'])) if self.position_at.has_key(t) else None

    def get_positionDict(self):
        return self.position_at

    def setPositionAt(self,t,XY_coord,position):
        try:
            self.position_at[t][XY_coord] = position
        except:
            self.position_at[t] = {"X_":'0.0',"Y_":'0.0'}
            self.position_at[t][XY_coord] = position

    def get_velocityAt(self,t):
        return self.velocity_at[t] if self.velocity_at.has_key(t) else None

    def get_velocityDict(self):
        return self.velocity_at

    def setVelocityAt(self,t, velocity):
        self.velocity_at[t] = velocity
