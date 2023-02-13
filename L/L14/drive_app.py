from vehicles import Car
from vehicles import Motorcycle
from vehicles import Bicycle
from car_service import CarService
import random
import time


if __name__ == '__main__':
    vehicle_park = [
        Car(
            color='Silver',
            model='Toyota Corolla',
            gasoline_use=8
        ),
        Car(
            color='Black',
            model='Mitsubishi Outlander',
            gasoline_use=15
        ),
        Motorcycle(
            color='Red',
            model='Jaguar',
            gasoline_use=2
        ),
        Bicycle(
            color='Green',
            model='Для города'
        )
    ]

    my_car_service = CarService('СТО')

    speed_limit = [50, 90, 140]
    while True:
        v = random.choice(vehicle_park)
        distance = random.randint(100, 1000)
        ride_time = v.ride(distance, random.choice(speed_limit))
        if ride_time > 0:
            print(f'Using {v} to ride {distance}km: {ride_time}h')
        else:
            my_car_service.maintenance(v)
        time.sleep(1)