from vehicles import Vehicle


class CarService:
    def __init__(self, name):
        self.name = name

    def maintenance(self, vehicle: Vehicle):
        """
        Обслуживание транспортного средства
        """
        if not vehicle.construction_needed:
            print(f'На {self.name} проводится ТО для {vehicle}')
            for point in vehicle.maintenance_checklist:
                print(point)

            vehicle.maintenance_needed = False
        else:
            print(f'{vehicle} не готово к ТО'
                  f' - его должны собрать на заводе!')