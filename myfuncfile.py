import random
# Display function
def display_board(board):
    print('\n'*80)
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('-----------')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('-----------')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('\n')

# Player input
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?\n').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[1] == board[2] == board[3] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[8] == board[5] == board[2] == mark) or
            (board[9] == board[6] == board[3] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark))

def choose_first():
    if random.randint(0, 1) == 0:
        return 'PLAYER 2'
    else:
        return 'PLAYER 1'

def space_check(board, position):
    return board[position]== ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def player_choice(board, turn):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input(f'{turn} Choose your position: (1-9) \n'))

    return position

def replay():
    ans='wrong'
    while ans not in ['Y','y','n','N']:
        ans=input('Keep Playing (Y/N)\n')
    if ans in ['Y','y']:
        return True
    else:
        return False