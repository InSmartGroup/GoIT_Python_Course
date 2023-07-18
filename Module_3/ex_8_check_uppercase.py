def is_all_upper(text: str):
    """
    Check if the message contains only uppercase letters.
    :param text: Any message
    :type text: str
    :return: If there are any lowercase letters, the function returns False
    :rtype: bool
    """
    text = text.replace(" ", "")
    if text.isupper() or text.isnumeric() or not len(text):
        return True

    for letter in text:
        if letter.islower():
            return False


# These "asserts" are used for self-checking
print(is_all_upper("ALL UPPER"))
print(is_all_upper("all lower"))
print(is_all_upper("mixed UPPER and lower"))
print(is_all_upper(""))
print(is_all_upper("444"))
print(is_all_upper("55 55 5 "))
