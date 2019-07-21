##
#  The Legend of Maui
#  V0.10
## =====----------- Color Module ----------=====
import sys
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")
## =====----------- Map Generation ----------=====
def map_generator_1(option):
    """Generates the stage should go in format [Stage Size] [Player Starting Position]"""
    # Stage Size + Player Starting Position
    STAGE_1 = ([5,5], [1,1])

    # Non-Ocean tiles
    STAGE_1_TILES = {         
        "1,2":"rock",
        "1,3":"mountain",
        "3,3":"rock",
        "4,5":"mountain",
        "5,5":"end"
    }

    # Special Tiles that trigger an event
    STAGE_1_SPECIAL = {       
        "5,5":"end"
    }

    # Decide what data to return
    if option == "stage":
        return STAGE_1
    elif option == "tiles":
        return STAGE_1_TILES
    elif option == "special":
        return STAGE_1_SPECIAL
    else:
        print("Something Broke! map_generator_1")

def tile_set():
    """Contains the data for tiles"""
    TILES = {
        "ocean":"~"
        ,"rock":"R"
        ,"mountain":"M"
        ,"player":"X"
        ,"end":"E"
        }

    return TILES

## =====----------- Turn Processing ----------=====

#  ------------------ Movement -----------------
def movement_processor(stage, player,
                       stage_tiles):
    """Takes input from players to move"""
    player_x = player[0]
    player_y = player[1]

    valid = False
    while not valid:
        movement = input("Enter a movement:").lower()
        # Detect if the movement command is not valid
        if (movement != "up"
            and movement != "down"
                and movement !="right"
                    and movement !="left"):
            print("Please enter a valid command.")

        # Change player's co-ordinates appropriately
        elif movement == "down":
            player_y = player_y - 1
        elif movement == "up":
            player_y = player_y + 1
        elif movement == "right":
            player_x = player_x + 1
        elif movement == "left":
            player_x = player_x - 1

        # Movement validation
        player_new = [player_x, player_y]
        valid = boundary_checker(stage, player_new)
        if valid:
            valid = tile_checker(stage_tiles, player_new)

        # Reset the x and y
        if not valid:
            player_x = player[0]
            player_y = player[1]
    
    return player_new

def boundary_checker(stage, player_new):
    """Checks to see whether movement is would take the player out of bounds"""
    # Go through each possible direction a player can travel
    if player_new[0] == 0:
        valid = False
        color.write("You can't leave the map!\n","ERROR")
    elif player_new[1] == 0:
        valid = False
        color.write("You can't leave the map!\n","ERROR")
    elif player_new[0] > stage[0]:
        valid = False
        color.write("You can't leave the map!\n","ERROR")
    elif player_new[1] > stage[1]:
        valid = False
        color.write("You can't leave the map!\n","ERROR")
    # Flag validity if player still within bounds of map
    else:
        valid = True

    return valid

def tile_checker(stage_tiles,
                 player_new):
    """Checks to see what tile the player would be on"""
    tile = stage_tiles.get("{0},{1}".format(player_new[0], player_new[1]), "ocean")
    #  Check each possible terrain
    if tile == "rock" or tile == "mountain":
        valid = False
        color.write("You can't sail into a {}!\n".format(tile),"ERROR")
    else:
        valid = True

    return valid


def special_condition_checker(special_tiles,
                              player_new):
    """Checks to see whether there is a special condition triggered by the player"""
    tile = special_tiles.get("{0},{1}".format(player_new[0], player_new[1]), None)
    if tile == None: # If theres no special condition on that tile
        return
    elif tile == "end":
        return tile

    
    
## =====----------- UI Elements ----------=====

#  ------------------ Map Gen -----------------
def map_displayer(stage, player,
                  stage_tiles, TILES):
    """Displays the map in the console"""
    color.write("=============================================\n","STRING")  # Hard seperation to show that a new turn has begun
    # Setup variables
    x = 1
    y = stage[1]
    player_x = player[0]
    player_y = player[1]

    while y > 0:
        while x < stage[0]+1:
            if x == player_x and y == player_y:
                color.write(TILES.get("player", "X"), "KEYWORD")
            elif "{0},{1}".format(x, y) in stage_tiles:
                tile = stage_tiles.get("{0},{1}".format(x, y), "ocean")
                color.write(TILES[tile], "stderr")
            else:
                print(TILES["ocean"], end='')
            x += 1
            print(" ",end='')
        print("")
        y -= 1
        x = 1
            
    
    print(player)

def main():
    """Main Routine"""
    # Setup values to be used in current stage
    stage = map_generator_1("stage")
    player = stage[1]
    stage = stage[0]
    stage_tiles = map_generator_1("tiles")
    special = map_generator_1("special")                              
    TILES = tile_set()

    # Menu

    # Intro
    
    # Game Start
    playing = True
    while playing:
        map_displayer(stage,player, stage_tiles, TILES)
        # Print status
        # Ask player for command
        player = movement_processor(stage, player, stage_tiles)
        update = special_condition_checker(special, player)
        if update == "end":
            playing = False
        # Perform post turn actions
    color.write("Thanks for playing!","KEYWORD")

main()
