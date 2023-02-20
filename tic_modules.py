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


def checkboard(board):
    while True:
        def user_vs_bot_won():
            print_board(board)
            print("User Wins! ")
            quit()
        if board[0] == "X" and board[1] == "X" and board[2] == "X":
            user_vs_bot_won()
        if board[3] == "X" and board[4] == "X" and board[5] == "X":
            user_vs_bot_won()
        if board[6] == "X" and board[7] == "X" and board[8] == "X":
            user_vs_bot_won()
        if board[0] == "X" and board[3] == "X" and board[6] == "X":
            user_vs_bot_won()
        if board[1] == "X" and board[4] == "X" and board[7] == "X":
            user_vs_bot_won()
        if board[2] == "X" and board[5] == "X" and board[8] == "X":
            user_vs_bot_won()
        if board[0] == "X" and board[4] == "X" and board[8] == "X":
            user_vs_bot_won()
        if board[2] == "X" and board[4] == "X" and board[6] == "X":
            user_vs_bot_won()
        else:
            break

def bot_checkboard(board):
    while True:
        def bot_won():
            print_board(board)
            print("Bot Won.")
            quit()
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
def user1_checkboard(board):
    while True:
        def user_vs_bot_won():
            print_board(board)
            print("User Wins 1! ")
            quit()
        if board[0] == "X" and board[1] == "X" and board[2] == "X":
            user_vs_bot_won()
        if board[3] == "X" and board[4] == "X" and board[5] == "X":
            user_vs_bot_won()
        if board[6] == "X" and board[7] == "X" and board[8] == "X":
            user_vs_bot_won()
        if board[0] == "X" and board[3] == "X" and board[6] == "X":
            user_vs_bot_won()
        if board[1] == "X" and board[4] == "X" and board[7] == "X":
            user_vs_bot_won()
        if board[2] == "X" and board[5] == "X" and board[8] == "X":
            user_vs_bot_won()
        if board[0] == "X" and board[4] == "X" and board[8] == "X":
            user_vs_bot_won()
        if board[2] == "X" and board[4] == "X" and board[6] == "X":
            user_vs_bot_won()
        else:
            break

def user2_checkboard(board):
    while True:
        def user2_won():
            print_board(board)
            print("User 2 Wins! ")
            quit()
        if board[0] == "O" and board[1] == "O" and board[2] == "O":
            user2_won()
        if board[3] == "O" and board[4] == "O" and board[5] == "O":
            user2_won()
        if board[6] == "O" and board[7] == "O" and board[8] == "O":
            user2_won()
        if board[0] == "O" and board[3] == "O" and board[6] == "O":
            user2_won()
        if board[1] == "O" and board[4] == "O" and board[7] == "O":
            user2_won()
        if board[2] == "O" and board[5] == "O" and board[8] == "O":
            user2_won()
        if board[0] == "O" and board[4] == "O" and board[8] == "O":
            user2_won()
        if board[2] == "O" and board[4] == "O" and board[6] == "O":
            user2_won()
        else:
            break