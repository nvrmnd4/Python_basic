import json
import csv
import os

if __name__ = '__main__':
    json_filename = os.path.join('..', 'L10', 'hr_department.json')
    json_data = json.load(open(json_filename,'r'))
    # проверяем не пустой ли файл
    if not json_data
