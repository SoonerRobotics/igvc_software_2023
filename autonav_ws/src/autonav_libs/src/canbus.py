#!/usr/bin/env python3


from enum import Enum

class MessageID(Enum):
    ESTOP = 0
    MOBILITY_STOP = 1
    RESET_MOTOR_CONTROLLER = 8
    MOBILITY_START = 9
    WRITE_MOTORS = 10
    WRITE_SAFETY_LIGHTS = 13
    ODOMETRY_FEEDBACK = 14
