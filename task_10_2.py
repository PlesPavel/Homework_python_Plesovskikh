from abc import ABC


class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @property
    def consumption(self):
        return f'Количество ткани: {self.name / 6.5 + 0.5 + 2 * self.name + 0.3 :.2f}'


class Coat(Clothes):
    def consumption(self):
        return f'Для пальто нужно: {self.name / 6.5 + 0.5 :.2f} ткани'


class Costume(Clothes):
    def consumption(self):
        return f'Для костюма нужно: {2 * self.name + 0.3 :.2f} ткани'


coat = Coat(1000)
costume = Costume(200)
print(coat.consumption())
print(costume.consumption())
