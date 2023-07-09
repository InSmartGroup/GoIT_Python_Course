operators = [i for i in "+-/*"]

result = []

counter = 0

operand = None
operator = None
wait_for_number = None

while True:
    action = input("Type: ")

    if counter == 0 and action.isdigit():
        result.append(action)
        counter += 1
        if len(result) == 3:
            result_intermediate = ""
            for i in result:
                result_intermediate += str(i)
            result_intermediate = eval(result_intermediate)
            result = [result_intermediate]

    elif counter == 1 and action.isdigit():
        print("Please type an operator instead of a number.")

    if counter == 1 and action in operators:
        result.append(action)
        counter -= 1

    elif counter == 0 and action in operators:
        print("Please type a number instead of an operator.")

    if action == "=":
        result = float(result[0])
        break

    print(result)

print(f"Result: {result}")
