# When provided with a letter, return its position in the alphabet
# E.g. Input: "a"
# Ouput: "Position of alphabet: 1"

def position(letter):
    letters_lower = [chr(i) for i in range(97, 123)]
    letters_upper = [chr(i) for i in range(65, 91)]

    if letter in letters_lower:
        index = letters_lower.index(letter) + 1
    else:
        index = letters_upper.index(letter) + 1

    return f"Position of alphabet: {index}"


print(position('c'))
print(position('W'))
print(position('t'))
print(position('U'))
