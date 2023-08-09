"""Скрипт приймає один аргумент під час запуску — це ім'я папки, в якій він буде здійснювати сортування
Припустимо, що файл з програмою називається sort.py, тоді, щоб відсортувати папку /user/Desktop/Мотлох,
потрібно запустити скрипт командою python sort.py /user/Desktop/Мотлох
"""

import sys
import os
from pathlib import Path
import shutil
import functions

path = "C:\\Users\\gostapenko\\PycharmProjects\\GoIT_Python_Course\\Homeworks\\homework_1\\various_files\\"
print(sys.argv[0])

# this function was used to automatically create multiple files, please ignore this piece of code
# functions.create_empty_files(path, name_prefix='', name_suffix="_old")

# for i in Path(path).iterdir():
#     print(i.name)
    # print(i.name.split("."))
