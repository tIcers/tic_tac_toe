row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[1] + '|' + board[2] + '|' + board[3])


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']


def player_input():
    """
    output = (player 1 maker, player 2 marker)

    """
    marker = ''
    while not (marker != 'X' or marker != 'O'):
        marker = input("Choose X or O").upper()

        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')


# function that takes in the board list obj,
# a marker (x or O ) and desired position between 1 and 9 and assign it to the end

def place_marker(board, marker, position):
    board[position] = marker


# test


# check if that mark has won

def check_win(board, mark):
    # all rows and check to see if they all share the same marker
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            # all colums
            (board[7] == board[4] == board[1] == mark) or
            (board[8] == board[5] == board[2] == mark) or
            (board[9] == board[6] == board[3] == mark) or
            # diag
            (board[7] == board[5] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark))


print(check_win(test_board, 'X'))


# func that uses the random to randomly decie which player goes first

def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'player1'
    else:
        return 'player2'


def check_space(board, position):
    return board[position] == ''


def check_full(board, position):
    for i in range(0, 10):  # up to 10 but not including 10 for board
        if check_space(board, i):
            return False
        # board is full if we return true
    return True


def player_choice(board):
    # 1 ask for a players' next positon from 1 to 9
    position = 0
    # check if the choice has still a space
    # if so then store it for later use then

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not check_space(board, position):
        position = int(input("Choose a position 1-9: "))

    return position


def replay():
    play_again = input("Do you want to play this game again? Y or N").upper()

    return play_again == 'Y'


print("Welecome to tic tac toe")

while True:
    # play game

    # set everything up (board, whos first, choose markers x or o

    the_board = [' '] * 10
    player1_marker= player_input()
    player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('ready to play? y or n: ').lower()

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'player1':

            # show the board
            display_board(the_board)

            # choose a position

            position = player_choice(the_board)

            # place the marker on the position
            place_marker(the_board, player1_marker, position)

            # check if they win
            if check_win(the_board, player1_marker):
                display_board(the_board)
                print("Player 1 has won!")
                game_on = False
            else:
                if check_full(the_board):
                    display_board(the_board)
                    print("Tie game!")
                    game_on = False
                else:
                    turn = 'player2'

            # check if they are tied

            # no tie and no win

        else:
            # show the board
            display_board(the_board)

            # choose a position

            position = player_choice(the_board)

            # place the marker on the position
            place_marker(the_board, player2_marker, position)

            # check if they win
            if check_win(the_board, player2_marker):
                display_board(the_board)
                print("Player 2 has won!")
                game_on = False
            else:
                if check_full(the_board):
                    display_board(the_board)
                    print("Tie game!")
                    game_on = False
                else:
                    turn = 'player1'

    # game play

    # player one turn

    # player two turn

    if not replay():
        break
    # break the loop if they do not want to play game again
