"""
Є чотирикутна схема польотів дронів з координатами (0, 1, 2, 3).
У нас є словник points, ключі якого — кортежі, точки польоту між координатами чотирикутника, вигляду (1, 2).
Значення словника — це відстані між вказаними точками.

Напишіть функцію calculate_distance, яка на вхід приймає список координат чотирикутника
зі словника [0, 1, 3, 2, 0, 2]. Функція повинна підрахувати, використовуючи вказаний словник,
яку загальну відстань пролетить дрон, рухаючись між точками польоту.

Примітки:
1. коли беремо у словника points значення, у ключі кортежі завжди має бути першою координата
з меншим значенням — (2, 3), але не (3, 2);
2. для порожнього списку та списку з однією координатою функція calculate_distance має повертати 0.
"""
# calculate_distance([0, 1, 3, 2, 0, 2]) == 17.6

points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    global points

    flight_distance = 0

    for index, item in enumerate(coordinates):
        try:
            coordinate = sorted((coordinates[index], coordinates[index + 1]))
            flight_distance += points[tuple(coordinate)]

        except IndexError:
            pass

    return flight_distance


print(calculate_distance([0, 1, 3, 2, 0, 2]))
