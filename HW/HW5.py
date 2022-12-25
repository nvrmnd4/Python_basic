# ДОМАШНЕЕ ЗАДАНИЕ №5 Полищук Анастасия


def Palindrome(s):
    return s == s[::-1]

word_input = str(input("""Введите строку """))
word_low = word_input.lower()
word = word_low.replace("\n", "")
filtered_word = word.replace(',', '').replace('.', '').replace('?', '').replace(';', '').replace('!','').replace(':', '').replace('-', '').replace("'", '').replace('"', '').replace(' ', '')

final_word = Palindrome(filtered_word)

if final_word:
    print(f"Вы ввели {filtered_word}, это паллиндром")
else:
    print(f"Вы ввели {filtered_word}, это не является паллиндромом")


