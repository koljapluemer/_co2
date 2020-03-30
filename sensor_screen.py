import csv
import time
import mh_z19
import collections

from datetime import datetime, timedelta


from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
import time

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

measurements = {}


while True:
    for i in range(6):
        now = datetime.now()
        co2 = mh_z19.read()
        #print(co2)
        measurements[now] = co2['co2']
        orderedMeasurements = collections.OrderedDict(sorted(measurements.items(), reverse=True)).values()
        #print(orderedMeasurements)

        minuteAgo = now - timedelta(minutes=1)

        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            draw.text((5, 5), ("CO2: " + str(co2['co2'])), fill="white")
            draw.line((5,20,5,55), fill="white")
            draw.line((5,55,120,55), fill="white")

            for i, m in enumerate(orderedMeasurements[:115]):
#                print(i)
                height = 55 - m / 29
                height = max(min(55, height), 20)
         #       print(height)
                draw.point(((120 -  i), height), fill="white")


    with open ('co2.csv', mode='w') as f:
        writer = csv.writer(f)
        for k, v in measurements.items():
            writer.writerow([k,v])

        time.sleep(1)

