##
#  The Legend of Maui
#  V0.07

def map_generator_1(option):
    """Generates the stage should go in format [Stage Size] [Player Starting Position]"""
    STAGE_1 = ([5,5],[1,1]) 
    STAGE_1_TILES = {
        "1,2":"rock",
        "1,3":"mountain"}
    if option == "stage":
        return STAGE_1
    elif option == "tiles":
        return STAGE_1_TILES
    else:
        print("Something Broke! map_generator_1")

def tile_set():
    """Contains the data for tiles"""
    TILES = {
        "ocean":"O"
        ,"rock":"V"
        ,"mountain":"W"
        ,"player":"X"
        }
    return TILES

def movement_processor(stage,player,stage_tiles):
    """Takes input from players to move"""
    player_x = player[0]
    player_y = player[1]

    valid = False
    while not valid:
        movement = input("Enter a movement:").lower()
        if (movement != "up"
            and movement != "down"
                and movement !="right"
                    and movement !="left"):
            print("Please enter a valid command.")
        elif movement == "down":
            player_y = player_y - 1
        elif movement == "up":
            player_y = player_y + 1
        elif movement == "right":
            player_x = player_x + 1
        elif movement == "left":
            player_x = player_x - 1

        player_new = [player_x,player_y]
        valid = movement_checker(stage,player_new)
        #  reset the x and y
        if not valid:
            player_x = player[0]
            player_y = player[1]
    
    return player_new

def movement_checker(stage,player_new):
    """Checks to see whether movement is valid"""
    if player_new[0] == 0:
        valid = False
        print("No")
    elif player_new[1] == 0:
        valid = False
        print("No")
    elif player_new[0] > stage[0]:
        valid = False
        print("No")
    elif player_new[1] > stage[1]:
        valid = False
        print("No")
    else:
        valid = True
        print("Yes")
    return valid
    
        

def map_displayer(stage,player,stage_tiles,TILES):
    """Displays the map in the console"""
    print("=============================================")
    x = 1
    y = stage[1]
    player_x = player[0]
    player_y = player[1]
    while y > 0:
        while x < stage[0]+1:
            if x == player_x and y == player_y:
                print(TILES.get("player","X"), end='')
            elif "{0},{1}".format(x,y) in stage_tiles:
                tile = stage_tiles.get("{0},{1}".format(x,y),"ocean")
                print(TILES[tile],end='')
            else:
                print('O', end='')
            x += 1
        print("")
        y-=1
        x= 1
            
    
    print(player)

def main():
    """Main Routine"""
    stage = map_generator_1("stage")
    player = stage[1]
    stage = stage[0]
    stage_tiles = map_generator_1("tiles")
    
    TILES = tile_set()

    playing = True
    while playing:
        map_displayer(stage,player,stage_tiles,TILES)
        player = movement_processor(stage,player,stage_tiles)
    pass

main()
