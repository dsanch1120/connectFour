import copy
import os
import sys
from board import Board
from node import Node

visited = set()

# Handles the arguments given
def handle_args():
    # Ensures correct number of arguments
    if len(sys.argv) != 5:
        exit("Incorrect number of arguments\n"
             "Format Expected:\n"
             "$ python main.py [interactive] [path/to/file] [computer-next/human-next] [depth]\n"
             "or\n"
             "$ python main.py [one-move] [input_file] [output_file] [depth]")
    else:
        error_output = ""
        # Handles an "interactive" game input"
        if sys.argv[1].upper() == "INTERACTIVE":
            if not (sys.argv[3].upper() == "COMPUTER-NEXT" or sys.argv[3].upper() == "HUMAN-NEXT"):
                error_output += "Error in third argument (" + sys.argv[3] + "): Must be \"computer-next\" or " \
                                                                            "\"human-next\"\n"
            if not (sys.argv[4].isdigit()):
                error_output += "Error in fourth argument (" + sys.argv[4] + "): Must be integer value > 0\n"
        # Handles a "one-move" game input
        elif sys.argv[1].upper() == "ONE-MOVE":
            if not (sys.argv[4].isdigit()):
                error_output += "Error in fourth argument (" + sys.argv[4] + "): Must be integer value > 0\n"
        # Handles an improper game-type input
        else:
            error_output = "Error in first argument (" + sys.argv[
                1] + "): Must be \"interactive\" or \"one-move\"\n" + error_output
        # Exits program with error code if problems exist in arguments
        if error_output != "":
            exit(error_output[:-1])
        # Returns list of relevant system arguments.
        return [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]


# Uses the input given from the input file and creates a board object from it
def createBoard(layout):
    if not os.path.isfile(layout):
        return Board(["0000000", "0000000", "0000000", "0000000", "0000000", "0000000"])
    else:
        f = open(layout, "r")
        if f.mode != 'r':
            exit("Error reading given file")
        contents = f.readlines()
        for i in range(len(contents)):
            contents[i] = contents[i][:-1]
        return Board(contents[:-1])


# Helper function for generate Possible Turns
#   Determines lowest available slot for piece drop
def drop(column):
    for i in range(5, -1, -1):
        if column[i] == '0':
            return i
    return None


# Given a board, generates all possible turns
def generatePossibleTurns(player, board):
    output = []
    for i in range(7):
        j = drop([board[0][i], board[1][i], board[2][i], board[3][i], board[4][i], board[5][i]])
        if j is None:
            continue
        else:
            temp = [list(board[0]), list(board[1]), list(board[2]), list(board[3]), list(board[4]), list(board[5])]
            temp[j][i] = player
            for k in range(len(temp)):
                temp[k] = "".join(temp[k])
            output += [temp]
    return output


def generateTree(depth, state):
    if depth == 0:
        return None
    for i in generatePossibleTurns(str((state.player % 2) + 1), state.board.gameBoard):
        n = Node(Board(copy.deepcopy(i)), (state.player % 2) + 1)

        state.addChildren(n)
        generateTree(depth - 1, n)
    return state


def initiate(board, startingPlayer, maxDepth):
    iRoot = generateTree(maxDepth, Node(board, startingPlayer))
    return iRoot


if __name__ == '__main__':
    # args = handle_args()
    args = ["interactive", "input1.txt", "human-next", "3"]
    if args[2].upper() == "HUMAN-NEXT":
        args[2] = 1
    else:
        args[2] = 2
    b = createBoard(args[1])
    root = initiate(b, args[2], int(args[3]))
    print("Program ran successfully")
