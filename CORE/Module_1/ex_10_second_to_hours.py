# Given the number of seconds from a user, transform it into hours, minutes, and seconds
user_input = int(input("Enter the number of seconds: "))

hours = user_input // 3600
user_input = user_input - hours * 3600

minutes = user_input // 60
user_input = user_input - minutes * 60

seconds = user_input

print(f"It is {hours} hours, {minutes} minutes, and {seconds} seconds")
