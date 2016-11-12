import RPi.GPIO as GPIO
import time
import os


class Lights:
  def __init__(self):
    # Define PiLITEr to GPIO mapping
    self.leds = [7,11,13,12,15,16,18,22]
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    for pin in self.leds:
      GPIO.setup(pin, GPIO.OUT)

  def nightRide(self, loop):
    # Define the ranges for the indexes
    forward = range(len(self.leds))
    backward = list(reversed(forward))

    # Define the interval for the light on/off
    SLEEP_TIME = 0.08

    while loop > 0:
      # Turn On the first light as the loop continues with the first
      pin = self.leds[0]
      #print "on(" + str(pin) + ")"
      GPIO.output(pin, GPIO.HIGH)
      time.sleep(SLEEP_TIME)

      # Loop going forward
      for i in forward:
        first = i
        second = i if i + 1 == len(forward) else i + 1

        # Don't show when the position is the same
        if (first == second):
          continue

        self.setNeighborPinsOffOn(first, second, SLEEP_TIME)

      # Loop going backward
      for j in backward:
        second = j
        first = j if j + 1 == len(backward) else j + 1

        if (first == second) or (second == 0):
          continue

        self.setNeighborPinsOffOn(first, second, SLEEP_TIME)

      # Turn off the second light as the loop continues with the first
      pin = self.leds[1]
      #print "off(" + str(pin) + ")"
      GPIO.output(pin, GPIO.LOW)

      # Continue the loop over the values
      loop = loop - 1

  def setNeighborPinsOffOn(self, firstIndex, secondIndex, sleepTime):
    firstPin = self.leds[firstIndex]
    secondPin = self.leds[secondIndex]
    #print "# " + str(firstIndex) + ":" + str(secondIndex)
    #print "off(" + str(firstPin) + ") - on(" + str(secondPin) + ")"
    GPIO.output(firstPin, GPIO.LOW)
    GPIO.output(secondPin, GPIO.HIGH)
    time.sleep(sleepTime)

  def hide(self):
    leds = self.leds
    for pin in leds:
      GPIO.output(pin, GPIO.LOW)

  def show(self):
    leds = self.leds
    for pin in leds:
      GPIO.output(pin, GPIO.HIGH)

  def cleanup(self):
    GPIO.cleanup()
