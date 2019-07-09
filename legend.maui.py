##
#  The Legend of Maui
#  V0.03


def map_generator_1():
    """Generates the stage should go in format [Stage Size] [Player Starting Position]"""
    STAGE_1 = ([5,5],[1,1])
    
    return STAGE_1


def movement_processor(player):
    """Takes input from players to move"""
    movement = input().lower()
    player_x = player[0]
    player_y = player[1]
    print(player_x,player_y)
    
    if movement != "up" and movement and "down" and movement !="right" and movement !="left":
        print("broke")
    elif movement == "up":
        player_x = player_x + 1
    elif movement == "down":
        player_x = player_x - 1
    elif movement == "left":
        player_y = player_y + 1
    elif movement == "right":
        player_y = player_y - 1

    player = [player_x,player_y]
    return player

def movement_checker(stage,player_new):
    """Checks to see whether movement is valid"""
    if player_new[0] == 0:
        print("no")
    elif player_new[1] == 0:
        print("bad")
    elif player_new[0] == stage[0]:
        print("NO")
    elif player_new[0] == stage[1]:
        print("BAD")
    else:
        return player_new
        

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
        player = movement_checker(stage,movement_processor(player))
    pass

main()
