import random


def display_choice(player_choice, enemy_choice):
    try:
        if enemy_choice == 'r':
            ec = 'ROCK'
        elif enemy_choice == 'p':
            ec = 'PAPER'
        elif enemy_choice == 's':
            ec = 'SCISSORS'

        if player_choice == 'r':
            pc = 'ROCK'
        elif player_choice == 'p':
            pc = 'PAPER'
        elif player_choice == 's':
            pc = 'SCISSORS'
        else:
            print("Please type 'r', 'p', or 's'.")

        print(f"\n{pc} versus {ec}")

    except UnboundLocalError:
        pass


def computer_choice():
    options = 'rps'
    choice = random.choice(options)

    return choice
