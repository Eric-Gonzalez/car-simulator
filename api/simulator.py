import vrep


class Simulator:
    def __init__(self):
        self.clientID = -1

    def connect(self):
        self.disconnect()
        self.clientID = vrep.simxStart('127.0.0.1', 19997, True, True, -500000, 5)
        return self.clientID

    def disconnect(self):
        vrep.simxFinish(-1)
        vrep.simxStopSimulation(self.clientID, vrep.simx_opmode_oneshot_wait)

    def start(self):
        vrep.simxStartSimulation(self.clientID, vrep.simx_opmode_oneshot_wait)

    def stop(self):
        vrep.simxStopSimulation(self.clientID, vrep.simx_opmode_oneshot_wait)
