"""Make a function that receive age, and return what they drink.

Rules:
Children under 14 old.
Teens under 18 old.
Young under 21 old.
Adults have 21 or more.

Examples:
13 --> "drink toddy"
17 --> "drink coke"
18 --> "drink beer"
20 --> "drink beer"
30 --> "drink whisky"""


def people_with_age_drink(age):
    message = ""

    if age < 14:
        message = "drink toddy"

    elif age < 18 and age >= 14:
        message = "drink coke"

    elif age < 21 and age >= 18:
        message = "drink beer"

    elif age >= 21:
        message = "drink whisky"

    return message


print(people_with_age_drink(13))
print(people_with_age_drink(17))
print(people_with_age_drink(18))
print(people_with_age_drink(20))
print(people_with_age_drink(30))
