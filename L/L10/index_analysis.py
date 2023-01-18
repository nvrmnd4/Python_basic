# HR department data
import json
from random import randint, choice
"""
name, surname, position, date_started, inn, department, salary

"""


# extracting full name via regular for-loop
with open('actor_names') as f:
    list_of_names = list()
    for line in f.readlines():
        if line.count(' ') == 1:
            list_of_names.append(line.strip())
print(list_of_names)

# extracting full name via comprehension
with open('actor_names') as f:
    list_of_names = [line.strip() for line in f.readlines() if line.count(' ') == 1]
    print(list_of_names)

# extracting and splitting name to first and last name via regular for-loop

with open('actor_names') as f:
    list_of_first_names = list()
    list_of_last_names = list()
    for line in f.readlines():
        line = line.split()
        if len(line) == 2:
            list_of_first_names.append(line[0])
            list_of_last_names.append(line[1])
    print(list_of_first_names)
    print(list_of_last_names)

# extracting and split name to first and last name via list comprehension
# dopisat



# list comprehension  когда нужно сделать более 1 списка - не эффективно
positions = ['Enginner', 'Manager', 'Administrator', 'Director', 'Employee']
departments = ['Security', 'Art', 'Economics', 'HR', 'Production', 'Research']

first_names = set(list_of_first_names)
last_names = set(list_of_last_names)

NUM_EMPLOYEES = 100
SALARY_LOWER_BOUND = 300
SALARY_UPPER_BOUND = 4000

json_object = list()
for i in range(NUM_EMPLOYEES):
    d = {
        'name': choice(list(first_names)),
        'surname': choice(list(last_names)),
        'position': choice(positions),
        'department': choice(departments),
        'salary': randint(SALARY_LOWER_BOUND // 100, SALARY_UPPER_BOUND // 100) *100
    }
    json_object.append(d)
json.dump({"data":json_object}, open('hr_department.json', 'w'), indent=4)
