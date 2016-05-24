from FourWins import GamingBoard

"""
   Here starts the AI to play against.
"""

class MiniMax:
    def __init__(self):
        pass

    def minimaxAI(self, list, player):
        print ("analyzing board...")
        ai_list = self.copyList(list)
        value, col = self.max(player, 0, ai_list)
        
        return col
            
    """
       max part of the minimax-algorithm
    """
    def max(self, player, depth, list, column=-1):
        """
        Die Abbruchbedingungen sind:
         - Board voll
         - Einer der Spieler hat gewonnen
        Sollte eine (oder mehrere) der Abbruchbedingungen eintreten, so 
        soll das Board bewertet werden und der Wert zurückgegeben werden.
        
        Für eine bessere KI muss hierbei auch die Suchtiefe mitgegeben werden.
        Dies sorgt dafür, dass die KI auch bei einem aussichtslosen Board (wie es beispielsweise
        anfangs der Fall sein kann) immer noch bestmöglich spielt, und versucht möglichst lange
        zu "überleben".
        """
        if (self._checkListFull(list) or self._checkGameOver(list)):
            print ("End of analyzing one path")
            return (self.score(player, list, column) + depth , -1)

        value = -1000
        best_turn = -1

        #for each column check if there is a available turn
        for i in range(0, len(list[0]), 1):
            if list[0][i] != 0:
                #print "DEBUG: column " + str(i) + "is full"
                continue
            index = len(list[0])-1

            #apply possible turn
            for sublist in list:
                if sublist[i] == 0:
                    sublist[i] = player
                    break
                else:
                    index = index - 1

            #determine next player
            next_player = 0
            if player == 1:
                next_player = 3
            else:
                next_player = 1

            new_value, bin = self.max(next_player, (depth+1), list, i)

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
        won, winningStones = GamingBoard.checkWin(player,list)
        if won:
            return 100
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
            
        tmp, winningStones = GamingBoard.checkWin(player, list)
        
        #return board to old state
        if player == 1:
            list[row][column] = 1
        else:
            list[row][column] = 3
            
        return tmp
    
    def _checkListFull(self, list):
        # If one column has the top spot free the board is not full
        for j in range(0, len(list[0])-1, 1):
            if list[0][j] == 0:
                return False
    
        return True
    
    def _checkGameOver(self, list):
        won, winningStones = GamingBoard.checkWin(1, list)
        if(won):
            return True
        
        won, winningStones = GamingBoard.checkWin(3, list)
        if(won):
            return True
        
        return False    
        
