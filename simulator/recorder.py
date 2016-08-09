import csv
import datetime
import errno
import os
from threading import Timer

from PIL import Image


def _create_directory(directory_name):
    try:
        os.makedirs(directory_name)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(directory_name):
            pass
        else:
            raise


class Recorder:
    def __init__(self, car, interval_in_seconds=.5, file_name="driving.csv",
                 directory_name="frames"):
        self._timer = None
        self.is_running = False
        self.interval = interval_in_seconds
        self.car = car
        self.file_name = file_name
        self.file = open(self.file_name, 'a')
        self.directory_name = directory_name
        _create_directory(directory_name)

    def __call__(self):
        self.is_running = False
        self.start()
        self.record_snapshot()

    def record_snapshot(self):
        # Write Image frame to disk
        current_time = datetime.datetime.now().__str__()
        image_file_name = os.path.join(self.directory_name, current_time + '.png')
        with open(image_file_name, 'wb') as file:
            self.car.get_front_camera_image().transpose(Image.FLIP_TOP_BOTTOM).save(file, "PNG")
        csv_writer = csv.writer(self.file)
        csv_writer.writerow(
            [current_time, self.car.get_steering_angle(), self.car.get_throttle(), image_file_name])

    def start(self):
        self._timer = Timer(self.interval, self)
        self._timer.start()
        self.is_running = True

    def stop(self):
        if self._timer:
            self._timer.cancel()
        self.is_running = False
