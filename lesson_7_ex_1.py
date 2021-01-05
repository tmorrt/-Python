class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        for n in self.lst:
            for m in n:
                print(m, end='  ')
            print()

    def __add__(self, other):
        for n in range (len(self.lst)):
            for m in range (len(self.lst[n])):
                self.lst[n][m] = self.lst[n][m] + other.lst[n][m]
        Matrix.__str__(self)

matrix_1 = Matrix([[1, 2, 3],
                   [-1, 0, 1],
                   [2, 1, -1]])

matrix_2 = Matrix([[3, 2, 1],
                   [1, 1, 1],
                   [4, -3, -2]])

print('Метод __str__:')
matrix_1.__str__()

print()

print('Метод __add__:')
matrix_1.__add__(matrix_2)