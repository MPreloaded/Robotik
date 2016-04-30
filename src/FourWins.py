class GamingBoard:
    """ Class for the gaming board, including rules."""

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = []
        self.currentPosition = 4
        self.gameOver = False
        for i in range (0, self.rows):
            row = []
            for j in range (0, self.columns):
                row.append(0)
            self.board.append(row)
        self.currentPlayer = 1

    ############
    #  Public  #
    ############
    def throw(self, player):
        stoneSet = False
        for row in range(self.rows-1, -1, -1):
            if self.board[row][self.currentPosition-1] == 0:
                self.board[row][self.currentPosition-1] = player
                stoneSet = True
                break
        if stoneSet == False:
            raise 1
        self.currentPosition = 4
        won, winningStones = GamingBoard.checkWin(player, self.board)
        if won:
            for stone in winningStones:
                self.board[stone[0], stone[1]] = 2
            self.gameOver = True
        else:
            self.getNextPlayer()

    ############
    # Private  #
    ############
    @staticmethod
    def checkWin(player, list):
        won = False

        if not won:
            won, winningStones = GamingBoard._checkColWin(player, list)

        if not won:
            won, winningStones = GamingBoard._checkRowWin(player, list)

        if not won:
            won, winningStones = GamingBoard._checkDiagULWin(player, list)

        if not won:
            won, winningStones = GamingBoard._checkDiagURWin(player, list)

        return (won, winningStones)


    @staticmethod
    def _checkRowWin(player, list):
        winningStones = []
        count = 0
        for row in range (0, len(list), 1):
            for col in range (0, len((list)[0]), 1):
                if list[row][col] == player:
                    count = count+1
                else:
                    count = 0
                if count == 4:
                    for i in range (0, 4):
                        winningStones.append((row, col-i))
                    return (True, winningStones)
        return (False, winningStones)

    @staticmethod
    def _checkColWin(player, list):
        winningStones = []
        count = 0
        for col in range (0, len(list[0]), 1):
            for row in range(0, len(list), 1):
                if list[row][col] == player:
                    count = count + 1
                else:
                    count = 0
                if count == 4:
                    for i in range (0, 4):
                        winningStones.append((row-i, col))
                    return (True, winningStones)
        return (False, winningStones)

    @staticmethod
    def _checkDiagULWin(player, list):
        winningStones = []
        for row in range (0, len(list)-3, 1):
            for col in range (0, len(list[0])-3, 1):
                count = 0
                for n in range (0, 4, 1):
                    if list[row+n][col+n] == player:
                        count = count + 1
                    if count == 4:
                        for i in range (0, 4):
                            winningStones.append((row-i, col-i))
                        return (True, winningStones)
        return (False, winningStones)

    @staticmethod
    def _checkDiagURWin(player, list):
        winningStones = []
        for row in range(0, len(list)-3, 1):
            for col in range(len(list[0])-3, 0, -1):
                count = 0
                for n in range (0, 4, 1):
                    if list[row+n][col-n] == player:
                        count = count + 1
                    if count == 4:
                        for i in range (0, 4):
                            winningStones.append((row-i, col+i))
                        return (True, winningStones)
        return (False, winningStones)

    def getNextPlayer(self):
        if self.currentPlayer == 1:
            self.currentPlayer = 3
        else:
            self.currentPlayer = 1

    def printWinner(self, player):
            print ("Spieler " + str(player) + " gewinnt!!!")
            print ("!!!Herzlichen Glueckwunsch!!!")

    def moveRight(self):
        if self.currentPosition < 7:
            self.currentPosition = self.currentPosition+1

    def moveLeft(self):
        if self.currentPosition > 1:
            self.currentPosition = self.currentPosition-1
