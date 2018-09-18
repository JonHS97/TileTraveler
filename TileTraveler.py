#First create the tile map from 1,1 to 3,3
#Make possible moves for each tile
#request input for direction
#respond to that input.(if it is not a valid input re-request input)
#If player reaches 3,1 print victory! and exit program

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

x = 1
y = 1

print("You can travel: (N)orth.")

while (x,y) != (3,1):
    if (x,y) == (1,1):
        valid_direction = ("n","N")
        Direction = str(input("Direction: "))
        if Direction in list(valid_direction):
            y += 1
            printing(x,y)
        elif Direction != valid_direction:
            print("Not a valid direction!")
    if (x,y) == (2,1):
        valid_direction = ("n","N")
        Direction = str(input("Direction: "))
        if Direction in list(valid_direction):
            y += 1
            print("You can travel: (S)outh or (W)est.")
        elif Direction != valid_direction:
            print("Not a valid direction!")
    elif (x,y) == (1,2):
        valid_direction = ("n","N","s","S","e","E")
        Direction = str(input("Direction: "))
        if (Direction == "n" or Direction == "N") and (Direction in list(valid_direction)):
            y += 1
            print("You can travel: (E)ast or (S)outh.")
        elif (Direction == "s" or Direction == "S") and (Direction in list(valid_direction)):
            y -= 1
            print("You can travel: (N)orth.")
        elif (Direction == "e" or Direction == "E") and (Direction in list(valid_direction)):
            x += 1
            print("You can travel: (S)outh or (W)est.")
        elif Direction != valid_direction:
            print("Not a valid direction!")
    elif (x,y) == (2,2):
        valid_direction = ("s","S","w","W")
        Direction = str(input("Direction: "))
        if (Direction == "s" or Direction == "S") and (Direction in list(valid_direction)):
            y -= 1
            print("You can travel: (N)orth.")
        elif (Direction == "w" or Direction == "W") and (Direction in list(valid_direction)):
            x -= 1
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        elif Direction != valid_direction:
            print("Not a valid direction!")
    elif (x,y) == (3,3):
        valid_direction = ("s","S","w","W")
        Direction = str(input("Direction: "))
        if (Direction == "s" or Direction == "S") and (Direction in list(valid_direction)):
            y -= 1
            print("You can travel: (N)orth or (S)outh.")
        elif (Direction == "w" or Direction == "W") and (Direction in list(valid_direction)):
            x -= 1
            print("You can travel: (E)ast or (W)est.")
        elif Direction != valid_direction:
            print("Not a valid direction!")
    elif (x,y) == (1,3):
        valid_direction = ("e","E","s","S")
        Direction = str(input("Direction: "))
        if (Direction == "e" or Direction == "E") and (Direction in list(valid_direction)):
            x += 1
            print("You can travel: (E)ast or (W)est.")
        elif (Direction == "s" or Direction == "S") and (Direction in list(valid_direction)):
            y -= 1
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        elif Direction != valid_direction:
            print("Not a valid direction!")
    elif (x,y) == (2,3):
        valid_direction = ("e","E","w","W")
        Direction = str(input("Direction: "))
        if (Direction == "e" or Direction == "E") and (Direction in list(valid_direction)):
            x += 1
            print("You can travel: (S)outh or (W)est.")
        elif (Direction == "w" or Direction == "W") and (Direction in list(valid_direction)):
            x -= 1
            print("You can travel: (E)ast or (S)outh.")
        elif Direction != valid_direction:
            print("Not a valid direction!")
    elif (x,y) == (3,2):
        valid_direction = ("s","S","n","N")
        Direction = str(input("Direction: "))
        if (Direction == "s" or Direction == "S") and (Direction in list(valid_direction)):
            y -= 1
        elif (Direction == "n" or Direction == "N") and (Direction in list(valid_direction)):
            y += 1
            print("You can travel: (S)outh or (W)est.")
        elif Direction != valid_direction:
            print("Not a valid direction!")
else:
    print("Victory!")
    exit



