from board import Board
from node import Node


class HumanPlayer:
    def __init__(self, player):
        self.player = player
        self.human = True

    # Displays the board on the player's turn
    def display(self, tree):
        print("\nPlayer Turn")
        for i in tree.board.gameBoard:
            print(i)

    # Human move function
    def move(self, depth=None, tree=None, isMax=None):
        while True:
            inp = input("\nEnter Column Number to Drop Piece: ")
            try:
                inp = int(inp)
            except ValueError:
                print("Bad Input:", inp, "is not an integer")
                continue
            return [None, int(inp)]
