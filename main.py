import copy
import os
import sys
from board import Board
from node import Node
from engine import Engine

first = 1


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
def createBoard(layout, player):
    if not os.path.isfile(layout):
        return Board(["0000000", "0000000", "0000000", "0000000", "0000000", "0000000"], player)
    else:
        f = open(layout, "r")
        if f.mode != 'r':
            exit("Error reading given file")
        contents = f.readlines()
        for i in range(len(contents)):
            contents[i] = contents[i][:-1]
        first = int(contents[-1][:-1])
        return Board(contents[:-1], player)


if __name__ == '__main__':
    # args = handle_args()
    args = ["interactive", "input1.txt", "computer-next", "5"]
    if args[0].upper() == "INTERACTIVE":
        args[0] = True
    else:
        args[0] = False
    b = createBoard(args[1], first)
    if args[2].upper() == "HUMAN-NEXT":
        args[2] = 1
        e = Engine(b, int(args[3]), args[2], args[0])
    elif args[2].upper() == "COMPUTER-NEXT":
        args[2] = 2
        e = Engine(b, int(args[3]), args[2], args[0])
    else:
        e = Engine(b, int(args[3]), first, args[0], args[2][:-1])

    e.playGame()
    # root = initiate(b, args[2], int(args[3]))
    print("Program ran successfully")
