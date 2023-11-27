# a = 'asd'.encode('utf-8')
# b = b"asd"
# c = 'asd'.encode('utf-16')
# d = 'asd'.encode('utf-32')
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))
#
# a = a.decode()
# b = b.decode()
# c = c.decode('utf-16')
# d = d.decode('utf-32')
# print(a)
# print(b)
# print(c)
# print(d)

# while True:
#     something = input("Type something: ")
#
#     if something == 'quit':
#         break
#
#     something = something.encode()
#
#     something_bytearray = bytearray(something)
#     print(list(something_bytearray))

# latin_lower = 'abcdefghijklmnopqrstuvwxyz'
# latin_upper = latin_lower.upper()
# letters = dict()
# for i in latin_lower:
#     letter = i.encode('utf-16')
#     letters[i] = list(letter)
#
# for i in latin_upper:
#     letter = i.encode('utf-16')
#     letters[i] = list(letter)
#
# print(letters['A'])
# print(letters['r'])
# print(letters['U'])

# latin_lower = 'abcdefghijklmnopqrstuvwxyz'
# latin_upper = latin_lower.upper()
# ascii_lower = []
# ascii_upper = []
#
# for i in latin_lower:
#     ascii_lower.append(ord(i))
#     ascii_upper.append(ord(i.upper()))
#
# print(ascii_lower)
# print(ascii_upper)
