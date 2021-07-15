class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt(self):
        asphalt = self._length * self._width * self.weight * self.height / 1000
        print(f'для укладки асфальта необходимо {asphalt} тонн материала')

highway = Road(100000, 12)
highway.asphalt()