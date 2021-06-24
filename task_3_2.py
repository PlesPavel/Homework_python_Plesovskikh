# Не могу понять почему при вводе цифры с первой буквой
# верхнего регистра выдает None как только не крутил

numb = input('Введите число от 1 до 10 на русском ')

def num_translate(num):
    num_dict = {'один': 'one', 'два': 'two', 'три': 'three', 'четыре': 'four',
        'пять': 'five', 'шесть': 'six', 'семь': 'seven', 'восемь': 'eight',
        'девять': 'nine', 'десять': 'ten'}

    if num.istitle():
        print(num_dict.get(num.title()))
    print(num_dict.get(num))

num_translate(str(numb))
