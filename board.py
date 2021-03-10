class Board:

    def __init__(self, state):
        self.gameBoard = state
        self.player1Score = 0
        self.player2Score = 0
        self.score = self.getScore()
        self.getPlayerScore()

    def getScore(self):
        return 0

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
