grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}


def formatted_grades(students_collection):
    table = []

    for index, key in enumerate(students):
        table.append("{:>4}|{:<10}|{:^5}|{:^5}|".format(index + 1, key, students[key], grades[students[key]]))

    return table


print(formatted_grades(students))
