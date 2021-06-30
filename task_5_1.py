def gen_nums(n):
    for el in range(0, n + 1):
        if el % 2:
            yield el


# Выводим работу нашего генератора (для примера)

nums = gen_nums(10)  # 10 взято для примера, вместо него можем подставить что угодно

for i in nums:
    print(i)
