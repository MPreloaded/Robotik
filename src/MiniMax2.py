# -*- coding: utf-8 -*-

from FourWins import GamingBoard
import copy
import random

class MiniMaxDepth:
    
    def __init__(self, depth):
        self.maxDepth = depth
        
    def getMove(self, board, player):
        print("DEBUG: Analyzing board...")
        copied = copy.deepcopy(board)
                    
        values = {}            
        for i in range(0, len(copied[0]), 1):
            if copied[0][i] != 0:
                continue
            
            nextPlayer = 3 if player == 1 else 1
            
            row = -1
            for j in range(len(copied)-1, -1, -1):
                if copied[j][i] == 0:
                    copied[j][i] = player
                    row= j
                    break
            
            value = self._maximize(nextPlayer, 1, copied, i)
            
            print (i+1, value)
            
            values[i] = value
            
            copied[j][i] = 0        
        
        bestValue = -1000
        bestTurns = []
        for i in values.keys():
            if -values[i] > bestValue:
                bestTurns = []
                bestValue = -values[i]
                bestTurns.append(i)
            elif -values[i] == bestValue:
                bestTurns.append(i)
        
        r = random.randint(0, len(bestTurns)-1)
        
        col = bestTurns[r]
        
        return col
    
    def _maximize(self, player, depth, board, column):
        
        if((depth >= self.maxDepth) or self._checkBoardFull(board) or self._checkGameOver(board, player)):
            lastPlayer = 1 if player == 3 else 3
            score = self._score(lastPlayer, board, column)
            return (-score - depth)
        
        bestValue = -1000
        bestTurn = -1
        
        for i in range(0, len(board[0]), 1) :
            """
            Determine if this column is already full
            """
            if board[0][i] != 0:
                continue
            
            """
            Place token in lowest possible slot, save slot in "index"
            """
            index = -1
            for j in range(len(board)-1, -1, -1):
                if board[j][i] == 0:
                    board[j][i] = player
                    index = j
                    break
            
            """
            Determine next player
            """
            nextPlayer = 3 if player == 1 else 1
                
            """
            Calculate best value for the next possible moves
            """
            moveValue = self._maximize(nextPlayer, (depth+1), board, i)
            
            """
            Check whether move value is better or worse
            """
            if (-moveValue) > bestValue:
                bestValue = (-moveValue)
                bestTurn = i 
                
            """
            Redo changes to the board for the next loop iteration
            """
            board[index][i] = 0

        return (bestValue, bestTurn)

    def printBoard(self, board):
        print ("Redo")
        print ("1  2  3  4  5  6  7")
        for i in range (0, 6, 1):
            print (board[i])
        print


    def _checkBoardFull(self, board):
        """
        If at least one spot is free in the top row the board is not full
        """
        for j in range(0, len(board[0]), 1):
            if board[0][j] == 0:
                return False
    
        return True
    
    def _checkGameOver(self, board, player):
        lastPlayer = 3 if player == 1 else 1
        
        won, winningStones = GamingBoard.checkWin(lastPlayer, board)
        if(won):
            return True
        
        return False 
    
    def _score(self, player, board, column):        
        won, tmp = GamingBoard.checkWin(player, board)
        
        if (won):
            return 500
        elif (self._checkPrevent(player, board, column)):
            return 400
            
        return 0
        
    def _checkPrevent(self, player, board, column):
       
        #determine which row the stone was set in
        row = -1
        for i in range(len(board)-1, -1, -1):
            if board[i][column] == 0:
                row = i+1
                break
            
        if row == -1:
            row = len(board)-1
        
        if player == 1:
            board[row][column] = 3
        else:
            board[row][column] = 1
            
        otherP = 3 if player == 1 else 1
            
        prevented, tmp = GamingBoard.checkWin(otherP, board)
        
        #return board to old state
        board[row][column] = player
            
        return prevented
    
    def _printBoard(self, board):
        
        for i in range (0, len(board), 1):
            print (board[i])
        print ("")