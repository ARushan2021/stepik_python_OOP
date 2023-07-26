class PowerTwo:

    def __init__(self, degreeMax):
        self.degreeMax = degreeMax
        self.degree = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.degree > self.degreeMax:
            raise StopIteration
        a = self.degree
        self.degree += 1
        return 2**a

numbers = PowerTwo(2)

assert hasattr(numbers, '__next__') is True
assert hasattr(numbers, '__iter__') is True

iterator = iter(numbers)
print('Элементы итератора PowerTwo(2)')
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
    raise ValueError('Не реализовали StopIteration')
except StopIteration:
    pass

print('-' * 15)
print('Элементы итератора PowerTwo(20)')
for i in PowerTwo(20):
    print(i)