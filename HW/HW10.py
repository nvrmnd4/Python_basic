# ДОМАШНЕЕ ЗАДАНИЕ №10 Полищук Анастасия

import csv
from uuid import uuid4

# один в один функция с прошлого занятия
def create_index(tech_ids: dict, index_key: str) -> dict:
    """
    Создаем уникальные айдишники для товаров
    :param tech_ids: индекс уникальных id
    :param index_key: ключ для создания индекса
    :return: уникальные id
    """
    new_index = dict()
    for id, tech in tech_ids.items():
        if tech[index_key] in new_index:
            new_index[tech[index_key]].append(id)
        else:
            new_index[tech[index_key]] = [id]
    return new_index

# это тоже как с работниками с прошлого занятия
def brand(uids_b: dict, index_b: dict, category_name: str, debug: bool = False) -> dict:
    """
    Считает количество брендов в зарпрашиваемой категории

    :param uids_b: словарь уникальных индексов
    :param index_b: индекс категории
    :param category_name: название категории
    :param debug: флаг для проверки корректной работы
    :return: словарь
    """

    dict_brands = dict()
    for id in index_b[category_name]:
        if debug:
            print(uids_b[id])
        brand = uids_b[id]['brand']
        if brand in dict_brands:
            dict_brands[brand] += 1
        else:
            dict_brands[brand] = 1
    return dict_brands


if __name__ == '__main__':
    # Словарь для хранения данных из файла , который был дан в условии
    data = {
        'data': list()
    }
    # Делаем из файла словарь
    with open('tech_inventory.csv', newline='') as f:
        file = csv.DictReader(f)
        for row in file:
            data['data'].append(row)

    # Словарь, где ключ это id, а значение полная информация по товару
    dict_uid = dict()
    for row in data['data']:
        uid = uuid4()
        dict_uid[uid] = row

    # теперь выводим весь словарь dict_uid
    print('Перечень информации со всеми товарами с их уникальными idшниками ')
    for key, value in dict_uid.items():
        print(f'{key}, {value}')

    # Делаем вывод кол-ва в зависимости от бренда
    dict_brand = create_index(dict_uid, 'brand')
    for key, value in dict_brand.items():
        print(f'У бренда {key} есть {len(value)} товаров ')

    # Делаем вывод кол-ва товаров в категории
    dict_category = create_index(dict_uid, 'category')
    for key, value in dict_category.items():
        print(f'В категории {key} есть {len(value)} товаров ')

    # Вывод data про товары одного бренда и одной категории
    print('Все товары Apple')
    key_brand = 'Apple'
    for elem in dict_brand[key_brand]:
        print(f' {dict_uid[elem]}')

    # Вывод data про товары одной категории
    print('Все товары в категории - Smartphones')
    key_category = 'Smartphones'
    for elem in dict_category[key_category]:
        print(f'{dict_uid[elem]}')

    # Вывод сколько в каждой категории товаров разных брендов
    for category_name in dict_category.keys():
        print(f'В категории {category_name}  доступно :', brand(dict_uid, dict_category, category_name))