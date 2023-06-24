
import numpy as np


class player:  
    def __init__(self):
        self.boat_coordinates = np.empty((0, 2))
        self.artillery_coordinates = np.empty((0, 2))
        self.board = np.full((5, 5), "*")
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
    check_hits(player1)
    check_hits(player2)
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


def call_artillery(player, artillery_coordinates):
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

    
def check_hits(player):
    direct_hits = np.where(np.all(player.artillery_coordinates == player.boat_coordinates[:, None], axis=2))
    for i in range(len(direct_hits[0])):
        row = int(direct_hits[0][i])
        column = int(direct_hits[1][i])
        player.board[row, column] = player.boat["boat1"]["damaged_icon"]
    return player.board



update_UI()
get_boat_coordinates()
# print(player1.boat_coordinates)
plot_coordinates(player1, player1.boat_coordinates)
update_UI()
call_artillery(player1, player1.artillery_coordinates)
update_UI()

