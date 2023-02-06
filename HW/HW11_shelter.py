from HW11_dog import Dog
from datetime import datetime, timedelta
import random

if __name__ == '__main__':
    last_vet_check = datetime.now()

    # Делаем собачек и еду
    dogs = list()
    dog_food = ['мясо',
                'рыбка',
                'корм',
                'кости',
                'субпродукты',
                'колбаса']
    for name in ['Симба',
                 'Джон',
                 'Майк',
                 'Буся',
                 'Макс',
                 'Мухтар']:
        last_vet_check -= timedelta(days=30)
        dogs.append(Dog(
            name=name,
            gender=random.choice(['мальчик', 'девочка']),
            age=random.randint(1, 10),
            breed=random.choice(['корги','шпиц','овчарка','мопс']),
            preferable_meal=set(random.choices(dog_food, k=3)),
            last_vet_check=last_vet_check
        ))
    # performing pet everyday lifestyle
    for dog in dogs:
        dog.walk(random.randint(1, 5))
        for food in random.choices(dog_food, k=3):
            dog.eat(food)

    # Проверяем все ли хорошо у собачек
    for dog in dogs:
        print(f'Проверяем все ли хорошо с собачкой {dog}')
        # Кушала ли
        if not dog.fed_check:
            if dog.gender == 'мальчик':
                print(f'{dog.name} голодный')
            elif dog.gender == 'девочка':
                print(f'Warning! {dog.name} голодная')
            else:
                print(f'{dog.name} - неизвестная особь {dog.gender}!')
        else:
            print(f'{dog.name} кушала')

        # Проверяем гуляла ли собака
        if not dog.walk_check:
            if dog.gender == 'мальчик':
                print(f'{dog.name} не гулял')
            elif dog.gender == 'девочка':
                print(f'{dog.name} не гуляла')
            else:
                print(f'{dog.name} - неизвестная особь {dog.gender}!')
        else:
            print(f'{dog.name} сегодня гуляла')

        # Была ли у ветеринара
        if not dog.vet_check:
            if dog.gender == 'мальчик':
                print(f'Warning! {dog.name} давно не был у ветеринара')
            elif dog.gender == 'девочка':
                print(f'Warning! {dog.name} давно не была у ветеринара')
            else:
                print(f'{dog.name} - неизвестная особь {dog.gender}!')
        else:
            print(f'{dog.name} была у ветеринара')
