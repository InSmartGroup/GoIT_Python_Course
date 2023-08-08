import pathlib

path = pathlib.Path("C:\\Users\\gostapenko")

files = []
folders = []

for i in path.iterdir():
    if i.is_file():
        files.append(i.name)
    elif i.is_dir():
        folders.append(i.name)

print(len(files))
print(len(folders))
