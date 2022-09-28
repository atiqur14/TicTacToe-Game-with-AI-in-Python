board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Match Draw!")
            exit()
        if checkForWin():
            if letter == '$':
                print("Computer Wins!")
                exit()
            else:
                print("Human Wins!")
                exit()

        return


    else:
        print("Can't insert there!")
        position = int(input("Please Choose Another Option: "))
        insertLetter(letter, position)
        return


def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def checkforCompWon(comp):
    if board[1] == board[2] and board[1] == board[3] and board[1] == comp:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == comp):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == comp):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == comp):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == comp):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == comp):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == comp):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == comp):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


def playerMove():
    position = int(input("Enter Your Option 'HUMAN': "))
    insertLetter(player, position)
    return


def compMove():
    bestScore = -1000
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return


def minimax(board, depth, isMaximizing):
    if (checkforCompWon(bot)):
        return 1
    elif (checkforCompWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -1000
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 1000
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore



printBoard(board)
print("Computer goes first! Good luck!")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("Computer Sign_$")
print("Human Sign_@")
print("\n")

player = '@'
bot = '$'

global firstComputerMove
firstComputerMove = True

while not checkForWin():
    compMove()
    playerMove()