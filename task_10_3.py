class Cell:
    def __init__(self, num_cells):
        self.num_cells = int(num_cells)

    def __add__(self, other):
        return f'Размер клетки из двух равен: {self.num_cells + other.num_cells}'

    def __sub__(self, other):
        sub = self.num_cells - other.num_cells
        return f'Клетка равна: {sub}' if sub > 0 else 'Клетки больше нет'

    def __truediv__(self, other):
        return self.num_cells // other.num_cells

    def __mul__(self, other):
        return self.num_cells * other.num_cells

    def make_order(self, row):
        result = ''
        for i in range(int(self.num_cells / row)):
            result += '*' * row + '\n'
        result += '*' * (self.num_cells % row) + '\n'
        return result


cell = Cell(50)
cell_1 = Cell(14)
print(cell + cell_1)
print(cell - cell_1)
print(cell / cell_1)
print(cell * cell_1)
print(cell.make_order(10))
