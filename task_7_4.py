import os

dict_task = {10: 0, 100: 0, 1000: 0, 10000: 0}

def get_file(dir_name):
    for el in os.listdir(dir_name):
        if os.path.isdir(f'{dir_name}/{el}'):
            get_file(f'{dir_name}/{el}')
        else:
            if os.stat(f'{dir_name}/{el}').st_size < 10:
                dict_task[10] += 1
            elif 10 < os.stat(f'{dir_name}/{el}').st_size < 100:
                dict_task[100] += 1
            elif 100 < os.stat(f'{dir_name}/{el}').st_size < 1000:
                dict_task[1000] += 1
            elif 1000 < os.stat(f'{dir_name}/{el}').st_size < 10000:
                dict_task[10000] += 1
            else:
                print('Остальные файлы больше 100000 байт')

get_file('my_project')
print(dict_task)
