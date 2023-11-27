# Given the input from a user, calculate the sum of all values and its average
user_input = input("Enter any number: ")

values = [float(i) for i in user_input]

sum_values = sum(values)
average = sum_values / len(user_input)

print(f"The sum of all values: {sum_values}")
print(f"The average: {average}")
