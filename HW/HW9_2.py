# ДОМАШНЕЕ ЗАДАНИЕ №9 Полищук Анастасия

def word_gen(text: str):
    """
    Генератор каждое слово с новой строки
    :param text: строка s
    :return: при каждом запросе выдает следующее слово из строки s
    """
    s = text.split()
    for i in s:
        yield i

if __name__ == '__main__':
    for word in word_gen('i am generating words from text'):
        print(word)
