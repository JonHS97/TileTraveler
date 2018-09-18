#First create the tile map from 1,1 to 3,3
#Make possible moves for each tile
#request input for direction
#respond to that input.(if it is not a valid input re-request input)
#If player reaches 3,1 print victory! and exit program

for i in range(1,4):
    for j in range(1,4):
        print(i,j)

player_start = (1,1)

player_location = player_start

if player_location == (1,1) or player_location == (2,1):
    print("You can travel: (N) orth.")
    Direction = str(input("Directions: "))
elif player_location == (1,2):
    print("You can travel: (N) orth or (S) outh or (W) est.")
    Direction = str(input("Directions: "))
elif player_location == (2,2) or player_location == (3,3):
    print("You can travel: (W) est or (S) outh.")
    Direction = str(input("Directions: "))
elif player_location == (1,3):
    print("You can travel: (E) ast or (S) outh.")
    Direction = str(input("Directions: "))
elif player_location == (2,3):
    print("You can travel: (W) est or (E) ast.")
    Direction = str(input("Directions: "))
elif player_location == (3,2):
    print("You can travel: (N) orth or (S) outh.")
    Direction = str(input("Directions: "))
else:
    print("Victory!")
    exit