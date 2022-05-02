row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
from IPython.display import clear_output


def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[1] + '|' + board[2] + '|' + board[3])


test_board = [' '] * 10
display_board(test_board)


def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


position = int(input('Choose a position'))


def user_choice():
    # variables

    # initioanl
    choice = 'wrong'
    acceptable_range = range(0, 10)
    within_range = False

    # two condition to check
    # digit or within range == false

    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number (0-10): ")

        # digit check
        if not choice.isdigit():
            print("Sorry, that is not a digit!")

        # range check
        if choice.isdigit():
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, please enter the number between 1- 10 ")
                within_range = False

    return int(choice)


def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)


def position_choice():
    choice = 'wrong'

    while choice not in ['0', '1', '2']:
        choice = input('Enter a position (0,1,2): ')
        if choice not in ['0', '1', '2']:
            print("Invalid choice")

    return int(choice)


def replace_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")
    game_list[position] = user_placement

    return game_list


def game_on_choice():
    choice = 'wrong'

    while choice not in ['y', 'n']:
        choice = input('Keep playing?: (Y or N) ').lower()

        if choice not in ['y', 'n']:
            print('Sorry, invalid input, please enter Y or N ')

        if choice == 'y':
            return True

        else:
            return False


game_on = True
game_list = [0, 1, 2]

while game_on:
    display_game(game_list)

    position = position_choice()

    game_list = replace_choice(game_list, position)

    display(game_list)

    game_on = game_on_choice()
