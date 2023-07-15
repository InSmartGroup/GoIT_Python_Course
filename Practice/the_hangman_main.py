import random

WORDS = ['apple', 'milk', 'elephant', 'snow', 'mountain', 'chair', 'football', 'state', 'attitude']

random_word = random.choice(WORDS)

word_list = [i for i in random_word]

word_coded_list = ["-" for i in word_list]

guess_attempts = 4

while True:
    print("".join(word_coded_list))
    print(f"Guess attempts left: {guess_attempts}")

    user_choice = input("Guess a letter: ")

    # process the user's input
    if len(user_choice) > 1:
        print("\nYou must enter only one letter.")
        continue
    elif user_choice.isdigit():
        print("\nIt's a number. Please enter a letter")

    # compare the coded word with user's input
    for index, letter in enumerate(word_list):
        if letter == user_choice:
            word_coded_list[index] = user_choice

    if user_choice not in word_list:
        print(f"\nThere's no letter \"{user_choice}\" in this word. Try again.")
        guess_attempts -= 1
        continue

    # game end conditions
    if guess_attempts == 0:
        print("\nYou ran out of guess attempts. GAME OVER!")
        break

    elif word_coded_list == word_list:
        print("\nYou guessed the word! Good job!")
        break
