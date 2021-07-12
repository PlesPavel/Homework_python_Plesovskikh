def val_checker(callback):
    def val_checker_1(func):
        def val_checker_2(*args):
            if callback(*args):
                a = func(*args)
                return a
            else:
                raise ValueError('Ошибка')

        return val_checker_2
    return val_checker_1

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

print(calc_cube(-2))
