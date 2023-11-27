def get_fullname(first_name, last_name, middle_name=None):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name


print(get_fullname("Petro", "Zaliznyak", "Ivanovich"))
