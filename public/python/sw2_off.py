# Edit line 6 to match your chosen GPIO pin

import RPi.GPIO as GPIO
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.output(11, GPIO.HIGH)
