import json
import csv
import os

if __name__ == '__main__':
    # готовим путь к джсон файлу
    json_filename = os.path.join('..', 'lesson_10', 'hr_department.json')
    # читаем джсон файл
    json_data = json.load(open(json_filename, 'r'))
    # проверяем не пустой ли файл
    if not json_data['data']:
        print(f'File {json_filename} is empty')
        exit(-1)
    # получаем заголовки таблицы
    fieldnames = list(json_data['data'][0].keys())
    # подготавливаем .csv файл для записи
    with open('hr_department.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # записываем в файл заголовки таблицы
        writer.writeheader()
        # записываем каждый ряд
        for row in json_data['data']:
            writer.writerow(row)