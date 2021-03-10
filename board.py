class Board:

    def __init__(self, state, player):
        self.gameBoard = state
        self.player = player
        self.player1Score = 0
        self.player2Score = 0
        self.getPlayerScore()
        self.score = self.getScore()

    # Given a move, updates the board
    def updateBoard(self, move, piece):
        for i in range(5, -1, -1):
            if self.gameBoard[i][move] == '0':
                self.gameBoard[i] = self.gameBoard[i][:move-1] + piece + self.gameBoard[i][move:]

    # Checks number of free spaces around a given location
    def freeSpaces(self, x, y):

        emptySpaces = 0
        if x > 0:
            if self.gameBoard[x - 1][y] == '0':
                emptySpaces += 1
        if x < 5:
            if self.gameBoard[x + 1][y] == '0':
                emptySpaces += 1
        if y > 0:
            if self.gameBoard[x][y - 1] == '0':
                emptySpaces += 1
        if y < 6:
            if self.gameBoard[x][y + 1] == '0':
                emptySpaces += 1
        if (x > 0) and (y > 0):
            if self.gameBoard[x - 1][y - 1] == '0':
                emptySpaces += 1
        if (x < 5) and (y > 0):
            if self.gameBoard[x + 1][y - 1] == '0':
                emptySpaces += 1
        if (x > 0) and (y < 6):
            if self.gameBoard[x - 1][y + 1] == '0':
                emptySpaces += 1
        if (x < 5) and (y < 6):
            if self.gameBoard[x + 1][y + 1] == '0':
                emptySpaces += 1
        return emptySpaces

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
                    output += self.freeSpaces(i, j)

        # Checks opponent (subtracts points from score)
        for i in range(len(self.gameBoard)):
            for j in range(len(self.gameBoard[i])):
                # Checks for number of free spaces surrounding piece. Score increases by one for each
                if self.gameBoard[i][j] == '2':
                    output -= self.freeSpaces(i, j)

        return output

    # Gets the player's score of the board
    def getPlayerScore(self):
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
