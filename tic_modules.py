board = [
     '-','-','-',
     '-','-','-',
     '-','-','-']

def print_board(board):
    print(f'\n{board[0]} | {board[1]} | {board[2]}')
    print("----------")
    print(board[3] + " | " + board[4] + ' | ' + board[5])
    print("----------")
    print(f'{board[6]} | {board[7]} | {board[8]} \n')

def bot_won():
    print_board(board)
    print("Bot Won.")
    quit()

def checkboard(board):
    while True:
        if board[0] == "X" and board[1] == "X" and board[2] == "X":
            print_board(board)
            print("User Won!")
            quit()
        if board[3] == "X" and board[4] == "X" and board[5] == "X":
            print_board(board)
            print("User Won!")
            quit()
        if board[6] == "X" and board[7] == "X" and board[8] == "X":
            print_board(board)
            print("User Won!")
            quit()
        if board[0] == "X" and board[3] == "X" and board[6] == "X":
            print_board(board)
            print("User Won!")
            quit()
        if board[1] == "X" and board[4] == "X" and board[7] == "X":
            print_board(board)
            print("User Won!")
            quit()
        if board[2] == "X" and board[5] == "X" and board[8] == "X":
            print_board(board)
            print("User Won!")
            quit()
        if board[0] == "X" and board[4] == "X" and board[8] == "X":
            print_board(board)
            print("User Won!")
            quit()
        if board[2] == "X" and board[4] == "X" and board[6] == "X":
            print_board(board)
            print("User Won!")
            quit()
        else:
            break

def bot_checkboard(board):
    while True:
        if board[0] == "O" and board[1] == "O" and board[2] == "O":
            bot_won()
        if board[3] == "O" and board[4] == "O" and board[5] == "O":
            bot_won()
        if board[6] == "O" and board[7] == "O" and board[8] == "O":
            bot_won()
        if board[0] == "O" and board[3] == "O" and board[6] == "O":
            bot_won()
        if board[1] == "O" and board[4] == "O" and board[7] == "O":
            bot_won()
        if board[2] == "O" and board[5] == "O" and board[8] == "O":
            bot_won()
        if board[0] == "O" and board[4] == "O" and board[8] == "O":
            bot_won()
        if board[2] == "O" and board[4] == "O" and board[6] == "O":
            bot_won()
        else:
            break

        