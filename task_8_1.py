import re

email_adress = input('Введите email ')


def email_parse(email_adress):
    # parsed = re.findall(r'(^\w+)@([\w+]*\.[\w]{2,})$', email_adress) # 1 вариант
    # parsed = re.findall(r'(^\w+)@((\w+).(\w{2,}))$', email_adress) # 2 вариант
    parsed = re.findall(r'(^\w+)@(\w+).(\w{2,})$', email_adress)  # 3 вариант
    if not parsed:
        raise ValueError(f'Это не email: {email_adress}')
    # return dict(zip(['username', 'domain'], parsed[0]))  # для варианта 1 и 2
    return dict(zip(['username', 'domain', 'country'], parsed[0]))  # для 3 варианта


print(email_parse(email_adress))  # Проверил все 3 варианта и вроде как все 3 работают
