#1. The second implementation is easier because the ability to use functions makes creating the code a lot easier.
#2. The second implementation is more readable because functions allow you to store a set code to be used multiple times which reduces the amount of text you need.
#3. I was able to make a really clean and tidy code with clear information about each function which I was unable to do in the first implementation.

#First create the tile map from 1,1 to 3,3
#Make possible moves for each tile
#request input for direction
#respond to that input.(if it is not a valid input re-request input)
#If player reaches 3,1 print victory! and exit program

def printing(x,y):#Function that prints out the players movement choices depending on what tile he is on
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

def valid_directs(x,y):#Function that changes the allowed input by the user depending on what tile the character is
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

def moving(x,y):#Function that takes in user input for direction to move character and applies the results
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

def execute_code():#Main function that runs the whole game from start to finish
    x = 1
    y = 1
    printing(x,y)
    while (x,y) != (3,1):
        if (x,y) == (1,1):
            (x,y) = moving(1,1)
        if (x,y) == (2,1):
            (x,y) = moving(2,1)
        elif (x,y) == (1,2):
            (x,y) = moving(1,2)
        elif (x,y) == (2,2):
            (x,y) = moving(2,2)
        elif (x,y) == (3,3):
            (x,y) = moving(3,3)
        elif (x,y) == (1,3):
            (x,y) = moving(1,3)
        elif (x,y) == (2,3):
            (x,y) = moving(2,3)
        elif (x,y) == (3,2):
            (x,y) = moving(3,2)
    else:
        print("Victory!")
        exit

execute_code()#Runs the game