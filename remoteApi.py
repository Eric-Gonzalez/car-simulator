import io

import array
import matplotlib.pyplot as plt
from PIL import Image
import vrep


def getRobotSpeed(client):
    vrep.simxCallScriptFunction(client, 'remoteApiCommandServer', vrep.sim_scripttype_childscript,
                                'getSpeed', [], [], [], emptyBuff, vrep.simx_opmode_oneshot_wait)


def setRobotSpeed(client, value):
    print vrep.simxCallScriptFunction(client, 'remoteApiCommandServer',
                                      vrep.sim_scripttype_childscript,
                                      'setSpeed', [], [value], [], emptyBuff,
                                      vrep.simx_opmode_oneshot_wait)


vrep.simxFinish(-1)  # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, -500000, 5)

emptyBuff = bytearray()

if clientID != -1:
    print 'Connected to remote API server'

    # Start Session
    vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot_wait)

    figure = plt.figure(1)

    setRobotSpeed(clientID, 10)

    first = True
    while True:
        # Fetch Model References
        res, visionSensor = vrep.simxGetObjectHandle(clientID, 'vision',
                                                     vrep.simx_opmode_oneshot_wait)
        ret, res, data = vrep.simxGetVisionSensorImage(clientID, visionSensor, 0,
                                                       vrep.simx_opmode_oneshot_wait)

        image_byte_array = array.array('b', data)
        im = Image.frombuffer("RGB", res, image_byte_array, "raw", "RGB", 0, 1)

        if first:
            plotimg = plt.imshow(im, origin='lower')
            first = False

        plotimg.set_data(im)

        plt.draw()
        plt.pause(0.00000001)

        getRobotSpeed(clientID)

    # Display Dialog

    # Fetch Sensor Data

    # Set Acceleration Speed

    # Session Cleanup
    vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot_wait)
    vrep.simxFinish(clientID)
else:
    print 'Failed to connect to simulation'
