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

def cases():
    while True:
        print_board(board)
        user_move = getInputAsInt("Please Enter a number between 1 - 9 \n>") - 1
        if user_move in avaliable_spaces:
            board.pop(user_move); avaliable_spaces.remove(user_move)
            board.insert(user_move, "X")
            tic_modules.checkboard(board)
            break
        else:
            print("Sorry that spot is taken")

def bot_cases():
    if bot_move not in avaliable_spaces:
        print("Sorry that spot is taken")
    else:      
        board.pop(bot_move); avaliable_spaces.remove(bot_move)
        board.insert(bot_move, "O")
        tic_modules.bot_checkboard(board)

while True:
    cases()
    bot_move = random.choice(avaliable_spaces)
    match bot_move:
        case 0:
            bot_cases()
        case 1:
            bot_cases()
        case 2:
            bot_cases()
        case 3:
            bot_cases()
        case 4:
            bot_cases()
        case 5:
            bot_cases()
        case 6:
            bot_cases()
        case 7:
            bot_cases()
        case 8:
            bot_cases()
        case 9:
            bot_cases()