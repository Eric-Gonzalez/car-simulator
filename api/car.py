class Car:
    def __init__(self, simulator):
        self.simulator = simulator

    #  TODO Map Value from -1 to 1
    def set_throttle(self, value):
        """
        :param value: Between -1 and 1
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

    def set_steering_angle(self, value):
        """
        :param value: Between -1 and 1
        """
        return self.simulator.exec_script('setSteeringAngleRemote', inputFloats=[value])

    def get_steering_angle(self):
        return self.simulator.exec_script('getSteeringAngleRemote')

    def get_front_camera_image(self):
        pass

    def get_gps_position(self):
        pass
