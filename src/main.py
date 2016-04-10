from FourWins import GamingBoard
from LEDMatrix import LEDMatrix

def main():
    rows = 6
    columns = 7
    myBoard = GamingBoard(rows, columns)
    myLEDMatrix = LEDMatrix(myBoard)
    myLEDMatrix.start()
    getch = _find_getch()

    printList(myBoard)
    running = True
    while running:
        print("Spieler 1 ist am Zug!")
        turn(myBoard, 1)
        printList(myBoard)
        print("Spieler 2 ist am Zug!")
        turn(myBoard, 3)
        printList(myBoard)


def printList(myBoard):
    print ("1  2  3  4  5  6  7")
    for i in range (0, myBoard.rows, 1):
        print (myBoard.board[i])
    print

def turn(myBoard, player):
    while True:
        inp = getch()
    myBoard.turn(player, targetCol)

def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch

if __name__ == "__main__":
    main()
