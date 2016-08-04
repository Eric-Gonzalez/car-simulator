class Car:
    def __init__(self, simulator):
        self.simulator = simulator

    def set_throttle(self, value):
        """
        :param value: Between 0 and 1
        """
        return self.simulator.exec_script('setThrottleRemote', inputFloats=[value])

    def get_throttle(self):
        """
        :return: The current throttle position
        """
        return self.simulator.exec_script('getThrottleRemote')

    def set_brake(self, value):
        pass

    def get_brake(self):
        pass

    def set_steering(self, value):
        """
        :param value: Between -1 and 1
        """
        pass

    def get_sterring(self):
        pass

    def get_front_camera_image(self):
        pass

    def get_gps_position(self):
        pass
