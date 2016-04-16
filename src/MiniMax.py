from FourWins import GamingBoard

"""
   Here starts the AI to play against.
"""

class MiniMax:
    def __init__(self, depth):
        self.depth = depth

    def minimaxAI(self, list, player):
        print ("analyzing board...")
        ai_list = self.copyList(list)
        value, col = self.max(player, self.depth, ai_list)
        
        for row in range(len(list)-1, -1, -1):
            if list[row][col] == 0:
                list[row][col] = player
                break
            
    """
       max part of the minimax-algorithm
    """
    def max(self, player, depth, list, column=-1):
        if depth == 0:
            return self.score(player, list, column)

        value = -1000
        best_turn = -1

        #for each column check if there is a available turn
        for i in range(0, len(list[0]), 1):
            if list[0][i] != 0:
                #print "DEBUG: column " + str(i) + "is full"
                continue
            index = len(list)-1

            #apply possible turn
            for sublist in list:
                if sublist[index] == 0:
                    sublist[index] = player
                    break
                else:
                    index = index - 1

            #determine next player
            next_player = 0
            if player == 1:
                next_player = 3
            else:
                next_player = 1

            new_value, bin = self.max(next_player, depth-1, list, i)

            if (-new_value) > value:
                value = new_value
                best_turn = index

            #at the end of calculation redo changes
            list[index][i] = 0
            
        return (value, best_turn)

    """
       score of the board passed by list for given player
    """
    def score(self, player, list, column):
        if GamingBoard.checkWin(player, list):
            return 50
        elif self._checkPrevent(player, list, column):
            return 40
        else:
            return 0
        """elif self._checkThree(player, list):
            return 30
        elif self._checkPreventThree(player, list):
            return 20
        elif self._checkTwo(player, list):
            return 10"""

    """
       Copy a list so the AI can apply changes without changing the actual game board
    """
    def copyList(self, list):
        new_list = []
        for i in range(0, len(list), 1):
            sub_list = []
            for j in range(0, len(list[i]), 1):
                sub_list.append(list[i][j])
            new_list.append(sub_list)
        return new_list
    
    
    ##############
    # Private
    ##############
    def _checkPrevent(self, player, list, column):
       
        #determine which row the stone was set in
        row = -1
        for i in range(len(list)-1, -1, -1):
            if list[i][column] == 0:
                row = i+1
        
        if player == 1:
            list[row][column] = 3
        else:
            list[row][column] = 1
            
        tmp = GamingBoard.checkWin(player, list)
        
        #return board to old state
        if player == 1:
            list[row][column] = 1
        else:
            list[row][column] = 3
            
        return tmp
        
if __name__ == "__main__":
    import main
    rows = 6
    columns = 7
    depth = 2
    myBoard = GamingBoard(rows, columns)
    myAI = MiniMax(depth)

    main.printList(myBoard)
    running = True
    while running:
        print("Spieler 1 ist am Zug!")
        main.turn(myBoard, 1)
        main.printList(myBoard)
        print("KI ist am Zug!")
        myAI.minimaxAI(myBoard.board, 3)
        main.printList(myBoard)
