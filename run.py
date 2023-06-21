
import numpy as np


class player:  
    def __init__(self):
        self.boat_coordinates = []
        self.board = np.full((5, 5), "*")


player1 = player()


player2 = player()


def update_UI():
    print(player1.board)
    print("\n --------------------- \n")
    print(player2.board)


def get_boat_coordinates():
    i = 1
    while i < 6:
        y = int(input("pick a row from 1-5:")) 
        y = coordinate_validation(y)
        x = int(input("pick a column from 1-5:")) 
        x = coordinate_validation(x)
        y = y - 1 # subtracting 1 for zero indexing
        x = x - 1 # subtracting 1 for zero indexing
        c = [y, x]
        player1.boat_coordinates.append(c)
        i += 1
    print(player1.boat_coordinates)


def coordinate_validation(value):
    while value < 1 or value > 5:
        print("Choose between 1-5.")
        value = int(input("pick a row from 1-5:")) - 1
    return value


def plot_coordinates(player, player_coordinates):
    converted_player_coordinates = np.array(player_coordinates) # converts board to numpy array

    for i in range(converted_player_coordinates.shape[0]):
        row = converted_player_coordinates[i, 0]
        column = converted_player_coordinates[i, 1]
        player.board[row, column] = "#"

    return player.board

    
update_UI()
get_boat_coordinates()
plot_coordinates(player1, player1.boat_coordinates)
update_UI()