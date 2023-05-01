# imports
import board

# TicTackToe game
game = board.Board()

# game loop
while game.isDone() is False:
    game.printBoard()
    move = input()
    if move.isdigit():
        move = int(move)
        game.placeCharacter(move)
    else:
        print("Invalid input")

game.printBoard()
if game.winningChar != '_':
    print("Player " + str(game.winningChar) + " wins!")
else:
    print("Game ends in tie")
