with open('users.csv', 'r', encoding='utf-8') as f, open('hobby.csv', 'r', encoding='utf-8') as f_1, open('data.txt', 'w', encoding='utf-8') as f_2:
    f_list = []
    for line in f:
        f_list.append(line.strip().replace(',', ' '))
    f_list_1 = []
    for line in f_1:
        f_list_1.append(line.strip())
    for el in range(len(f_list_1)):
        if el < len(f_list):
            f_list_1.append(None)
        else:
            pass
    dict_task = dict(zip(f_list, f_list_1))
    for key, value in dict_task.items():
        f_2.write(f'{key}: {value}\n')
