class ComplexNumb:
    def __init__(self, num_1, num_2, *args):
        self.num_1 = num_1
        self.num_2 = num_2
        self.exp = num_1 + num_2

    def __add__(self, other):
        print(f'Сумма одного числа с другим равна')
        return f'{self.num_1 + other.num_1} + {self.num_2 + other.num_2}'

    def __mul__(self, other):
        print(f'Произведение одного числа на другое равно')
        return f'{self.num_1 * other.num_1 - (self.num_2 * other.num_2)} + {self.num_2 * other.num_1}'

    def __str__(self):
        return f'{self.num_1} + {self.num_2}'


num_3 = ComplexNumb(-5, 8)
num_4 = ComplexNumb(9, 13)
print(num_3)
print(num_3 + num_4)
print(num_3 * num_4)
