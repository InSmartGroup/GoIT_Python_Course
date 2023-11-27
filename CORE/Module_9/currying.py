# this script is to demonstrate currying
# def add(x, y):
#     return x + y
#
#
# def subtract(x, y):
#     return x - y
#
#
# def multiply(x, y):
#     return x * y
#
#
# def power(x, y):
#     return x ** y


# currying
# operations = {'+': add, '-': subtract, '*': multiply, '**': power}
#
# print(operations['+'])
# print(operations['-'])
#
# print(operations['*'](2, 3))
# print(operations['**'](2, 2))


# currying using a wrapper
# def operations_wrapper(operator):
#     return operations[operator]
#
#
# print(operations_wrapper('+')(10, 5))
# print(operations_wrapper('-')(10, 5))
# print(operations_wrapper('*')(3, 5))
# print(operations_wrapper('**')(2, 3))

