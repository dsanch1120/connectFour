from board import Board


class Node:

    def __init__(self, board, player):
        self.board = board
        self.score = board.score
        self.children = []
        self.player = player

    def addChildren(self, child):
        self.children.append(child)
