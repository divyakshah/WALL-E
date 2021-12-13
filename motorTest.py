#!/usr/bin/env python3

import Jetson.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
channel = 13

GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
#GPIO.setWarnings(False)
try:
  while True:
    print("I am running")
    GPIO.output(channel, GPIO.HIGH)
    time.sleep(0.25)
    #GPIO.output(channel, GPIO.LOW)
    #time.sleep(0.25)
finally:
  GPIO.cleanup()
  
def stopMotors():
  GPIO.output(channel, GPIO.LOW)
