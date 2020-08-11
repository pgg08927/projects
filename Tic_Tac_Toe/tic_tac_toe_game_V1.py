#setting board
board=["-","-","-",
       "-","-","-",
       "-","-","-"]

# function to display board
def display_board():
    print(board[0]+ " | "+ board[1]+ " | "+ board[2])
    print(board[3]+ " | "+ board[4]+ " | "+ board[5])
    print(board[6]+ " | "+ board[7]+ " | "+ board[8])


display_board()


current_player='X'
game_still_going=True

print(f"{current_player}'s turn")
inp_num=0

# taking input from player
def take_input():
    global current_player
    global inp_num
    inp_num=input('Please enter the number 1-9: ')
    while inp_num not in ['1','2','3','4','5','6','7','8','9']:
        inp_num = input('Please enter the valid number from 1-9: ')
        print(f"{current_player}'s turn")
    inp_num=int(inp_num)
    return inp_num


# updating board
def update_board():
    global inp_num
    while board[inp_num-1]!="-":
        print('That position is already taken, enter another num form 1-9: ')
        take_input()
    else:
        board[inp_num - 1] =current_player
    display_board()

# checking for tie
def check_for_tie():
    global game_still_going
    if game_still_going:
        if '-' not in board:
            print("It's Tie!")
            game_still_going=False
        else:
            game_still_going=True

# checking for win
def check_for_win():
    global game_still_going
    if game_still_going:
        row_1 = board[0] == board[1] == board[2] != "-"
        row_2 = board[3] == board[4] == board[5] != "-"
        row_3 = board[6] == board[7] == board[8] != "-"

        columns_1 = board[0] == board[3] == board[6] != "-"
        columns_2 = board[1] == board[4] == board[7] != "-"
        columns_3 = board[2] == board[5] == board[8] != "-"

        diagonal_1 = board[0] == board[4] == board[8] != "-"
        diagonal_2 = board[6] == board[4] == board[2] != "-"

        if row_1 or row_2 or row_3 or columns_1 or columns_2 or columns_3 or diagonal_1 or diagonal_2:
            game_still_going=False
            print(f'{current_player} WON!')
        else:
            game_still_going=True

# changing turn
def flip_player():
    global current_player
    if current_player=='X':
        current_player='O'
    else:
        current_player='X'
    if game_still_going:
        print(f"{current_player}'s turn: ")


def play():
    while game_still_going:
        take_input()
        update_board()
        check_for_win()
        check_for_tie()
        flip_player()


play()













