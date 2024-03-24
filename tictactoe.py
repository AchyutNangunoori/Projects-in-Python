board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
game = "Running"
mark = 'X'
def drawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")
def checkPosition(x):
    if board[x] == ' ':
        return True
    else:
        return False
def checkWin():
    global game
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        game = "Win"
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        game = "Win"
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        game = "Win"
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        game = "Win"
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        game = "Win"
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        game = "Win"
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        game = "Win"
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        game = "Win"
    elif board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        game = "Draw"
    else:
        game = "Running"
print("WELCOME To Tic-Tac-Toe Game")
print("Player1 - X")
print("Player2 - O")
for i in range(9):
    drawBoard()
    if(i%2==0):
        print("Player1's Turn")
        mark='X'
    else:
        print("Player2's Turn")
        mark='O'
    print("Enter the cell which you want to mark")
    ch=int(input())
    while(ch>9):
        print("Enter a valid Cell Number")
        ch=int(input())
    while((checkPosition(ch))!=True):
        print("The cell has been occupied already")
        print("Please chose a different cell")
        ch=int(input())
    if(checkPosition(ch)):
        board[ch]=mark
        checkWin()
        if(game=="Win"):
            if(i%2==0):
                print("Player 1 Wins")
            else:
                print("Player 2 Wins")
            break
        if(game=="Draw"):
            print("Game Tied")
            break
