# This program checks if a user enters his ATM pin correctly
tries = 3

while True:

    try:
        if tries == 0:
            print("The card has been blocked. Please contact your bank.")
            break

        elif tries == 1:
            print("Warning! You have 1 try left before your bank card is blocked.")

        pin = int(input("Enter your pin-code: "))

        if len(str(pin)) == 4:
            print("\nYou are now allowed to use the ATM.")
            break

        elif len(str(pin)) < 4 or len(str(pin)) > 4:
            tries -= 1
            print("The pin-code must contain 4 digits.\n")
            continue

    except ValueError:
        tries -= 1
        print("Incorrect pin-code. Please enter a 4-digit number.\n")
