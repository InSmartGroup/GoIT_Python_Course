def cut_sentence(line: str, length: int):
    """
    Given a string and a number of characters, the function returns only full words
    that contain the desired number of characters, and triple points at the end of the sentence.
    For example, given the input: ('Hi my name is Alex', 8),
    the output would be 'Hi my...'.
    :param line: Any message
    :type line: str
    :param length: The number of characters
    :type length: int
    :return: A shortened string that contains only full words
    :rtype: str
    """
    counter = length

    if counter <= 1:
        return "..."

    if len(line) > counter:
        for letter in range(counter):
            if line[counter].isalpha():
                counter -= 1
    else:
        return line

    return line[:counter] + "..."


print(cut_sentence('Hello guys it\'s very nice to meet you all', 15))
