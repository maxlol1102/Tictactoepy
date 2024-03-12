PLAYER = 'X'
BOT = 'O'

def printBoard(board):
    print('-------------')
    for i in range(0, 9, 3):
        print(f'| {board[i]} | {board[i + 1]} | {board[i + 2]} |')
        print('-------------')
    print("\n")

def checkForWin():
    for line in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        if board[line[0]] == board[line[1]] == board[line[2]] != ' ':
            return True
    return False

def checkDraw():
    return ' ' not in board

def playerMove():
    while True:
        position = int(input("Enter the move that you want to make: "))
        if 1 <= position <= 9 and board[position - 1] == ' ':
            board[position - 1] = PLAYER
            break
        else:
            print("Invalid move. Please try again.")

def compMove():
    bestScore = -800
    bestMove = 0
    for key, value in enumerate(board):
        if value == ' ':
            board[key] = BOT
            score = minimax(board, 0, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key + 1

    board[bestMove - 1] = BOT

def minimax(board, depth, isMaximizing):
    if checkWhichMarkWon(BOT):
        return 1
    elif checkWhichMarkWon(PLAYER):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -800
        for key, value in enumerate(board):
            if value == ' ':
                board[key] = BOT
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 800
        for key, value in enumerate(board):
            if value == ' ':
                board[key] = PLAYER
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                bestScore = min(score, bestScore)
        return bestScore

def checkWhichMarkWon(mark):
    for line in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        if board[line[0]] == board[line[1]] == board[line[2]] == mark:
            return True
    return False

board = [' '] * 9

printBoard(board)
print("You go first! Try your best")
print("Positions are as follows:")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |")
print("\n")

while not checkForWin():
    playerMove()
    printBoard(board)
    if checkForWin():
        break
    compMove()
    printBoard(board)


if checkWhichMarkWon(PLAYER):
    print("Congratulations, You win!")
elif checkWhichMarkWon(BOT):
    print("You tried your best. Thank you for playing.")
else:
    print("It's a Tie! Thank you for playing.")
