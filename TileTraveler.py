#First create the tile map from 1,1 to 3,3
#Make possible moves for each tile
#request input for direction
#respond to that input.(if it is not a valid input re-request input)
#If player reaches 3,1 print victory! and exit program

#for i in range(1,4):
#    for j in range(1,4):

x = 1
y = 1

while (x,y) != (3,1):
    if (x,y) == (1,1) or (x,y) == (2,1):
        print("You can travel: (N) orth.")
        valid_direction = "n" or "N"
        Direction = str(input("Directions: "))
        if Direction == valid_direction:
            y += 1
        else:
            print("Not a valid direction!")
    elif (x,y) == (1,2):
        print("You can travel: (N) orth or (S) outh or (E) ast.")
        Direction = str(input("Directions: "))
        if Direction == "n" or "N":
            y += 1
        elif Direction == "s" or "S":
            y -= 1
        elif Direction == "e" or "E":
            x += 1
        else:
            print("Not a valid direction!")
    elif (x,y) == (2,2) or (x,y) == (3,3):
        print("You can travel: (W) est or (S) outh.")
        Direction = str(input("Directions: "))
        if Direction == "s" or "S":
            y -= 1
        elif Direction == "w" or "W":
            x -= 1
        else:
            print("Not a valid direction!")
    elif (x,y) == (1,3):
        print("You can travel: (E) ast or (S) outh.")
        Direction = str(input("Directions: "))
        if Direction == "e" or "E":
            x += 1
        elif Direction == "s" or "S":
            y -= 1
        else:
            print("Not a valid direction!")
    elif (x,y) == (2,3):
        print("You can travel: (W) est or (E) ast.")
        Direction = str(input("Directions: "))
        if Direction == "e" or "E":
            x += 1
        elif Direction == "w" or "W":
            x -= 1
        else:
            print("Not a valid direction!")
    elif (x,y) == (3,2):
        print("You can travel: (N) orth or (S) outh.")
        Direction = str(input("Directions: "))
        if Direction == "s" or "S":
            y -= 1
        elif Direction == "n" or "N":
            y += 1
        else:
            print("Not a valid direction!")

#        if (Direction == str("n") or Direction == str("N")) and valid_direction == "n":
#            player_location = (x+0,y+1)
#        elif (Direction == str("s") or Direction == str("S")) and valid_direction == "s":
#            player_location = (x+0,y-1)
#        elif (Direction == str("e") or Direction == str("E")) and valid_direction == "e":
#            player_location = (x+1,y+0)
#        elif (Direction == str("w") or Direction == str("W")) and valid_direction == "w":
#            player_location = (x-1,y+0)
else:
    print("Victory!")
    exit



