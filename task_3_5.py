import random

jokes = input('Введите количество шуток, которые хотите услышать ')

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n):
    for el in range(n):
        noun = random.choice(nouns)
        adverb = random.choice(adverbs)
        adjective = random.choice(adjectives)
        joke = f'{noun} {adverb} {adjective}'
        print(joke)

get_jokes(int(jokes))
