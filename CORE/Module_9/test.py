"""
SOLID:
S - Single Responsibility principle
O - Open-Closed principle
L - Liskov substitution principle
I - Interface segregation principle
D - Dependency Inversion principle
"""

# def func(arg):
#     return f"{arg}"
#
#
# print(func)
# a = func
# print(a)
#
# print(func('test'))
# print(a('test'))


# def multiply(a):
#     def inner_func_1(b):
#         def inner_func_2(c):
#             return a * b * c
#
#         return inner_func_2
#
#     return inner_func_1
#
#
# multiply_ten = multiply(10)
# print(multiply_ten)
# multiply_ten_five = multiply_ten(5)
# print(multiply_ten_five)
# multiply_ten_five_three = multiply_ten_five(3)
# print(multiply_ten_five_three)
#
# # another way to use enclosed functions
# print(multiply(10)(5)(3))
