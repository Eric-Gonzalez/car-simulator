from api.car import Car
from api.simulator import Simulator

simulator = Simulator()
car = Car(simulator)

simulator.connect()

print simulator.start()

print car.set_throttle(0)
print car.set_steering_angle(0)