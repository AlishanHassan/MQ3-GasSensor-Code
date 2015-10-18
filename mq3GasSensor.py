import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD) #Using header layout for this implementation; change to GPIO.BCM to follow Broadcom GPIO
GPIO.setup(3, GPIO.IN) #Pin 3 on header, Pin 8 on BCM

while True:
    input = GPIO.input(3)
    print(input) #I don't think this outputs anything other than 0/1 0 might need to utilize the analog out to be useful
    time.sleep(1) #sleep for one second before the next reading
