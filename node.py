from board import Board


class Node:

    def __init__(self, board, player, move):
        self.board = board
        self.score = board.score
        self.children = []
        self.player = player
        self.move = move

    def addChildren(self, child):
        self.children.append(child)
