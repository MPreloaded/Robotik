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

    ############
    #  Public  #
    ############
    def turn(self, player, targetCol):
        try:
            targetCol = int(targetCol)
            if targetCol < 1:
                raise 0
            for row in range (self.rows-1, -1, -1):
                if self.board[row][targetCol-1] == 0:
                    self.board[row][targetCol-1] = player
                    break
        except:
            print ("Ungueltige Eingabe!")
        self.currentPosition = 4
        self.checkWin(player)

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
        self.checkWin(player)

    def checkWin(self, player):
        won = False

        if not won:
            won = self._checkColWin(player)

        if not won:
            won = self._checkRowWin(player)

        if not won:
            won = self._checkDiagULWin(player)

        if not won:
            won = self._checkDiagURWin(player)

        if won:
            self.printWinner(player)

    ############
    # Private  #
    ############

    def _checkRowWin(self, player):
        count = 0
        for row in self.board:
            for token in row:
                if token == player:
                    count = count+1
                else:
                    count = 0
                if count ==4:
                    return True
        return False

    def _checkColWin(self, player):
        count = 0
        for i in range (0, self.columns, 1):
            for row in self.board:
                if row[i] == player:
                    count = count + 1
                else:
                    count = 0
                if count == 4:
                    return True
        return False

    def _checkDiagULWin(self, player):
        for row in range (0, self.rows-3, 1):
            for col in range (0, self.columns-3, 1):
                count = 0
                for n in range (0, 4, 1):
                    if self.board[row+n][col+n] == player:
                        count = count + 1
                    if count == 4:
                        return True
        return False

    def _checkDiagURWin(self, player):
        count = 0
        for row in range(0, self.rows-3, 1):
            for col in range(self.columns-3, 0, -1):
                count = 0
                for n in range (0, 4, 1):
                    if self.board[row+n][col-n] == player:
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