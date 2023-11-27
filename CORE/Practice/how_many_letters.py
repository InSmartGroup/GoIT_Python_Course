text = "Niels Bohr was BORN to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen," \
       "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
       "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
       "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
       "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."


def find_letters(data):
    found_letters = {i: [] for i in "abcdefghijklmnopqrstuvwxyz"}
    for i in data:
        if i.isalpha():
            i = i.lower()
            found_letters[i].append(i)

    return found_letters


letters = find_letters(text)
print(len(letters['a']))
print(len(letters['b']))
print(len(letters['c']))