import curses

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

    return button

if __name__ == "__main__":
    try:
        # get the curses screen window
        screen = curses.initscr()

        # turn off input echoing
        curses.noecho()

        # respond to keys immediately (don't wait for enter)
        curses.cbreak()

        # map arrow keys to special values
        screen.keypad(True)

        while 1:
            screen.addstr(0, 0, cursors()+"   ")
    finally:
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
