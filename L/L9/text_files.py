# Лекция 9 файлы, работа с файлами

import os

# Варианты обмена данными с пользователем для программного обеспечения
# 1. ввод и вывод через консоль
# input()
# print()
# 2. иной вариант ввода/вывода данных - через графический интерфейс (GUI Graphical User Interface)
# 3. ввод/вывод через файл
# 4. ввод/вывод через интернет, адрес в сети

def read_file(filename: str):
    """
    Функция читает текстовый файл, пользуясь встроенной функцией read
    :param filename: имя файла для чтения
    """
    # with так делать нужно - автоматически вызывается "закрыватель файла", инфа из буфера попадает в файл
    # f = open(filename, mode='r') а вот так делать не рекомендуется

    with open(filename, mode='r') as f:
        # r - read, w - write, a - append
        print(f, type(f))
        x = f.read(10)
        while x:
            print(x)
            x = f.read(10)
        # EOF - end of file, служебный "невидимый" символ, натыкаясь на который, программа понимает что файл прочитан
        print('file is over')


def readlines_file(filename: str):
    """
    Функция читает текстовый файл, пользуясь встроенной функцией readlines
    :param filename: имя файла для чтения
    """
    with open(filename, mode='r') as f:
        print(f, type(f))
        for line in f.readlines():
            for word in line.split():
                print(word.capitalize(), end='')
        print()
        print('file is over')


def readline_file(filename: str):
    """
    Функция читает текстовый файл, пользуясь встроенной функцией readline
    :param filename: имя файла для чтения
    """
    # если некорректно пишет/читает кириллицу, добавьте encoding='utf-8'
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f, type(f))
        x = f.readline()
        while x:
            print(x, end='')
            x = f.readline()
        print()
        print('file is over')


def write_file(filename: str, text_to_write: str):
    """
    Записывает некий текст в файл, после чего добавляет содержимое из входных данных
    :param filename: имя файла куда записывать
    :param text_to_write: входные данные для записи
    """
    # with <> as <> == вместе с <> также известным как <>
    # (а весь остальной код "вместе" не работает - то есть "без" этой переменной)
    with open(filename, mode='w') as f:
        f.write("""Hello File!
My name is Kyrylo!
"""
                )
        f.write('How are you?\n')
        f.write(text_to_write)


def writelines_file(filename: str, text_to_write: list):
    """
    Записывает данные в файл, пользуясь методом writelines
    :param filename: имя файла
    :param text_to_write: данные для записи
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.writelines(text_to_write)


def rewrite_file(filename_a: str, filename_b: str):
    """
    Функция читает файл а и записывает его содержимое в файл b
    :param filename_a: имя файла из которого берутся данные
    :param filename_b: имя файла в который записываются данные
    """
    with open(filename_a, encoding='utf-8') as f_a:
        with open(filename_b, encoding='utf-8', mode='w') as f_b:
            for line in f_a.readlines():
                f_b.write(line)


def write_append_file(filename: str, text_to_write: str):
    """
    Функция добавляет данные в файл, пользуясь режимом append (a)
    :param filename: имя файла куда добавлять данные
    :param text_to_write: текст, который нужно добавить
    """
    with open(filename, encoding='utf-8', mode='a') as f:
        f.write(text_to_write)


if __name__ == '__main__':
    read_file('text_file.txt')
    readlines_file('text_file.txt')
    readline_file('text_file.txt')

    readline_file('text_files.py')
    # os.path.join - для прописи пути к файлу, вместо использования / или \ для перехода между директориями/папками
    print(os.path.join('..', 'beginner_train_tasks.md'))
    readline_file(os.path.join('..', 'beginner_train_tasks.md'))

    text = '\n'.join(['first line', 'second line', 'well lets not count', 'last line!'])
    write_file('new_text_file.txt', text)

    rewrite_file('text_file.txt.txt', 'text_file.txt (copy).txt')

    writelines_file("new_text_file_lines.txt", ['first line\n', 'second line\n', 'well lets not count\n', 'last line!\n'])

    write_append_file('text_file.txt.txt', text)