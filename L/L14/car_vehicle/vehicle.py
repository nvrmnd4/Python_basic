class Vehicle:
    # средство передвижения
    def __init__(self, speed_limit: int, wheel_count: int, tire_pressure: float,
                 maintenance_km: float, color: str, model: str):
        """
        Средство передвижения, отвечает за техническое состояния транспортного средства
        и передвижения с его помощью
        :param speed_limit: максимальная скорость, км/ч
        :param wheel_count: сколько колёс
        :param tire_pressure: давление в шинах
        :param maintenance_km: после скольких км транспортному средству нужно техобслуживание
        :param color: цвет
        :param model: модель/производитель/название
        """
        self.speed_limit = speed_limit
        self.wheels = wheel_count
        self.tire_pressure = tire_pressure
        self.color = color
        self.model = model

        # public - доступно всем
        # _protected - доступно только наследникам
        #   (фактически - доступно всем, но это недоработка Пайтона.
        #   Нижнее подчеркивание вначале это стандарт кода -
        #   такую переменную лучше не менять без полной уверенности
        #   в этой необходимости)
        # __private - недоступно никому кроме самого класса

        self._this_is_protected = 'Is it protected?'

        self._km_passed_after_mt = float()
        self.maintenance_needed_km = maintenance_km
        self._construction_needed = True
        self._maintenance_needed = False

        self.maintenance_checklist = [
            f'Подкачиваем шины в {self.wheels} колёсах давления {self.tire_pressure} в {self}'
        ]

        self.construct()

    # getter - метод для получения копии значения защищенного поля
    # setter - метод для установки значения защищенного поля

    @property
    def construction_needed(self):
        return self._construction_needed

    @property
    def maintenance_needed(self):
        return self._maintenance_needed

    @maintenance_needed.setter
    def maintenance_needed(self, new_value: bool):
        if not new_value:
            self._km_passed_after_mt = 0.0
            self._maintenance_needed = new_value
            print(f'ТО для {self} успешно завершено!')
        elif self._km_passed_after_mt > self.maintenance_needed_km:
            self._maintenance_needed = new_value
            print(f'Пройдено {self._km_passed_after_mt:.1f}км после последнего ТО на {self}! Необходимо ТО!')


    def __str__(self):
        return f'Транспортное средство {self.model} цвета {self.color}'

    def construct(self):
        """
        Сбор транспортного средства на заводе
        """
        print(f'На заводе исправно потрудились и создали шедевр: {self} на {self.wheels} колёсах!')
        self._construction_needed = False
        self._maintenance_needed = False

    def ride(self, km: float, local_speed_limit: float) -> float:
        """
        Проехать некое расстояние на транспортном средстве
        :param km: сколько км необходимо проехать
        :param local_speed_limit: максимальная скорость на этой местности, км/ч
        :return: время в часах, за которое это возможно (если время отрицательное - произошла ошибка)
        """
        if self._construction_needed:
            print(f'{self} не готово к перемещению'
                  f' - его должны собрать на заводе!')
            return -1
        if self._maintenance_needed:
            print(f'{self} не готово к перемещению и нуждается в обслуживании!')
            return -1
        actual_speed = min(local_speed_limit, self.speed_limit)
        self._km_passed_after_mt += km
        self.maintenance_needed = True

        return round(km / actual_speed, 2)