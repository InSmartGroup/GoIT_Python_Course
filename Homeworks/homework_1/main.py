import sys
from pathlib import Path
import shutil
import functions

# this function was used to automatically create multiple files, please ignore this piece of code
# functions.create_empty_files(path, name_prefix='', name_suffix="_old")

# path = "C:\\Users\\gostapenko\\PycharmProjects\\GoIT_Python_Course\\Homeworks\\homework_1\\various_files\\"

# standard pre-check
try:
    user_path = Path(sys.argv[0])
    print(user_path)
except IndexError:
    print("Please specify the folder path.")
    sys.exit()
if not user_path.exists():
    print("Invalid path. Please try again.")
    sys.exit()



if __name__ == "__main__":
    pass
