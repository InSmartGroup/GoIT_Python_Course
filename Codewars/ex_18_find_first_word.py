import re


def first_word(text: str):
    pattern = r"[A-Za-z']+"
    return re.findall(pattern, text)[0]


print(first_word('hello world!'))
print(first_word('  a word'))
print(first_word('don\'t touch it'))
print(first_word("... and so on ..."))
