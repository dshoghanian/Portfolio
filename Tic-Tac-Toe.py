# 6.7 LAB: Tic-Tac-Toe

# Write a program that allows users to play a friendly game of Tic-Tac-Toe. Each player will enter the index in the 2D list where they want to place their next token.

# Board indices:

# 0|1|2
# -+-+-
# 3|4|5
# -+-+-
# 6|7|8
# Request user input and verify that it falls within the expected range
# 1.5. If the input is "q", exit the loop and print "Goodbye!".
# Place the token on the game board
# Print the board
# You do not have to verify that the space is empty or whether the game is over or not.

ticTacToeGrid = [[" "] * 3 for _ in range(3)]
gameContinues = True
divider = '-+-+-'
activePlayer = 'X'

while gameContinues:
    playerChoice = input(f"\t{activePlayer}'s turn\n")
    if playerChoice.lower() == 'q':
        print('Goodbye!')
        gameContinues = False
        exit()
    playerChoice = int(playerChoice)

    if playerChoice < 3:
        ticTacToeGrid[0][playerChoice] = f"{activePlayer}"
    elif playerChoice < 6:
        ticTacToeGrid[1][playerChoice % 3] = f"{activePlayer}"
    elif playerChoice < 9:
        ticTacToeGrid[2][playerChoice % 3] = f"{activePlayer}"

    for index in range(5):
        if index % 2 == 0:
            print(
                ticTacToeGrid[index // 2][0],
                "|",
                ticTacToeGrid[index // 2][1],
                "|",
                ticTacToeGrid[index // 2][2],
                sep=""
            )
        else:
            print(divider)

    activePlayer = 'O' if activePlayer == 'X' else 'X'
    
