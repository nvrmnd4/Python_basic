# ДОМАШНЕЕ ЗАДАНИЕ №8 Полищук Анастасия

if __name__ == '__main__':
    with open('file', mode='r', encoding='utf-8') as f:
        txt = f.readlines()
    # Нужно удалить перенос строки
    # Вырезать до буквы а и добавить элемент, если есть маленькая буква а (если нет, то пустая строка)
    # Первая буква большая, а остальные маленьк е
    final = [x.strip()[x.find('a'):].capitalize() if 'a' in x else '' for x in txt]
    # Выводим результат
    print(f'Конечный список: {final}')

    # file.txt иногда на Маке выкидывает ошибку, поэтому написала в with open просто 'file'
    # Ошибка выглядит так:
    # FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
