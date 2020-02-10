class Car:
    def __init__(self, name: str, color: str, speed: int, is_police: bool):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'Car {self.name} moves with speed: {self.speed}')

    def stop(self):
        print(f'Car {self.name} stops.')

    def turn(self, direction: str):
        print(f'Car {self.name} turns {direction}.')

    def show_speed(self):
        print(f'Car {self.name} has the speed: {self.speed}')


class TownCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color, speed, is_police=False)

    def show_speed(self):
        if self.speed > 60:
            print(f'Speed of town car {self.name} is above the speed limit')
        else:
            super().show_speed()


class WorkCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color, speed, is_police=False)

    def show_speed(self):
        if self.speed > 40:
            print(f'Speed of work car {self.name} is above the speed limit')
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color, speed, is_police=True)


class SportCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color, speed, is_police=False)


cars = [
    TownCar('Banana', 'Black', 70),
    TownCar('Orange', 'Purple', 50),
    SportCar('Apple', 'White', 0),
    WorkCar('Pineapple', 'Blue', 70),
    WorkCar('Kiwi', 'Yellow', -70),
    PoliceCar('Coconut', 'Green', 42),
]

for car in cars:
    print(
        f'{type(car)=}\n'
        f'{car.name=}\n'
        f'{car.color=}\n'
        f'{car.speed=}\n'
        f'{car.is_police=}'
    )
    car.show_speed()

    car.go()
    car.stop()
    car.turn('left')
    car.turn('right')

    print()

