#!/usr/bin/python3
# Dice (sv. Tärning)
# License: GPLv3+ ABSOLUTELY NO WARRANTY
# Author: Mikael O. Bonnier, Lund, Sweden. mobluse on Scratch & GitHub

import RPi.GPIO as GPIO 
# Runs on Raspberry Pi 1 A & B Rev. 2.
# (sv. Fungerar på Raspberry Pi 1 A & B Rev. 2.)
import time
import random
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN) # Pin 3 (sv. Pinne 3)
# Pin 6 is GND. (sv. Pinne 6 är jord.)
GPIO.setup(23, GPIO.OUT) # Pin 16 (sv. Pinne 16)
# Pin 14 is GND. (sv. Pinne 14 är jord.)

for i in range(3): # Danish salute! (sv. Dansk lösen!)
    GPIO.output(23, True)
    time.sleep(0.2)
    GPIO.output(23, False)
    time.sleep(0.8)

GPIO.output(23, True) # Long hurrah! (sv. Långt hurra!)
time.sleep(8) # Show all colors. (sv. Visa alla färger.)
GPIO.output(23, False)
time.sleep(1)

while True:
    if not GPIO.input(2):
        dice = random.choice(range(1, 7))
        print(dice)
        for i in range(dice):
            GPIO.output(23, True)
            time.sleep(0.2)
            GPIO.output(23, False)
            time.sleep(0.3)
    else:
        GPIO.output(23, False)
    time.sleep(0.1)
