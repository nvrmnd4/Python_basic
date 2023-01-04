# ДОМАШНЕЕ ЗАДАНИЕ №6 Полищук Анастасия

# Функция выводит меню с командами, возвращает кортеж с ключами
def menu(dictionary: dict):
    print('Введите команду: ')
    for key, value in dictionary.items():
        # чтобы key занимал 8 символов в независимости скок в ней там знаков
        print(f'{key:8} {value}')
    return tuple(dictionary.keys())

# Возвращает булевое значение не пустой ли список
def empty(user_list: list):
    if len(user_list) > 0:
        return True
    else:
        print('Заметки не зафиксированы')

# Доп. часть задания -  Возвращает количество заметок, которое нужно вывести при выполнении earliest, latest, longest и shortest

# Верхняя границу не поняла как задать, в плане, что  заметок написано 1-2 штуки,
# а если попросить вывести 8, не выдает ошибку, а выдает эти 1-2, или это не надо?
def q() -> int:
    while True:
        try:
            n = int(input('Сколько заметок Вы хотите увидеть на экране: '))
            if n < 1:
                raise ValueError
            return n
        except Exception:
            print('Не работает, попробуйте еще раз')
            continue

# Главная функция, которая запрашивает команды, кортеж ключей menu_d
def get_user_choice(keys: tuple):
    my_list = list()  # список, куда сохраняются все данные
    while True:
        user = input()  # Переменная для ввода команд пользователя

        # add - добавление заметки
        if user == keys[0]:
            note = input('Введите заметку: ')
            my_list.append(note)

        # earliest - выводит сохраненные заметки в хронологичном порядке - от самой ранней до самой поздней
        elif user == keys[1]:
            if empty(my_list):
                n = q()
                print('От самой ранней до самой поздней')
                for i in my_list[:n]:
                    print(f'{i}')

        # latest - выводит сохраненные заметки в хронологичном порядке - от самой последней до старых
        elif user == keys[2]:
            if empty(my_list):
                n = q()
                print('От самой последней до старых')
                list_reverse = my_list[::-1]
                for i in list_reverse[:n]:
                    print(f'{i}')

        # longest - выводит заметки в порядке длины, от самой длинной до самой маленькой
        elif user == keys[3]:
            if empty(my_list):
                n = q()
                print('От самой длинной до самой короткой:')
                longest_my_list = sorted(my_list, key=len, reverse=True)
                for i in longest_my_list[:n]:
                    print(f'{i}')

        # shortest - выводит заметки в порядке длины, от самой маленькой до самой длинной
        elif user == keys[4]:
            if empty(my_list):
                n = q()
                print('От самой маленькой до самой длинной:')
                shortest_my_list = sorted(my_list, key=len, reverse=False)
                for i in shortest_my_list[:n]:
                    print(f'{i}')

        # vanish - очищает заметки
        elif user == keys[5]:
            my_list.clear()
            print('Заметки очищены')

        # exit - выходим из программы
        elif user == keys[6]:
            print('Спасибо за использование сервиса')
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
        'exit': '- выйти из программы'
    }

    tuple_keys = menu(menu_d)  # меняем ключи для дальнейшей работы программы
    get_user_choice(tuple_keys)  # работа программы уже с ключами

