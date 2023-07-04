
import numpy as np
import random 

class player:  
    def __init__(self):
        self.name = ""
        self.boat_coordinates = np.empty((5, 5), dtype=object)
        self.artillery_coordinates = np.empty((5, 5), dtype=object)
        self.board = np.full((5, 5), "*", dtype=object)
        self.boat = {
            "boat1": {
                "icon": "#",
                "damaged_icon": np.array(["X"], dtype=str),
                "length": 4,
                "hit": False
            },
            "boat2": {
                "icon": "@",
                "damaged_icon": np.array(["X"], dtype=str),
                "length": 2,
                "hit": False
            },
            "boat3": {
                "icon": "#",
                "damaged_icon": np.array(["X"], dtype=str),
                "length": 1,
                "hit": False
            },
            "boat4": {
                "icon": "#",
                "damaged_icon": np.array(["X"], dtype=str),
                "length": 5,
                "hit": False
            },
            "boat5": {
                "icon": "#",
                "damaged_icon": np.array(["X"], dtype=str),
                "length": 3,
                "hit": False
            },
        }
 

player1 = player()

player2 = player()


def get_names(player, second_player):   # THIS NEEDS VALIDATION FOR STRING LENGTH
    name = input("what is your name captain? \n type your name:")
    second_name = input("And what is your enemies name? \n type your enemies name:")
    print("Here is your board captain %s! \n your boats are shown as #" %name)
    player.name = name
    second_player.name = second_name


def update_UI():
    clean_player_boards(player2)
    print("\n --------------------- \n")
    clean_player_boards(player1)


def get_boat_coordinates(player):
    i = 1
    while i < 6:
        y = int(input("pick a row from 1-5:")) 
        y = coordinate_validation(y)
        x = int(input("pick a column from 1-5:")) 
        x = coordinate_validation(x)
        y = y - 1  # subtracting 1 for zero indexing
        x = x - 1  # subtracting 1 for zero indexing
        player.boat_coordinates[y, x] = player.boat["boat1"]["icon"]
        i += 1
    return player.boat_coordinates


def coordinate_validation(value):  # needs revisiting as not validating correctly
    while value < 1 or value > 5:
        print("Choose between 1-5.")
        value = int(input("pick a row from 1-5:"))
    return value


def plot_coordinates(player):
    for i in range(player.boat_coordinates.shape[0]):
        for j in range(player.board.shape[1]):
            if player.boat_coordinates[i, j] == '#':
                player.board[i, j] = '#'
    # print(player.boat_coordinates)
    return player.board


def call_artillery(player):
    print("Call your artillery shot!")

    y = int(input("pick a row from 1-5:")) 
    y = coordinate_validation(y)

    x = int(input("pick a column from 1-5:")) 
    x = coordinate_validation(x)

    y = y - 1  # subtracting 1 for zero indexing
    x = x - 1  # subtracting 1 for zero indexing

    player.artillery_coordinates[y, x] = '!'
    return player.artillery_coordinates
    

def check_hits(artillery, boat):
    hit = np.logical_and(artillery.artillery_coordinates == "!", boat.boat_coordinates == '#')
    miss = np.logical_and(artillery.artillery_coordinates == "!", np.logical_not(boat.boat_coordinates == "#"))
    boat.board[hit] = boat.boat["boat1"]["damaged_icon"]
    boat.board[miss] = '~'
    

def get_computer_boat_coordinates(player):
    i = 0
    while i < 5:
        while True:
            y = random.randint(0, 4)
            x = random.randint(0, 4)
            if player.boat_coordinates[y, x] != player.boat["boat1"]["icon"]:
                player.boat_coordinates[y, x] = player.boat["boat1"]["icon"]
                break
        i += 1
    return player.boat_coordinates


def computer_call_artillery(player):
    while True:
        y = random.randint(0, 4)
        x = random.randint(0, 4)
        if player.artillery_coordinates[y, x] != "!":
            player.artillery_coordinates[y, x] = '!'
            break
    return player.artillery_coordinates
    

def clean_player_boards(player):
    cleaned_board = np.array2string(player.board, separator=', ', formatter={'int': lambda x: f'{x:2d}'})
    cleaned_board = cleaned_board.replace('[', '').replace(']', '').replace(',', '').replace("'", '')
    print("  ", player.name, "\n", cleaned_board)








get_names(player1, player2)
update_UI()
get_boat_coordinates(player1)
get_computer_boat_coordinates(player2)
plot_coordinates(player1)
plot_coordinates(player2)
update_UI()
# print("player1 boat coordinates: \n", player1.boat_coordinates)
# print("player2 boat coordinates: \n", player2.boat_coordinates)
call_artillery(player1)
print(player1.artillery_coordinates)
check_hits(player1, player2)
update_UI()
computer_call_artillery(player2)
print(player2.artillery_coordinates)
check_hits(player2, player1)
update_UI()


