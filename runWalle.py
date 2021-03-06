#!/usr/bin/env python3

import board
import busio
import time
import adafruit_vl53l0x
import motors

i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)
motors.settingUp()

#Main loop will reach the range and print it every second
while True:
  if(vl53.range < 150):
    motors.stopMotors()
  else:
    motors.forwardws()
  print("Range: {0}mm".format(vl53.range))
  #time.sleep(0.1)
