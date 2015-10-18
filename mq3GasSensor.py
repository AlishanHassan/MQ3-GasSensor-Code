import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)

while True:
    input = GPIO.input(3)
    print(input)
    time.sleep(1) #sleep for one second before the next reading
