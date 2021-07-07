import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    list_task = []
    for line in f:
        list_task.append(line.strip())
    if len(sys.argv) == 1:
        print("\n".join(list_task))
    elif len(sys.argv) == 2:
        a = int(sys.argv[1])
        if a == 0:
            pass
        else:
            print("\n".join(list_task[(a - 1):]))
    elif len(sys.argv) == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print("\n".join(list_task[(a - 1):b]))
