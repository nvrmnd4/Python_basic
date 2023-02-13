from animals import Cat
from animals import Hen
from animals import Cow
import random


if __name__ == '__main__':
    animals = [
        Cat('Дымок', 3, 'дворовая'),
        Hen(1),
        Cow('Бурёнка', 4)
    ]
    food_variants = [
        'трава',
        'сено',
        'пшено',
        'зерно',
        'рыба',
        'мясо',
        'молоко'
    ]

    what_we_get = list()
    what_they_get = list()
    # Полиморфизм - свойство классов, при котором вызываются одинаково названные методы/атрибуты,
    # но результат вызова отличается
    # например, у классов Cat, Hen, Cow есть одинаково названные атрибуты: name и age
    # так же у этих же классов есть одинаково названные методы eat, treat & say

    for a in animals:
        a.say(3)
        for food in random.choices(food_variants, k=3):
            a.eat(food)
            what_they_get.append(food)
        what_we_get.append(a.treat())

    print(f'What we lost: {what_they_get}')
    print(f'What we got: {what_we_get}')