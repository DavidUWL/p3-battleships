
import numpy as np
import random 

class player:  
    def __init__(self):
        self.boat_coordinates = np.empty((0, 2))
        self.artillery_coordinates = np.empty((0, 2))
        self.board = np.full((5, 5), "*")
        self.score = 0
        self.boat = {
            "boat1": {
                "icon": "#",
                "damaged_icon": "X",
                "length": 4,
                "hit": False
            },

            "boat2": {
                "icon": "@",
                "damaged_icon": "X",
                "length": 2,
                "hit": False
            }
        }
 


player1 = player()

player2 = player()


def update_UI():
    check_hits(player1, player2)
    check_hits(player2, player1)
    print(player2.board)
    print("\n --------------------- \n")
    print(player1.board)


def get_boat_coordinates():
    i = 1
    while i < 6:
        y = int(input("pick a row from 1-5:")) 
        y = coordinate_validation(y)
        x = int(input("pick a column from 1-5:")) 
        x = coordinate_validation(x)
        y = y - 1  # subtracting 1 for zero indexing
        x = x - 1  # subtracting 1 for zero indexing
        c = np.array([[y, x]])
        player1.boat_coordinates = np.append(player1.boat_coordinates, c, axis=0)
        i += 1
    return player1.boat_coordinates


def coordinate_validation(value):
    while value < 1 or value > 5:
        print("Choose between 1-5.")
        value = int(input("pick a row from 1-5:")) - 1
    return value


def plot_coordinates(player, boat_coordinates):
    for i in range(boat_coordinates.shape[0]):
        row = int(boat_coordinates[i, 0])
        column = int(boat_coordinates[i, 1])
        player.board[row, column] = player.boat["boat1"]["icon"]
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
    c = np.array([[y, x]])
    player.artillery_coordinates = np.append(player.artillery_coordinates, c, axis=0)
    # print(player1.artillery_coordinates)

    
def check_hits(player_boats, player_artillery):
    direct_hits = np.where(np.all(player_artillery.artillery_coordinates == player_boats.boat_coordinates[:, None], axis=2))
    misses = np.where(np.all(player_artillery.artillery_coordinates != player_boats.boat_coordinates[:, None], axis=2))
    
    for i in range(len(direct_hits[0])):
        row = int(direct_hits[0][i])
        column = int(direct_hits[1][i])
        player_boats.board[row, column] = player_boats.boat["boat1"]["damaged_icon"]
    
    for i in range(len(misses[0])):
        row = int(misses[0][i])
        column = int(misses[1][i])
        player_artillery.board[row, column] = "~"
    return player_boats.board
    print(direct_hits)
    print(misses)


def get_computer_boat_coordinates(player):
    i = 0
    while i < 5:
        while True:
            computer_boat_coordinates = random.sample(range(0, 4), 2)
            if not any(np.array_equal(computer_boat_coordinates, coord) for coord in player.boat_coordinates):
                player.boat_coordinates = np.append(player.boat_coordinates, [computer_boat_coordinates], axis=0)
                break
        i += 1
    return player.boat_coordinates



def computer_call_artillery(player):
    while True:
        computer_artillery = random.sample(range(0, 4), 2)
        if not any(np.array_equal(computer_artillery, coord) for coord in player.artillery_coordinates):
            player.artillery_coordinates = np.append(player.artillery_coordinates, [computer_artillery], axis=0)
            break
        
    return player.artillery_coordinates
    








update_UI()
get_boat_coordinates()
get_computer_boat_coordinates(player2)
plot_coordinates(player1, player1.boat_coordinates)
update_UI()
print(player2.boat_coordinates)
call_artillery(player1)
computer_call_artillery(player2)
update_UI()
print(player1.artillery_coordinates, player2.artillery_coordinates)


