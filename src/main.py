from FourWins import GamingBoard
from LEDMatrix import LEDMatrix
import sys, tty, termios

def main():
    rows = 6
    columns = 7
    myBoard = GamingBoard(rows, columns)
    myLEDMatrix = LEDMatrix(myBoard)
    myLEDMatrix.setDaemon(True)
    myLEDMatrix.start()

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

def turn(myBoard, myLEDMatrix):
    while True:
        inp = getch()
        print(inp)
        if ord(inp) == 113:
            print("Exit")
            sys.exit()
        elif ord(inp) == 67:
            print("right")
            myBoard.moveRight()
        elif ord(inp) == 68:
            print("left")
            myBoard.moveLeft()

def getch():
    # POSIX system. Create and return a getch that manipulates the tty.
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

if __name__ == "__main__":
    main()
