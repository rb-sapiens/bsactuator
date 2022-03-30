# -*- coding: utf-8 -*-
import serial
import signal
import sys

class BsActuator:
  def __init__(self, port, baud):
    self.ser = serial.Serial(port, baud, timeout = 0.1)
    self.talking = False
    signal.signal(signal.SIGINT, self.signal_handler)


  def signal_handler(self, signal, frame):
    self.ser.close()
    sys.exit(0)
    def hello(self):
      print("hello")

  def set_length(self, length, speed):
    if length < 0 or length > 1500 or (not isinstance(length, int)):
      return False
    if speed < 1 or speed > 10 or (not isinstance(speed, int)):
      return False

    if self.talking == False:
      self.talking = True
      req_message = "set:"+str(length)+","+str(speed)+";"
      self.ser.write(bytes(req_message, 'utf-8'))
      while True:
        if self.ser.in_waiting > 0:
          recv_data = self.ser.readline()
          message = recv_data.strip().decode('utf-8')
          if "complete:" in message:
            length_str = message.replace("complete:", "")
            if length == int(length_str):
              self.talking = False
              return True
    return False

  def get_length(self):
    self.ser.write(b"get;")
    while True:
      if self.ser.in_waiting > 0:
        recv_data = self.ser.readline()
        message = recv_data.strip().decode('utf-8')
        if "length:" in message:
          length_str = message.replace("length:", "")
          return int(length_str)

  def hold(self):
    self.ser.write(b"hold;")

  def release(self):
    self.ser.write(b"release;")

  def reset(self):
    self.ser.write(b"reset;")
    while True:
      if self.ser.in_waiting > 0:
        recv_data = self.ser.readline()
        message = recv_data.strip().decode('utf-8')
        if "complete:" in message:
          length_str = message.replace("complete:", "")
          if int(length_str) == -1000:
            self.talking = False
            return True

  def close(self):
    self.ser.close()