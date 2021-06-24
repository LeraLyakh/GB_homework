class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police


    def go(self):
        print(f"{self.name}: машина поехала")

    def stop(self):
        print(f"{self.name}: машина остановилась")

    def turn(self, direction):
        print(f"{self.name}: машина повернула {direction}")

    def show_speed(self):
        print(f"Скорость {self.name}: {self.speed}")

    def info(self):
        print(f'\n{self.name}\nЦвет: {self.color}\nМашина полицейская: {self.is_police}')

class TownCar(Car):
    critical_speed = 60
    def show_speed(self):
        if self.speed > self.critical_speed:
            print(f"Скорость {self.name}: {self.speed} - превышение")
        else:
            print(f"Скорость {self.name}: {self.speed}")



class SportCar(Car):
    """" sport """

class WorkCar(TownCar):
    critical_speed = 40

class PoliceCar(Car):
    is_police = True

town_car = TownCar('BMW', 'Черный', 65)
sport_car = SportCar('Ferrari', 'Красный', 180)
work_car = WorkCar('BMW', 'Черный', 50)
police_car = PoliceCar('Lada', 'Белая', 60)

car_list = [town_car,sport_car,work_car,police_car]
for i in car_list:
    i.info()
    i.go()
    i.turn('направо')
    i.stop()
    i.show_speed()

