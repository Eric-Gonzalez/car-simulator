from api.car import Car
from api.simulator import Simulator
import matplotlib.pyplot as plt
import time

simulator = Simulator()
car = Car(simulator)

simulator.connect()

simulator.start()

print car.set_throttle(.1)
print car.get_throttle()
print car.set_steering_angle(.66)

duration = time.time() + 10
plot_image = plt.imshow(car.get_front_camera_image(), origin='lower')
while time.time() < duration:
    # Display Fetched Image
    plot_image.set_data(car.get_front_camera_image())
    plt.draw()
    plt.pause(.0001)
