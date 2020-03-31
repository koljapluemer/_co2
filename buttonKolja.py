import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from datetime import datetime
from time import sleep

def button_detect(pinNumbers):
    def button_callback(channel):
        print("Button was pushed!",channel,datetime.now().time())
        
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering
    buttons = {}
    for pin in pinNumbers:
        buttons[pin] = GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin,GPIO.RISING,callback=button_callback,bouncetime=500)
    message = input("Press enter to quit\n\n") 

if __name__ == "__main__":
    button_detect([22,23,24,25])