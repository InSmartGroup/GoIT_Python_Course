import re

# text = "Niels Bohr was BORN to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen," \
#        "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#        "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#        "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#        "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# print(re.search(r'[0-9]', text))  # finds the first match of a single digit in a specified range
# print(re.search(r'9', text))  # finds the first match of the exact digit
# print(re.search(r'[0-9]{4}', text))  # finds the first match of 4 digits in a specified range
# print(re.search(r'[8-9]{2}', text))  # finds the first match of 2 digits in a specified range

# result = re.search(r'[0-9]{4}', text)  # stores the result of the search in a variable
# print(result)
# print(result.group())  # the search result itself
# start_index = result.start()  # the 1st index of a sequence
# end_index = result.end()  # the last index of a sequence
# print(start_index, end_index)
# start_index, end_index = result.span()  # the same but done with one line of code
# print(start_index, end_index)
# print(result.string)  # the text itself

# print(re.findall(r'[0-9]', text))  # finds all the digits in a text within a specified range
# print(re.findall(r'[0-9]+', text))  # finds all the numbers within a specified range
# print(re.findall(r'[a-z]+', text))  # finds all the words that contain only letters from 'a' to 'z'
# print(re.findall(r'[A-Z]+', text))  # the same but only for capital letters
# print(re.findall(r'[A-Z]\w+', text))  # finds all the words that start with capital letter
# print(re.findall(r'[A-Z][a-z]{2}', text))  # returns only 1st capital letter and 2 lowercase letters
# print(re.findall(r'\w+', text))  # finds all the words and numbers
# print(re.compile(r'\w+').findall(text))  # the same as the previous one but with another syntax

# hard-code check
# phone_number_1 = '415-555-4242'
# phone_number_2 = '415 555-4242'
# phone_number_3 = '415-55-54242'
# phone_number_4 = '111-222-3344'
#
#
# def is_phone_number(data):
#     if len(data) != 12:
#         return False
#     for i in range(3):
#         if not data[i].isdecimal():
#             return False
#     if data[3] != "-":
#         return False
#     for i in range(4, 7):
#         if not data[i].isdecimal():
#             return False
#     if data[7] != "-":
#         return False
#     for i in range(8, 12):
#         if not data[i].isdecimal():
#             return False
#     else:
#         return True
#
#
# print(is_phone_number(phone_number_1))
# print(is_phone_number(phone_number_2))
# print(is_phone_number(phone_number_3))
# print(is_phone_number(phone_number_4))
#
# message = "Hey there! Please call me at 444-555-7171 by the end of the day." \
#           "Otherwise, you can contact me at 126-774-8754 when I'll get back home."
#
#
# def find_numbers(text):
#     found_phone_numbers = []
#
#     for i in range(len(text)):
#         piece = text[i:i + 12]
#         if is_phone_number(piece):
#             found_phone_numbers.append(piece)
#
#     return found_phone_numbers
#
#
# print(find_numbers(message))

# regular expressions
