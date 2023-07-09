message = input("Enter a message: ")
offset = int(input("Enter the offset: "))

upper_letters = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
lower_letters = [i for i in "abcdefghijklmnopqrstuvwxyz"]

encoded_message = ""

for char in message:
    if char in upper_letters:
        index = upper_letters.index(char)
        new_index = index + offset

        if new_index > 26:
            new_index = new_index % 26
        encoded_message += upper_letters[new_index]

    elif char in lower_letters:
        index = lower_letters.index(char)
        new_index = index + offset

        if new_index > 26:
            new_index = new_index % 26
        encoded_message += lower_letters[new_index]

    elif char in [" ", "!"]:
        encoded_message += char

print(encoded_message)
