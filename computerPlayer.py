from node import Node


class ComputerPlayer:

    def __init__(self, player):
        self.player = player
        self.max = False
        self.human = False
        if player == 1:
            self.max = True

    def display(self, tree):
        print("\nComputer Turn")
        for i in tree.board.gameBoard:
            print(i)

    def move(self, depth, tree, isMax):
        return self.minimax(depth, tree, isMax)

    def minimax(self, depth, tree, isMax):
        global bestMove
        if isMax == 0:
            isMax = True
        else:
            isMax = False
        # Base case. Returns score if maximum depth is reached
        if depth == 0:
            return [tree.score, tree.move]
        # Maximizing player
        if isMax:
            bestVal = -1000000
            for i in tree.children:
                value = self.minimax(depth - 1, i, False)[0]
                bestVal = max(bestVal, value)
                if bestVal == value:
                    bestMove = i.move
            return [bestVal, bestMove]
        # Minimizing player
        else:
            bestVal = 1000000
            for i in tree.children:
                value = self.minimax(depth - 1, i, True)[0]
                bestVal = min(bestVal, value)
                if bestVal == value:
                    bestMove = i.move
            return [bestVal, bestMove]
