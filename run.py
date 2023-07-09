import numpy as np
import random
from os import system
import time


def clear():  # clears terminal/python shell
    system("clear")


class Player:
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
                "hit": [False, False, False, False, False],
            },
            "boat2": {
                "icon": "@",
                "damaged_icon": np.array(["X"], dtype=str),
                "length": 2,
                "hit": False,
            },
            "boat3": {
                "icon": "#",
                "damaged_icon": np.array(["X"], dtype=str),
                "length": 1,
                "hit": False,
            },
            "boat4": {
                "icon": "#",
                "damaged_icon": np.array(["X"], dtype=str),
                "length": 5,
                "hit": False,
            },
            "boat5": {
                "icon": "#",
                "damaged_icon": np.array(["X"], dtype=str),
                "length": 3,
                "hit": False,
            },
        }


def new_game():

    player1 = Player()
    player2 = Player()

    def get_names(
        player, player2
    ):  # gets each players name and assigns to player.name
        name = input("what is your name captain? \n type your name:")

        while len(name) > 10:
            print("Captain your name is too long!")
            name = input("Choose a shorter name:")
        clear()  # clears the terminal
        splash_ascii()
        player2_name = input("And what is your enemies name? \n type your enemies name:")

        while len(player2_name) > 10:
            print("Are you sure thats the enemy?")
            player2_name = input("Choose a shorter name:")
        print("Here is your board, captain %s! \n your boats are shown as #" % player2_name)

        player.name = name  # assigns names to the player class
        player2.name = player2_name

    def update_UI():  # updates the visual's/board
        plot_coordinates(player1)
        clear()
        splash_ascii()
        clean_player_boards(player2)
        create_divider(player1.board)
        clean_player_boards(player1)

    def get_boat_coordinates(
        player,
    ):  # takes validated inputs from the player to assign coordinates for boats
        i = 1
        while i < 6:
            y = coordinate_validation(input("pick a row from 1-5:"))
            x = coordinate_validation(input("pick a column from 1-5:"))
            print(y)
            while player.boat_coordinates[y - 1, x - 1] == player.boat["boat1"]["icon"]:  # subtracting 1 for zero indexing
                print("Captain, there's already a boat there.")
                y = coordinate_validation(input("Pick a new row from 1-5:"))
                x = coordinate_validation(input("Pick a new column from 1-5:"))
            player.boat_coordinates[y - 1, x - 1] = player.boat["boat1"]["icon"]
            i += 1
            update_UI()
        return player.boat_coordinates

    def coordinate_validation(value):  # validates coordinates chosen for boats
        while True:
            try:
                value = int(value)
                if value < 1 or value > 5:
                    print("Choose between 1 and 5.")
                else:
                    break

            except ValueError:
                print("Have you forgotten numbers captain!?")

            value = input("choose from 1-5:")
        return value

    def plot_coordinates(
        player,
    ):  # plots the boats into the players boat_coardinates and pushes to respective board
        for i in range(player.boat_coordinates.shape[0]):
            for j in range(player.board.shape[1]):
                if player.boat_coordinates[i, j] == "#":
                    player.board[i, j] = "#"
        return player.board

    def call_artillery(
        player,
    ):  # takes validated input from the player and pushes to their artillery coordinates
        print("Call your artillery shot!")
        y = coordinate_validation(input("pick a row from 1-5:"))
        x = coordinate_validation(input("pick a column from 1-5:"))

        y = y - 1  # subtracting 1 for zero indexing
        x = x - 1  # subtracting 1 for zero indexing

        while True:
            if player.artillery_coordinates[y, x] == "!":
                print("You have already hit that coordinate!")
                y = coordinate_validation(input("pick a row from 1-5:"))
                x = coordinate_validation(input("pick a column from 1-5:"))
                clear()
                return x, y
            else:
                break

        player.artillery_coordinates[y, x] = "!"
        return player.artillery_coordinates

    def check_hits(
        artillery, boat
    ):  # checks whether the artillery coordinate matches a boat coordinates and changes value accordingly
        hit = np.logical_and(
            artillery.artillery_coordinates == "!", boat.boat_coordinates == "#"
        )
        miss = np.logical_and(
            artillery.artillery_coordinates == "!",
            np.logical_not(boat.boat_coordinates == "#"),
        )
        boat.board[hit] = boat.boat["boat1"]["damaged_icon"]
        boat.board[miss] = "~"

    def get_computer_boat_coordinates(
        player,
    ):  # randomely generates validated locations for computer boats
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

    def computer_call_artillery(
        player,
    ):  # generates location for computer artillery, validates if choosing same location twice and regenerates
        while True:
            y = random.randint(0, 4)
            x = random.randint(0, 4)
            if player.artillery_coordinates[y, x] != "!":
                player.artillery_coordinates[y, x] = "!"
                break
        time.sleep(1)  # 1 second wait time before code executes to delay gameplay
        return player.artillery_coordinates

    def clean_player_boards(player):  # removes unwanted characters when printing
        cleaned_board = np.array2string(
            player.board, separator=", ", formatter={"int": lambda x: f"{x:2d}"}
        )
        cleaned_board = (
            cleaned_board.replace("[", "")
            .replace("]", "")
            .replace(",", "")
            .replace("'", "")
        )
        print("  ", player.name, "\n", cleaned_board)

    def create_divider(
        array,
    ):  # creates a divider set to the length of the board row - will work regardless of board size initialised
        row_length = array.shape[1]
        divider_line = " -" * row_length
        print(divider_line)

    def loop_game():  # game structure loop that runs while condition is not met
        call_artillery(player1)
        check_hits(player1, player2)
        update_UI()
        computer_call_artillery(player2)
        check_hits(player2, player1)
        update_UI()
        check_for_winner(player1, player2)

    def check_for_winner(
        player1, player2
    ):  # when boards converted to boolean, gives loop_game function a condition to loop over
        p1_bool_boat_coord = player1.boat_coordinates == "#"
        p2_bool_boat_coord = player2.boat_coordinates == "#"

        p1_hits = np.logical_and(
            player1.artillery_coordinates == "!", player2.boat_coordinates == "#"
        )
        p1_winner_clause = np.all(np.equal(p1_hits, p2_bool_boat_coord))

        p2_hits = np.logical_and(
            player2.artillery_coordinates == "!", player1.boat_coordinates == "#"
        )
        p2_winner_clause = np.all(np.equal(p2_hits, p1_bool_boat_coord))

        # print(p1_bool_boat_coord)
        # print(p2_bool_boat_coord)
        # print(p1_hits)
        # print(p2_hits)
        # print(p1_winner_clause)
        # print(p2_winner_clause)

        while not (p1_winner_clause or p2_winner_clause):
            loop_game()
        if p1_winner_clause and p2_winner_clause:
            print("The game is a tie.")
            prompt_new_game()
        elif p1_winner_clause:
            print("%s is the winner!" % player1.name)
            prompt_new_game()
        else:
            print("%s is the winner!" % player2.name)
            prompt_new_game()

    def prompt_new_game():
        start_new_game = str(input("Would you like to play again? \n Y/N:").upper())

        if start_new_game == "Y":
            clear()
            new_game()
        elif start_new_game == "N":
            system.exit()
        else:
            prompt_new_game()

    def splash_ascii():
        logo = """  ###               ##     ##    ###                     ###
  ##                ##     ##     ##                     ##
  ##               #####  #####   ##    ####    #####    ##       ###    ######
  #####    ####     ##     ##     ##   ##  ##  ##        #####     ##     ##  ##
  ##  ##  #    #    ##     ##     ##   ######   #####    ##  ##    ##     ##  ##
  ##  ##  #   ##    ## ##  ## ##  ##   ##           ##   ##  ##    ##     #####
 ######    ### #     ###    ###  ####   #####  ######   ###  ##   ####    ##
 """
        print(logo)

    def begin_game():  # initial call of game functions to begin loop
        splash_ascii()
        get_names(player1, player2)
        update_UI()
        get_boat_coordinates(player1)
        get_computer_boat_coordinates(player2)
        plot_coordinates(player1)
        update_UI()
        loop_game()

    begin_game()


new_game()
