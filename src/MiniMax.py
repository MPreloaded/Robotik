"""
   Here starts the AI to play against.
"""
def minimaxAI(list, player):
    print "analyzing board..."
    ai_list = copyList(list)    
    
    value = max(player, 10, ai_list)
        

"""
   min part of the minimax-algorithm
"""
def min(player, depth, list):
    if depth == 0:
        return score(player, list)
    
    value = 1000
    
    #for each column check if there is a available turn
    for i in range(0, len(list[0]), 1):
        if list[len(list)-1][i] != 0:
            print "DEBUG: column " + str(i) + "is full"
            continue
        index = 0
        
        #apply possible turn
        for sublist in list:
            if sublist[index] == 0:
                sublist[index] = player
			else 
			    index++
        
        #determine next player
        next_player = 0
        if player == 1:
            next_player = 2
        else
            next_player = 1
        
        new_value = max(next_player, depth-1, list)
        
        if new_value < value:
            value = new_value
            best_turn = index
        
        #at the end of calculation redo changes
        list[index][i] = 0

"""
   max part of the minimax-algorithm
"""
def max(player, depth, list):
    if depth == 0:
        return score(player, list)
    
    value = -1000
    
    #for each column check if there is a available turn
    for i in range(0, len(list[0]), 1):
        if list[len(list)-1][i] != 0:
            print "DEBUG: column " + str(i) + "is full"
            continue
        index = 0
        
        #apply possible turn
        for sublist in list:
            if sublist[index] == 0:
                sublist[index] = player
			else 
			    index++
        
        #determine next player
        next_player = 0
        if player == 1:
            next_player = 2
        else
            next_player = 1
        
        new_value = min(next_player, depth-1, list)
        
        if new_value > value:
            value = new_value
            best_turn = index
        
        #at the end of calculation redo changes
        list[index][i] = 0
    
"""
   score of the board passed by list for given player
"""
def score(player, list):
    pass

"""
   Copy a list so the AI can apply changes without changing the actual game board
"""
def copyList(list):
    new_list = []
    for i in range(0, len(list), 1):
        sub_list = []
        for j in range(0, len(list[i]), 1):
            sub_list.append(list[i][j])
        new_list.appemd(subList)
    return new_list