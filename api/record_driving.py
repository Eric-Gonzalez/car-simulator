import signal
import sys

from api.car import Car
from api.recorder import Recorder
from api.simulator import Simulator


def signal_handler(signal, frame):
    recorder.stop()
    print 'Recording Saved to ' + recorder.file_name
    sys.exit(0)


simulator = Simulator()
car = Car(simulator)
recorder = Recorder(car)

simulator.connect()
simulator.start()

recorder.start()

print 'Now Recording Driving...'
print 'Press Ctrl-C to Stop Recording'

signal.signal(signal.SIGINT, signal_handler)
signal.pause()
