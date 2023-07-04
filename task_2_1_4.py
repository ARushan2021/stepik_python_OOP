class Counter:

    def start_from(self, arg=0):
        self.counter = arg

    def increment(self):
        self.counter += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.counter}')

    def reset(self):
        self.counter = 0


c1 = Counter()
c2 = Counter()

assert isinstance(c1, Counter)
assert isinstance(c2, Counter)
assert c1.__dict__ == {}
assert c2.__dict__ == {}

c1.start_from(45)
assert len(c1.__dict__) == 1
c1.increment()
c1.display()  # печатает 46
c1.increment()
c1.display()  # печатает 47

c2.start_from()
c2.display()  # печатает 0
c2.increment()
c2.display()  # печатает 1

c1.reset()  # обнулили с1, но с2 не должен меняться
c1.display()  # печатает 0

c2.display()  # попрежнему печатает 1
