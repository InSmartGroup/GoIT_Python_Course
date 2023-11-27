def get_grade(key):
    ects_grades = {'F': 1, 'FX': 2, 'E': 3, 'D': 3, 'C': 4, 'B': 5, 'A': 5, 'AA': None}

    if key:
        return ects_grades[key]
    else:
        return None


def get_description(key):
    grade_descriptions = {'F': 'Unsatisfactorily', 'FX': 'Unsatisfactorily',
                          'E': 'Enough', 'D': 'Satisfactorily', 'C': 'Good',
                          'B': 'Very good', 'A': 'Perfectly', 'AA': None}

    if key:
        return grade_descriptions[key]
    else:
        return None


print(get_grade('F'))
print(get_description('F'))
print(get_grade('FX'))
print(get_description('FX'))
print(get_grade('B'))
print(get_description('B'))
print(get_grade('C'))
print(get_description('C'))
print(get_grade('A'))
print(get_description('A'))
print(get_grade(""))
print(get_description(""))
print(get_grade('AA'))
print(get_description('AA'))
