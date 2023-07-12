import math


def number_of_groups(n, k):
    factorial_n = math.factorial(n)
    factorial_k = math.factorial(k)
    factorial_n_k = math.factorial(n - k)

    groups = factorial_n / (factorial_n_k * factorial_k)

    return groups


print(number_of_groups(50, 7))
