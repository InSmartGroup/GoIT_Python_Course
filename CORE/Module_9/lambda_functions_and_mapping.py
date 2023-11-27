# a 'classic' way to define a function
# def func(a, b, c):
#     return a + b + c
#
#
# print(func(1, 2, 3))

# doing the same but using lambda functions (anonymous functions)
# print((lambda a, b, c: a + b + c)(1, 2, 3))

# mapping, the 'classic' approach
# my_list = [1, 2, 3, 4, 5]
# result_list = []
#
# for i in my_list:
#     element = i + (i * 2)
#     result_list.append(element)
#
# print(result_list)

# # mapping using functions
# my_list = [1, 2, 3, 4, 5]
# result_list = []
#
#
# def operation(data: int):
#     return data + (data * 2)
#
#
# for i in my_list:
#     element = operation(i)
#     result_list.append(element)
#
# print(result_list)

# # mapping using lambda functions
# my_list = [1, 2, 3, 4, 5]
# result_list = []
#
# for i in my_list:
#     result_list.append((lambda x: x + (x * 2))(i))
#
# print(result_list)
#
# # mapping using the 'map' function
# my_map = map(operation, my_list)
# result = list(my_map)

# mapping multiple collections
# list_1 = [1, 2, 3, 4, 5]
# list_2 = ['a', 'b', 'c', 'd', 'e']
# list_3 = ['q', 'w', 'y', 'r', 't']
#
# result = map(lambda a, b, c: list[a, b, c], list_2, list_1, list_3)
# for i in result:
#     print(i)
