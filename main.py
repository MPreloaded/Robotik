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

def initList():
    my_list = []
    for i in range(0, 8, 1):
        sub_list = []
        for j in range(0, 8, 1):
            sub_list.append(0)
        my_list.append(sub_list)
    return my_list

def printList(list):
    print " 1  2  3  4  5  6  7  8"
    for i in range (len(list)-1, -1, -1):
        print list[i]
    print

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

def printWinner(count, player):
    if count == 4:
        print ("Spieler " + str(player) + " gewinnt!!!")
        print ("!!!Herzlichen Glueckwunsch!!!")
        exit()

def clear():
    print(' \n' * 10)

if __name__ == "__main__":
    main()