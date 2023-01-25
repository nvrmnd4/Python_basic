import csv

with open('eggs.csv', newline='') as csvfile:
    # csv файл - это таблицы рядов и колонок (как в экселе)
    # чтобы в тексте их задать, используется три специальных символа
    # каждая новая строка - это новый ряд таблицы (специальный символ \n )
    # каждая новая колонка - delimiter, по умолчанию запятая, однако можно переопределить (в данном примере - пробел)
    # чтобы внутри значений колонки пользоваться delimiter (например длинный текст где есть и пробелы и запятые и
    # вообще все символы), используется quotechar - защитный экранирующий символ (или набор символов).
    # Между такими quotechar csv не разделяет данные по колонкам. В данном примере - |
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(type(row), row)
        print(', '.join(row))

# читаем файл со стандартными разделителями и экранированием
with open('simple_csv.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    print(type(spamreader), spamreader)
    for row in spamreader:
        print(type(row), row)

# читаем файл с заголовками колонок
with open('csv_headers_file.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(type(row), row)
        print(row['first name'], row['last name'])