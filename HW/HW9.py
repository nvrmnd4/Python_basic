# ДОМАШНЕЕ ЗАДАНИЕ №9 Полищук Анастасия

def fib_generator(n):
    """
    Генератор чисел Фибоначчи
    :param n: количество элементов последовательности для вывода
    :return: возвращает числа Фибоначчи
    """
    a, b = 0, 1
    for x in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':

    while True:
        try:
            user_input = int(input('Cколько чисел Фибоначчи Вы хотите вывести на экран? '))
        except:
            raise ValueError
            continue
        # использование функции
        for elem in fib_generator(user_input):
            print(elem)

        exit(0)