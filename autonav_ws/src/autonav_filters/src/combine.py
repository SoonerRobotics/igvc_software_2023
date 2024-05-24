import math
import numpy as np
import particlefilter
import pandas
import time

from autonav_msgs.msg import MotorFeedback, Position, GPSFeedback

motor_message = MotorFeedback()

py_particle_filter = particlefilter.ParticleFilter(111086.2, 81978.2)
py_particle_filter.init_particles()

xs = [4.0, -4.0]
ys = [3.0, -3.0]
thetas = [2.0, -2.0]

motor_message.delta_x = xs[0]
motor_message.delta_y = ys[0]
motor_message.delta_theta = thetas[0]

position_vector = py_particle_filter.feedback(motor_message)
print(position_vector)

motor_message.delta_x = xs[0]
motor_message.delta_y = ys[0]
motor_message.delta_theta = thetas[1]

position_vector = py_particle_filter.feedback(motor_message)
print(position_vector)

motor_message.delta_x = xs[0]
motor_message.delta_y = ys[1]
motor_message.delta_theta = thetas[0]

position_vector = py_particle_filter.feedback(motor_message)
print(position_vector)

motor_message.delta_x = xs[0]
motor_message.delta_y = ys[1]
motor_message.delta_theta = thetas[1]

position_vector = py_particle_filter.feedback(motor_message)
print(position_vector)

motor_message.delta_x = xs[1]
motor_message.delta_y = ys[0]
motor_message.delta_theta = thetas[0]

position_vector = py_particle_filter.feedback(motor_message)
print(position_vector)

motor_message.delta_x = xs[1]
motor_message.delta_y = ys[0]
motor_message.delta_theta = thetas[1]

position_vector = py_particle_filter.feedback(motor_message)
print(position_vector)

motor_message.delta_x = xs[1]
motor_message.delta_y = ys[1]
motor_message.delta_theta = thetas[0]

position_vector = py_particle_filter.feedback(motor_message)
print(position_vector)

motor_message.delta_x = xs[1]
motor_message.delta_y = ys[1]
motor_message.delta_theta = thetas[1]

position_vector = py_particle_filter.feedback(motor_message)
print(position_vector)