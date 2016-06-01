# -*- coding: utf-8 -*-

from FourWins import GamingBoard
from MiniMax2 import MiniMaxDepth
from LEDMatrix import LEDMatrix

import sys, tty, termios

def main():
    rows = 6
    columns = 7
    maxDepth = 4
    
    global myBoard
    myBoard = GamingBoard(rows, columns)
    myAI = MiniMaxDepth(maxDepth)
    
    myLEDMatrix = LEDMatrix(myBoard)
    myLEDMatrix.setDaemon(True)
    myLEDMatrix.start()

    while True:
        mode = getch()

        # 1 Player Mode
        if ord(mode) == 49:
            while not myBoard.gameOver:
                if (myBoard.currentPlayer == 1):
                    turn()
                else :
                    col = myAI.getMove(myBoard.board, 3)
                    if (col == -1):
                        sys.exit()
                    myBoard.currentPosition = col+1
                    myBoard.throw(myBoard.currentPlayer)
                printList()
            while myBoard.gameOver:
                inp = getch()
                if ord(inp) == 113:
                    sys.exit()
                elif ord(inp) == 114:
                    resetBoard()

        # 2 Player mode
        elif ord(mode) == 50:
            while not myBoard.gameOver:
                if (myBoard.currentPlayer == 1):
                    turn()
                else:
                    turn()
            while myBoard.gameOver:
                inp = getch()
                if ord(inp) == 113:
                    sys.exit()
                elif ord(inp) == 114:
                    resetBoard()

        elif ord(mode) == 113:
            sys.exit()

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
    '''
    loop = True
    while loop:
        inp = input("Packe einen Stein in Spalte: ")
        if inp.isdigit():
            myBoard.currentPosition = int(inp)
            myBoard.throw(myBoard.currentPlayer)
            loop = False
        else :
            print("Keine gültige Eingabe!")
    '''
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
