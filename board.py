# Game board

class Board:

    winningChar = 'x'
    currPlayer = 'x'
    board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]

    def __init__(self):
        self.player = 0


    def printBoard(self):
        printStr = "Player " + str(self.currPlayer) + "'s turn, enter character(1-9)\n"
        for inner in self.board:
            printStr += "| "
            for item in inner:
                printStr += str(item) + " | "
            printStr += "\n"
        print(printStr)

    # place new character on board in given space
    # if space is occupied log warning and have same player try again
    def placeCharacter(self, position):
        row, col = 0, 0
        pos = position - 1
        if pos < 3 and pos > -1:
            col = pos
            row = 0
        elif pos < 6:
            row = 1
            col = pos - 3
        elif pos < 9:
            row = 2
            col = pos - 6
        else:
            print("must choose position in (1-9)")
            return

        # return if space is taken
        checkChar = self.board[row][col]
        if checkChar.lower() != '_':
            print("space taken, choose again")
            return

        if self.currPlayer == 'x':
            checkChar = 'x'
            self.currPlayer = 'o'
        else:
            checkChar = 'o'
            self.currPlayer = 'x'

        self.board[row][col] = checkChar


    def isDone(self):
        if self.board[0][0] == 'x' and self.board[0][1] == 'x' and self.board[0][2] == 'x':
            self.winningChar = 'x'
            return True
        elif self.board[0][0] == 'o' and self.board[0][1] == 'o' and self.board[0][2] == 'o':
            self.winningChar = 'o'
            return True
        elif self.board[1][0] == 'x' and self.board[1][1] == 'x' and self.board[1][2] == 'x':
            self.winningChar = 'x'
            return True
        elif self.board[1][0] == 'o' and self.board[1][1] == 'o' and self.board[1][2] == 'o':
            self.winningChar = 'o'
            return True
        elif self.board[2][0] == 'x' and self.board[2][1] == 'x' and self.board[2][2] == 'x':
            self.winningChar = 'x'
            return True
        elif self.board[2][0] == 'o' and self.board[2][1] == 'o' and self.board[2][2] == 'o':
            self.winningChar = 'o'
            return True
        elif self.board[0][0] == 'x' and self.board[1][0] == 'x' and self.board[2][0] == 'x':
            self.winningChar = 'x'
            return True
        elif self.board[0][0] == 'o' and self.board[1][0] == 'o' and self.board[2][0] == 'o':
            self.winningChar = 'o'
            return True
        elif self.board[0][1] == 'x' and self.board[1][1] == 'x' and self.board[2][1] == 'x':
            self.winningChar = 'x'
            return True
        elif self.board[0][1] == 'o' and self.board[1][1] == 'o' and self.board[2][1] == 'o':
            self.winningChar = 'o'
            return True
        elif self.board[0][2] == 'x' and self.board[1][2] == 'x' and self.board[2][2] == 'x':
            self.winningChar = 'x'
            return True
        elif self.board[0][2] == 'o' and self.board[1][2] == 'o' and self.board[2][2] == 'o':
            self.winningChar = 'o'
            return True
        elif self.board[0][0] == 'x' and self.board[1][1] == 'x' and self.board[2][2] == 'x':
            self.winningChar = 'x'
            return True
        elif self.board[0][0] == 'o' and self.board[1][1] == 'o' and self.board[2][2] == 'o':
            self.winningChar = 'o'
            return True
        elif self.board[0][2] == 'x' and self.board[1][1] == 'x' and self.board[2][0] == 'x':
            self.winningChar = 'x'
            return True
        elif self.board[0][2] == 'o' and self.board[1][1] == 'o' and self.board[2][0] == 'o':
            self.winningChar = 'o'
            return True
        else:
            for row in self.board:
                for col in row:
                    if col == '_':
                        return False
            self.winningChar = '_'
            return True
