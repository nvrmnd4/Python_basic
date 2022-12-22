# Полищук Анастасия ДЗ №4

# Второй вариант решения  без try и except

n = 0  #итератор - показывает какой элемент мы сейчас рассматриваем
total = 0  #конечная сумма после выполнения программы
num = None
while True:
    number = input('Ваше число: ')
    if number.isdigit():  #проверяем является ли ввод числом с помощью функции isdigit()
        num = int(number)
    else:
        if number == 'sum':
            print(total)
        else:
            print('Введіть число або sum будь-ласка!')
        continue # continue, потому что в условии задачи программа должна и дальше работать после ошибки
    n = n+1
    total = total + num