# ДОМАШНЕЕ ЗАДАНИЕ №11 Полищук Анастасия
from datetime import datetime

class Dog:

    def __init__(self, name: str, age: int, gender: str, breed: str,
                 preferable_meal: set, last_vet_check: datetime = None):
        """
        Собачка
        :param name: кличка
        :param age: возраст
        :param gender: пол
        :param breed: порода
        :param preferable_meal: еда
        :param last_vet_check: был ли у ветеринара
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.preferable_meal = preferable_meal
        self.fed_check = False
        self.walk_check = False

#  вот эта вет. проверка один в один с нашей лекции
        if isinstance(last_vet_check, datetime):
            month_difference = (datetime.now() - last_vet_check).days // 30
            if month_difference > 6:
                self.vet_check = False
            else:
                self.vet_check = True

    def __str__(self) -> str:
        return f'{self.gender.capitalize()} породы {self.breed} по имени {self.name}, возраст {self.age} лет, обычно кушает {", ".join(self.preferable_meal)}'

    def eat(self, food: str):
        """
        Собачка ест. Если еда не подходит, собачка погавкает и есть не будет
        :param food: еда собачки
       """
        if food in self.preferable_meal:
            print(f'{self.name} кушает {food} с удовольствием')
            self.fed_check = True
        else:
            print(f'{self.name} проходит мимо {food} и ни о чем не жалеет')
            self.bark(2)
            self.fed_check = False

    def walk(self, hours: int):
        """
        Собачка гуляет
        :param hours: сколько гуляет собачка
        """
        if self.fed_check:
            print(f'{self.name} гуляет с удовольствием')
            self.walk_check = True
        else:
            print(f'{self.name} голодная, никуда не пойдет')
            self.walk_check = False

    def bark(self, count: int):
        """
        Собачка гавкает
        :param count: сколько раз собачка гавкнула
        """
        for i in range(count):
            print(f'{self.name} гавкает')