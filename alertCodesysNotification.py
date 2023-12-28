#!/usr/bin/python

import RPi.GPIO as GPIO
import time

if __name__ == "__main__":

	GPIO.setmode(GPIO.BCM)

	alertOut = 4
	GPIO.setup(alertOut, GPIO.OUT, initial = 0)

	GPIO.output(alertOut, 1)
	print("Pin 4 HIGH  -> PLC Notification ON")

	time.sleep(1)
	GPIO.cleanup()
	print("Pin 4 RESET -> PLC Notification OFF")

else:
	print("Nicht als __main__ aufgerufen")

