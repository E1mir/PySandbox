"""Imported for random choosing"""
import random


def clear_output():
    """
        This function clear output in the console
    """
    print("\n" * 20)


def init_board():
    """
        This function initialize our game board and return it
    """
    board = ['#', 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def display_board(board):
    """
    This function print a gameboard to the console
    INPUT: board
    OUTPUT: Console view of board
    """
    spaces = " " * 3
    vertical_line = "|"
    horizontal_line = "–"
    border = [3, 6, 9]
    for i in range(1, len(board)):
        marker = str(board[i])
        if i in border:
            print(spaces + marker, end=spaces + "\n")
        else:
            print(spaces + marker, end=spaces + vertical_line)
        if i in border and i != 9:
            print(horizontal_line * 24)
    print()


def player_input():
    """
    This function ask for choosing player X or O
    """
    x_o = ['X', 'O']
    player = ""
    while True:
        player = input('Choose your player X or O: ')
        if player.upper() in x_o:
            break
        else:
            print('It is neither X nor O! Choose again:')
    player = player.upper()
    print(f"Your player is {player}")
    return player


def place_marker(board, marker, position):
    """
    This function place marker in position on our board
    INPUT: board, marker, position
    """
    board[position] = marker


def win_check(board, mark):
    """
    This function check if choosen mark is winner on our board or not
    INPUT: board, mark
    OUTPUT: boolean
    """
    win_positions = ["123", "456", "789", "147", "258", "369", "159", "357"]
    is_winner = False
    for positions in win_positions:
        for idx in positions:
            idx = int(idx)
            if board[idx] != mark:
                break
        else:
            is_winner = True

    return is_winner


def choose_first():
    """
    Randomly choose who playes first
    """
    rand = random.randint(1, 2)
    print(f"The first is Player-{rand}")
    return rand


def space_check(board, position):
    """
    Check if position on our board is empty
    INPUT: board, position
    """
    return board[position] == " "


def full_board_check(board):
    """
    Checks if our board is full or not
    """
    is_full = True
    for i in range(1, 10):
        if str(board[i]).strip() == "":
            is_full = False
            break
    return is_full


def player_choice(board):
    """
    This function returns a position of selected position in our board
    """
    position = -1
    while True:
        try:
            position = int(input("Choose your position: "))

            if 0 < position <= 9:
                is_empty_position = space_check(board, position)
                if is_empty_position:
                    break
                else:
                    print('Position is not empty, choose again!')
            continue
        except ValueError:
            print('Invalid position, choose again!')
    return position


def replay():
    """
    This function asks players if they want to play again
    """
    answer = input("Do you want to play again? - ").lower()
    return answer == "yes" or answer == "y"


def main():
    """
    Main method
    """
    game_board = init_board()
    display_board(game_board)
    players = {
        "p1": {'mark': '', 'wins': 0},
        "p2": {'mark': '', 'wins': 0}
    }
    while True:
        game_board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        first = choose_first()
        second = 2 if first == 1 else 1
        first_player = players[f'p{first}']
        second_player = players[f'p{second}']
        mark = player_input()
        game_on = True
        first_player['mark'] = mark
        if mark == "X":
            second_player['mark'] = "O"
        else:
            second_player['mark'] = "X"
        while game_on:
            print(f'Player-{first} choose your position')
            position = player_choice(game_board)
            place_marker(game_board, first_player['mark'], position)
            is_winner = win_check(game_board, first_player['mark'])
            if is_winner:
                print(f'\nPlayer-{first} winner! Congratulations!\n')
                first_player['wins'] += 1
                game_on = False
                continue
            is_board_full = full_board_check(game_board)
            if is_board_full:
                print('The board is full!')
                print('It is draw!')
                game_on = False
                continue
            clear_output()
            display_board(game_board)

            print(f'Player-{second} choose your position')
            position = player_choice(game_board)
            place_marker(game_board, second_player['mark'], position)
            is_winner = win_check(game_board, second_player['mark'])
            if is_winner:
                print(f'\nPlayer-{second} winner! Congratulations!\n')
                second_player['wins'] += 1
                game_on = False
                continue
            is_board_full = full_board_check(game_board)
            if is_board_full:
                print('The board is full!')
                print('It is draw!')
                game_on = False
                continue
            clear_output()
            display_board(game_board)
        print("Player-{} score is: {}\nPlayer-{} score is: {}".format(
            first,
            first_player['wins'],
            second,
            second_player['wins']
        ))
        if not replay():
            break
    print("Thanks for playing ;)")


if __name__ == '__main__':
    print("\nWelcome to Tic Tac Toe!\n")
    main()
