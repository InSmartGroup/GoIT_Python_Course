import random


def pick_random_word(list_of_words: list):
    """
    Returns a random word from the list of words.

    :param list_of_words: A list of words
    :type list_of_words: list
    :return: A random word from the list
    :rtype: str
    """
    return random.choice(list_of_words)


def encode_the_word(word_to_encode):
    """
    Encodes a word and hides its letters from the user.

    :param word_to_encode: A single word
    :type word_to_encode: str
    :return: Encoded word
    :rtype: str
    """
    word_split = [i for i in word_to_encode]
    encoded_word = []

    for i in word_split:
        encoded_word.append("_")

    return encoded_word


def display_the_word(word_to_display: str):
    """
    Given the encoded word as a list, displays it to a user as a string.

    :param word_to_display: An encoded word as a list
    :type word_to_display: list
    :return: An encoded words as a string
    :rtype: str
    """
    return "".join([i for i in word_to_display])


def check_user_input(user_input, word_to_check):
    """
    Checks if the user has entered a letter that is presented in a word.
    :param user_input: A single letter
    :type user_input: str
    :return: True or False
    :rtype: bool
    """
    return True if user_input in word_to_check else False


def decode_the_word(letter, ):
    """

    :param letter:
    :type letter:
    :param word_to_decode:
    :type word_to_decode:
    :return:
    :rtype:
    """


def game_goes_or_not(encoded_letters):
    """

    :param encoded_letters:
    :type encoded_letters:
    :return:
    :rtype:
    """
    return True if "_" in encoded_letters else False
