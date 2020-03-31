import RPi.GPIO as GPIO  
from time import sleep     # this lets us have a time delay (see line 15)  
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # set GPIO25 as input (button)  
  
try:
    Button = 0
    ButtonPressed = 0
    ButtonReleased = 0
    while True:            # this will carry on until you hit CTRL+C  
        if GPIO.input(25): # if port 25 == 1
            if Button is 0:
                ButtonPressed = 1
                Button = 1
            else:
                ButtonPressed = 0
            
        else:  
            if Button is 1:
                ButtonReleased = 1
                Button = 0

            else:
                ButtonReleased = 0
        
        if ButtonPressed:
            print "Button presssed"
        if ButtonReleased:
            print "Button released"
        sleep(0.1)         # wait 0.1 seconds  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  
