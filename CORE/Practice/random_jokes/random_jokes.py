"""
This script highlights Oleg's drastic contribution to the 'Random Jokes' domain, which has already become legendary.
Get a new random joke non-stop 24/7, every single day, throughout the calendar year, and LMFAO!
P.S. Try not to die laughing.
"""
from pathlib import Path
import random

path = Path.cwd()


def get_random_joke():
    with open(path / 'jokes.txt', 'r') as file:
        jokes = file.readlines()

        clean_jokes = []
        for joke in jokes:
            for i in joke:
                if i in "1234567890.":
                    joke = joke.replace(i, "")

            joke = joke.strip()
            clean_jokes.append(joke)

        return random.choice(clean_jokes)


print(get_random_joke())
