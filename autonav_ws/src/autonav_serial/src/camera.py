#!/usr/bin/env python3

import rclpy
import time
import threading
import cv2
from enum import IntEnum

from autonav_libs import Device, AutoNode, DeviceStateEnum, SystemStateEnum as SystemState
from sensor_msgs.msg._image import Image

from cv_bridge import CvBridge

bridge = CvBridge()

class Register(IntEnum):
    REFRESH_RATE = 0


class CameraNode(AutoNode):
    def __init__(self):
        super().__init__(Device.CAMERA_TRANSLATOR, "autonav_serial_camera")
        self.config.writeInt(Register.REFRESH_RATE, 1)

    def setup(self):
        self.m_cameraPublisher = self.create_publisher(
            Image, "/autonav/camera/raw", 20)
        self.m_cameraThread = threading.Thread(target=self.camera_read)
        self.m_cameraThread.start()

    def shutdown(self):
        self.m_cameraThread.join()

    def camera_read(self):
        if self.getSystemState() != SystemState.SHUTDOWN:
            return

        # Check if /dev/video0 exists
        capture = None
        try:
            capture = cv2.VideoCapture(0)
            if capture is None or not capture.isOpened():
                raise Exception("Could not open video device")

            self.setDeviceState(DeviceStateEnum.READY)
        except:
            self.setDeviceState(DeviceStateEnum.STANDBY)
            time.sleep(3.0)
            self.camera_read()
            return
            

        while rclpy.ok():
            if self.getDeviceState() != DeviceStateEnum.OPERATING:
                continue

            try:
                ret, frame = capture.read()
            except:
                if capture is not None:
                    capture.release()
                    capture = None

                self.setDeviceState(DeviceStateEnum.STANDBY)
                time.sleep(1.0)
                self.camera_read()
                return

            if not ret or frame is None:
                continue

            self.m_cameraPublisher.publish(bridge.cv2_to_imgmsg(frame))
            time.sleep(1.0 / self.config.readInt(Register.REFRESH_RATE))


def main():
    rclpy.init()
    rclpy.spin(CameraNode())
    rclpy.shutdown()


if __name__ == "__main__":
    main()