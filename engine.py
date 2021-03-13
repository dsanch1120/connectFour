from node import Node
from board import Board
from computerPlayer import ComputerPlayer as cp
from humanPlayer import HumanPlayer as hp
import copy

class Engine:
    def __init__(self, b, d, startingPlayer, mode, output=None):
        self.turns = 0
        self.b = b
        self.MAX_DEPTH = d
        self.player = startingPlayer
        self.interactive = mode
        self.root = self.initiate(self.b, self.player, self.MAX_DEPTH)
        self.outputFile = output

    # Plays the game
    def playGame(self):
        if not self.interactive:
            self.playOneMove()
            return
        players = []
        if self.player == 1:
            players = [cp(2), hp(1)]
        else:
            self.player = 1
            players = [hp(2), cp(1)]
        while self.turns != 42:
            players[self.player].display(self.root)
            print("Player 1 Score: %d" % self.b.player1Score)
            print("Player 2 Score: %d" % self.b.player2Score)
            while True:
                m = players[self.player].move(self.MAX_DEPTH, self.root,self.player)[1]
                if (m < 1) or (m > 7):
                    print("Bad Input: Column %d does not exist. Choose column between 1 and 7" % m)
                    continue
                if self.b.gameBoard[0][m-1] == '0':
                    break
                else:
                    print("Bad Input: Column Full")

            for i in self.root.children:
                if m == i.move:
                    self.root = copy.deepcopy(i)
            #self.b.gameBoard = self.root.board
            self.b = self.root.board
            # self.b.gameBoard = copy.deepcopy(self.b.updateBoard(m, str(self.player + 1)))
            self.b.getPlayerScore()
            self.player = ((self.player + 1) % 2)

            self.root = self.generateTree(self.MAX_DEPTH, Node(self.b, self.player, self.root.move))
            self.turns += 1
        self.determineWinner()

    def playOneMove(self):
        print("One move")


    # Based upon player scores, determines the winner of the game
    def determineWinner(self):
        if self.b.player1Score > self.b.player2Score:
            print("\n\n***************************************")
            print("**** Player 1 wins with score of %d ****" % self.b.player1Score)
            print("***************************************")

        else:
            print("\n\n***************************************")
            print("**** Player 2 wins with score of %d ****" % self.b.player2Score)
            print("***************************************")

    # Determines lowest available slot for piece drop
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
        if depth != 0 and len(state.children) == 0:
            for i in self.generatePossibleTurns(str((state.player % 2) + 1), state.board.gameBoard):
                n = Node(Board(copy.deepcopy(i[0]), (state.player % 2) + 1), (state.player % 2) + 1, i[1])
                state.addChildren(n)
                self.generateTree(depth - 1, n)
        else:
            for i in range(len(state.children)):
                self.generateTree(depth - 1, state.children[i])
        return state

    def initiate(self, board, startingPlayer, maxDepth):
        iRoot = self.generateTree(maxDepth, Node(board, startingPlayer, 0))
        return iRoot
