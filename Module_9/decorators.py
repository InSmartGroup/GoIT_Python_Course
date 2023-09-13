# one way to decorate a function (not a good-looking one)
# def decorator(function):  # create a decorator
#
#     def wrapper():
#         print('Before the function')
#         function()
#         print('After the function')
#
#     return wrapper  # return the wrapper signature
#
#
# def func():  # create a function that should be decorated
#     print('Hello')
#
#
# decor = decorator(func)  # finally, call a decorated function
# decor


# another way to decorate a function (a better-looking one)
# def decorator(func):  # create a decorator
#
#     def internal_wrapper():
#         print("Before the function")
#         func()
#         print("After the function")
#
#     return internal_wrapper  # return the wrapper's signature
#
#
# @decorator  # apply the decorator to a function
# def function():  # create a function that should be decorated
#     print('Hello')
#
#
# function()  # call a decorated function


# how to properly decorate any function with any number of arguments
# def decorator(function):  # create a decorator as before
#
#     def wrapper(*args, **kwargs):  # specify any arguments of a given function in a wrapper
#         print('Before the function')
#         result = function(*args, **kwargs)  # define the function execution result
#         print('After the function\n')
#
#         return result  # return the result
#
#     return wrapper  # return the wrapper
#
#
# @decorator  # create a decorated function
# def func(a, b, c, d):
#     return f"It is {a + b} and {c * d}."
#
#
# print(func(6, 4, 3, 3))  # call the decorated function
# print(func(a=4, b=4, c=2, d=3))
# print(func(7, 2, c=5, d=3))

# it's also possible to apply arguments to decorators
def decorator_with_arguments(arg):

    def decorator(function):

        def wrapper(*args, **kwargs):
            print(f"Before: {arg}")
            result = function(*args, **kwargs)
            print(f"After: {arg}")

            return result

        return wrapper

    return decorator


@decorator_with_arguments('TEST TEXT')
def func(a, b, c):
    return f"{a + b} and {a + c}"


print(func(2, c=5, b=7))
