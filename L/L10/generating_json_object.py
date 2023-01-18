from random import randint, choice
import json

NUM_EMPLOYEES = 100
SALARY_LOWER_BOUND = 300
SALARY_UPPER_BOUND = 4000

# HR department data
"""
name,surname,position,date_started,inn,department,salary
"""

"""
Hunsur Krishnamurthy
I
I. S. Johar\n
Iftekar\n
Imaad Shah\n
"""
def full_for():
    # extracting full name via regular for-loop
    with open('actor_names.txt') as f:
        list_of_names = list()
        for line in f.readlines():
            if line.count(' ') == 1:
                list_of_names.append(line.strip())
        print(list_of_names)


def full_comp():
    # extracting full name via list comprehension
    with open('actor_names.txt') as f:
        list_of_names = [line.strip() for line in f.readlines() if line.count(' ') == 1]
        print(list_of_names)


def split_for() -> (list, list):
    # extracting and splitting name to first and last name via regular for-loop
    with open('actor_names.txt') as f:
        list_of_first_names = list()
        list_of_last_names = list()
        for line in f.readlines():
            line = line.split()
            if len(line) == 2:
                list_of_first_names.append(line[0])
                list_of_last_names.append(line[1])
        print(list_of_first_names)
        print(list_of_last_names)
    return list_of_first_names, list_of_last_names

def split_comp():
    # extracting and splitting name to first and last name via list comprehension
    with open('actor_names.txt') as f:
        list_of_first_names = [line.split()[0] for line in f.readlines() if line.count(' ') == 1]

    with open('actor_names.txt') as f:
        list_of_last_names = [line.split()[1] for line in f.readlines() if line.count(' ') == 1]

    print(list_of_first_names)
    print(list_of_last_names)


if __name__ == '__main__':
    first_names, last_names = split_for()
    # list comprehension когда нужно сделать более одного списка - не эффективен
    positions = ['Engineer', 'Engineer', 'Engineer', 'Manager', 'Administrator', 'Director', 'Employee', 'Employee', 'Employee', 'Employee', 'Employee']
    departments = ['Security', 'Art', 'Economics', 'HR', 'Production', 'Research']
    first_names = set(first_names)
    last_names = set(last_names)

    json_object = list()
    # генерируем случайные данные по каждому работнику
    for i in range(NUM_EMPLOYEES):
        d = {
            "name": choice(list(first_names)),
            "surname": choice(list(last_names)),
            "position": choice(positions),
            "department": choice(departments),
            "salary": randint(SALARY_LOWER_BOUND // 100, SALARY_UPPER_BOUND // 100) * 100
        }
        # к сожалению в джсон нельзя записывать о записи - можно только весь объект. Поэтому набираем его
        json_object.append(d)
    # сохраняем в джсон файл
    json.dump({"data": json_object}, open('hr_department.json', 'w'), indent=4)
