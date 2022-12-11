# ДОМАШНЕЕ ЗАДАНИЕ №2 Полищук Анастасия

# Задание №1

word_input = input()
# перевести всё в нижний регистр
word_low = word_input.lower()
# убираем переход на новую строку
word = word_low.replace("\n","")
# убираем лишние знаки и перенос строки
filtered_word = word.replace(',', '').replace('.', '').replace('?', '').replace(';', '').replace('!', '').replace(':', '').replace('-', '').replace("'", '').replace('"', '').replace(' ', '')
# проверяем будет ли паллиндромом
if str(word) == str(word)[::-1] :
    print(f"Вы ввели {filtered_word}, это паллиндром")
else:
    print(f"Вы ввели {filtered_word}, это не является паллиндромом")

