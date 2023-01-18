# ДОМАШНЕЕ ЗАДАНИЕ №7 Полищук Анастасия

# Комментарии старого кода написала с новой стилистикой

def file() -> list:
    """
    Создает файл для заметок
    :return: заметки в итоге должны быть как спискок
    """
    try:
        with open('text_file.txt', mode='r', encoding='utf-8') as f:
            start_file = f.readlines()
    except Exception:
        start_file = list() # просто пустой список
    return start_file

def menu(dictionary: dict):
    """
    Функция выводит меню с командами, возвращает кортеж с ключами
    :param dictionary: словарь
    :return:ключи с типом данных tuple
    """
    print('Введите команду: ')
    for key, value in dictionary.items():
        # чтобы key занимал 12 символов в независимости скок в ней там знаков
        print(f'{key:12} {value}')
    return tuple(dictionary.keys())

def empty(user_list: list):
    """
    Возвращает булевое значение не пустой ли список
    :param user_list: список с заметками
    :return: булевые значения в зависимости наполнения списка
    """
    if len(user_list) > 0:
        return True
    else:
        print('Заметки не зафиксированы')


def q() -> int:
    """
    :return:Возвращает количество заметок, которое нужно вывести при выполнении earliest, latest, longest и shortest
    """
    while True:
        try:
            n = int(input('Сколько заметок Вы хотите увидеть на экране: '))
            if n < 1:
                raise ValueError
            return n
        except Exception:
            print('Не работает, попробуйте еще раз')
            continue


def get_user_choice(keys: tuple, txt: list):
    """
   Главная функция, которая запрашивает команды, кортеж ключей menu_d
    :param keys: ключи dict из функции меню
    :param txt: список с заметками из текстового файла
    :return: в соответсивии запросов пользователя выводит результат команд
    """
    # Вот тут изначальный список меняем на файл, куда сохраняются все данные
    final_l = [element.strip() for element in txt]
    while True:
        user = input()  # Переменная для ввода команд пользователя

        # add - добавление заметки
        if user == keys[0]:
            note = input('Введите заметку: ')
            final_l.append(note)

        # earliest - выводит сохраненные заметки в хронологичном порядке - от самой ранней до самой поздней
        elif user == keys[1]:
            if empty(final_l):
                n = q()
                print('От самой ранней до самой поздней')
                for i in final_l[:n]:
                    print(f'{i}')

        # latest - выводит сохраненные заметки в хронологичном порядке - от самой последней до старых
        elif user == keys[2]:
            if empty(final_l):
                n = q()
                print('От самой последней до старых')
                list_reverse = final_l[::-1]
                for i in list_reverse[:n]:
                    print(f'{i}')

        # longest - выводит заметки от самой длинной до самой маленькой
        elif user == keys[3]:
            if empty(final_l):
                n = q()
                print('От самой длинной до самой короткой:')
                longest_list = sorted(final_l, key=len, reverse=True)
                for i in longest_list[:n]:
                    print(f'{i}')

        # shortest - выводит заметки от самой маленькой до самой длинной
        elif user == keys[4]:
            if empty(final_l):
                n = q()
                print('От самой маленькой до самой длинной:')
                shortest_list = sorted(final_l, key=len, reverse=False)
                for i in shortest_list[:n]:
                    print(f'{i}')

        # vanish - очищает заметки
        elif user == keys[5]:
            final_l.clear()
            print('Заметки очищены')

        #  save and exit - выходим из программы и записываем в файл, каждая заметка с новой строки
        elif user == keys[6]:
            with open('text_file.txt', mode='w', encoding='utf-8') as ff:
                for element in final_l:
                    ff.write(element)
                    ff.write('\n')
            exit(0)
        else:
            print('Введите команду из списка!')


if __name__ == '__main__':

    menu_d = {
        'add': '- добавить заметку',
        'earliest': '- выводит сохраненные заметки в хронологическом порядке от самой ранней к самой поздней',
        'latest': '- выводит сохраненные заметки в хронологическом порядке от самой поздней к самой ранней',
        'longest': '- выводит сохраненные заметки в порядке их длины от самой длинной до кратчайшей',
        'shortest': '- выводит сохраненные заметки в порядке их длины от кратчайшей до самой длинной',
        'vanish': '- очистить блокнот',
        'save & exit': '- выйти из программы'
    }

# Откывает заметки и получает их после введения
    final_f = file()
    k = menu(menu_d)
    get_user_choice(k, final_f)