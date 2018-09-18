#First create the tile map from 1,1 to 3,3
#Make possible moves for each tile
#request input for direction
#respond to that input.(if it is not a valid input re-request input)
#If player reaches 3,1 print victory! and exit program

#for i in range(1,4):
#    for j in range(1,4):

x = 1
y = 1
player_start = (x,y)

player_location = player_start

while player_location != (3,1):
    if player_location == (1,1) or player_location == (2,1):
        print("You can travel: (N) orth.")
        valid_direction = "n"
        Direction = str(input("Directions: "))
    elif player_location == (1,2):
        print("You can travel: (N) orth or (S) outh or (W) est.")
        valid_direction = "n" "s" "w"
        Direction = str(input("Directions: "))
    elif player_location == (2,2) or player_location == (3,3):
        print("You can travel: (W) est or (S) outh.")
        valid_direction = "w" "s"
        Direction = str(input("Directions: "))
    elif player_location == (1,3):
        print("You can travel: (E) ast or (S) outh.")
        valid_direction = "e" "s"
        Direction = str(input("Directions: "))
    elif player_location == (2,3):
        print("You can travel: (W) est or (E) ast.")
        valid_direction = "w" "e"
        Direction = str(input("Directions: "))
    elif player_location == (3,2):
        print("You can travel: (N) orth or (S) outh.")
        valid_direction = "n" "s"
        Direction = str(input("Directions: "))

    while (Direction == valid_direction):
        if (Direction == str("n") or Direction == str("N")) and valid_direction == "n":
            player_location = (x+0,y+1)
        elif (Direction == str("s") or Direction == str("S")) and valid_direction == "s":
            player_location = (x+0,y-1)
        elif (Direction == str("e") or Direction == str("E")) and valid_direction == "e":
            player_location = (x+1,y+0)
        elif (Direction == str("w") or Direction == str("W")) and valid_direction == "w":
            player_location = (x-1,y+0)
    else:
        print("Not a valid direction!")
        Direction = str(input("Directions: "))
else:
    print("Victory!")
    exit



