# Given a radius of a circle, define its diameter, length, and square
import math

radius = float(input("Enter the radius: "))

pi = math.pi  # math constant

diameter = round(radius * 2, 2)
length = round(2 * pi * radius, 2)
square = round((pi * radius ** 2) / 2, 2)

print(f"A triangle with a radius of {radius} has the following parameters:")
print(f"Diameter: {diameter}")
print(f"Length: {length}")
print(f"Square: {square}")
