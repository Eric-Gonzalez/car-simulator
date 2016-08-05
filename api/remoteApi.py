from api.car import Car
from api.simulator import Simulator
import matplotlib.pyplot as plt

simulator = Simulator()
car = Car(simulator)

simulator.connect()

print simulator.start()

print car.set_throttle(0)
print car.set_steering_angle(0)

# Display Fetched Image
plot_image = plt.imshow(car.get_front_camera_image(), origin='lower')
plt.draw()
plt.pause(1)
