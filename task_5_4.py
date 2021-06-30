src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

result = [el for el, el1 in zip(src[1:], src[:]) if el > el1]

print(result)
