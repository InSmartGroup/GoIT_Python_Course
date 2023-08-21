from pathlib import Path
import shutil

path = Path.cwd()
print(path)

# for i in path.iterdir():
#     if i.is_file():
#         print(f"Drive: {i.drive}")
#         print(f"Anchor: {i.anchor}")
#         print(f"File full name: {i.name}")
#         print(f"File name only: {i.stem}")
#         print(f"File suffix: {i.suffix}")
#         print(f"Parent path: {i.parent}\n")

# try:
#     with open(path/'test.bin', 'xb') as file:
#         file.write('This is a binary string'.encode('utf-8'))
# except FileExistsError:
#     pass

# with open(path/"test.bin", "rb") as file:
#     content = file.read()
#     print(content)
#     print(type(content))

# with open(path/'test.bin', 'rb') as file:  # read the file content chuck by chunk
#     while True:
#         content_chunk = file.read(20)  # read 20 bytes of file content
#         print(content_chunk)
#
#         if not content_chunk:
#             break

message = "This is a binary file.\n" \
          "It contains strings of text.\n" \
          "I made this file just for practice purposes,\n" \
          "So let's see what will happen.\n".encode('utf-16')

with open(path/'test.bin', 'wb') as file:
    file.write(message)

with open(path/'test.bin', 'rb') as file:
    print(file.read())
