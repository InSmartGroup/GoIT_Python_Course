def three_in_a_row(words: str):
    """
    The function returns True if there are 3 or more lateral items in a row
    :param words: A message, separated by whitespace
    :type words: str
    :return: True, if there are 3 or more str() items in a row, otherwise, returns False
    :rtype: bool
    """
    words_list = words.split()
    words_counter = 0

    for item in words_list:
        if item.isalpha():
            words_counter += 1

            if words_counter >= 3:
                return True

        elif item.isdigit():
            words_counter = 0

    if words_counter < 3:
        return False


print(three_in_a_row("one two 3 four five six 7 eight 9 ten eleven 12"))
