# ДОМАШНЕЕ ЗАДАНИЕ №12 Полищук Анастасия

from cat import Cat
from hen import Hen
from cow import Cow
from dog import Dog
import random


if __name__ == '__main__':
    animals = [
        Cat('Дымок', 3, 'дворовая'),
        Hen(1),
        Cow('Бурёнка', 4),
        Dog('Буся', 2, 'корги')
    ]
    food_variants = [
        'трава',
        'сено',
        'пшено',
        'зерно',
        'рыба',
        'мясо',
        'молоко',
        'косточка',
        'вода'
    ]
    # Полиморфизм - свойство классов, при котором вызываются одинаково названные методы/атрибуты,
    # но результат вызова отличается
    # например, у классов Cat, Hen, Cow есть одинаково названные атрибуты: name и age
    # так же у этих же классов есть одинаково названные методы eat, treat & say
    what_we_get = list()
    what_they_get = list()

    for a in animals:
        a.say(3)
        for food in random.choices(food_variants, k=5):
            a.eat(food)
            what_they_get.append(food)
        what_we_get.append(a.treat())

    print(f'What we lost: {what_they_get}')
    print(f'What we got: {what_we_get}')

    # Выводим на экран тех, кому нужен уход и если все ок - пишем что так и есть
    check = 0
    for anim in animals:
        if anim.eat_today:
            print(f'{anim.name} голодный, нужно покормить')
            check += 1
    if check == 0:
        print('все прекрасно! Все животные счастливы')