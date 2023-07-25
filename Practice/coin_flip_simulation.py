import random

coin_sides = ['H', 'T']
game = True

while game:
    flips = []

    num_flips = int(input("Enter the number of coin flips: "))

    for flip in range(num_flips):
        flips.append(random.choice(coin_sides))

    print(f"You made {num_flips} and flipped:")
    print(f"Heads: {flips.count('H')} times ({round(flips.count('H') / num_flips * 100, 2)}%)")
    print(f"Tails: {flips.count('T')} times ({round(flips.count('T') / num_flips * 100, 2)}%)")

    go_on = input("Would you like to start over? Type (y) or (n): ")

    if go_on == 'y':
        continue

    else:
        print("See you!")
        game = False
