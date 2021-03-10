from node import Node
from board import Board
from computerPlayer import ComputerPlayer as cp
from humanPlayer import HumanPlayer as hp
import copy

class Engine:
    def __init__(self, b, d, startingPlayer, mode):
        self.turns = 0
        self.b = b
        self.MAX_DEPTH = d
        self.player = startingPlayer
        self.interactive = mode
        self.root = self.initiate(self.b, self.player, self.MAX_DEPTH)

    # Plays the game
    def playGame(self):
        players = []
        if self.player == 1:
            players = [cp(2), hp(1)]
        else:
            players = [hp(2), cp(1)]
        while self.turns != 42:
            self.b.updateBoard(players[self.player].move(self.MAX_DEPTH, self.root,self.player)[1], chr(self.player + 1))

            self.player = ((self.player + 1) % 2)
            self.turns += 1

    #   Determines lowest available slot for piece drop
    def drop(self, column):
        for i in range(5, -1, -1):
            if column[i] == '0':
                return i
        return None

    # Given a board, generates all possible turns
    def generatePossibleTurns(self, player, board):
        output = []
        for i in range(7):
            j = self.drop([board[0][i], board[1][i], board[2][i], board[3][i], board[4][i], board[5][i]])
            if j is None:
                continue
            else:
                temp = [list(board[0]), list(board[1]), list(board[2]), list(board[3]), list(board[4]), list(board[5])]
                temp[j][i] = player
                for k in range(len(temp)):
                    temp[k] = "".join(temp[k])
                output += [[temp, i + 1]]
        return output

    # Given a board, recursively generates all possible future moves
    # FIXME - Need to add alpha-beta pruning
    def generateTree(self, depth, state):
        if depth == 0:
            return None
        for i in self.generatePossibleTurns(str((state.player % 2) + 1), state.board.gameBoard):
            n = Node(Board(copy.deepcopy(i[0]), (state.player % 2) + 1), (state.player % 2) + 1, i[1])
            state.addChildren(n)
            self.generateTree(depth - 1, n)
        return state

    def initiate(self, board, startingPlayer, maxDepth):
        iRoot = self.generateTree(maxDepth, Node(board, startingPlayer, 0))
        return iRoot
