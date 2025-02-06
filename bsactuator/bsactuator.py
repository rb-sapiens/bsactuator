# -*- coding: utf-8 -*-
import serial
import signal
import sys
import time

class BsActuator:
  def __init__(self, port, baud, model=None):
    self.ser = serial.Serial(port, baud, timeout = 0.1)
    self.talking = False
    self.timeout = 20
    self.timeout_get = 1
    self.model = model
    signal.signal(signal.SIGINT, self.signal_handler)

  def signal_handler(self, signal, frame):
    self.ser.close()
    sys.exit(0)

  def set_length(self, length, speed = None):
    req_message = "set:"+str(length)+";"
    version = sys.version_info[0]
    if version == 2:
      self.ser.write(bytes(req_message).encode("utf-8"))
    if version == 3:
      self.ser.write(bytes(req_message, "utf-8"))

  def get_length(self):
    try:
      self.ser.write(b"get;")
      timeout = time.time() + self.timeout_get
      while True:
        if time.time() > timeout:
          break
        if self.ser.in_waiting > 0:
          recv_data = self.ser.readline()
          message = recv_data.strip().decode('utf-8')
          if "length:" in message:
            length_str = message.replace("length:", "")
            return int(length_str)
    except Exception as e:
      print(e)
      return None
    return None

  def stop(self):
    self.ser.write(b"stop;")

  def initialized(self):
    timeout = time.time() + self.timeout_get
    self.ser.write(b"initialized;")
    while True:
      if time.time() > timeout:
        break
      if self.ser.in_waiting > 0:
        recv_data = self.ser.readline()
        message = recv_data.strip().decode('utf-8')
        if message == "false":
          return False
        elif message == "true":
          return True
        else:
          return False
    return False

  def reset(self):
    self.ser.write(b"reset;")
    timeout = time.time() + self.timeout
    if self.model == "25mm01":
      while True:
        if time.time() > timeout:
          break
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