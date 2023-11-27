CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {k: v for k, v in zip(CYRILLIC_SYMBOLS, TRANSLATION)}
TRANS[" "] = " "


def translate(name):
    name_translated = ""

    for i in name:
        if i.upper():
            i = i.lower()
            name_translated += TRANS[i]
        else:
            name_translated += TRANS[i]

    return " ".join([i.title() for i in name_translated.split()])


print(translate("Дмитро Короб"))
print(translate("Олекса Івасюк"))
print(translate("Авточек скотиняка"))
print(translate("григорій остапенко"))
print(translate("кім ван хорн"))
print(translate("хавал жовані штани"))
