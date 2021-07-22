class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        for el in day_month_year.split():
            if el != '-':
                my_date.append(el)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Есть такая дата'
                else:
                    return f'Такой год еще не наступил'
            else:
                return f'Нет такого месяца'
        else:
            return f'Нет столько дней в месяце'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('22 - 07 - 2021')

print(today)
print(Data.valid(20, 10, 2036))
print(today.valid(27, 13, 2021))
print(Data.extract('10 - 8 - 2019'))
print(today.extract('12 - 11 - 2021'))
print(Data.valid(8, 12, 2010))
