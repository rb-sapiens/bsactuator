# -*- coding: utf-8 -*-
import serial

class BsActuator:
  def __init__(self, port, baud):
    self.ser = serial.Serial(port, baud, timeout = 0.1)
    self.talking = False

  def hello(self):
    print("hello")

  def set_length(self, length, speed):
    if self.talking == False:
      self.talking = True
      self.ser.write(b"stretch:"+str(length)+","+speed+";")
      while True:
        if self.ser.in_waiting > 0:
          recv_data = self.ser.readline()
          message = recv_data.strip().decode('utf-8')
          if message == "complete":
              self.talking = False

  def get_length(self):
    self.ser.write(b"get;")

  def hold(self):
    self.ser.write(b"hold;")

  def release(self):
    self.ser.write(b"release;")