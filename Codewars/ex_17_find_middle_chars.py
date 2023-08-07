def middle(text: str):
    middle = len(text) // 2 + 1

    if middle % 2 != 0:
        return text[-middle:middle]
    else:
        return text[-middle:middle]


print(middle('example'))
print(middle('test'))
print(middle('hellOWorld'))
print(middle('myfuNCtion'))
print(middle('    few whitespaces   '))
print(middle('Hi'))
