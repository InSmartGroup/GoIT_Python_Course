def func(arg):
    return f"{arg}"


print(func)
a = func
print(a)

print(func('test'))
print(a('test'))

