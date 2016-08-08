import time

from api.car import Car
from api.recorder import Recorder
from api.simulator import Simulator

simulator = Simulator()
car = Car(simulator)

simulator.connect()

simulator.start()

print car.set_throttle(.3223)
print car.get_throttle()
print car.set_steering_angle(.1)
print car.get_steering_angle()

duration = time.time() + 10
recorder = Recorder(car)
try:
    recorder.start()
    time.sleep(5)
finally:
    recorder.stop()
    simulator.stop()
