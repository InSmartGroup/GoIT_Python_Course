from pathlib import Path
import shutil

path = Path.cwd()

with open(path/'test.txt', 'w') as file:
    file.write('Hello world\n')

filenames = []
for i in path.iterdir():
    if i.is_file():
        filenames.append(i.name)

file_2_rename = path/'test.txt'
file_2_rename.rename("testing_test.txt")
shutil.move("testing_test.txt", "../testing_test.txt")  # move the file to a specified folder
