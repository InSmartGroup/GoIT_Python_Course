def from_camel_case(name: str):
    """
    The function accepts a message written in CamelCase and returns the same message in snake_case.
    :param name: Any message in written in CamelCase
    :type name: str
    :return: The same message in snake_case
    :rtype: str
    """
    name_list = list(name)
    for index, letter in enumerate(name_list):
        if letter.isupper():
            name_list[index] = letter.lower()
            name_list.insert(index, "_")

    return "".join(name_list[1:])


print(from_camel_case("MyFunctionName"))
print(from_camel_case("IPhone"))
print(from_camel_case("HereIsMyFunction"))
print(from_camel_case("IceCreamTastesSoGood"))
