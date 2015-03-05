#!/usr/bin/python3
# Dice (sv. Tärning) Copyright (C) 2015 Mikael O. Bonnier, Lund, Sweden. mobluse on Scratch & GitHub
# This program comes with ABSOLUTELY NO WARRANTY.
# This is free software, and you are welcome to redistribute it under certain conditions.
# License: GPLv3+ http://www.gnu.org/copyleft/gpl.html
# Runs on Raspberry Pi 1 A & B Rev. 2.
# (sv. Fungerar på Raspberry Pi 1 A & B Rev. 2.)
# (sv. Utrustning: 5 sladdar hona-hona, 1 LED, 1 resistor 330 ohm, 1 del av motståndsben.)

import RPi.GPIO as GPIO 
import time
import random
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN) # Pin 3 (sv. Pinne 3)
# Pin 6 is GND. (sv. Pinne 6 är jord.)
# (sv. koppla sladdar till pinnarna och en del av ett komponentben till en sladd som prob.
#  Peta med komponentbenet på metalldelen på den andra sladden för att kasta tärningen.) 
GPIO.setup(23, GPIO.OUT) # Pin 16 (sv. Pinne 16)
# Pin 14 is GND. (sv. Pinne 14 är jord.)
# (sv. Koppla in lysdiod och resistor i serie mellan pinnarna med 3 sladdar.)

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
