def translate(text: str):
    vowels = 'aioeuy'
    consonants = 'qwrtpsdfghjklzxcvbnm'
    word = [i for i in text]
    try:
        for index, letter in enumerate(word):
            if letter in consonants:
                word.pop(index + 1)
            if letter in vowels and word[index + 1] == word[index]:
                word.pop(index)
                word.pop(index + 1)

    except IndexError:
        pass

    return "".join(word)


print(translate("hieeelalaooo"))
print(translate("hoooowe yyyooouuu duoooiiine"))
print(translate("aaa bo cy da eee fe"))
print(translate("sooooso aaaaaaaaa"))
