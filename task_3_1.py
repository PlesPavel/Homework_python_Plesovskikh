numb = input('Введите число от 1 до 10 на русском ')

def num_translate(num):
    num_dict = {'один': 'one', 'два': 'two', 'три': 'three', 'четыре': 'four',
                'пять': 'five', 'шесть': 'six', 'семь': 'seven', 'восемь': 'eight',
                'девять': 'nine', 'десять': 'ten'}
    if num == numb:
        return num_dict.get(num)

print(num_translate(numb))
