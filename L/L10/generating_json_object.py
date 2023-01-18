import json

def create_index(employee_data: list, index_key: str) -> dict:
    new_index = dict()
    for employee in data['data']:
        if employee[index_key] in new_index:
            new_index[employee[index_key]].append(employee)
        else:
            new_index[employee[index_key]] = [employee]
    return new_index


if __name__ == '__main__':
    data = json.load(open('hr_department.json', 'r'))
    print(type(data), data)

    position_index = create_index(data['data'], 'position')
# группировка по должностям и анализ
    print(position_index)
    for key, value in position_index.items():
        print(f'на должности {key} работает {len(value)} людей')

    department_index = create_index(data['data'], 'department')
    print(department_index)
    for key, value in position_index.items():
        print(f'В отделе {key} работает {len(value)} людей')

