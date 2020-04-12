from statemachine import StateMachine
from cursors import cursors
import curses
from time import sleep

def measure_screen(button):
    global mode
    mode = "awake"
    screen.clear()
    screen.addstr(0, 0, "This is going to be the measuring graph")
    screen.addstr(5, 0, str(button))
    button = "None"
    while 1:
        button = cursors()
        if button is "Go":
            newState = "MeasureSleep"; break
        elif button is "Back":
            newState = "MenuMeasure"; break

    return (newState, button)

def measure_sleep(button):
    global mode
    mode = "asleep"
    screen.clear()
    screen.addstr(0, 0, "This is going to be the sleep measurement")
    screen.addstr(5, 0, str(button))
    button = "None"
    while 1:
        button = cursors()
        if button is "Go":
            newState = "MeasureScreen"; break
        elif button is "Back":
            newState = "MenuMeasure"; break
    return (newState,button)

def menu_measure(button):
    global mode
    screen.clear()
    screen.addstr(0, 0, "Measure", curses.A_BOLD)
    screen.addstr(1, 0, "Screen Off")
    screen.addstr(2, 0, "Calibrate")
    screen.addstr(3, 0, "Turn Off")
    screen.addstr(5, 0, str(button))

    button = "None"

    while 1:
        button = cursors()

        if button is "Go" or button is "Back":
            if mode is "awake":
                newState = "MeasureScreen"; break
            elif mode is "asleep":
                newState = "MeasureSleep"; break
        elif button is "Up":
            newState = "MenuTurnOff"; break
        elif button is "Down":
            newState = "MenuScreenOff"; break
    return (newState, button)

def menu_screen_off(button):
    global sleep
    screen.clear()
    screen.addstr(0, 0, "Measure")
    screen.addstr(1, 0, "Screen Off", curses.A_BOLD)
    screen.addstr(2, 0, "Calibrate")
    screen.addstr(3, 0, "Turn Off")
    screen.addstr(5, 0, str(button))

    button = "None"

    while 1:
        button = cursors()
        if button is "Go":
            newState = "ScreenOff"; break
        elif button is "Back":
            if mode is "awake":
                newState = "MeasureScreen"; break
            elif mode is "asleep":
                newState = "MeasureSleep"; break
        elif button is "Up":
            newState = "MenuMeasure"; break
        elif button is "Down":
            newState = "MenuCalibrate"; break
    return (newState, button)

def screen_off(button):
    global sleep
    screen.clear()
    screen.addstr(5, 0, str(button))

    button = "None"

    while 1:
        button = cursors()
        if button is not "None":
            if mode is "awake":
                newState = "MeasureScreen"; break
            elif mode is "asleep":
                newState = "MeasureSleep"; break

    return (newState, button)

def menu_calibrate(button):
    global sleep
    screen.clear()
    screen.addstr(0, 0, "Measure")
    screen.addstr(1, 0, "Screen Off")
    screen.addstr(2, 0, "Calibrate", curses.A_BOLD)
    screen.addstr(3, 0, "Turn Off")
    screen.addstr(5, 0, str(button))

    button = "None"

    while 1:
        button = cursors()
        if button is "Go":
            newState = "Calibrate"; break
        elif button is "Back":
            if mode is "awake":
                newState = "MeasureScreen"; break
            elif mode is "asleep":
                newState = "MeasureSleep"; break
        elif button is "Up":
            newState = "MenuScreenOff"; break
        elif button is "Down":
            newState = "MenuTurnOff"; break

    return (newState, button)

def calibrate(button):
    global mode
    screen.clear()
    screen.addstr(0, 0, "I am calibrating. Please wait a sec")
    screen.addstr(5, 0, str(button))

    button = "None"

    while(1):
        button = cursors()
        if button is not "None":
            if mode is "awake":
                newState = "MeasureScreen"; break
            elif mode is "asleep":
                newState = "MeasureSleep"; break

    return (newState, button)

def menu_turn_off(button):
    global mode
    screen.clear()
    screen.addstr(0, 0, "Measure")
    screen.addstr(1, 0, "Screen Off")
    screen.addstr(2, 0, "Calibrate")
    screen.addstr(3, 0, "Turn Off", curses.A_BOLD)
    screen.addstr(5, 0, str(button))

    button = "None"

    while 1:
        button = cursors()
        if button is "Go":
            newState = "TurnOff"; break
        elif button is "Back":
            if mode is "awake":
                newState = "MeasureScreen"; break
            elif mode is "asleep":
                newState = "MeasureSleep"; break
        elif button is "Up":
            newState = "MenuCalibrate"; break
        elif button is "Down":
            newState = "MenuMeasure"; break

    return (newState, button)

'''
def turn_off(button):
    global mode
    screen.clear()
    screen.addstr(0, 0, "Measure")
    screen.addstr(1, 0, "Screen Off")
    screen.addstr(2, 0, "Calibrate")
    screen.addstr(3, 0, "Turn Off", curses.A_BOLD)
    screen.addstr(5, 0, str(button))

    button = "None"

    while 1:
        button = cursors()
        if button is "Go":
            newState = ""; break
        elif button is "Back":
            newState = ""; break
        elif button is "Up":
            newState = ""; break
        elif button is "Down":
            newState = ""; break

    return (newState, button)
'''

def cursors():
    char = screen.getch()

    if char == curses.KEY_RIGHT:
        # print doesn't work with curses, use addstr instead
        button = "Go"
    elif char == curses.KEY_LEFT:
        button = "Back"
    elif char == curses.KEY_UP:
        button = "Up"
    elif char == curses.KEY_DOWN:
        button = "Down"
    else:
        button = "None"

    return button


if __name__ == "__main__":
    # get the curses screen window
    screen = curses.initscr()

    # turn off input echoing
    curses.noecho()

    # respond to keys immediately (don't wait for enter)
    curses.cbreak()

    # map arrow keys to special values
    screen.keypad(True)

    mode = "awake"

    try:
        menu = StateMachine()
        menu.add_state("MeasureScreen", measure_screen)
        menu.add_state("MeasureSleep", measure_sleep)
        menu.add_state("MenuMeasure", menu_measure)
        menu.add_state("MenuScreenOff", menu_screen_off)
        menu.add_state("ScreenOff",screen_off)
        menu.add_state("MenuCalibrate", menu_calibrate)
        menu.add_state("Calibrate", calibrate)
        menu.add_state("MenuTurnOff", menu_turn_off)

        #menu.add_state("")

        menu.add_state("TurnOff",None, end_state=1)

        menu.set_start("MeasureScreen")
        menu.run("None")

    finally:
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
