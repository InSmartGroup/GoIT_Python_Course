import numpy as np


def calculate_triangle_level_sum(level):
    return f"The sum of all numbers in line {level} gives you {np.power(level, 3)}."


print(calculate_triangle_level_sum(2))
print(calculate_triangle_level_sum(3))
print(calculate_triangle_level_sum(4))
print(calculate_triangle_level_sum(5))
print(calculate_triangle_level_sum(11))
print(calculate_triangle_level_sum(54671))