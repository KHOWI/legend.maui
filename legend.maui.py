##
#  The Legend of Maui
#  V0.11
## =====----------- Color Module ----------=====
import time
import sys
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")

## =====----------- Menu/Intro ----------=====
def intro():
    color.write("A new dawn breaks the crest of the sea")
    intro_dots()
    color.write("The mighty sea rises, and from the depths a new hero arises")
    intro_dots()
    color.write("The era of man has begun")
    intro_dots()
    color.write("Awaken, and discover")
    intro_dots()
    time.sleep(1)
    color.write("The Legend of Maui!\n","ERROR")
    time.sleep(2)
    color.write("""
   _____                __ 
  /     \ _____   __ __|__|
 /  \ /  \\\__  \ |  |  \  |
/    Y    \/ __ \|  |  /  |
\____|__  (____  /____/|__|
        \/     \/          \n""")
    time.sleep(0.5)
    color.write("   Press ENTER to begin!","KEYWORD")
    input()
    print("For right now R is Rock, M is mountain, E is End and X is you")

def intro_dots():
    i = 0
    time.sleep(0.6)
    while i != 3:
        color.write(".")
        time.sleep(0.6)
        i += 1
    print("")

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
def command_processor():
    """Processes commands based on keyowrds that the user has entered"""
    MOVEMENT = ["up","right","down","left","north","west","east","south"]
    FISHING = ["fish","fishing"]
    
    validity = 0
    while validity == 0:
        command = []
        action = input("Enter a command").lower()
        action = ' ' + action + ' '
        for direction in MOVEMENT:
            if direction in action:
                command.append('movement')
                command.append(direction)
                validity += 1

        for fish in FISHING:
            if fish in action:
                command.append('fishing')
                command.append(fish)
                validity +=1

        if validity > 1:
            print("Please type less keywords")
            validity = 0
        elif validity == 1:
            return command
        elif validity == 0:
            print("PLEASE TYPE A KEYWORD")
    

#  ------------------ Movement -----------------
def movement_processor(stage, player,
                       stage_tiles,command):
    """Takes input from players to move"""
    player_x = player[0]
    player_y = player[1]
    movement = command[1].strip().lower()

    # Change player's co-ordinates appropriately
    if movement == "down" or movement == "south":
        player_y = player_y - 1
    elif movement == "up" or movement == "north":
        player_y = player_y + 1
    elif movement == "right" or movement == "east":
        player_x = player_x + 1
    elif movement == "left" or movement == "west":
        player_x = player_x - 1

    # Movement validation
    player_new = [player_x, player_y]
    valid = boundary_checker(stage, player_new)
    if valid:
        valid = tile_checker(stage_tiles, player_new)
        
    # Reset the program
    if not valid:
        player_new = player
        player_new.append(False)
    else:
        player_new.append(True)   
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

def main():
    """Main Routine"""
    # Setup values to be used in current stage
    stage = map_generator_1("stage")
    player = stage[1]
    stage = stage[0]
    stage_tiles = map_generator_1("tiles")
    special = map_generator_1("special")                              
    TILES = tile_set()
    FISH = []

    # Menu

    # Intro
    intro() # Delete this to skip intro for now
    # Game Start
    playing = True
    while playing:
        map_displayer(stage,player, stage_tiles, TILES)
        # Print status
        # Ask player for command
        turn = True
        while turn:
            command = command_processor()
            # If player
            if command[0] == 'movement':
                player = movement_processor(stage, player, stage_tiles, command)
                if player[2] == True:
                    update = special_condition_checker(special, player)
                    if update == "end":
                        playing = False
                    turn = False
                    del player[-1]

                elif player[2] == False:
                    del player[-1]
                else:
                    print("Something crititcal has occured within the movement processcer")
                    del player[-1]
                    
            elif command[0] == 'fishing':
                print("Fishing time i havent actually developed this yet lol soz")
                turn = False
            else:
                print("Beep Boop")
        # Perform post turn actions
    color.write("Thanks for playing!","KEYWORD")

main()
