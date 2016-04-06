from FourWins import GamingBoard
from LEDMatrix import LEDMatrix

def main():
    rows = 6
    columns = 7
    myBoard = GamingBoard(rows, columns)
    myLEDMatrix = LEDMatrix(myBoard)
    myLEDMatrix.start()
    myLEDMatrix.run()

    printList(myBoard)
    running = True
    while running:
        print("Spieler 1 ist am Zug!")
        turn(myBoard, 1)
        printList(myBoard)
        print("Spieler 2 ist am Zug!")
        turn(myBoard, 2)
        printList(myBoard)


def printList(myBoard):
    print ("1  2  3  4  5  6  7")
    for i in range (0, myBoard.rows, 1):
        print (myBoard.board[i])
    print

def turn(myBoard, player):
    targetCol = raw_input("In welche Reihe soll der Stein geworfen werden?: ")
    myBoard.turn(player, targetCol)

if __name__ == "__main__":
    main()