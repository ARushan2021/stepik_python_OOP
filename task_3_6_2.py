class Addition:

    def __call__(self, *args):
        res = sum(filter(lambda x: type(x) == int or type(x) == float, args))
        return f'Сумма переданных значений = {res}'


add = Addition()
add(10, 20)
assert add(10, 20) == "Сумма переданных значений = 30"
assert add(1, 2, 3.4) == "Сумма переданных значений = 6.4"
assert add(1, 2, 'hello', [1, 2], 3) == "Сумма переданных значений = 6"


add2 = Addition()
assert add2(10, 20, 3, 3, 4, 3, 2, 43, 43) == "Сумма переданных значений = 131"
assert add2() == "Сумма переданных значений = 0"
assert add2('hello') == "Сумма переданных значений = 0"

print('Good')