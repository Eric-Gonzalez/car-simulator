import array

import matplotlib.pyplot as plt
from PIL import Image

from api.car import Car
from api.simulator import Simulator
import vrep


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


emptyBuff = bytearray()

simulator = Simulator()
car = Car(simulator)

simulator.connect()

print simulator.start()

print car.set_throttle(0)
print car.set_steering_angle(0)

# while True:
#     print 'Throttle Position: ' + car.get_throttle().__str__()
#     print 'Steering Angle: ' + car.get_steering_angle().__str__()

# simulator.disconnect()

# if clientID != -1:
#     print 'Connected to remote API server'
#
#     # Start Session
#     simulator.start()

# figure = plt.figure(1)
# setRobotSpeed(clientID, 8)
# first = True
# while True:
#     # Fetch Model References
#     image = getVisionSensorImage(clientID)
#     if first:
#         plotimg = plt.imshow(image, origin='lower')
#         first = False
#
#     plotimg.set_data(image)
#
#     plt.draw()
#     plt.pause(0.00000001)
#
#     getRobotSpeed(clientID)

# Display Dialog

# Fetch Sensor Data

# Set Acceleration Speed

# Session Cleanup
#     simulator.stop()
#     simulator.disconnect()
# else:
#     print 'Failed to connect to simulation'
