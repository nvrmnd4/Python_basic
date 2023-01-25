def simple_generator(n):
    for i in range(n):
        yield 'i am generator'


def readlines_generator(filename, bytes):
    """
    Функция реализует аналог встроенной readlines, но через генератор
    :param filename: имя файла для чтения
    :param bytes: скольок символов за раз обрабатывать
    :returns: функция генерирует строки файла
    """
    # Открываем файл
    with open(filename, mode='r') as f:
        # чтение первого фрагмента
        s = f.read(bytes)
        # нумерация строк
        i = 0
        # пока мы не достигли конца файла - читаем дальше
        while s:
            # проверяем есть ли в прочитанном перенос на новую строку
            lines = s.split('\n')
            # случай когда переноса на новую строку нет
            if len(lines) == 1:
                # читаем дальше
                s += f.read(bytes)
            # замечен перенос на новую строку
            else:
                # строка у нас в первом элементе списка, её и "сгенерируем"
                yield f'{i}. {lines[0]}'
                i += 1
                # всё остальное - сохраним для дальнейшего чтения
                s = '\n'.join(lines[1:])
                # если остальное - пустота, читаем вне очереди чтобы не выйти из цикла
                if not s:
                    s = f.read(bytes)


def geom_progression(start_value: float, end_value: float, q: float):
    current_value = start_value
    while current_value < end_value:
        yield current_value
        current_value *= q


if __name__ == '__main__':
    y = simple_generator(100)
    print(type(y), y)
    for x in simple_generator(10):
        print(x)

    for chunk in readlines_generator('hr_department.csv', 50):
        print(chunk)

    for x in geom_progression(1, 1000000, 3):
        print(x)