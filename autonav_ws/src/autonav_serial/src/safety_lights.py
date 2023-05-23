#!/usr/bin/env python3

from ctypes import Structure, c_bool, c_uint8
from scr_core.state import DeviceStateEnum
from autonav_msgs.msg import SafetyLights
from scr_msgs.msg import SystemState
from scr_core.node import Node
import threading
import serial
import rclpy
import json


class SafetyLightsPacket(Structure):
    _fields_ = [
        ("autonomous", c_bool, 1),
        ("eco", c_uint8, 1),
        ("mode", c_uint8, 6),
        ("brightness", c_uint8, 8),
        ("red", c_uint8, 8),
        ("green", c_uint8, 8),
        ("blue", c_uint8, 8)
    ]


class SafetyLightsSerial(Node):
    def __init__(self):
        super().__init__("autonav_serial_safetylights")

    def configure(self):
        self.safetyLightsSubscriber = self.create_subscription(SafetyLights, "/autonav/SafetyLights", self.onSafetyLightsReceived, 20)
        self.pico = serial.Serial("/dev/autonav-mc-safetylights", baudrate = 115200)
        self.writeQueue = []
        self.writeQueueLock = threading.Lock()
        self.writeThread = threading.Thread(target=self.picoWriteWorker)
        self.writeThread.start()
        self.setDeviceState(DeviceStateEnum.OPERATING)
        
    def transition(self, old: SystemState, updated: SystemState):
        pass

    def picoWriteWorker(self):
        while rclpy.ok():
            if not self.pico.is_open or self.pico.in_waiting > 0:
                continue
            
            self.writeQueueLock.acquire()
            if len(self.writeQueue) > 0:
                jsonStr = json.dumps(self.writeQueue.pop(0))
                self.log(jsonStr)
                self.pico.write(bytes(jsonStr, "utf-8"))
            self.writeQueueLock.release()

    def onSafetyLightsReceived(self, lights: SafetyLights):
        data = {}
        data["autonomous"] = lights.autonomous
        data["eco"] = lights.eco
        data["mode"] = lights.mode
        data["brightness"] = lights.brightness
        data["red"] = lights.red
        data["green"] = lights.green
        data["blue"] = lights.blue
        self.writeQueueLock.acquire()
        self.writeQueue.append(data)
        self.writeQueueLock.release()


def main():
    rclpy.init()
    rclpy.spin(SafetyLightsSerial())
    rclpy.shutdown()


if __name__ == "__main__":
    main()
