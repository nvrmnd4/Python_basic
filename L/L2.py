# Лекция №2 03.12.2022 Числа

x = 5
print(x+3)

#type - функция возвращает тип данных переменной
print(type(x))
#int целые числа, float - числа с плавающей точкой, str - строка

z = 5*7
print (z)

y = 5.5
y = int(y)
print(y)
y = float(y)
print(y)

# для округления по правилам математики - round(число, сколько знаков после запятой оставить)

a = 5.433172671
print(round(a, 2))

# уменьшаем переменную на 1

u = 10
u -= 1
print(u)

u += 1
u *= 2
u /= 4

# для деления без остатка
print(9//2)

# операция получения остатка от деления
print(9 % 2)

# сразу делает и деление нацело, и нахождение остатка от деления
d,m = (divmod(9,2))

# более сложный вариант получить значения внутренние
dm = (divmod(9,2))
d = dm[0]
m = dm[1]

# степень это или **, или pow()
print(25**(0.5))
print(pow(25,0.5))

# abs это модуль
x = 10-100
print(x)
print(abs(x))

#площадь треугольника по формуле Герона и проверка существует ли такой треугольник
a, b, c = 3, 4, 5
# условие if добавляет ответвление, сначала при выполнение, потом при не выполнении
# вместо and может быть or, чтобы выолнялось хотя бы одно из условий
if a + b > c and b + c > a and a + c > b:
    print(' Условие выполняется')
else:
    print(f'треугольника со сторонами {a}, {b}, {c} существовать не может и площади у него тоже нет')
p = (a + b + c)/2
s = pow(p*(p-a)*(p-b)*(p-c),0.5)
print(f'Площадь треугольника со сторонами {a}, {b}, {c} составляет: {s}')

# покупка валюты

buy_usd = 40.3
sell_usd = 39.8

user_choice = input("""Выберите одно:
 1. Продать USD
 2. Купить USD
 >>""")

user_usd = input("""Сколько USD?
 >>""")
user_usd = float(user_usd)

print(type(user_choice))
# = оператор присвоениея, == оператор сравнения
if user_choice == "1":
    uah = round(user_usd * sell_usd)
    print(f"Вы продаёте ${user_usd} USD, вот Ваши {uah} UAH")
if user_choice == "2":
    uah = round(user_usd * buy_usd)
    print(f"Вы покупаете ${user_usd} USD, вот Ваши {uah} UAH")


# количество секунд, минут, часов и дней

orig_seconds = 3665

minutes, seconds = divmod(orig_seconds,60)
hours, minutes = divmod(minutes, 60)
days, hours = divmod(hours,24)
print(f"{hours} hours, {minutes} minutes, {seconds} seconds")


