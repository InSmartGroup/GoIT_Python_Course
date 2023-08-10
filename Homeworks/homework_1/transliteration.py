def transliterate(filename):
    """
    Converts the file name from Cyrillic into a Latin using transliteration.
    :param filename: The name of the file you want to transliterate.
    :type filename: str

    :return: A new file transliterated file name.
    :rtype: str
    """
    transliteration = {"а": 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z',
                       'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
                       'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sh',
                       'ы': 'y', 'ь': '', 'ъ': '', 'э': 'e', 'ю': 'yu', 'я': 'ja'}

    new_filename = ""

    for i in filename:
        if i in ",.?!:;'\"\\/<>~#$%^&*()=+-@№":
            i = "_"

        if i.isupper():
            i = i.lower()

            if i in transliteration:
                new_i = transliteration[i].upper()
                new_filename += new_i
            else:
                new_filename += i

        elif i.lower() in transliteration and i.islower():
            new_i = transliteration[i].lower()
            new_filename += new_i
        else:
            new_filename += i

    return new_filename