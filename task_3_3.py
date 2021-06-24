def thesaurus(*args):
    name_dict = {}
    for el in args:
        name_dict.setdefault(el[0], [])
        name_dict[el[0]].append(el)
    return name_dict

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Николай", "Павел", "Артем", "Евгений", "Дмитрий"))
