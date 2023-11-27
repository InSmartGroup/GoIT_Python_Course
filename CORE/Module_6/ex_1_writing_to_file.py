employees = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
path = "ex_1_employees.txt"


def write_employees_to_file(employee_list, path):
    file = open(path, 'w')
    for i in range(len(employee_list)):
        for j in range(len(employee_list[i])):
            file.write(f"{employee_list[i][j]}\n")


write_employees_to_file(employees, path)
