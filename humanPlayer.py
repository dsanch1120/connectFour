from board import Board
from node import Node


class HumanPlayer:
    def __init__(self, player):
        self.player = player

    def display(self, tree):
        print("\nPlayer Turn")
        for i in tree.board.gameBoard:
            print(i)

    def move(self, depth=None, tree=None, isMax=None):
        while True:
            inp = input("\nEnter Row Number to Drop Piece: ")
            if not (isinstance(inp, int)):
                print("Bad Input:", inp, "is not an integer")
                continue
            return [None, int(inp)]
