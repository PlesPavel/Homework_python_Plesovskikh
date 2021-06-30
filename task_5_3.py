tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Павел', 'Алексей'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def gens_tutor_klass(index):
    for el in range(0, index + 1):
        if el < len(tutors) and el < len(klasses):
            yield tutors[el], klasses[el]
        elif len(tutors) > el >= len(klasses):
            yield tutors[el], None
        else:
            yield None


gens = gens_tutor_klass(8)  # Число 8 выбрано для примера, можно подставить любое

for i in gens:
    print(i)
