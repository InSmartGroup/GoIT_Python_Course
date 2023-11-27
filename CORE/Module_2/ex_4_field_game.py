import random

field_size = int(input("Enter the size of the field: "))

char_x = random.randint(0, field_size - 1)
char_y = random.randint(0, field_size - 1)

exit_x = random.randint(0, field_size - 1)
exit_y = random.randint(0, field_size - 1)

turns = 0

while True:
    world_map = ""

    for j in range(field_size):
        row = "|"

        for i in range(field_size):

            if char_x == j and char_y == i:
                row += "X|"
            elif exit_x == j and exit_y == i:
                row += "O|"
            else:
                row += " |"

        world_map += row + '\n'

    print(world_map)

    direction = input("Enter direction ('u', 'd', 'l', 'r'): ")

    if direction == 'u' and char_x > 0:
        char_x -= 1
    elif direction == 'd' and char_x < field_size - 1:
        char_x += 1
    elif direction == 'l' and char_y > 0:
        char_y -= 1
    elif direction == 'r' and char_y < field_size - 1:
        char_y += 1

    turns += 1

    if char_x == exit_x and char_y == exit_y:
        print(f"\nYou won in {turns} turns!\nGAME OVER.")
        break
