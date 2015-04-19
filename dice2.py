#!/usr/bin/python3
# Dice (sv. Tärning) Copyright (C) 2015 Mikael O. Bonnier, Lund, Sweden. mobluse on Scratch & GitHub
# This program comes with ABSOLUTELY NO WARRANTY.
# This is free software, and you are welcome to redistribute it under certain conditions.
# License: GPLv3+ http://www.gnu.org/copyleft/gpl.html
# Tested on Raspberry Pi 1 A & B Rev. 2 & B+ Rev. 3, but should work on 1 B Rev. 1 and 2 B.
# (sv. Testat på Raspberry Pi 1 A & B Rev. 2 & B+ Rev. 3, men bör fungera på 1 B Rev. 1 och 2 B.)
# (sv. Utrustning: 5 sladdar hona-hona, 1 LED, 1 resistor 330 ohm, 1 del av motståndsben.)

import RPi.GPIO as GPIO 
import time
import random

print(GPIO.RPI_INFO)
GPIO.setmode(GPIO.BOARD)
GPIO2 = 3 # GPIO2 = P1-03, but GPIO0 = P1-03 on RPi 1 B Rev. 1. 
GPIO.setup(GPIO2, GPIO.IN)
GPIO.add_event_detect(GPIO2, GPIO.FALLING, bouncetime=200)
# P1-06 = GND. (sv. P1-06 = jord.)
# (sv. koppla sladdar till pinnarna och en del av ett komponentben till en sladd som prob.
#  Peta med komponentbenet på metalldelen på den andra sladden för att kasta tärningen.) 
GPIO23 = 16 # GPIO23 = P1-16
GPIO.setup(GPIO23, GPIO.OUT)
# P1-14 = GND. (sv. P1-14 = jord.)
# (sv. Koppla in lysdiod och resistor i serie mellan pinnarna med 3 sladdar.)

for i in range(3): # Danish salute! (sv. Dansk lösen!)
    GPIO.output(GPIO23, True)
    time.sleep(0.2)
    GPIO.output(GPIO23, False)
    time.sleep(0.8)

GPIO.output(GPIO23, True) # Long hurrah! (sv. Långt hurra!)
time.sleep(8) # Show all colors. (sv. Visa alla färger.)
GPIO.output(GPIO23, False)
time.sleep(1)

try:
    while True:
        if GPIO.event_detected(GPIO2):
            dice = random.choice(range(1, 7))
            print(dice)
            for i in range(dice):
                GPIO.output(GPIO23, True)
                time.sleep(0.2)
                GPIO.output(GPIO23, False)
                time.sleep(0.3)
        else:
            GPIO.output(GPIO23, False)
        time.sleep(0.2)

except KeyboardInterrupt:
    print(" Ctrl+C tryckt!")

except:
    print("Annat undantag.")

finally:
    GPIO.cleanup()
