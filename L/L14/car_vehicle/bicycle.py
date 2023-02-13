from .vehicle import Vehicle


class Bicycle(Vehicle):
    def __init__(self, model: str, color: str):
        super().__init__(
            speed_limit=30,
            wheel_count=2,
            tire_pressure=2.0,
            color=color,
            model=model,
            maintenance_km=1000
        )
        self.maintenance_checklist.append(f'Чистка цепи {self}')

    def __str__(self):
        return f'Велосипед {self.model} цвета {self.color}'

    def ride(self, km: float, local_speed_limit: float) -> float:
        """
        Такая же логика как и у базового (супер) класса, но
        так же указываем сколько расходуется топлива
        :param km:
        :param local_speed_limit:
        :return:
        """
        if km > 500:
            print(f'{km}км велосипедист без перерыва отказывается проезжать!')
            return -1
        return super().ride(km, local_speed_limit)