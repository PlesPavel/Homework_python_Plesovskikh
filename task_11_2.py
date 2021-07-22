class DivisionByZero:
    def __init__(self, divider, divisor):
        self.divider = divider
        self.divisor = divisor

    @staticmethod
    def division_by_zero(divider, divisor):
        try:
            return (divider / divisor)
        except:
            return (f'Делить на ноль нельзя')


div = DivisionByZero(11, 200)
print(DivisionByZero.division_by_zero(15, 0))
print(DivisionByZero.division_by_zero(15, 2))
print(div.division_by_zero(200, 0))
print(div.division_by_zero(200, 4))
