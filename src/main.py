from FourWins import GamingBoard
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
    while True:
        while not myBoard.gameOver:
            turn()
            printList()
        while myBoard.gameOver:
            inp = getch()
            if ord(inp) == 113:
                sys.exit()
            elif ord(inp) == 114:
                resetBoard()

def printList():
    print ("1  2  3  4  5  6  7")
    for i in range (0, myBoard.rows, 1):
        print (myBoard.board[i])
    print

def resetBoard():
    for row in range (0, myBoard.rows):
        for col in range (0, myBoard.columns):
            myBoard.board[row][col] = 0
    myBoard.gameOver = False
    myBoard.currentPlayer = 1

def turn():
    while True:
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
                myBoard.throw(myBoard.currentPlayer)
            except:
                continue
            break

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
