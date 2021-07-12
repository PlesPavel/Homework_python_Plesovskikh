def type_logger(func):

    def wrapper(*args):
        num = func(*args)
        arg_list = []
        for i in args:
            arg_list.append(str(type(i)))
        print(", ".join(arg_list))
        return num

    return wrapper

@type_logger
def grant(a, b, c):  # для примера
    print(a + b + c)

grant(10, 6, 'dfvdfvdfvdfv')
