"""
Другий етап. Необхідно написати функцію is_valid_password, яка перевірятиме отриманий
параметр — пароль на надійність.

Критерії надійного пароля:
1. Довжина рядка пароля вісім символів.
2. Містить хоча б одну літеру у верхньому регістрі.
3. Містить хоча б одну літеру у нижньому регістрі.
4. Містить хоча б одну цифру.

Функція is_valid_password повинна повернути True, якщо переданий параметр пароль
відповідає вимогам на надійність. Інакше повернути False.
"""


def is_valid_password(password):
    uppercase = False
    lowercase = False
    digits = False
    valid = False

    for i in password:
        if i.isupper():
            uppercase = True
        elif i.islower():
            lowercase = True
        elif i.isnumeric():
            digits = True

    if len(password) == 8 and uppercase and lowercase and digits:
        valid = True

    return valid


print(is_valid_password('AAAa9'))
print(is_valid_password('aaarty123'))
print(is_valid_password('aaArty12'))
