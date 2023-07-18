def checkio(number: int):
    """
    The function multiplies only real numbers. Zeros are skipped.
    :param number: Any number
    :type number: int
    :return: The result of multiplication
    :rtype: int
    """
    number_str = str(number).replace("0", "")
    result = 1

    for num in number_str:
        result *= int(num)

    return result


print(checkio(10000))
print(checkio(999))
print(checkio(123405))
print(checkio(100267407))
