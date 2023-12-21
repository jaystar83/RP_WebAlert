#!/usr/bin/python

import RPi.GPIO as GPIO

if __name__ == "__main__":

	GPIO.setmode(GPIO.BCM)
	GPIO.cleanup()

	alertOut = 4
	GPIO.setup(alertOut, GPIO.OUT, initial = 1)

	print("Pin 4 auf HIGH gesetzt -> PLC Notification")

else:
	print("Nicht als __main__ aufgerufen")

