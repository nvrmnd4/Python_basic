import csv

with open('eggs.csv', newline='') as csvfile:
    # csv файл это таблицы рядов и колонок
    # чтобы в тексте их задать используются три специльных символа
    # каждая новая строка, это новый ряд таблицы (специальный символ \n)
    # каждая новая колонка - delimeter по умолчанию это запятая , однако можно переопределить (в данном примере это пробел)
    # quotechar - защитный экранирующий символ, чтобы группу слов не разделить в разные колонки
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))

# дописать кусок

# читаем файл с заголовками колонок
with open('csv_headers_file.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(type(row), row) # выводит <class 'dict'> {'first name': 'Nastya', 'last name': ' Hruck'}
        print(row['first name'], row['last name']) # выводит Nastya  Hruck
