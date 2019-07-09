##
#  The Legend of Maui
#  V0.04


def map_generator_1():
    """Generates the stage should go in format [Stage Size] [Player Starting Position]"""
    STAGE_1 = ([5,5],[1,1])
    
    return STAGE_1


def movement_processor(stage,player):
    """Takes input from players to move"""
    player_x = player[0]
    player_y = player[1]
    print(player_x,player_y)

    valid = False
    while not valid:
        movement = input("Enter a movement").lower()
        if (movement != "up"
            and movement != "down"
                and movement !="right"
                    and movement !="left"):
            print("Please enter a valid command.")
        elif movement == "up":
            player_x = player_x + 1
        elif movement == "down":
            player_x = player_x - 1
        elif movement == "left":
            player_y = player_y + 1
        elif movement == "right":
            player_y = player_y - 1

        player_new = [player_x,player_y]
        valid = movement_checker(stage,player_new)
        #  reset t
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
    elif player_new[0] == stage[0]:
        valid = False
        print("No")
    elif player_new[1] == stage[1]:
        valid = False
        print("No")
    else:
        valid = True
        print("Yes")
    return valid
    
        

def map_displayer(player):
    """Displays the map in the console"""
    print(player)

def main():
    """Main Routine"""
    stage = map_generator_1()
    player = stage[1]
    stage = stage[0]

    playing = True
    while playing:
        map_displayer(player)
        player = movement_processor(stage,player)
    pass

main()
