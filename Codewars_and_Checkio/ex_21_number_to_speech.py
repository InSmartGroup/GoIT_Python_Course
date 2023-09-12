one_digit_numbers = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}

two_digit_numbers = {
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'fourty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
}


def number_length(number: str):
    return len(number)


def main(length: int, number: str):
    if length == 1:
        return f"{one_digit_numbers[number]}"

    elif length == 2:
        if number in two_digit_numbers:
            return f"{two_digit_numbers[number]}"
        else:
            new_number = number[0] + "0"
            return f"{two_digit_numbers[new_number]} {one_digit_numbers[number[1]]}"

    elif length == 3:
        if number[1:] == '00':
            return f"{one_digit_numbers[number[0]]} hundred"

        elif number[1] == '0':
            return f"{one_digit_numbers[number[0]]} hundred {one_digit_numbers[number[2]]}"

        else:
            if number[1:] in two_digit_numbers:
                return f"{one_digit_numbers[number[0]]} hundred {two_digit_numbers[number[1:]]}"
            else:
                new_number = number[1] + "0"
                return f"{one_digit_numbers[number[0]]} hundred {two_digit_numbers[new_number]} {one_digit_numbers[number[2]]}"


while True:
    number = input("Enter a number between 1 and 999: ")
    if number == 'quit' or number == 'exit':
        break

    print(main(number_length(number), number).capitalize(), '\n')
