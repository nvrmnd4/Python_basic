from animal import Animal

# Задаем новый класс с параметрами
class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        # Инициализация
        super().__init__(f'Собачка {name}', {'корм', 'рыбка', 'мясо'}, age)
        self.say_word = 'Гав'
        self.breed = breed

    def treat(self) -> str:
        """
        Уделяем время животному, ухаживаем за ним
        :return: Играем с собачкой и настроение улучшается :)
        """
        print(f'Заботимся об {self.name} и гуляем!')
        return 'Настроение улучшилось!'