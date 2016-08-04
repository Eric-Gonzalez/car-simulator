import array

import matplotlib.pyplot as plt
from PIL import Image

import vrep


# throttle ( 0 -> 1 )
# brake (0 -> 1)
# steer (-1 to 1)
# gps (X, Y, Z)
# front camera image
# start Simulation
# stop Simulation

def getRobotSpeed(client):
    return _simSendCommand(client, 'getSpeed')


def setRobotSpeed(client, value):
    return _simSendCommand(client, 'setSpeed', inputFloats=[value])


def getVisionSensorImage(clientID):
    res, visionSensor = _simGetObject(clientID, 'front_camera')
    ret, res, data = vrep.simxGetVisionSensorImage(clientID, visionSensor, 0,
                                                   vrep.simx_opmode_oneshot_wait)
    imageByteArray = array.array('b', data)
    image = Image.frombuffer("RGB", res, imageByteArray, "raw", "RGB", 0, 1)
    return image


def _simGetObject(clientID, objectName):
    return vrep.simxGetObjectHandle(clientID, objectName, vrep.simx_opmode_oneshot_wait)


def _simSendCommand(clientID, functionName, inputInts=[], inputFloats=[], inputStrings=[],
                    byteBuffer=bytearray()):
    return vrep.simxCallScriptFunction(clientID, 'remoteApiCommandServer',
                                       vrep.sim_scripttype_childscript, functionName, inputInts,
                                       inputFloats, inputStrings, byteBuffer,
                                       vrep.simx_opmode_oneshot_wait)


vrep.simxFinish(-1)  # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, -500000, 5)

emptyBuff = bytearray()

if clientID != -1:
    print 'Connected to remote API server'

    # Start Session
    vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot_wait)

    figure = plt.figure(1)

    setRobotSpeed(clientID, 8)

    first = True
    while True:
        # Fetch Model References
        image = getVisionSensorImage(clientID)
        if first:
            plotimg = plt.imshow(image, origin='lower')
            first = False

        plotimg.set_data(image)

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
