class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'\n{self.name} остановилась'

    def turn(self, direction):
        return f'\n{self.name} повернула {direction}'

    def show_speed(self):
        return f'Твоя скорость {self.speed}'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'Твоя скорость {self.speed}! Это превышение'
        else:
            return f'Твоя скорость {self.speed}! Это нормально'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nТвоя скорость {self.speed}! Это превышение'
        else:
            return f'Твоя скорость {self.speed}! Это нормально'


class PoliceCar(Car):
    pass


town = TownCar(50, 'Синяя', 'Kia', False)
print(town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar(250, 'Красная', 'Audi', False)
print(sport.go(), sport.show_speed(), sport.turn('направо'), sport.turn('направо'), sport.stop())

work = WorkCar(50, 'Серая', 'Lada', False)
print(work.go(), work.show_speed(), work.turn('налево'), work.stop())

police = PoliceCar(150, 'Белый', 'Mersedes', True)
print(police.go(), police.show_speed(), police.turn('направо'), police.stop())


