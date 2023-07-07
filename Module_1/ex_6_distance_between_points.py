# Given the values of point A and B, calculate the distance between them
import math

x1 = float(input("Specify point 1, axis X: "))
y1 = float(input("Specify point 1, axis Y: "))

x2 = float(input("Specify point 2, axis X: "))
y2 = float(input("Specify point 2, axis Y: "))

distance = round(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)), 3)

print(f"The distance between points A and B is {distance}")
