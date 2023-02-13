from .vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, model: str, color: str, gasoline_use: float):
        super().__init__(
            speed_limit=250,
            wheel_count=2,
            tire_pressure=2.2,
            color=color,
            model=model,
            maintenance_km=5000
        )
        self.gasoline_use = gasoline_use
        self.maintenance_checklist.append(f'Меняем масляный фильтр и масло в двигателе {self}')

    def __str__(self):
        return f'Мотоцикл {self.model} цвета {self.color}'

    def ride(self, km: float, local_speed_limit: float) -> float:
        """
        Такая же логика как и у базового (супер) класса, но
        так же указываем сколько расходуется топлива
        :param km:
        :param local_speed_limit:
        :return:
        """
        response = super().ride(km, local_speed_limit)
        if response > 0:
            x = self.gasoline_use * km / 100
            print(f'Во время поездки на {self} было потрачено {x:.1f} литров бензина')
        return response