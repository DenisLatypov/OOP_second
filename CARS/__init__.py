class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала со скоростью {self.speed} км/ч.")

    def stop(self):
        print(f"{self.name} остановилась.")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}.")

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)

# Примеры использования классов
town_car = TownCar(60, "синий", "Городской автомобиль")
sport_car = SportCar(150, "красный", "Спортивный автомобиль")
work_car = WorkCar(80, "желтый", "Рабочий автомобиль")
police_car = PoliceCar(120, "черный", "Полицейский автомобиль")

town_car.go()
sport_car.turn("налево")
work_car.stop()
police_car.go()