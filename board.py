class Board:

    def __init__(self, state, player):
        self.gameBoard = state
        self.player = player
        self.player1Score = 0
        self.player2Score = 0
        self.getPlayerScore()
        self.score = self.getScore()

    # Calls all functions to update scores
    def updateScores(self):
        self.getPlayerScore()
        self.score = self.getScore()

    # Given a move, updates the board
    def updateBoard(self, move, piece):
        for i in range(5, -1, -1):
            if self.gameBoard[i][move - 1] == '0':
                self.gameBoard[i] = self.gameBoard[i][:move - 1] + piece + self.gameBoard[i][move:]
                self.updateScores()
                return self.gameBoard

    # Checks number of free spaces around a given location
    def freeSpaces(self, x, y):

        emptySpaces = [0]
        if x > 0:
            if self.gameBoard[x - 1][y] == '0':
                emptySpaces[0] += 1
        if x < 5:
            if self.gameBoard[x + 1][y] == '0':
                emptySpaces[0] += 1
        if y > 0:
            if self.gameBoard[x][y - 1] == '0':
                emptySpaces[0] += 1
        if y < 6:
            if self.gameBoard[x][y + 1] == '0':
                emptySpaces[0] += 1
        if (x > 0) and (y > 0):
            if self.gameBoard[x - 1][y - 1] == '0':
                emptySpaces[0] += 1
        if (x < 5) and (y > 0):
            if self.gameBoard[x + 1][y - 1] == '0':
                emptySpaces[0] += 1
        if (x > 0) and (y < 6):
            if self.gameBoard[x - 1][y + 1] == '0':
                emptySpaces[0] += 1
        if (x < 5) and (y < 6):
            if self.gameBoard[x + 1][y + 1] == '0':
                emptySpaces[0] += 1
        return emptySpaces

    # Checks for diagonals in a row
    def checkDiagonals(self, arr, pSlope, piece):
        output = 0
        sFactor = 1
        check = ""
        row = ""
        if pSlope:
            sFactor = -1
        try:
            for i in arr:
                row += str(self.gameBoard[i[0]][i[1]])
                check += piece
            row += str(self.gameBoard[arr[-1][0] + 1][arr[-1][1] + sFactor])
        except IndexError:
            pass
        check += '0'
        if row == check:
            output += 1
        check = "0"
        try:
            row = str(self.gameBoard[arr[0][0] - 1][arr[0][1] - sFactor])
            for i in arr:
                row += str(self.gameBoard[i[0]][i[1]])
                check += piece
        except IndexError:
            pass
        if row == check:
            output += 1
        return output

    # Gets the minimax score of the board
    def getScore(self):
        output = 0
        # The current score of both players will impact the score
        output += (self.player1Score * 5)
        output -= (self.player2Score * 5)

        # Checks itself (adds points to score)
        for i in range(len(self.gameBoard)):
            for j in range(len(self.gameBoard[i])):
                # Checks for number of free spaces surrounding piece. Score increases by one for each
                if self.gameBoard[i][j] == '1':
                    output += self.freeSpaces(i, j)[0]
        # Checks horizontally for 2 or more in a row with open ends
        for row in self.gameBoard:
            # Checks for 2 in a row
            if (row[0:3] == "011") or (row[0:3] == "110"):
                output += 1
            if (row[1:4] == "011") or (row[1:4] == "110"):
                output += 1
            if (row[2:5] == "011") or (row[2:5] == "110"):
                output += 1
            if (row[3:6] == "011") or (row[3:6] == "110"):
                output += 1
            if (row[4:7] == "011") or (row[4:7] == "110"):
                output += 1
            # Checks for 3 in a row
            if (row[0:4] == "0111") or (row[0:4] == "1110"):
                output += 1
            if (row[1:5] == "0111") or (row[1:5] == "1110"):
                output += 1
            if (row[2:6] == "0111") or (row[2:6] == "1110"):
                output += 1
            if (row[3:7] == "0111") or (row[3:7] == "1110"):
                output += 1
            # Checks for 4 in a row
            if (row[0:5] == "01111") or (row[0:5] == "11110"):
                output += 1
            if (row[1:6] == "01111") or (row[1:6] == "11110"):
                output += 1
            if (row[2:7] == "01111") or (row[2:7] == "11110"):
                output += 1
            # Checks for 5 in a row
            if (row[0:6] == "01111") or (row[0:6] == "11110"):
                output += 1
            if (row[1:7] == "01111") or (row[1:7] == "11110"):
                output += 1
            # Checks for 6 in a row
            if (row[0:7] == "011111") or (row[0:7] == "111110"):
                output += 1
        # Checks vertically for 2 or more in a row with open ends
        for j in range(7):
            column = self.gameBoard[0][j] + self.gameBoard[1][j] + self.gameBoard[2][j] + self.gameBoard[3][j] + \
                     self.gameBoard[4][j] + self.gameBoard[5][j]
            # Checks for 2 in a row
            if (column[0:3] == "011") or (column[0:3] == "110"):
                output += 1
            if (column[1:4] == "011") or (column[1:4] == "110"):
                output += 1
            if (column[2:5] == "011") or (column[2:5] == "110"):
                output += 1
            if (column[3:6] == "011") or (column[3:6] == "110"):
                output += 1
            # Checks for 3 in a row
            if (column[0:4] == "0111") or (column[0:4] == "1110"):
                output += 1
            if (column[1:5] == "0111") or (column[1:5] == "1110"):
                output += 1
            if (column[2:6] == "0111") or (column[2:6] == "1110"):
                output += 1
            # Checks for 4 in a row
            if (column[0:5] == "01111") or (column[0:5] == "11110"):
                output += 1
            if (column[1:6] == "01111") or (column[1:6] == "11110"):
                output += 1
            # Checks for 5 in a row
            if (column[0:6] == "01111") or (column[0:6] == "11110"):
                output += 1
        # Checks diagonally for 2 or more in a row with open ends
        for i in range(len(self.gameBoard)):
            for j in range(len(self.gameBoard[i])):
                if i + 1 == j or i - 1 == j:
                    # Negative diagonal
                    if i < 5 and j < 6:
                        output += self.checkDiagonals([[i, j], [i + 1, j + 1]], False, '1')
                        output += self.checkDiagonals([[i, j], [i + 1, j + 1], [i + 2, j + 2]], False, '1')
                        output += self.checkDiagonals([[i, j], [i + 1, j + 1], [i + 2, j + 2], [i + 3, j + 3]], False,
                                                      '1')
                        output += self.checkDiagonals(
                            [[i, j], [i + 1, j + 1], [i + 2, j + 2], [i + 3, j + 3], [i + 4, j + 4]], False, '1')

                    # Positive diagonal
                    if i > 0 and j < 6:
                        output += self.checkDiagonals([[i, j], [i + 1, j - 1]], True, '1')
                        output += self.checkDiagonals([[i, j], [i + 1, j - 1], [i + 2, j - 2]], True, '1')
                        output += self.checkDiagonals([[i, j], [i + 1, j - 1], [i + 2, j - 2], [i + 3, j - 3]], True,
                                                      '1')
                        output += self.checkDiagonals(
                            [[i, j], [i + 1, j - 1], [i + 2, j - 2], [i + 3, j - 3], [i + 4, j - 4]], True, '1')

        # Checks opponent (subtracts points from score)
        for i in range(len(self.gameBoard)):
            for j in range(len(self.gameBoard[i])):
                # Checks for number of free spaces surrounding piece. Score increases by one for each
                if self.gameBoard[i][j] == '2':
                    output -= self.freeSpaces(i, j)[0]
        # Checks horizontally for 2 or more in a row with open ends
        for row in self.gameBoard:
            # Checks for 2 in a row
            if (row[0:3] == "022") or (row[0:3] == "220"):
                output -= 1
            if (row[1:4] == "022") or (row[1:4] == "220"):
                output -= 1
            if (row[2:5] == "022") or (row[2:5] == "220"):
                output -= 1
            if (row[3:6] == "022") or (row[3:6] == "220"):
                output -= 1
            if (row[4:7] == "022") or (row[4:7] == "220"):
                output -= 1
            # Checks for 3 in a row
            if (row[0:4] == "0222") or (row[0:4] == "2220"):
                output -= 1
            if (row[1:5] == "0222") or (row[1:5] == "2220"):
                output -= 1
            if (row[2:6] == "0222") or (row[2:6] == "2220"):
                output -= 1
            if (row[3:7] == "0222") or (row[3:7] == "2220"):
                output -= 1
            # Checks for 4 in a row
            if (row[0:5] == "02222") or (row[0:5] == "22220"):
                output -= 1
            if (row[1:6] == "02222") or (row[1:6] == "22220"):
                output -= 1
            if (row[2:7] == "02222") or (row[2:7] == "22220"):
                output -= 1
            # Checks for 5 in a row
            if (row[0:6] == "022222") or (row[0:6] == "222220"):
                output -= 1
            if (row[1:7] == "022222") or (row[1:7] == "222220"):
                output -= 1
            # Checks for 6 in a row
            if (row[0:7] == "0222222") or (row[0:7] == "2222220"):
                output -= 1
        # Checks vertically for 2 or more in a row with open ends
        for j in range(7):
            column = self.gameBoard[0][j] + self.gameBoard[1][j] + self.gameBoard[2][j] + self.gameBoard[3][j] + \
                     self.gameBoard[4][j] + self.gameBoard[5][j]
            # Checks for 2 in a row
            if (column[0:3] == "022") or (column[0:3] == "220"):
                output -= 1
            if (column[1:4] == "022") or (column[1:4] == "220"):
                output -= 1
            if (column[2:5] == "022") or (column[2:5] == "220"):
                output -= 1
            if (column[3:6] == "022") or (column[3:6] == "220"):
                output -= 1
            # Checks for 3 in a row
            if (column[0:4] == "0222") or (column[0:4] == "2220"):
                output -= 1
            if (column[1:5] == "0222") or (column[1:5] == "2220"):
                output -= 1
            if (column[2:6] == "0222") or (column[2:6] == "2220"):
                output -= 1
            # Checks for 4 in a row
            if (column[0:5] == "02222") or (column[0:5] == "22220"):
                output -= 1
            if (column[1:6] == "02222") or (column[1:6] == "22220"):
                output -= 1
            # Checks for 5 in a row
            if (column[0:6] == "022222") or (column[0:6] == "222220"):
                output -= 1
        # Checks diagonally for 2 or more in a row with open ends
        for i in range(len(self.gameBoard)):
            for j in range(len(self.gameBoard[i])):
                if i + 1 == j or i - 1 == j:
                    # Negative diagonal
                    if i < 5 and j < 6:
                        output -= self.checkDiagonals([[i, j], [i + 1, j + 1]], False, '2')
                        output -= self.checkDiagonals([[i, j], [i + 1, j + 1], [i + 2, j + 2]], False, '2')
                        output -= self.checkDiagonals([[i, j], [i + 1, j + 1], [i + 2, j + 2], [i + 3, j + 3]], False,
                                                      '2')
                        output -= self.checkDiagonals(
                            [[i, j], [i + 1, j + 1], [i + 2, j + 2], [i + 3, j + 3], [i + 4, j + 4]], False, '2')
                    # Positive diagonal
                    if i > 0 and j < 6:
                        output -= self.checkDiagonals([[i, j], [i + 1, j - 1]], True, '2')
                        output -= self.checkDiagonals([[i, j], [i + 1, j - 1], [i + 2, j - 2]], True, '2')
                        output -= self.checkDiagonals([[i, j], [i + 1, j - 1], [i + 2, j - 2], [i + 3, j - 3]], True,
                                                      '2')
                        output -= self.checkDiagonals(
                            [[i, j], [i + 1, j - 1], [i + 2, j - 2], [i + 3, j - 3], [i + 4, j - 4]], True, '2')

        return output

    # Gets the player's score of the board
    def getPlayerScore(self):
        self.player1Score = 0
        self.player2Score = 0
        # Check horizontally
        for row in self.gameBoard:
            # Check player 1
            if row[0:4] == '1' * 4:
                self.player1Score += 1
            if row[1:5] == '1' * 4:
                self.player1Score += 1
            if row[2:6] == '1' * 4:
                self.player1Score += 1
            if row[3:7] == '1' * 4:
                self.player1Score += 1
            # Check player 2
            if row[0:4] == '2' * 4:
                self.player2Score += 1
            if row[1:5] == '2' * 4:
                self.player2Score += 1
            if row[2:6] == '2' * 4:
                self.player2Score += 1
            if row[3:7] == '2' * 4:
                self.player2Score += 1

        # Check vertically
        for j in range(7):
            # Check player 1
            if (self.gameBoard[0][j] == '1' and self.gameBoard[1][j] == '1' and
                    self.gameBoard[2][j] == '1' and self.gameBoard[3][j] == '1'):
                self.player1Score += 1
            if (self.gameBoard[1][j] == '1' and self.gameBoard[2][j] == '1' and
                    self.gameBoard[3][j] == '1' and self.gameBoard[4][j] == '1'):
                self.player1Score += 1
            if (self.gameBoard[2][j] == '1' and self.gameBoard[3][j] == '1' and
                    self.gameBoard[4][j] == '1' and self.gameBoard[5][j] == '1'):
                self.player1Score += 1
            # Check player 2
            if (self.gameBoard[0][j] == '2' and self.gameBoard[1][j] == '2' and
                    self.gameBoard[2][j] == '2' and self.gameBoard[3][j] == '2'):
                self.player2Score += 1
            if (self.gameBoard[1][j] == '2' and self.gameBoard[2][j] == '2' and
                    self.gameBoard[3][j] == '2' and self.gameBoard[4][j] == '2'):
                self.player2Score += 1
            if (self.gameBoard[2][j] == '2' and self.gameBoard[3][j] == '2' and
                    self.gameBoard[4][j] == '2' and self.gameBoard[5][j] == '2'):
                self.player2Score += 1

        # Check diagonally

        # Check player 1
        if (self.gameBoard[2][0] == '1' and self.gameBoard[3][1] == '1' and
                self.gameBoard[4][2] == '1' and self.gameBoard[5][3] == '1'):
            self.player1Score += 1
        if (self.gameBoard[1][0] == '1' and self.gameBoard[2][1] == '1' and
                self.gameBoard[3][2] == '1' and self.gameBoard[4][3] == '1'):
            self.player1Score += 1
        if (self.gameBoard[2][1] == '1' and self.gameBoard[3][2] == '1' and
                self.gameBoard[4][3] == '1' and self.gameBoard[5][4] == '1'):
            self.player1Score += 1
        if (self.gameBoard[0][0] == '1' and self.gameBoard[1][1] == '1' and
                self.gameBoard[2][2] == '1' and self.gameBoard[3][3] == '1'):
            self.player1Score += 1
        if (self.gameBoard[1][1] == '1' and self.gameBoard[2][2] == '1' and
                self.gameBoard[3][3] == '1' and self.gameBoard[4][4] == '1'):
            self.player1Score += 1
        if (self.gameBoard[2][2] == '1' and self.gameBoard[3][3] == '1' and
                self.gameBoard[4][4] == '1' and self.gameBoard[5][5] == '1'):
            self.player1Score += 1
        if (self.gameBoard[0][1] == '1' and self.gameBoard[1][2] == '1' and
                self.gameBoard[2][3] == '1' and self.gameBoard[3][4] == '1'):
            self.player1Score += 1
        if (self.gameBoard[1][2] == '1' and self.gameBoard[2][3] == '1' and
                self.gameBoard[3][4] == '1' and self.gameBoard[4][5] == '1'):
            self.player1Score += 1
        if (self.gameBoard[2][3] == '1' and self.gameBoard[3][4] == '1' and
                self.gameBoard[4][5] == '1' and self.gameBoard[5][6] == '1'):
            self.player1Score += 1
        if (self.gameBoard[0][2] == '1' and self.gameBoard[1][3] == '1' and
                self.gameBoard[2][4] == '1' and self.gameBoard[3][5] == '1'):
            self.player1Score += 1
        if (self.gameBoard[1][3] == '1' and self.gameBoard[2][4] == '1' and
                self.gameBoard[3][5] == '1' and self.gameBoard[4][6] == '1'):
            self.player1Score += 1
        if (self.gameBoard[0][3] == '1' and self.gameBoard[1][4] == '1' and
                self.gameBoard[2][5] == '1' and self.gameBoard[3][6] == '1'):
            self.player1Score += 1

        if (self.gameBoard[0][3] == '1' and self.gameBoard[1][2] == '1' and
                self.gameBoard[2][1] == '1' and self.gameBoard[3][0] == '1'):
            self.player1Score += 1
        if (self.gameBoard[0][4] == '1' and self.gameBoard[1][3] == '1' and
                self.gameBoard[2][2] == '1' and self.gameBoard[3][1] == '1'):
            self.player1Score += 1
        if (self.gameBoard[1][3] == '1' and self.gameBoard[2][2] == '1' and
                self.gameBoard[3][1] == '1' and self.gameBoard[4][0] == '1'):
            self.player1Score += 1
        if (self.gameBoard[0][5] == '1' and self.gameBoard[1][4] == '1' and
                self.gameBoard[2][3] == '1' and self.gameBoard[3][2] == '1'):
            self.player1Score += 1
        if (self.gameBoard[1][4] == '1' and self.gameBoard[2][3] == '1' and
                self.gameBoard[3][2] == '1' and self.gameBoard[4][1] == '1'):
            self.player1Score += 1
        if (self.gameBoard[2][3] == '1' and self.gameBoard[3][2] == '1' and
                self.gameBoard[4][1] == '1' and self.gameBoard[5][0] == '1'):
            self.player1Score += 1
        if (self.gameBoard[0][6] == '1' and self.gameBoard[1][5] == '1' and
                self.gameBoard[2][4] == '1' and self.gameBoard[3][3] == '1'):
            self.player1Score += 1
        if (self.gameBoard[1][5] == '1' and self.gameBoard[2][4] == '1' and
                self.gameBoard[3][3] == '1' and self.gameBoard[4][2] == '1'):
            self.player1Score += 1
        if (self.gameBoard[2][4] == '1' and self.gameBoard[3][3] == '1' and
                self.gameBoard[4][2] == '1' and self.gameBoard[5][1] == '1'):
            self.player1Score += 1
        if (self.gameBoard[1][6] == '1' and self.gameBoard[2][5] == '1' and
                self.gameBoard[3][4] == '1' and self.gameBoard[4][3] == '1'):
            self.player1Score += 1
        if (self.gameBoard[2][5] == '1' and self.gameBoard[3][4] == '1' and
                self.gameBoard[4][3] == '1' and self.gameBoard[5][2] == '1'):
            self.player1Score += 1
        if (self.gameBoard[2][6] == '1' and self.gameBoard[3][5] == '1' and
                self.gameBoard[4][4] == '1' and self.gameBoard[5][3] == '1'):
            self.player1Score += 1

        # Check player 2
        if (self.gameBoard[2][0] == '2' and self.gameBoard[3][1] == '2' and
                self.gameBoard[4][2] == '2' and self.gameBoard[5][3] == '2'):
            self.player2Score += 1
        if (self.gameBoard[1][0] == '2' and self.gameBoard[2][1] == '2' and
                self.gameBoard[3][2] == '2' and self.gameBoard[4][3] == '2'):
            self.player2Score += 1
        if (self.gameBoard[2][1] == '2' and self.gameBoard[3][2] == '2' and
                self.gameBoard[4][3] == '2' and self.gameBoard[5][4] == '2'):
            self.player2Score += 1
        if (self.gameBoard[0][0] == '2' and self.gameBoard[1][1] == '2' and
                self.gameBoard[2][2] == '2' and self.gameBoard[3][3] == '2'):
            self.player2Score += 1
        if (self.gameBoard[1][1] == '2' and self.gameBoard[2][2] == '2' and
                self.gameBoard[3][3] == '2' and self.gameBoard[4][4] == '2'):
            self.player2Score += 1
        if (self.gameBoard[2][2] == '2' and self.gameBoard[3][3] == '2' and
                self.gameBoard[4][4] == '2' and self.gameBoard[5][5] == '2'):
            self.player2Score += 1
        if (self.gameBoard[0][1] == '2' and self.gameBoard[1][2] == '2' and
                self.gameBoard[2][3] == '2' and self.gameBoard[3][4] == '2'):
            self.player2Score += 1
        if (self.gameBoard[1][2] == '2' and self.gameBoard[2][3] == '2' and
                self.gameBoard[3][4] == '2' and self.gameBoard[4][5] == '2'):
            self.player2Score += 1
        if (self.gameBoard[2][3] == '2' and self.gameBoard[3][4] == '2' and
                self.gameBoard[4][5] == '2' and self.gameBoard[5][6] == '2'):
            self.player2Score += 1
        if (self.gameBoard[0][2] == '2' and self.gameBoard[1][3] == '2' and
                self.gameBoard[2][4] == '2' and self.gameBoard[3][5] == '2'):
            self.player2Score += 1
        if (self.gameBoard[1][3] == '2' and self.gameBoard[2][4] == '2' and
                self.gameBoard[3][5] == '2' and self.gameBoard[4][6] == '2'):
            self.player2Score += 1
        if (self.gameBoard[0][3] == '2' and self.gameBoard[1][4] == '2' and
                self.gameBoard[2][5] == '2' and self.gameBoard[3][6] == '2'):
            self.player2Score += 1

        if (self.gameBoard[0][3] == '2' and self.gameBoard[1][2] == '2' and
                self.gameBoard[2][1] == '2' and self.gameBoard[3][0] == '2'):
            self.player2Score += 1
        if (self.gameBoard[0][4] == '2' and self.gameBoard[1][3] == '2' and
                self.gameBoard[2][2] == '2' and self.gameBoard[3][1] == '2'):
            self.player2Score += 1
        if (self.gameBoard[1][3] == '2' and self.gameBoard[2][2] == '2' and
                self.gameBoard[3][1] == '2' and self.gameBoard[4][0] == '2'):
            self.player2Score += 1
        if (self.gameBoard[0][5] == '2' and self.gameBoard[1][4] == '2' and
                self.gameBoard[2][3] == '2' and self.gameBoard[3][2] == '2'):
            self.player2Score += 1
        if (self.gameBoard[1][4] == '2' and self.gameBoard[2][3] == '2' and
                self.gameBoard[3][2] == '2' and self.gameBoard[4][1] == '2'):
            self.player2Score += 1
        if (self.gameBoard[2][3] == '2' and self.gameBoard[3][2] == '2' and
                self.gameBoard[4][1] == '2' and self.gameBoard[5][0] == '2'):
            self.player2Score += 1
        if (self.gameBoard[0][6] == '2' and self.gameBoard[1][5] == '2' and
                self.gameBoard[2][4] == '2' and self.gameBoard[3][3] == '2'):
            self.player2Score += 1
        if (self.gameBoard[1][5] == '2' and self.gameBoard[2][4] == '2' and
                self.gameBoard[3][3] == '2' and self.gameBoard[4][2] == '2'):
            self.player2Score += 1
        if (self.gameBoard[2][4] == '2' and self.gameBoard[3][3] == '2' and
                self.gameBoard[4][2] == '2' and self.gameBoard[5][1] == '2'):
            self.player2Score += 1
        if (self.gameBoard[1][6] == '2' and self.gameBoard[2][5] == '2' and
                self.gameBoard[3][4] == '2' and self.gameBoard[4][3] == '2'):
            self.player2Score += 1
        if (self.gameBoard[2][5] == '2' and self.gameBoard[3][4] == '2' and
                self.gameBoard[4][3] == '2' and self.gameBoard[5][2] == '2'):
            self.player2Score += 1
        if (self.gameBoard[2][6] == '2' and self.gameBoard[3][5] == '2' and
                self.gameBoard[4][4] == '2' and self.gameBoard[5][3] == '2'):
            self.player2Score += 1
