import math
import numpy as np
import particlefilter
import pandas
import time

from autonav_msgs.msg import MotorFeedback, Position, GPSFeedback

gps_message = GPSFeedback()

gps_message = GPSFeedback()
gps_message.latitude = 42.6681254
gps_message.longitude = -83.2188876
gps_message.altitude = 234.891
gps_message.gps_fix = 4
gps_message.is_locked = True
gps_message.satellites = 16

py_particle_filter = particlefilter.ParticleFilter(111086.2, 81978.2)
py_particle_filter.init_particles()

gps_vector = py_particle_filter.gps(gps_message)

print(gps_vector)

# gps_message_3 = GPSFeedback()
# gps_message_3.latitude = 42.67
# gps_message_3.longitude = -83.2188876
# gps_message_3.altitude = 234.891
# gps_message_3.gps_fix = 4
# gps_message_3.is_locked = True
# gps_message_3.satellites = 16

# gps_vector = py_particle_filter.gps(gps_message_3)
# print(gps_vector)

gps_message_2 = GPSFeedback()
gps_message_2.latitude = 42.66
gps_message_2.longitude = -83.2188876
gps_message_2.altitude = 234.891
gps_message_2.gps_fix = 4
gps_message_2.is_locked = True
gps_message_2.satellites = 16

motor_message = MotorFeedback()

for i in range(10000):
    gps_vector = py_particle_filter.gps(gps_message_2)
    py_particle_filter.feedback(motor_message)

print(gps_vector)