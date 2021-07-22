class Check:

    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                el = int(input('Введите значение - '))
                self.my_list.append(el)
                print(self.my_list)
            except:
                print(f'Недопустимое значение, нужно число')
                choice = input(f'Еще пробуем? Введите да или нет ')

                if choice == 'да':
                    print(try_except.my_input())
                elif choice == 'нет':
                    return f'Ок, как хочешь'
                    break
                else:
                    return f'Ну и ладно'


try_except = Check()
print(try_except.my_input())
