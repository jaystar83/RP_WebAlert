#!/usr/bin/python

import signal
import sys
import RPi.GPIO as GPIO
import time


def signal_handler(sig, frame):
	GPIO.cleanup()
	print("\nProgramm beendet durch Str + c")
	sys.exit(0)
def button_pressed_callback(channel):
        GPIO.cleanup()
        print("\nProgramm beendet durch Stop-Button")
        sys.exit(0)

if __name__ == "__main__":

	GPIO.setmode(GPIO.BCM)
	GPIO.cleanup()

	alertOut = 18
	GPIO.setup(alertOut, GPIO.OUT, initial = 0)
	buttonLeft = 22
	GPIO.setup(buttonLeft, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	print("Strg + c beendet das Programm")

	GPIO.add_event_detect(buttonLeft, GPIO.RISING, callback=button_pressed_callback, bouncetime=100)

	signal.signal(signal.SIGINT, signal_handler)

	RUN = True
	cnt = 0
	cnt_max = 60 #60 sec. Alarm

	while RUN:
		GPIO.output(alertOut, 1)
		time.sleep(0.5)
		GPIO.output(alertOut, 0)
		time.sleep(0.5)
		cnt = cnt + 1;
		if cnt >= cnt_max:
			RUN = False
	print("\nProgramm beendet nach " + str(cnt_max) + " Durchläufen\n")
	GPIO.cleanup()


else:
	print("Nicht als __main__ aufgerufen")

