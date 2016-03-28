def main():
    print ("hello world!")
    my_desire = raw_input("What do you desire, friend? ")
    if my_desire == "4 Gewinnt":
        print ("Geil!")
        my_list = initList()
        printList(my_list)
        running = True
        while running:
            print("Spieler 1 ist am Zug!")
            my_list = turn(my_list, 1)
            clear()
            printList(my_list)
            checkWin(my_list, 1)
            print("Spieler 2 ist am Zug!")
            my_list = turn(my_list, 2)
            clear()
            printList(my_list)
            checkWin(my_list, 2)

    else:
        print ("What?")

"""
   Initialize the list for the game "Connect Four"    
"""
def initList():
    my_list = []
    #the ranges should be made by input maybe? or as global variable (easier to change in more complex code)
    for i in range(0, 8, 1):
        sub_list = []
        for j in range(0, 8, 1):
            sub_list.append(0)
        my_list.append(sub_list)
    return my_list

"""
   Print list of the board of game "Connect Four"
"""
def printList(list):
    print " 1  2  3  4  5  6  7  8"
    for i in range (len(list)-1, -1, -1):
        print list[i]
    print

    
"""
   Get input of player to put token in to a column
   What the fuck is this mixture of german and english?
"""    
def turn(list, player):
    try:
        index = input("Where do you want to put your token? ")
        if index < 1:
            raise 0
        for sublist in list:
            if sublist[index-1] == 0:
                sublist[index-1] = player
                return list
    except:
        print "ungueltige Eingabe"
        return turn(list, player)
    print ("An dieser Stelle kann kein Chip platziert werden!")
    return turn(list, player)

"""
   Check win condition for a given board and player
"""    
def checkWin(list, player):
    count = 0
    for sublist in list:
        for token in sublist:
            if token == player:
                count = count+1
            else:
                count = 0
            printWinner(count, player)

    count = 0
    for i in range (0, len(list), 1):
        for sublist in list:
            if sublist[i] == player:
                count = count + 1
            else:
                count = 0
            printWinner(count, player)

    count = 0
    for i in range (0, len(list)-4, 1):
        for j in range (0, len(list)-4, 1):
            for n in range (0, len(list)-max(i, j), 1):
                if list[i+n][j+n] == player:
                    count = count + 1
                else:
                    count = 0
                printWinner(count, player)
            for n in range (0, len(list)-max(i, j), 1):
                if list[j+n][i+n] == player:
                    count = count + 1
                else:
                    count = 0
                printWinner(count, player)

"""
   print winner and exit game
"""                
def printWinner(count, player):
    if count == 4:
        print ("Spieler " + str(player) + " gewinnt!!!")
        print ("!!!Herzlichen Glueckwunsch!!!")
        exit()

"""
   rudimentary clear function
"""        
def clear():
    print(' \n' * 10)
    
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
    

if __name__ == "__main__":
    main()