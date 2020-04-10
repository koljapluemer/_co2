# -*- coding: utf-8 -*-
import csv
import time
import mh_z19
import collections

from datetime import datetime, timedelta

import numpy


from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
import time

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

measurements = {}
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from datetime import datetime
from time import sleep

measurements = {}
screenOn = True
lastPressed = 0
oldLastPressed = 0

def measure():
    global screenOn
    global lastPressed
    global oldLastPressed

    for i in range(6):
        now = datetime.now()
        co2 = mh_z19.read()
        measurements[now] = co2['co2']
        print(measurements[now])
        orderedMeasurements = collections.OrderedDict(sorted(measurements.items(), reverse=True)).values()
        
        minuteAgo = now - timedelta(minutes=1)
        recentMeasurements = {k: v for k, v in measurements.items() if k > minuteAgo}
        minuteAvg = sum(recentMeasurements.values()) / len(recentMeasurements.values()) 
        minuteStd = numpy.std(numpy.array(recentMeasurements.values()), axis=0)
        if lastPressed != oldLastPressed:
            screenOn = not screenOn
        oldLastPressed = lastPressed
        if screenOn:
            device.show()
            with canvas(device) as draw:
                draw.rectangle(device.bounding_box, outline="white", fill="black")
                draw.text((5, 5), (str(co2['co2'])), fill="white")
                draw.text((33, 5), ('avg ' + str(minuteAvg) + "(" + str(int(round(minuteStd, 0))) + ")"), fill="white")
                draw.line((5,20,5,55), fill="white")
                draw.line((5,55,120,55), fill="white")

                for i, m in enumerate(orderedMeasurements[:115]):
                    height = 55 - m / 29
                    height = max(min(55, height), 20)
                    draw.point(((120 -  i), height), fill="white")
        else:
            device.hide()
        time.sleep(10)


    with open ('co2.csv', mode='w') as f:
        writer = csv.writer(f)
        for k, v in measurements.items():
            writer.writerow([k,v])

def button_callback(channel):
    global lastPressed
    lastPressed = datetime.now()
    print("Button was pushed!",channel,lastPressed.time())
    
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering
buttons = {}
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(24,GPIO.RISING,callback=button_callback,bouncetime=500)

while True:
    try:  
        measure()
    finally:                   # this block will run no matter how the try block exits
        GPIO.cleanup()         # clean up after yourself

