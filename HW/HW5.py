# ДОМАШНЕЕ ЗАДАНИЕ №5 Полищук Анастасия

import math
user_deg = float(input(""" Введите значение в градусах """))
def radian(d):
    rad = round(d * math.pi / 180, 5)
    return rad

result = radian(user_deg)
print(f"Вы ввели {user_deg} градусов, это {result} радиан")

