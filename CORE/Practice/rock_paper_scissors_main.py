import rock_paper_scissors_functions as rps_func

print("WELCOME TO THE 'ROCK, PAPER, SCISSORS' GAME!")

game = True

wins = 0
losses = 0
draws = 0

while game:
    player_choice = input("(r)ock, (p)aper, (s)cissors, or (quit). Make your move: ").lower()

    enemy_choice = rps_func.computer_choice()

    rps_func.display_choice(player_choice, enemy_choice)

    if player_choice == enemy_choice:
        draws += 1
    elif player_choice == 'r' and enemy_choice == 'p':
        losses += 1
    elif player_choice == 'p' and enemy_choice == 'r':
        wins += 1
    elif player_choice == 'r' and enemy_choice == 's':
        wins += 1
    elif player_choice == 'p' and enemy_choice == 's':
        losses += 1
    elif player_choice == 's' and enemy_choice == 'r':
        losses += 1
    elif player_choice == 's' and enemy_choice == 'p':
        wins += 1

    print(f"WINS: {wins}, LOSSES: {losses}, DRAWS: {draws}")

    if player_choice == 'quit':
        print("\nTHANK YOU FOR PLAYING!")
        print(f"You won {wins} times and lost {losses} times.")
        break
