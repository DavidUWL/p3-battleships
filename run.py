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
        c = [y, x]
        player1.boat_coordinates.append(c)
        i += 1
    print(player1.boat_coordinates)


def coordinate_validation(value):
    while value < 1 or value > 5:
        print("Choose between 1-5.")
        value = int(input("pick a row from 1-5:"))
    return value


update_UI()
get_boat_coordinates()

