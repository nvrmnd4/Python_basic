# последняя домашка :( Полищук Анастасия
import csv
import json
import os

class DataEntry:
    def __init__(self, name, value):
        """Объект с именем и значением"""
        self.name = name
        self.value = value


class FileProcessor:
    def __init__(self, path):
        """ путь в папку с файлами """
        self.path = path
        self.input = list()  # список для сохранения данных для class DataEntry
    def workwith(self):
        """Обробляє файли з папки та додає результат в список input."""
        for filename in os.listdir(self.path):
            if filename.endswith('.json'):  # если JSON
                json_file = JSONFileProcessor(os.path.join(self.path, filename))
                self.input += json_file.workwith()  # добавляем в список
            elif filename.endswith('.csv'):  # если CSV
                csv_file = CSVFileProcessor(os.path.join(self.path, filename))
                self.input += csv_file.workwith()  # опять добавляем в список


class JSONFileProcessor(FileProcessor):
    def __init__(self, path):
        """путь к JSON"""
        super().__init__(path)
        self.input = list()
    def workwith(self):
        """Обрабатывает JSON"""
        with open(self.path, 'r') as f:
            data = json.load(f)
            for x in data:
                if isinstance(x, dict):
                    item = DataEntry(x['name'], x['value'])
                    self.input.append(item)
        return self.input  # возвращает список


class CSVFileProcessor(FileProcessor):
    def __init__(self, path):
        """путь к CSV """
        super().__init__(path)
        self.input = list()
    def workwith(self):
        """Обрабатывает CSV """
        with open(self.path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                item = DataEntry(row[0], row[1])
                self.input.append(item)
        return self.input  # возвращает список

# Основная программа
if __name__ == '__main__':
    final = FileProcessor('SKU')
    final.workwith()
    for item in final.input:
        print(item.name, item.value)