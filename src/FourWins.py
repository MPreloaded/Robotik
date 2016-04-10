class GamingBoard:
    """ Class for the gaming board, including rules."""

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = []
        self.currentPosition = 4
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
        won = GamingBoard.checkWin(player, self.board)
        self.currentPlayer = player

    ############
    # Private  #
    ############
    @staticmethod
    def checkWin(player, list):
        won = False

        if not won:
            won = GamingBoard._checkColWin(player, list)

        if not won:
            won = GamingBoard._checkRowWin(player, list)

        if not won:
            won = GamingBoard._checkDiagULWin(player, list)

        if not won:
            won = GamingBoard._checkDiagURWin(player, list)

        return won


    @staticmethod
    def _checkRowWin(player, list):
        count = 0
        for row in list:
            for token in row:
                if token == player:
                    count = count+1
                else:
                    count = 0
                if count ==4:
                    return True
        return False

    @staticmethod
    def _checkColWin(player, list):
        count = 0
        for i in range (0, len(list[0]), 1):
            for row in list:
                if row[i] == player:
                    count = count + 1
                else:
                    count = 0
                if count == 4:
                    return True
        return False

    @staticmethod
    def _checkDiagULWin(player, list):
        for row in range (0, len(list)-3, 1):
            for col in range (0, len(list[0])-3, 1):
                count = 0
                for n in range (0, 4, 1):
                    if list[row+n][col+n] == player:
                        count = count + 1
                    if count == 4:
                        return True
        return False

    @staticmethod
    def _checkDiagURWin(player, list):
        count = 0
        for row in range(0, len(list)-3, 1):
            for col in range(len(list[0])-3, 0, -1):
                count = 0
                for n in range (0, 4, 1):
                    if list[row+n][col-n] == player:
                        count = count + 1
                    if count == 4:
                        return True
        return False

    def printWinner(self, player):
            print ("Spieler " + str(player) + " gewinnt!!!")
            print ("!!!Herzlichen Glueckwunsch!!!")

    def moveRight(self):
        if self.currentPosition < 7:
            self.currentPosition = self.currentPosition+1

    def moveLeft(self):
        if self.currentPosition > 1:
            self.currentPosition = self.currentPosition-1
