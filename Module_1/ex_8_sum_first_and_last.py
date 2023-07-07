# Given the input from a user, calculate the sum of the first and the last values
user_input = input("Enter any number: ")

values = [float(i) for i in user_input]

sum_values = values[0] + values[-1]

print(f"The sum of the first and the last values is {sum_values}")
