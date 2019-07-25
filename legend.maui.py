##
#  The Legend of Maui
#  V0.12
## =====----------- Color Module ----------=====
import os
import time
import sys
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")
class PlayerWin(Exception): pass
        
class PlayerStarve(Exception): pass

## =====----------- Menu/Sequences ----------=====
def intro():
    """Intro Sequence"""
    color.write("A new dawn breaks the crest of the sea")
    intro_dots()
    color.write("The mighty sea beckons, and from the depths a new hero arises")
    intro_dots()
    color.write("Now is the time of man, and your people need a land in which to thrive")
    intro_dots()
    color.write("Awaken, and discover Aotearoa as you begin")
    intro_dots()
    time.sleep(1)
    color.write("The Legend of Māui!\n","ERROR")
    time.sleep(2)
    color.write("""
                                                        
     ______  _______          ____    ____   ____  ____ 
    |      \/       \    ____|\   \  |    | |    ||    |
   /          /\     \  /    /\    \ |    | |    ||    |
  /     /\   / /\     ||    |  |    ||    | |    ||    |
 /     /\ \_/ / /    /||    |__|    ||    | |    ||    |
|     |  \|_|/ /    / ||    .--.    ||    \_/    ||    |
|     |       |    |  ||    |  |    ||           ||    |
|\____\       |____|  /|____|  |____||\__________||____|
| |    |      |    | / |    |  |    || |         ||    |
 \|____|      |____|/  |____|  |____| \|_________||____|
    \(          )/       \(      )/      \(   )/    \(  
     '          '         '      '        '   '      '  
                                                        
\n""")
    time.sleep(0.5)
    color.write("                 Press ENTER to begin!","KEYWORD")
    input()
    print("\nWelcome Māui,")

def intro_dots():
    """Prints the dots in the intro sequence"""
    i = 0
    time.sleep(0.6)
    while i != 3:
        color.write(".")
        time.sleep(0.6)
        i += 1
    print("")

def ending(type):
    
    if type == "win":
        time.sleep(1)
        color.write("""
                    -                                  
                    \ \                               
                    /    \                            
                     \    \                            
                      \    \                               
                       \   /                           
                        `  \                           
                         |  \                         
                         |   \                         
                         |     \  ||                   
                         |      | ||                   
                         |          \                  
                        /             \                
                        |               \    ---\      
                       /                  -/     |     
                      -                         /      
                    /                         /
                /                            |
               |                             |    
                \ -                      / - -    
                    \                 |           
                      \                \          
                       \               /          
                        |           /             
                       /          /               
                      /        /                  
                      |      /                    
                      |    /                      
                      \_ _/\n""")
        color.write("You've fished up the North Island! Thanks for playing!","KEYWORD")
    elif type == "starve":
        color.write("lol you starved to death")
        exit()
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
    MOVEMENT = ["up","right","down","left","north","west","east","south","u","r","l","d"]
    FISHING = ["fish","fishing"," f "]
    HELP = ["help"," h "]
    EAT = ["eat","eating","refuel","nom","e"]
    
    validity = 0
    while validity == 0:
        command = []
        action = input("Enter a command").lower()
        action = ' ' + action + ' '
        for direction in MOVEMENT:
            direction = ' ' + direction + ' '
            if direction in action:
                command.append('movement')
                command.append(direction)
                validity += 1

        for fish in FISHING:
            fish = ' ' + fish + ' '
            if fish in action:
                command.append('fishing')
                command.append(fish)
                validity +=1

        for help in HELP:
            help = ' ' + help + ' '
            if help in action:
                command.append("help")
                validity += 1

        for eat in EAT:
            eat = ' ' + eat + ' '
            if eat in action:
                command.append("eat")
                validity += 1
        

        if validity > 1:
            print("Please type less keywords")
            validity = 0
        elif validity == 1:
            return command
        elif validity == 0:
            print("PLEASE TYPE A KEYWORD")

def help_module():
    helping = True
    color.write("Hello! Welcome to the Legend of Maui! ")
    while helping:
        query = input("Enter the number of the subject you need help with")
        if query == "":
            helping = False
#  ------------------ Fishing/Hunger -----------------
def fishing_processor():
    """Process fishing"""
    pass

def hunger_processor(turn,hunger):
    """Process hunger per turn"""
    hunger -= 1


    if hunger <= 0:
        pass
    elif hunger > 6:
        color.write("wait how","ERROR")
    elif hunger == 4:
        color.write("You begin to feel peckish","KEYWORD")
    elif hunger == 3:
        color.write("You feel hungry.","ERROR")
    elif hunger == 2:
        color.write("You feel hungry. You should probably eat soon","ERROR")
    elif hunger == 1:
        color.write("The throes of hunger stab at your being as your strength leaves you. You should definitely eat something.","ERROR")
    print("")
    
    return hunger

def replenishment_processor(fish,hunger):
    zip = []
    zip.append(fish - 1)
    zip.append(6)

    if hunger > 3:
        print("You eat a fish from your reserve, leaving you with {} left.".format(fish - 1))

    elif hunger > 1:
        print("You gobble down a fish from your reserve, leaving you with {} left.".format(fish - 1))

    elif hunger > 0:
        print("The taste of fish has never seemed so good as you devour one. You have {} left.".format(fish - 1))

    elif hunger >= 0:
        print("Somehow, you have survived at the brink of death. You vicously gobble down a fish, leaving you with {} left.".format(fish - 1))

    print("\n")

    return zip


#  ------------------ Movement -----------------
def movement_processor(stage, player,
                       stage_tiles,command):
    """Takes input from players to move"""
    player_x = player[0]
    player_y = player[1]
    movement = command[1].strip().lower()

    # Change player's co-ordinates appropriately
    if movement == "down" or movement == "south" or movement == "d":
        player_y = player_y - 1
    elif movement == "up" or movement == "north" or movement == "u":
        player_y = player_y + 1
    elif movement == "right" or movement == "east" or movement == "r":
        player_x = player_x + 1
    elif movement == "left" or movement == "west" or movement == "l":
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
    class PlayerWin(Exception): pass
    class PlayerStarve(Exception): pass
    fish = 4
    hunger = 6
    turn_number = 1

    # Menu

    # Intro
    #intro() # Delete this to skip intro for now
    # Game Start
    try:
        playing = True
        while playing:
            map_displayer(stage,player, stage_tiles, TILES)
            # Print status
            # Ask player for command
            turn = True
            color.write("Turn {}\n".format(turn_number))
            while turn:
                
                command = command_processor()
                # If player
                if command[0] == 'movement':
                    player = movement_processor(stage, player, stage_tiles, command)
                    if player[2] == True:
                        update = special_condition_checker(special, player)
                        if update == "end":
                            raise PlayerWin
                        turn = False
                        del player[-1]

                    elif player[2] == False:
                        del player[-1]
                    else:
                        print("Something crititcal has occured within the movement processcer")
                        del player[-1]
                        
                elif command[0] == 'fishing':
                    print("Fishing time i havent actually developed this yet lol soz")
                    

                elif command[0] == 'eat':
                    unzip = replenishment_processor(fish,hunger)
                    fish = unzip[0]
                    hunger = unzip[1]

                elif command[0] == 'help':
                    help_module()
                              
                else:
                    print("Beep Boop")

            #  Perform post turn actions
            hunger = hunger_processor(turn_number,hunger)
            if hunger == 0:
                raise PlayerStarve
            turn_number += 1
            
    except PlayerWin:
        ending("win")
    except PlayerStarve:
        ending("starve")
    except:
        print("broke")
main()
