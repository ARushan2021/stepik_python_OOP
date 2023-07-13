import time

time.time()


class Timer:

    def __init__(self, func):
        self.func = func

    def __call__(self):
        start = time.time()
        self.func()
        end = time.time()
        delta_time = end - start
        print(f'Время работы программы {delta_time}')


@Timer
def calculate():
    for i in range(10000000):
        2 ** 100


calculate()
