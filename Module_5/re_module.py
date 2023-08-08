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
# phone_number_1 = '415-555-4242'
# phone_number_2 = '415 555 4242'
# phone_number_3 = '415-55-54242'
# phone_number_4 = '111-222-3344'


# def find_phone_number_simple(data):
#     return re.findall(r'\d\d\d-\d\d\d-\d\d\d\d', data)
#
#
# print(find_phone_number_simple(phone_number_1))
# print(find_phone_number_simple(phone_number_4))


# def find_phone_number_simple_2(data):
#     phone_number = re.compile(r'\d{3}-\d{3}-\d{4}')
#     return phone_number.findall(data)
#
#
# print(find_phone_number_simple_2(phone_number_1))
# print(find_phone_number_simple_2(phone_number_4))

# message = "Hey there! Please call me at 444-555-7171 by the end of the day." \
#           "Otherwise, you can contact me at 126-774-8754 when I'll get back home."


# def find_phone_number_match_group(data):
#     regex_object = re.compile(r"\d{3}-\d{3}-\d{4}")
#     found_number = regex_object.search(data)
#     return found_number.group()
#
#
# print(find_phone_number_match_group(message))


# def find_phone_numbers(data):
#     pattern = r"\d{3}-\d{3}-\d{4}"
#     found_numbers = re.search(pattern, data)
#     return found_numbers.group()
#
#
# print(find_phone_numbers(message))  # this code finds only one number


# def find_phone_numbers(data):
#     pattern = r"\d{3}-\d{3}-\d{4}"
#     found_numbers = re.findall(pattern, data)
#     return found_numbers
#
#
# print(find_phone_numbers(message))  # this code finds all the numbers that match the pattern


# def find_phone_numbers(data):
#     pattern = r"(\d{3})-(\d{3}-\d{4})"
#     found_numbers = re.search(pattern, data)
#     print(f"Found groups: {found_numbers.groups()}")
#     print(f"Area code: {found_numbers.group(1)}")
#     print(f"The number itself: {found_numbers.group(2)}")
#     print(f"The whole phone number: {found_numbers.group(0)}")
#
#
# find_phone_numbers(message)


# def find_phone_numbers(data):
#     pattern = re.compile(r"(\d{3})-(\d{3}-\d{4})")
#     found_phone_numbers = pattern.findall(data)
#     for i in found_phone_numbers:
#         print(f"Area code: {i[0]}, number: {i[1]}")
#
#
# find_phone_numbers(message)

# message = "Hey there! Please call me at 444-555-7171 by the end of the day." \
#           "Otherwise, you can contact me at (126) 774-8754 when I'll get back home."


# def find_phone_numbers(data):
#     pattern = re.compile(r"[(0-9) -]+")
#     found_numbers = pattern.findall(data)
#     phone_numbers = []
#     for i in found_numbers:
#         if i != " ":
#             i = i.strip().replace("-", "").replace("(", "").replace(")", "").replace(" ", "")
#
#             phone_numbers.append(i)
#
#     return phone_numbers
#
#
# print(find_phone_numbers(message))

# text = "Niels Bohr was BORN to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen," \
#        "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#        "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#        "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#        "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# pattern_1 = re.compile(r"d......r")
# print(pattern_1.findall(text))

# pattern_2 = r"([d]\w+)"
# print(re.findall(pattern_2, text))

# pattern_3 = r"profes*"  # zero or more occurrences
# print(re.findall(pattern_3, text))

# text_1 = 'Adventures of Batman'
# text_2 = 'Adventures of Batwoman'
# text_3 = 'Adventures of Batman and Batwoman'
#
# pattern = r"bat(wo)?man"
# found_1 = re.search(pattern, text_1, flags=re.IGNORECASE)
# found_2 = re.search(pattern, text_2, flags=re.IGNORECASE)
# found_3 = re.search(pattern, text_3, flags=re.IGNORECASE)
# print(found_1.group())
# print(found_2.group())
# print(found_3.group())

# text = 'Adventures of Batman and Batwoman'
# regex = re.compile(r"bat\w+", flags=re.I)
# print(regex.sub("Batwoman", text))

# text = "Niels Bohr was BORN to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen," \
#        "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#        "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#        "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#        "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."
#
# regex_1 = re.compile(r"[0-9]{4}-[0-9]{4}")
# regex_2 = re.compile(r"N\w+\sB\w+")
# new_text_1 = regex_1.sub('1986-2023', text)
# new_text_2 = regex_2.sub('Gregory Ostapenko', new_text_1)
# print(new_text_2)
