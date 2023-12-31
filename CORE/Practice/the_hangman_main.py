import random
import the_hangman_words as h_words


random_word = random.choice(h_words.WORDS)

word_list = [i for i in random_word]

word_coded_list = ["-" for i in word_list]

guess_attempts = 5

guesses_made = []

while True:
    print("\n" + "".join(word_coded_list))
    print(f"Guess attempts left: {guess_attempts}")

    user_choice = input("Guess a letter: ").lower()

    # process the user's input
    if len(user_choice) > 1:
        print("\nYou must enter only one letter.")

    elif user_choice.isdigit():
        print("\nIt's a number. Please enter a letter")

    # compare the coded word with user's input
    for index, letter in enumerate(word_list):
        if letter == user_choice:
            word_coded_list[index] = user_choice

    if user_choice not in word_list and user_choice not in guesses_made:
        guesses_made.append(user_choice)
        print(f"\nThere's no letter \"{user_choice}\" in this word. Try again.")
        guess_attempts -= 1

    elif user_choice not in word_list and user_choice in guesses_made:
        print(f"\nYou already made a guess for letter \"{user_choice}\". Try another letter.")
        continue

    # game end conditions
    if guess_attempts == 0:
        print("\nYou ran out of guess attempts. GAME OVER!")
        break

    elif word_coded_list == word_list:
        print(f"\nYou guessed the word \"{''.join(word_list)}\"! Good job!")
        break
