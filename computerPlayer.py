from node import Node


class ComputerPlayer:

    def __init__(self, player):
        self.player = player
        self.max = False
        if player == 1:
            self.max = True

    def miniMax(self, depth, tree, isMax):
        # Base case. Returns score if maximum depth is reached
        if depth == 0:
            return tree.score
        # Maximizing player
        if isMax:
            bestVal = -1000000
            for i in tree.children:
                value = self.miniMax(depth - 1, i, False)
                bestVal = max(bestVal, value)
            return bestVal
        # Minimizing player
        else:
            bestVal = 1000000
            for i in tree.children:
                value = self.miniMax(depth - 1, i, True)
                bestVal = min(bestVal, value)
            return bestVal
