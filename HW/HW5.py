# ДОМАШНЕЕ ЗАДАНИЕ №5 Полищук Анастасия

import math

# Все действия сделаем, как функцию
def radian(d):
    rad = round(d * math.pi / 180, 5)
    print(f"Вы ввели {user_deg} градусов, это {rad} радиан")
    return rad

if __name__ == '__main__':
    # применяем функцию для входных данных и выводим результаты
    user_deg = int(input("""Введите значение в градусах """))
    result = radian(user_deg)


