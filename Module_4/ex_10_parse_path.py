"""
Напишіть функцію parse_folder, вона приймає єдиний параметр path, який є об'єктом Path.
Функція повинна просканувати директорію path та повернути кортеж із двох списків.
Перший — це список файлів усередині директорії, другий — список директорій.
"""
from pathlib import Path


def parse_folder(path):
    files = []
    folders = []

    for i in path.iterdir():

        if i.is_file():
            files.append(i.name)
        else:
            folders.append(i.name)

    return files, folders
