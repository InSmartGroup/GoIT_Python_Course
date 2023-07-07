# Given legs of a triangle, define its hypotenuse and square
import math

leg_1 = float(input("Leg 1: "))
leg_2 = float(input("Leg 2: "))

hypotenuse = round(math.sqrt((math.pow(leg_1, 2) + math.pow(leg_2, 2))), 3)

triangle_square = round((leg_1 * leg_2) / 2, 3)

print(f"The square of a triangle: {triangle_square}")
print(f"Its hypotenuse: {hypotenuse}")
