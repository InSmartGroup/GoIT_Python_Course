# Given constant X and user inputs A and B, solve the following equation: a * x + b = 0
a = int(input("Enter A: "))
b = int(input("Enter B: "))

x = -b / a

print("The answer is: {}".format(a * x + b))
