##
#  The Legend of Maui
#  V1.06
## =====----------- Color Module ----------=====
import time
import random
import sys
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")   


class PlayerWin(Exception): pass
class PlayerCaveEnter1(Exception): pass
class PlayerCaveEnter2(Exception): pass
class PlayerCaveLeave1(Exception): pass
class PlayerCaveLeave2(Exception): pass
class PlayerStarve(Exception): pass
class TutorialEnd(Exception): pass

## =====----------- Menu/Sequences ----------=====
def intro(type):
    """Intro Sequence"""
    if type == "opening":
        try:
            print("Ctrl + C to skip!")
            slow_print("A new dawn breaks the crest of the sea")
            intro_dots()
            slow_print("The mighty sea beckons, and from the depths a new hero arises")
            intro_dots()
            slow_print("Now is the time of man, and your people need a land in which to thrive")
            intro_dots()
            slow_print("Awaken, and discover Aotearoa as you begin",)
            intro_dots()
            time.sleep(1)
            slow_print("The Legend of Māui!~","ERROR")
            time.sleep(2)
        except KeyboardInterrupt:    # Skip Intro
            pass
        color.write("""
                              _________                              
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

    elif type == "stage_1":
        try:
            print("Ctrl + C to skip!")
            intro_dots()
            slow_print("My brothers")
            intro_dots()
            slow_print("They plan to leave for the high seas to fish without me")
            intro_dots()
            slow_print("They think me not capable, they despise me, and so they exclude me")
            intro_dots()
            slow_print("Ha")
            intro_dots()
            slow_print("Ahahaha")
            intro_dots()
            slow_print("I will show them.~")
            time.sleep(1.5)
            slow_print("I will show them that Māui-pōtiki is the greatest of all!~","ERROR")
            time.sleep(1)
            slow_print("I will sail for the great caves where my grandma resides, and I shall ask for a boon.~")
            time.sleep(1)
            slow_print("I will follow the ⋆ of Tangaroa, to find the best spot to fish.~")
            time.sleep(1)
            slow_print("I, Māui, will fish up the greatest catch of all! This will be,","ERROR")
            time.sleep(2)
            slow_print(" my legend.~~","ERROR")
            time.sleep(3.5)
            slow_print("Press ENTER to begin.","KEYWORD")
            input()
            
        except KeyboardInterrupt:
            pass
        
                   
        

def intro_dots():
    """Prints the dots in the intro sequence"""
    i = 0
    time.sleep(0.6)
    while i != 3:
        color.write(".")
        time.sleep(0.3)
        i += 1
    print("")

def slow_print(text,color_choice = None):
    for letter in text:
        if letter == "~":
            color.write("\n")
        elif color_choice == None:
            color.write(letter)
        else:
            color.write(letter,color_choice)
        time.sleep(0.01)
        

def fast_print(text,color_choice = None):
    for letter in text:
        if letter == "~":
            color.write("\n")
        elif color_choice == None:
            color.write(letter)
        else:
            color.write(letter,color_choice)
        time.sleep(0.005)

def ending(type):
    """Determines the type of ending a user gets"""
    
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
        color.write("lol you were hungry so you went home")
    exit()
## =====----------- Map Generation ----------=====
def tile_set():
    """Contains the data for tiles"""
    TILES = {
        "ocean":"~"
        ,"rock":"R"
        ,"mountain":"M"
        ,"player":"X"
        ,"end":"⋆"
        ,"npc":"I"
        ,"cave":"C"
        ,"dirt":"+"
        ,"sign":"!"
        }

    return TILES

def stage_1_generator(option):
    """Generates the stage should go in format [Stage Size] [Player Starting Position]"""
    # Stage Size + Player Starting Position
    STAGE_1 = ([10,10], [1,1])

    # Non-Ocean tiles
    STAGE_1_TILES = {         
        "1,2":"rock",
        "1,3":"mountain",
        "2,4":"rock",
        "2,7":"rock",
        "2,8":"rock",
        "3,3":"rock",
        "3,4":"rock",
        "3,8":"mountain",
        "3,9":"rock",
        "3,10":"rock",
        "4,4":"rock",
        "4,5":"mountain",
        "5,6":"rock",
        "6,1":"rock",
        "6,2":"rock",
        "6,7":"rock",
        "6,10":"rock",
        "7,1":"rock",
        "7,2":"rock",
        "7,6":"rock",
        "7,10":"rock",
        "8,5":"rock",
        "8,6":"rock",
        
        "8,10":"rock",
        "9,1":"sign",
        "9,3":"rock",
        "9,4":"rock",
        "9,9":"rock",
        "9,10":"rock",
        "10,1":"cave",
        "10,3":"rock",
        "10,4":"cave",
        "10,8":"rock",
        "10,9":"rock",
        "10,10":"rock",
        
        "1,10":"end",
    }

    # Special Tiles that trigger an event
    STAGE_1_SPECIAL = {       
        "1,10":"end",
        "9,1":"sign_cave",
        "10,1":"cave_entrance_1",
        "10,4":"cave_entrance_2",
        "1,9":"dark_water",
        "2,9":"dark_water",
        "2,10":"dark_water"
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

def cave_generator(option):
    """Generates the stage should go in format [Stage Size] [Player Starting Position]"""
    # Stage Size + Player Starting Position
    CAVE = ([10,10], [1,1])

    # Non-Ocean tiles
    CAVE_TILES = {         
        "1,1":"cave",
        "1,4":"rock",
        "1,5":"rock",
        "2,5":"rock",
        "3,5":"rock",
        "4,6":"rock",
        "5,1":"rock",
        "5,3":"rock",
        "5,6":"rock",
        "5,7":"rock",
        "6,8":"rock",
        "6,9":"rock",
        "6,10":"rock",
        "7,1":"rock",
        "7,5":"rock",
        "7,7":"ocean",
        "7,8":"ocean",
        "7,9":"ocean",
        "8,1":"mountain",
        "8,2":"mountain",
        "8,3":"mountain",
        "8,7":"ocean",
        "8,8":"ocean",
        "8,9":"npc",
        "8,10":"ocean",
        "9,1":"mountain",
        "9,2":"mountain",
        "9,3":"mountain",
        "9,4":"mountain",
        "9,5":"mountain",
        "9,8":"ocean",
        "9,9":"ocean",
        "10,1":"mountain",
        "10,2":"mountain",
        "10,3":"mountain",
        "10,4":"mountain",
        "10,5":"mountain",
        "10,6":"mountain",
        "10,10":"cave",
        
        
    }

    # Special Tiles that trigger an event
    CAVE_SPECIAL = {       
        "1,1":"cave_exit_1",
        "10,10":"cave_exit_2",
        "8,9":"npc_grandma",
    }

    # Decide what data to return
    if option == "stage":
        return CAVE
    elif option == "tiles":
        return CAVE_TILES
    elif option == "special":
        return CAVE_SPECIAL
    else:
        print("Something Broke! CAVE")

def tutorial_generator(option):
    """Generates the stage should go in format [Stage Size] [Player Starting Position]"""
    # Stage Size + Player Starting Position
    TUTORIAL = ([3,9], [2,2])

    # Non-Ocean tiles
    TUTORIAL_TILES = {         
        "1,2":"mountain",
        "1,3":"mountain",
        "1,4":"mountain",
        "1,1":"mountain",
        "2,1":"mountain",
        "3,1":"mountain",
        "3,2":"mountain",
        "3,3":"mountain",
        "3,4":"mountain",
        "2,6":"rock",
        "2,9":"end",
    }

    # Special Tiles that trigger an event
    TUTORIAL_SPECIAL = {       
        "2,9":"tutorial_end"
    }

    # Decide what data to return
    if option == "stage":
        return TUTORIAL
    elif option == "tiles":
        return TUTORIAL_TILES
    elif option == "special":
        return TUTORIAL_SPECIAL
    else:
        print("Something Broke! map_generator_1")
    
# ------------------ Map Gen Tutorial -----------------
def tutorial():
    """The tutorial stage"""
    #  Setup variables
    TILES = tile_set()    # Call tile set
    stage = tutorial_generator("stage")
    player = stage[1] 
    stage = stage[0] 
    stage_tiles = tutorial_generator("tiles")
    special = tutorial_generator("special")
    fish = 1
    hunger = 6
    turn_number = 0

    print("Tutorial has been triggered!")
    # Introduction to Maui
    color.write("\nHaere Mai Māui-tikitiki-a-Taranga, Māui-pōtiki, divine descendant of Tama-nui-te-rā.\n"
      "Your future deeds are great and many, and now is the time to claim the title of Maui-te-whare-kino.\n"
      "Embark now, and discover the land of the long white cloud.\n\n")

    try:
        turn(player,stage,stage_tiles,special,TILES,fish,hunger,"yes",turn_number,
                 {"legend_rod":False,
                  "rock_smasher":False,
                  },"ocean")
    except KeyboardInterrupt:
        print("Tutorial has been skipped! Good Luck!")

    print("The tutorial has now ended. It's time to begin your journey!")

def tutorial_tips(turn_number):
    """Determines what tips are shown in the tutorial"""

    if turn_number == 1:
        color.write("To move in this game, we enter keywords. For example, to move up we'd type 'Move Up'. Try it out!")
    elif turn_number == 2:
        color.write("Great job! In this game, M stands for mountain, and R stands for rock. You're the X, and your goal is the ⋆.")
    elif turn_number == 3:
        color.write("Did you know, you can type the intials of some actions to trigger them? Try typing 'u'!")
    elif turn_number == 4:
        color.write("""Right! Now that there's a rock in front of you, you can't go up anymore. (Try it out if you want!)
Instead, try typing a sentence containing the words left/right.""")
    elif turn_number == 5:
        color.write("""Good Job! At this point, your character is getting hungry. It's time to eat! Eat by entering 'eat' or something similar.
Eating doesn't consume a turn, so afterwards keep moving up.""")
    elif turn_number == 6:
        color.write("To get more fish, enter a sentence containing 'Fishing' or something of the like. Give it a go!")
    elif turn_number == 7:
        color.write("You're getting the hang of this. Keep in mind, you can only fish on Ocean tiles (~). \nJust go towards the end now! Good luck! Enter 'h' or 'help' for more help!")

    print("")
# ------------------ Map Gen Stage 1 -----------------

def stage_1(player, fish, hunger, turn_number, items):
    """Stage 1"""
    # Setup values to be used in current stage
    TILES = tile_set()
    stage = stage_1_generator("stage")
    stage = stage[0]
    stage_tiles = stage_1_generator("tiles")
    special = stage_1_generator("special")                              
    default_tile = "ocean"
    
    stats = turn(player,stage,stage_tiles,special,TILES,fish,hunger,"no", turn_number, items, "ocean")
    return stats

# ------------------ Map Gen Cave -----------------

def cave(player, fish, hunger, turn_number, items):
    """Cave"""
    # Setup values to be used in current stage
    TILES = tile_set()
    stage = cave_generator("stage")
    stage = stage[0]
    stage_tiles = cave_generator("tiles")
    special = cave_generator("special")
    default_tile = "dirt"

    stats = turn(player,stage,stage_tiles,special,TILES,fish,hunger,"no",turn_number, items, "dirt")
    return stats
## =====----------- Turn Mechanics ----------=====

#  ------------------ Turn Processing -----------------
def command_processor():
    """Processes commands based on keyowrds that the user has entered"""
    MOVEMENT = ["up","right","down","left","north","west","east","south","u","r","l","d"]
    FISHING = ["fish","fishing","f"]
    HELP = ["help"," h "]
    EAT = ["eat","eating","refuel","nom","e"]
    
    validity = 0
    while validity == 0:
        command = []
        action = input("Enter a command: ").lower()
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
            print("Please enter a keyword. Enter help for instructions.")
        
#  ------------------ Help -----------------
def help_module():
    """Starts the help module"""
    helping = True
    color.write("Hello! Welcome to the Legend of Maui!\n")
    while helping:
        query = input("""Enter the number of the subject you need help with:
{1} Objective of the Game
{2} Moving
{3} Hunger
{4} Eating
{5} Terrain
{6} Fishing
Enter nothing to exit the help module""").lower().strip()

        if query == "":
            helping = False
        elif query == "1":
            color.write("The objective of the game is to move to the 'E' square, while trying not to starve to death.")
        elif query == "2":
            color.write("Enter sentences containing movement keywords to move. For example, 'I want to move right' will move the player right.")
        elif query == "3":
            color.write("You decay one hunger every turn, so make sure to pay attention to Maui's prompts to gauge your hunger!")
        elif query == "4":
            color.write("Enter sentences containing eating keywords to move. For example, 'Eat something' will consume a fish from your stores.")
        elif query == "5":
            color.write("""'R' = Rock
'M' = Mountain
'~' = Ocean
'X' = Player""")
        elif query == "6":
            color.write("lol i havent implemeted this in")
        print("\n")
          
        
#  ------------------ Fishing/Hunger -----------------
def fishing_processor(player,stage_tiles,fish,default_tile,items):
    """Process fishing"""
    tile = stage_tiles.get("{0},{1}".format(player[0], player[1]), default_tile)
    zipped = []
    if items['legend_rod'] == True:
        fish_chance = 100
        print("You sense the rod of legends resonating with Tūmatauenga, enchancing your fishing abilities.")
    else:
        fish_chance = 70
    if tile == "ocean":
        fish_check = random.randint(1,100)
        if fish_check <= fish_chance - 40:
            fish += 2
            print("Wow! You managed to catch 2 fish with one hook! Tūmatauenga/Tangaroa must be blessing you. You give thanks. You now have {} fish.".format(fish))
        elif fish_check <= fish_chance:
           fish += 1
           print("You caught a fish! You now have {0} fish.".format(fish))
        else:
            print("You failed to catch a fish...")
        return fish, False

    else:
        print("You can't fish on this tile!")
        return fish, True


def hunger_processor(turn,hunger):
    """Process hunger per turn"""
    hunger -= 1

    if hunger > 6:
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

def starve_checker(hunger):
    """Calculates the chance for a user to die"""
    death_chance = -30
    hunger -= 1

    if (death_chance * (hunger-1)) > random.randint(1,100):
        death = True
    else:
        color.write("Somehow, through divine intervention, you manage to survive though the pain, although you know that the end is near. You should definitely eat something.\n","ERROR")
        death = False
    return death
    
    
def replenishment_processor(fish,hunger):
    """Processes the eating to fish to replenish hunger"""
    zip = []
    if fish == 0:
        print("You don't have any fish!")
        zip.append(fish)
        zip.append(hunger)
        return zip
    else:
        zip.append(fish - 1)
        zip.append(7) # Hunger to give back

        if hunger > 3:
            print("You eat a fish from your reserve, leaving you with {} left.".format(fish - 1))

        elif hunger > 1:
            print("You gobble down a fish from your reserve, leaving you with {} left.".format(fish - 1))

        elif hunger > 0:
            print("The taste of fish has never seemed so good as you devour one. You have {} left.".format(fish - 1))

        elif hunger >= 0:
            print("Somehow, you have survived at the brink of death. You vicously gobble down a fish, leaving you with {} left.".format(fish - 1))

        print("")

    return zip


#  ------------------ Movement -----------------
def movement_processor(stage, player,
                       stage_tiles,command,
                       special,items):
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

    #  Special Checker
    special, items, valid = special_condition_checker(special, items, player_new)
    if valid:
        pass                  
    else:
        player_new = player
        player_new.append(True)   
        return player_new, special, items

    #  Boundary and Collision checking
    valid = boundary_checker(stage, player_new)
    if valid:
        valid = tile_checker(stage_tiles, player_new)   
    # Reset the program
    if not valid:
        player_new = player
        player_new.append(False)
    else:
        player_new.append(True)
    

    return player_new, special, items
        

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
        color.write("You can't move into a {}!\n".format(tile),"ERROR")
    else:
        valid = True

    return valid


def special_condition_checker(special_tiles, items,
                              player_new):
    """Checks to see whether there is a special condition triggered by the player"""
    tile = special_tiles.get("{0},{1}".format(player_new[0], player_new[1]), None)
    valid = True

    #  Victory conditions
    if tile == "end":
        raise PlayerWin
    elif tile == "shop":
        pass

    # Stage Change Condition
    elif tile == "cave_entrance_1":
        raise PlayerCaveEnter1
    elif tile == "cave_entrance_2":
        raise PlayerCaveEnter2
    elif tile == "cave_exit_1":
        raise PlayerCaveLeave1
    elif tile == "cave_exit_2":
        raise PlayerCaveLeave2

    # NPC Condiitions
    elif tile == "npc_grandma":
        print("boo")
        if items["legend_rod"] == True:
            print("Buzz off young one")
        else:
            items["legend_rod"] = True
            print("You now have the legendary rod of Maui!")
        valid = False

    # Sign Condition
    elif tile == "sign_cave":
        slow_print("If I remember correctly, the cave should be pretty dry.\nThere may not be limited chances for me to fish inside.\nI should probably stock up on some fish before I enter.\n")
        time.sleep(1)
        special_tiles["{0},{1}".format(player_new[0], player_new[1])] = None
        

    # Tutorial Conditions
    elif tile == "tutorial_end":
        raise TutorialEnd
    return special_tiles, items, valid

    
    
## =====----------- UI Elements ----------=====

#  ------------------ Map Gen -----------------
def map_displayer(stage, player,
                  stage_tiles, TILES, special_tiles, default_tile):
    """Displays the map in the console"""
    color.write("=============================================\n","BUILTIN")  # Hard seperation to show that a new turn has begun
    # Setup variables
    x = 1
    y = stage[1]
    player_x = player[0]
    player_y = player[1]

    while y > 0:
        while x < stage[0]+1:
            if x == player_x and y == player_y:
                color.write(TILES.get("player", "X"), "hit")

            elif ("{0},{1}".format(x, y) in stage_tiles
                  and "{0},{1}".format(x, y) in special_tiles):
                if (stage_tiles["{0},{1}".format(x, y)] == "npc"
                    or stage_tiles["{0},{1}".format(x, y)] == "sign"):
                    tile = stage_tiles.get("{0},{1}".format(x, y), default_tile)
                    color.write(TILES[tile], "KEYWORD")
                
                else:
                    tile = stage_tiles.get("{0},{1}".format(x, y), default_tile)
                    color.write(TILES[tile], "STRING")

            elif "{0},{1}".format(x, y) in stage_tiles:
                if (stage_tiles["{0},{1}".format(x, y)] == "rock"
                    or stage_tiles["{0},{1}".format(x, y)] == "mountain"):
                    tile = stage_tiles.get("{0},{1}".format(x, y), default_tile)
                    color.write(TILES[tile], "stderr")

                else:
                    tile = stage_tiles.get("{0},{1}".format(x, y), default_tile)
                    color.write(TILES[tile], "stdout")

            elif "{0},{1}".format(x,y) in special_tiles:
                if (special_tiles["{0},{1}".format(x, y)] == "dark_water"):
                    tile = stage_tiles.get("{0},{1}".format(x, y), default_tile)
                    color.write(TILES[tile],"stdin")        
            else:
                print(TILES[default_tile], end='')
            x += 1
            print(" ",end='')
        print("")
        y -= 1
        x = 1

## =====----------- Turn ----------=====
def turn(player,stage,stage_tiles,special,TILES,fish,hunger,tutorial,turn_number, items, default_tile):
    """A turn"""
    try:
        playing = True
        while playing:
            #  Pre-turn actions
            turn_number += 1
            hunger = hunger_processor(turn_number,hunger)
            if hunger <= 0:
                 if starve_checker(hunger) == True:
                     raise PlayerStarve

            given_tutorial_tip = False

            #  Turn start one-offs
            map_displayer(stage,player, stage_tiles, TILES,special, default_tile)
            turn = True
            color.write("Turn {}\n".format(turn_number))
            #  Commands start
            while turn:
                if tutorial == "yes" and given_tutorial_tip == False:
                    tutorial_tips(turn_number)
                    given_tutorial_tip = True
                command = command_processor()

                if command[0] == 'help':
                    help_module()

                #  Tutorial Conditions start here
                try:
                    if( tutorial == "yes"
                        and turn_number < 4 
                            and command[1] != " up "
                                and command[1] != " u "
                                    and command[1] != " north "):    
                        color.write("Hey! Just keep going up for now, ok?\n\n","ERROR")
                    elif(tutorial == "yes"
                         and turn_number == 4
                             and command[1] != " r "
                                 and command[1] != " right "
                                     and command[1] != " west"
                                         and command[1] != " left "
                                             and command[1] != " l "
                                                 and command[1] != " east "
                                                     and command[1] != " up "
                                                         and command[1] != " north "
                                                            and command[1] != " u "):
                        color.write("Hey! Just move right or left for now, ok?\n\n","ERROR")
                    elif(tutorial == "yes"
                         and turn_number == 5
                             and hunger < 4
                                 and command[0] != 'eat'):
                         color.write("Hey! Maui's feeling kinda hungry, maybe eat some grub!\n\n","ERROR")
                    elif(tutorial =="yes"
                         and turn_number == 5
                             and hunger > 4
                                and command[1] != " up "
                                    and command[1] != " u "
                                        and command[1] != " north "):
                        color.write("Now that you're full, let's continue moving up!\n\n", "ERROR")
                    elif(tutorial =="yes"
                         and turn_number == 6
                             and command[0] != 'fishing'):
                        color.write("Hey! Now would be a good time to fish!")
                    elif(tutorial =="yes"
                         and turn_number ==6
                             and command[0] == 'fishing'):
                        fish += 1
                        print("You caught a fish! You now have {0} fish.".format(fish))
                        turn = False
                        pass

                    #  Tutorial Conditions end here
                    else:

                        if command[0] == 'movement':   
                                player, special, items = movement_processor(stage, player, stage_tiles, command, special, items)
                                if player[2] == True:
                                    
                                    turn = False
                                    del player[-1]

                                elif player[2] == False:
                                    del player[-1]
                                else:
                                    print("Something critical has occured within the movement processcer")
                                    del player[-1]
                                
                        elif command[0] == 'fishing':
                            fish, turn = fishing_processor(player,stage_tiles,fish,default_tile, items)

                        elif command[0] == 'eat':
                            unzip = replenishment_processor(fish,hunger)
                            fish = unzip[0]
                            hunger = unzip[1]
                        else:
                            print("Beep Boop")
                except IndexError:
                    color.write("Please try something else\n","ERROR")

            #  Perform post turn actions
    #  Conditions            
    except PlayerWin:
        ending("win")
    except PlayerStarve:
        ending("starve")
    except PlayerCaveEnter1:
        stage = cave_generator("stage")
        stats = ["cave",[1,1], fish, hunger, turn_number, items]
        return stats
    except PlayerCaveEnter2:
        stage = cave_generator("stage")
        stats = ["cave",[10,10], fish, hunger, turn_number, items]
        return stats
    except PlayerCaveLeave1:
        stage = stage_1_generator("stage")
        stats = ["stage_1",[10,1], fish, hunger, turn_number, items]
        return stats
    except PlayerCaveLeave2:
        stage = stage_1_generator("stage")
        stats = ["stage_1",[10,4], fish, hunger, turn_number, items]
        return stats
    except TutorialEnd:
        pass
    except KeyboardInterrupt:
        return KeyboardInterrupt

## =====----------- Routines ----------=====


def main():
    """Main Routine"""
    
    intro("opening")
    
    start_tutorial = input("Would you like to play the tutorial?").lower().strip()
    if start_tutorial == "no" or start_tutorial == "n":
        pass
    else:
        tutorial()

    save_file = False
    if save_file == True:
        stats = save_file
    else:
        stage = stage_1_generator("stage")
        stats = ["stage_1",stage[1],1,7,0,
                 {"legend_rod":False,
                  "rock_smasher":False,
                  }]  # [Stage, Player, Fish, Hunger, Turn, Item]

    intro("stage_1")
    while True:
    
        if stats[0] == "stage_1":
            stats = stage_1(stats[1], stats[2], stats[3], stats[4],stats[5])
        elif stats[0] == "cave":
            stats = cave(stats[1], stats[2], stats[3], stats[4],stats[5])

main()
