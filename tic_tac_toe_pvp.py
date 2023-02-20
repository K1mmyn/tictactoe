import random
import tic_modules

board = [
     '-','-','-',
     '-','-','-',
     '-','-','-']

avaliable_spaces = [0,1,2,3,4,5,6,7,8]

def print_board(board):
    print(f'\n{board[0]} | {board[1]} | {board[2]}')
    print("----------")
    print(board[3] + " | " + board[4] + ' | ' + board[5])
    print("----------")
    print(f'{board[6]} | {board[7]} | {board[8]} \n')

def getInputAsInt(msg):
    while True:
        try:
            return int(input(msg))
        except:
            print("\nPlease Enter a number\n")
            continue

def user1_cases():
    while True:
        print_board(board)
        user_move = getInputAsInt("\nPlease Enter a number between 1 - 9 \n>") - 1
        if user_move in avaliable_spaces:
            board.pop(user_move); avaliable_spaces.remove(user_move)
            board.insert(user_move, "X")
            tic_modules.user1_checkboard(board)
            break
        else:
            print("Sorry that spot is taken")

def user2_cases():
    while True:
        print_board(board)
        user2_move = getInputAsInt("\nPlease Enter a number between 1 - 9 \n>") - 1
        if user2_move in avaliable_spaces:
            board.pop(user2_move); avaliable_spaces.remove(user2_move)
            board.insert(user2_move, "O")
            tic_modules.user2_checkboard(board)
            break
        else:
            print("Sorry that spot is taken")

while True:
    user1_cases()
    user2_cases()