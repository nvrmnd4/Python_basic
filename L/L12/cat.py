from datetime import datetime
# для каждого класса - отдельный файл


class Cat:
    # init = initialize
    # конструктор класса, в нём мы объявляем и заполняем все поля класса
    # вызывается автоматически, когда создаётся объект класса
    def __init__(
            self, name: str, gender: str, age: int,
            breed: str, preferable_meal: set, last_vet_check: datetime = None
         ):
        """
        Кот или кошка, отвечает за реализацию основных элементов жизнедеятельности
        :param name:
        :param gender: пол кошки
        :param age: возраст в годах
        :param breed: порода
        :param preferable_meal: предпочитаемая еда
        :param last_vet_check: дата последней проверки у ветеринара
        """
        # в конструкторе мы записываем в self все поля/атрибуты/свойства для контекста объекта класса
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.preferable_meal = preferable_meal
        self.fed_check = True

        if isinstance(last_vet_check, datetime):
            # month_difference = datetime.now().month - last_vet_check.month
            month_difference = (datetime.now() - last_vet_check).days // 30
            if month_difference > 6:
                self.vet_check = False
            else:
                self.vet_check = True

    def __str__(self) -> str:
        return f'{self.gender.capitalize()} породы {self.breed} по имени {self.name}, возраст {self.age} лет, обычно кушает {", ".join(self.preferable_meal)}'

    def __repr__(self) -> str:
        # repr - representation
        return str(self)

    def sleep(self, hours: int):
        """
        Кошка спит. Чем старше кошка, тем дольше спит
        :param hours: сколько часов спать
        """
        if self.age > 3:
            hours += 2
        elif self.age > 8:
            hours += 4
        print(f'{self.name} спит {hours} часов')

    def eat(self, food: str):
        """
        Кошка кушает. Если еда не подходит, кошка помякуает и есть не будет
        :param food: что кушает
        """
        if food in self.preferable_meal:
            print(f'{self.name} кушает {food} с удовольствием')
            self.fed_check = True
        else:
            print(f'{self.name} проходит мимо {food} и ни о чём не жалеет')
            self.meow(3)
            self.fed_check = False

    def meow(self, count: int):
        """
        Мяукает
        :param count: сколько раз мяукать
        """
        for i in range(count):
            print(f'{self.name} мяукает')