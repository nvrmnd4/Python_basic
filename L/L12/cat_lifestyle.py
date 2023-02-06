import random
from cat import Cat


if __name__ == '__main__':
    cat_food = [
        'whiskas',
        'мясо',
        'рыба',
        'молоко',
        'вода',
        'сухой корм',
        'purina pro',
        'gourmet',
        'club 4 paws'
    ]
    cats = [
        Cat(name='Соник', gender='кот', age=1, breed='дворняга', preferable_meal=set(random.choices(cat_food, k=5))),
        Cat('Фантомасина', 'кошка', 13, 'британец', set(random.choices(cat_food, k=5))),
        Cat('Цезарик', 'кот', 4, 'дворняга', set(random.choices(cat_food, k=5)))
    ]
    for cat in cats:
        print(cat)
        print([cat])
        print(type(cat))
        print(cat.name, cat.age, cat.breed, cat.gender, cat.preferable_meal)
        cat.meow(random.randint(1, 6))
        for food in random.choices(cat_food, k=3):
            cat.eat(food)
        cat.sleep(random.randint(1, 15))