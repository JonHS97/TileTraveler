#1. The second implementation is easier because the ability to use functions reduces the amount of work you have to do for less effort.
#2. The second implementation is more readable because functions allow you to store a set code to be used multiple times which reduces the amount of text you need.
#3. The only problem I think I had was that my code was sloppy and really long. By using functions I am able to make my code neater and easier to read.

#First create the tile map from 1,1 to 3,3
#Make possible moves for each tile
#request input for direction
#respond to that input.(if it is not a valid input re-request input)
#If player reaches 3,1 print victory! and exit program

#I ran out of time to properly implement all the functions I wanted but I atleast managed to solve the problem and tune it a little bit.

def printing(x,y):
    if (x,y) == (1,1) or (x,y) == (2,1):
        print("You can travel: (N)orth.")
    elif (x,y) == (1,2):
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif (x,y) == (2,2) or (x,y) == (3,3):
        print("You can travel: (S)outh or (W)est.")
    elif (x,y) == (1,3):
        print("You can travel: (E)ast or (S)outh.")
    elif (x,y) == (2,3):
        print("You can travel: (E)ast or (W)est.")
    elif (x,y) == (3,2):
        print("You can travel: (N)orth or (S)outh.")
    return(x,y)

def move(x,y):#didnt finish this. Was going to make a function that I could use to allways add or subtract the correct amount of x and y based on the input
    valid_direction = valid_directs(x,y)
    Direction = str(input("Direction: "))
    if (Direction == "n" or Direction == "N") and (Direction in list(valid_direction)):
        (x,y) = (x,y+1)
        printing(x,y)
    elif (Direction == "s" or Direction == "S") and (Direction in list(valid_direction)):
        (x,y) = (x,y-1)
        printing(x,y)
    elif (Direction == "e" or Direction == "E") and (Direction in list(valid_direction)):
        (x,y) = (x+1,y)
        printing(x,y)
    elif (Direction == "w" or Direction == "W") and (Direction in list(valid_direction)):
        (x,y) = (x-1,y)
        printing(x,y)
    elif Direction != valid_direction:
        print("Not a valid direction!")
    return(x,y)

def valid_directs(x,y): #not sure how to fix this. Was supposed to replace valid_direction in all the if statements.
    if (x,y) == (1,1) or (x,y) == (2,1):
        valid_direction = ("n","N")
    elif (x,y) == (1,2):
        valid_direction = ("n","N","s","S","e","E")
    elif (x,y) == (1,3):
        valid_direction = ("e","E","s","S")
    elif (x,y) == (2,2) or (x,y) == (3,3):
        valid_direction = ("s","S","w","W")
    elif (x,y) == (2,3):
        valid_direction = ("e","E","w","W")
    elif (x,y) == (3,2):
        valid_direction = ("s","S","n","N")
    return(valid_direction)

x = 1
y = 1

printing(x,y)

while (x,y) != (3,1):
    if (x,y) == (1,1):
        move(x,y)
        #valid_direction = ("n","N")
        #Direction = str(input("Direction: "))
        #if Direction in list(valid_direction):
        #    y += 1
        #    printing(x,y)
        #elif Direction != valid_direction:
        #    print("Not a valid direction!")
    if (x,y) == (2,1):
        move(x,y)
        #valid_directs(x,y)
        #valid_direction = ("n","N")
        #Direction = str(input("Direction: "))
        #if Direction in list(valid_direction):
        #    y += 1
        #    printing(x,y)
        #elif Direction != valid_direction:
        #    print("Not a valid direction!")
    elif (x,y) == (1,2):
        move(x,y)
        #valid_directs(x,y)
        #valid_direction = ("n","N","s","S","e","E")
        #Direction = str(input("Direction: "))
        #if (Direction == "n" or Direction == "N") and (Direction in list(valid_direction)):
        #    y += 1
        #    printing(x,y)
        #elif (Direction == "s" or Direction == "S") and (Direction in list(valid_direction)):
        #    y -= 1
        #    printing(x,y)
        #elif (Direction == "e" or Direction == "E") and (Direction in list(valid_direction)):
        #    x += 1
        #    printing(x,y)
        #elif Direction != valid_direction:
        #    print("Not a valid direction!")
    elif (x,y) == (2,2):
        move(x,y)
        #valid_directs(x,y)
        #valid_direction = ("s","S","w","W")
        #Direction = str(input("Direction: "))
        #if (Direction == "s" or Direction == "S") and (Direction in list(valid_direction)):
        #    y -= 1
        #    printing(x,y)
        #elif (Direction == "w" or Direction == "W") and (Direction in list(valid_direction)):
        #    x -= 1
        #    printing(x,y)
        #elif Direction != valid_direction:
        #    print("Not a valid direction!")
    elif (x,y) == (3,3):
        move(x,y)
        #valid_directs(x,y)
        #valid_direction = ("s","S","w","W")
        #Direction = str(input("Direction: "))
        #if (Direction == "s" or Direction == "S") and (Direction in list(valid_direction)):
        #    y -= 1
        #    printing(x,y)
        #elif (Direction == "w" or Direction == "W") and (Direction in list(valid_direction)):
        #    x -= 1
        #    printing(x,y)
        #elif Direction != valid_direction:
        #    print("Not a valid direction!")
    elif (x,y) == (1,3):
        move(x,y)
        #valid_directs(x,y)
        #valid_direction = ("e","E","s","S")
        #Direction = str(input("Direction: "))
        #if (Direction == "e" or Direction == "E") and (Direction in list(valid_direction)):
        #    x += 1
        #    printing(x,y)
        #elif (Direction == "s" or Direction == "S") and (Direction in list(valid_direction)):
        #    y -= 1
        #    printing(x,y)
        #elif Direction != valid_direction:
        #    print("Not a valid direction!")
    elif (x,y) == (2,3):
        move(x,y)
        #valid_directs(x,y)
        #valid_direction = ("e","E","w","W")
        #Direction = str(input("Direction: "))
        #if (Direction == "e" or Direction == "E") and (Direction in list(valid_direction)):
        #    x += 1
        #    printing(x,y)
        #elif (Direction == "w" or Direction == "W") and (Direction in list(valid_direction)):
        #    x -= 1
        #    printing(x,y)
        #elif Direction != valid_direction:
        #    print("Not a valid direction!")
    elif (x,y) == (3,2):
        move(x,y)
        #valid_directs(x,y)
        #valid_direction = ("s","S","n","N")
        #Direction = str(input("Direction: "))
        #if (Direction == "s" or Direction == "S") and (Direction in list(valid_direction)):
        #    y -= 1
        #elif (Direction == "n" or Direction == "N") and (Direction in list(valid_direction)):
        #    y += 1
        #    printing(x,y)
        #elif Direction != valid_direction:
        #    print("Not a valid direction!")
else:
    print("Victory!")
    exit



