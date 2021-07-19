class Matrix:

    def __init__(self, task_list):
        self.task_list = task_list

    def __str__(self):
        for row in self.task_list:
            for i in row:
                print(f"{i:3}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.task_list)):
            for el in range(len(other.task_list[i])):
                self.task_list[i][el] = self.task_list[i][el] + other.task_list[i][el]
        return Matrix.__str__(self)

neo = Matrix([[-1, 0, 1], [0, -1, 1], [0, 1, -1]])
morphius = Matrix([[-2, 0, 2], [0, -2, 2], [2, 0, -2]])
print(neo.__add__(morphius))