from math import prod


class Vector:

    def __init__(self, *args):
        self.values = [args[i] for i in range(len(args)) if type(args[i]) == int]
        self.values.sort()
        if len(self.values) < 1:
            self.values = []

    def __str__(self):
        if len(self.values) > 0:
            val = str(self.values)[1:-1]
            return f'Вектор({val})'
        else:
            return 'Пустой вектор'

    def __add__(self, other):
        if isinstance(other, int):
            new_arr = [i + other for i in self.values]
            return Vector(*new_arr)
        elif isinstance(other, Vector) and len(other.values) == len(self.values):
            new_arr = [self.values[i] + other.values[i] for i in range(len(self.values))]
            return Vector(*new_arr)
        elif isinstance(other, Vector) and len(other.values) != len(self.values):
            return print('Сложение векторов разной длины недопустимо')
        else:
            return print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, int):
            new_arr = [i * other for i in self.values]
            return Vector(*new_arr)
        elif isinstance(other, Vector) and len(other.values) == len(self.values):
            new_arr = [self.values[i] * other.values[i] for i in range(len(self.values))]
            return Vector(*new_arr)
        elif isinstance(other, Vector) and len(other.values) != len(self.values):
            return print('Умножение векторов разной длины недопустимо')
        else:
            return print(f'Вектор нельзя умножать с {other}')


v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"

