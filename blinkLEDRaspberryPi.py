import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(40, GPIO.IN)

pbSwitchState = 0
while True:
    pbSwitchState = GPIO.input(40)
    if pbSwitchState == 1:
        for i in range(3):
            GPIO.output(5, 1)
            time.sleep(0.1)
            GPIO.output(5, 0)
            time.sleep(0.1)
