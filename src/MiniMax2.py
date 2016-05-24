# -*- coding: utf-8 -*-

from FourWins import GamingBoard
import copy

class MiniMaxDepth:
    
    def __init__(self, depth):
        self.maxDepth = depth
        
    def getMove(self, board, player):
        print("DEBUG: Analyzing board...")
        copied = copy.deepcopy(board)
        value, col = self._maximize(player, 0, copied)
        
        return col
    
    def _maximize(self, player, depth, board, column=-1):
        
        if((depth >= self.maxDepth) or self._checkBoardFull(board) or self._checkGameOver(board)):
            score = self._score(player, board, column)
            return (score - depth, -1)
        
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
            nextPlayer = 0
            if player == 1: 
                nextPlayer = 3
            else:
                nextPlayer = 1
                
            """
            Calculate best value for the next possible moves
            """
            moveValue, tmp = self._maximize(nextPlayer, (depth+1), board, i)
            
            """ DEBUG OUTPUT """
            if (depth == 0) :
                print (i+1, -moveValue)
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
            self.printBoard(board)
        
        return (bestValue, bestTurn)

    def printBoard(self, board):
        print ("Redo")
        print ("1  2  3  4  5  6  7")
        for i in range (0, 6, 1):
            print (board[i])
        print

    def _checkBoardFull(self, board):
        """
        If one spot is free in the top row the board is not full
        """
        for j in range(0, len(board[0]), 1):
            if board[0][j] == 0:
                return False
    
        return True
    
    def _checkGameOver(self, board):
        won, winningStones = GamingBoard.checkWin(1, board)
        if(won):
            return True
        
        won, winningStones = GamingBoard.checkWin(3, board)
        if(won):
            return True
        
        return False 
    
    def _score(self, player, board, column):
        actPlayer = 3 if player == 1 else 1
        
        won, tmp = GamingBoard.checkWin(actPlayer, board)
        
        if (won):
            return -500
        elif (self._checkPrevent(actPlayer, board, column)):
            return -400
            
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
        