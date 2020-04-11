from gpiozero import Button
from signal import pause
from datetime import datetime

def btn():
    print("Button was pushed!",datetime.now().time())

buttonUp = Button(22, pull_up=False)
buttonDown = Button(24, pull_up=False)
buttonBack = Button(25, pull_up=False)
buttonGo = Button(23, pull_up=False)

buttonUp.when_pressed = btn

pause()