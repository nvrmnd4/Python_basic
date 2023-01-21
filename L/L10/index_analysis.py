import json
# unique user identification
from uuid import uuid4
import random


def create_index(employee_uids: dict, index_key: str) -> dict:
    """
    Создаёт индекс по точному совпадению
    :param employee_uids: индекс уникальных айдишников каждого студента
    :param index_key: ключ по которому создавать индекс
    :return:
    """
    new_index = dict()
    for uid, employee in employee_uids.items():
        # если это значение уже есть в индексе, просто добавляем
        # например, представителей должности Инженер еще не было, а Директор - уже был
        if employee[index_key] in new_index:
            new_index[employee[index_key]].append(uid)
        # иначе, создаём список под это значение
        else:
            new_index[employee[index_key]] = [uid]
    return new_index


if __name__ == '__main__':
    data = json.load(open('hr_department.json', 'r'))
    print(type(data), data)

    # создаём уникальный айдишник под каждую запись (работника)
    # помещаем их в словарь (индекс), чтобы можно было найти полные данные о работнике по его айдишнику
    employee_ids_index = dict()
    for employee in data['data']:
        # несовершенный способ создания уникального айдишника
        _id = f'{employee["name"]}{employee["surname"]}{employee["position"]}{employee["department"]}{employee["salary"]}'
        # максимально надёжный
        _uid = uuid4()
        # сохраняем под уникальный айдишник (uuid4()) полные данные о записи
        employee_ids_index[_uid] = employee
    print(employee_ids_index)

    # создаём индекс по колонке должность
    position_index = create_index(employee_ids_index, 'position')
    """
        "name": "Anup",
        "surname": "Jha",
        "position": "Engineer",
        "department": "Art",
        "salary": 500
    """
    print(position_index)
    # смотрим сколько людей работает на каждой должности
    for key, value in position_index.items():
        print(f'На должности {key} работает {len(value)} людей')

    # то же самое с отделом
    department_index = create_index(employee_ids_index, 'department')
    print(department_index)
    for key, value in department_index.items():
        print(f'В отделе {key} работает {len(value)} людей')


    # Сделать разбивку по должностям (position) внутри каждого отдела (department)
    # Сколько работает директоров в НR? Сколько работает инженеров в ресерче? И т.д.
    # Варианты решения
    # 1. Пользоваться только одним индексом (отдела/должности), после чего фильтруем каждую группу
    # 2. Воспользоваться set и операцией intersection

# extracting and split name to first and last name via list comprehension
# dopisat

# Считает сколько должностей работает в запрашиваемом отделе
def positions_in_department_view(employee_uids: dict, _department_index: dict, department_name: str, debug: bool = False):
    """
    Функция считает сколько должностей работает в запрашиваемом отделе
    В возвращаемом словаре будут только те должности, которые есть в отделе
    :param employee_uids: индекс сотрудников
    :param _department_index: индекс отделов
    :param department_name: имя запрашиваемого отдела
    :param debug: флаг для проверки корректной работы
    :return: словарь, где ключи -  представленные в отделе должности,  значения их популяция
    """
    print(f'Кто работает в отделе {department_name}')
    positions_in_department = dict()
    for uid in _department_index[department_name]:
        if debug:
            print(employee_uids[uid])
        employee_position = employee_ids_index[uid]['position']
        if employee_position in positions_in_department:
            positions_in_department[employee_position] += 1
        else:
            positions_in_department[employee_position] = 1
        return(positions_in_department)


# list comprehension  когда нужно сделать более 1 списка - не эффективно
positions = ['Enginner', 'Manager', 'Administrator', 'Director', 'Employee']
departments = ['Security', 'Art', 'Economics', 'HR', 'Production', 'Research']



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


# Смотрим на конкретный отдел

for department_name in department_index.keys():
    print(f'В отделе {department_name} работают такие должности: ', positions_in_departments)