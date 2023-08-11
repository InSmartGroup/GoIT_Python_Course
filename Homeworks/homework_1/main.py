import sys
from pathlib import Path
import shutil
import functions as fn

# create a new folder and define the path to it
path = fn.select_folder('various_stuff')

# create multiple files and put them into a specified folder
# fn.create_empty_files(path, name_prefix='новый_', name_suffix='')

for i in path.iterdir():
    filename = i.stem
    new_filename = fn.transliterate(filename)
    file = open(path/new_filename, 'w')
    file.close()

