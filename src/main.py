from FourWins import GamingBoard
from MiniMax import MiniMax
from LEDMatrix import LEDMatrix

import sys, tty, termios

def main():
    rows = 6
    columns = 7
    global myBoard
    myBoard = GamingBoard(rows, columns)
    
    myLEDMatrix = LEDMatrix(myBoard)
    myLEDMatrix.setDaemon(True)
    myLEDMatrix.start()

    printList()
    running = True
    while running:
        print("Spieler 1 ist am Zug!")
        turn(1)
        printList()
        print("Spieler 2 ist am Zug!")
        turn(3)
        printList()


def printList():
    print ("1  2  3  4  5  6  7")
    for i in range (0, myBoard.rows, 1):
        print (myBoard.board[i])
    print

def resetBoard():
    for row in myBoard:
        for val in row:
            val = 0
    myBoard.gameOver = False
    myBoard.currentPlayer = 1

def turn(player):
    while True:
        while not myBoard.gameOver:
            inp = getch()
            if ord(inp) == 113:
                sys.exit()
            elif ord(inp) == 114:
                resetBoard()
            elif ord(inp) == 67:
                myBoard.moveRight()
            elif ord(inp) == 68:
                myBoard.moveLeft()
            elif ord(inp) == 13:
                try:
                    myBoard.throw(player)
                except:
                    continue
        inp = getch()
        if ord(inp) == 114:
            resetBoard()
        elif ord(inp) == 113:
            sys.exit()

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
