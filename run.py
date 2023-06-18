import numpy as np


class player:  
    def __init__(self):
        self.picks = []
        self.board = np.full((5, 5), "*")

player1 = player()
player2 = player()

print(player1.board)
print("\n --------------------- \n")
print(player2.board)



# def game_initialize():
#     player1 = player()
#     player2 = player()
#     player1.construct_board()
#     player2.construct_board()
#     return player1, player2


# def update_UI():
#     print(np.array(player1.board))
#     print(np.array(player2.board))








# player1, player2 = game_initialize()
# get_user_picks()
# # update_UI()
