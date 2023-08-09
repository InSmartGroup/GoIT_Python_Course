def to_camel_case(data):
    word = data.split("_")
    word = [i.title() for i in word]
    return "".join(word)


print(to_camel_case("my_function_name"))
print(to_camel_case("i_phone"))
