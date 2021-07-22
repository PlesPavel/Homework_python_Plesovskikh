# task_11_4, 11_5, 11_6
class Store:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.store_full = []
        self.store = []
        self.unit = {'Техника': self.name, 'Цена': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        try:
            name_machine = input(f'Введите название ')
            price = int(input(f'Введите цену '))
            lot = int(input(f'Введите количество '))
            unique = {'Техника': name_machine, 'Цена': price, 'Количество': lot}
            self.unit.update(unique)
            self.store.append(self.unit)
            print(f'Список всей оргтехники -\n {self.store}')
        except:
            return f'Введены не правильные данные'

        q = input('Для выхода введите - esc, для продолжения - y ')
        if q == 'Q' or q == 'q':
            self.store_full.append(self.store)
            print(f'На складе -\n {self.store_full}')
            return f'Выход'
        else:
            return Store.reception(self)


class Printer(Store):
    def to_print(self):
        return f'На складе {self.numb} принтеров'


unit_machine = Printer('hp', 2000, 5, 10)
print(unit_machine.reception())
print(unit_machine.to_print())
