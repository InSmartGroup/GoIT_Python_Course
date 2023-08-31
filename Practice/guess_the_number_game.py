import random


def guessed_number():
    num = [i for i in '1234567890']
    return list(random.choices(num, k=3))


def user_guess():
    guess = input("Make your guess: ")
    if len(guess) != 3:
        print("The number should contain 3 digits. Please try again")
    else:
        return list(guess)


def compare_guesses(guessed_number, user_guess):
    try:
        clues = []

        if user_guess == guessed_number:
            print(f'Correct! The number was {"".join(guessed_number)}.')
            return True

        for index, item in enumerate(user_guess):
            if item in guessed_number and guessed_number[index] == user_guess[index]:
                clues.append('Exact')
            elif item in guessed_number and guessed_number[index] != user_guess[index]:
                clues.append('Close')
            else:
                if len(clues) == 0:
                    clues.append('All wrong')

        if 'All wrong' in clues and len(clues) > 1:
            clues.remove('All wrong')

        print(" ".join(clues))

    except TypeError:
        pass


guessed_number = guessed_number()

while True:
    user_guessed_number = user_guess()
    result = compare_guesses(guessed_number, user_guessed_number)

    if result:
        break
