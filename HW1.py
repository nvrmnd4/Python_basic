# ДОМАШНЕЕ ЗАДАНИЕ ПОСЛЕ ЗАНЯТИЯ №2 Полищук Анастасия

# Задание №1 перевода градусов в радианы решено 2 способами

# первый способ
import math
user_deg = float(input(""" Введите значение в градусах
>> """))
# считаем по формуле конвертации градусов в радианы и округляем до 5 знаков после запятой
rad = round(user_deg * math.pi / 180, 5)
print(f"Вы ввели {user_deg} градусов, это {rad} радиан")

# второй способ
# библиотека math уже импортирована
user_d = float(input(""" Введите значение в градусах
>> """))
# math.radians это функция, которая конвертирует значение x из градусов в радианы
r = round(math.radians(user_d), 5)
print(f"Вы ввели {user_d} градусов, это {r} радиан")


# Задание №2 Комунальные услуги (газ)

# t это тариф за 1 кубометр газа, дан изначально
t = float(input(""" Введите Ваш тариф
>> """))

# показания всегда вносятся как целые числа при оплате коммунальных услуг, поэтому они integer
user_last = int(input(""" Введите показания прошлого месяца в кубометрах
>> """))
user_now = int(input(""" Введите показания этого месяца в кубометрах
>> """))

# округлить до 2х цифр
pay = round((user_now - user_last) * t, 2)
print(f"На Вашем счетчике {user_last} кубометров за прошлый месяц, {user_now} кубометров за "
      f"этот месяц, Вы должны заплатить {pay} грн при тарифе {t}")


# Задание №3 Налог предпринимателя

revenue = int(input(""" Введите выручку предприятия
>> """))
# налог на прибыль обычно дается в процентах, сейчас он в Украине 18%
tax = float(input(""" Введите налог на выручку
>> """))
# считаем сколько нужно заплатить налога
# мы делим на 100, потому что налог дан в процентах
tax_pay = round(tax /100 * revenue, 2)
# считаем сколько останется чистой прибыли
profit = round( revenue - tax, 2)

print(f"Вам нужно заплатить налог в размере {tax_pay} грн, тогда Ваша чистая прибыль"
      f" будет составлять {profit} грн")


# Задание №4 Затраты на топливо

сonsumption = float(input(""" Введите расход топлива на 100 км
>> """))
price = float(input(""" Введите цену на 1 л топлива
>> """))
km = int(input(""" Сколько км нужно проехать
>> """))

# Делим на 100, потому что расход дан как литры на 100 км
cost = сonsumption * km / 100 * price

print(f" Поездка обойдется Вам в {cost} грн")