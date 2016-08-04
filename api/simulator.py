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
        return vrep.simxStartSimulation(self.clientID, vrep.simx_opmode_oneshot_wait)

    def stop(self):
        vrep.simxStopSimulation(self.clientID, vrep.simx_opmode_oneshot_wait)

    def exec_script(self, functionName, inputInts=[], inputFloats=[], inputStrings=[],
                    byteBuffer=bytearray()):
        return vrep.simxCallScriptFunction(self.clientID, 'car',
                                           vrep.sim_scripttype_childscript, functionName, inputInts,
                                           inputFloats, inputStrings, byteBuffer,
                                           vrep.simx_opmode_oneshot_wait)
