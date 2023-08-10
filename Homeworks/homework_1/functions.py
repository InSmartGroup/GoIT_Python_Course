def create_empty_files(path, name_prefix="", name_suffix=""):
    """
    Creates the same number of empty files as the number of file extensions in the 'file_extensions' variable.
    :param path: The path to a folder where you want to create those files.
    :type path: str

    :param name_prefix: Optional parameter that adds a custom prefix at the beginning of the filename.
    :type name_prefix: str

    :param name_suffix: Optional parameter that adds a custom suffix at the end of the filename.
    :type name_suffix: str

    :return: This function returns nothing.
    :rtype: None
    """
    file_extensions = {"image": ['JPEG', 'PNG', 'JPG', 'SVG'],
                       "video": ['AVI', 'MP4', 'MOV', 'MKV'],
                       "document": ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'],
                       "audio": ['MP3', 'OGG', 'WAV', 'AMR'],
                       "archive": ['ZIP', 'GZ', 'TAR']}

    if len(name_prefix) > 0 or len(name_suffix) > 0:
        for key, value in file_extensions.items():
            for index, item in enumerate(value):
                file = open(path + f"{name_prefix}{key}_{index + 1}{name_suffix}.{item.lower()}", 'w')
                file.close()
    else:
        for key, value in file_extensions.items():
            for index, item in enumerate(value):
                file = open(path + f"{key}_{index + 1}.{item.lower()}", 'w')
                file.close()


def transliterize(filename):
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
