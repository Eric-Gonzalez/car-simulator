import array

from PIL import Image

from api import vrep


class Simulator:
    SCRIPT_NAME = 'car'
    OP_WAIT = vrep.simx_opmode_oneshot_wait

    def __init__(self):
        self.clientID = -1

    def connect(self):
        self.disconnect()
        self.clientID = vrep.simxStart('127.0.0.1', 19997, True, True, -500000, 5)
        return self.clientID

    def disconnect(self):
        vrep.simxFinish(-1)
        vrep.simxStopSimulation(self.clientID, self.OP_WAIT)

    def start(self):
        return vrep.simxStartSimulation(self.clientID, self.OP_WAIT)

    def stop(self):
        vrep.simxStopSimulation(self.clientID, self.OP_WAIT)

    def exec_script(self, function_name, input_ints=None, input_floats=None, input_strings=None,
                    byte_buffer=bytearray()):
        if input_strings is None:
            input_strings = []
        if input_floats is None:
            input_floats = []
        if input_ints is None:
            input_ints = []

        return vrep.simxCallScriptFunction(self.clientID, self.SCRIPT_NAME,
                                           vrep.sim_scripttype_childscript, function_name,
                                           input_ints,
                                           input_floats, input_strings, byte_buffer,
                                           self.OP_WAIT)

    def get_object_handle(self, object_name):
        return vrep.simxGetObjectHandle(self.clientID, object_name, self.OP_WAIT)

    def get_sensor_image(self, sensor_name):
        return_code, sensor = self.get_object_handle(sensor_name)
        return_code, resolution, data = vrep.simxGetVisionSensorImage(self.clientID, sensor, 0,
                                                                      self.OP_WAIT)
        image_byte_array = array.array('b', data)
        return Image.frombuffer("RGB", resolution, image_byte_array, "raw", "RGB", 0, 1)
