#!/usr/bin/env python3

import Jetson.GPIO as GPIO
import time

def settingUp():
  GPIO.cleanup()
  GPIO.setmode(GPIO.BOARD)
  channel = 13
  GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
  #GPIO.setWarnings(False)
def forwards():
  settingUp()
  try:
    #while True"
    print("I am running")
    GPIO.output(13, GPIO.HIGH)
    #time.sleep(0.25)
    GPIO.output(13, GPIO.LOW)
    #time.sleep(0.25)
  finally:
    GPIO.cleanup()
def stopMotors():
  settingUp()
  print("I have stopped")
  GPIO.output(13, GPIO.LOW)
