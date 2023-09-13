# a generator is a function with multiple entry points
# def func():
#     print("Entry point 1")
#     yield None  # the 'yield' word defines a generator and an iteration
#     print("Entry point 2")
#     yield None
#     print('Final point')
#
#
# print(func())  # prints a generator's signature
# gen = func()
# next(gen)  # first iteration
# next(gen)  # second interation
# next(gen)  # last iteration and StopIteration
