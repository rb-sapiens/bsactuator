# -*- coding: utf-8 -*-
import serial
import signal
import sys
import time

class SwitchPusher:
  def __init__(self, port, baud):
    self.ser = serial.Serial(port, baud, timeout = 0.1)
    self.talking = False
    self.timeout = 20
    self.timeout_get = 1
    self.current_position = [0,0,0]
    self.switch_statuses = [False,False,False]
    signal.signal(signal.SIGINT, self.signal_handler)


  def signal_handler(self, signal, frame):
    self.ser.close()
    sys.exit(0)

  def move(self, motor_num, length):
    req_message = "move:"+str(motor_num)+","+str(length)+";"
    version = sys.version_info[0]
    if version == 2:
      self.ser.write(bytes(req_message).encode("utf-8"))
    if version == 3:
      self.ser.write(bytes(req_message, "utf-8"))
    return True

  def get_position(self):
    self.ser.write(b"get_position;")
    timeout = time.time() + self.timeout_get
    while True:
      if time.time() > timeout:
        break
      if self.ser.in_waiting > 0:
        recv_data = self.ser.readline()
        message = recv_data.strip().decode('utf-8')
        if "position:" in message:
          position_str = message.split("position:")[1]
          self.current_position = position_str.split()
    return -1


  def get_switch_statuses(self):
    self.ser.write(b"get_switch_statuses;")
    timeout = time.time() + self.timeout_get
    while True:
      if time.time() > timeout:
        break
      if self.ser.in_waiting > 0:
        recv_data = self.ser.readline()
        message = recv_data.strip().decode('utf-8')
        if "switch_statuses:" in message:
          switch_statuses_str = message.split("switch_statuses:")[1]
          switch_statuses_arr = switch_statuses_str.split()
          self.switch_statuses[0] = switch_statuses_arr[0] == "true"
          self.switch_statuses[1] = switch_statuses_arr[1] == "true"
          self.switch_statuses[2] = switch_statuses_arr[2] == "true"
    return -1

  def close(self):
    self.ser.close()