class Robot:

    def __init__(self):
        self.name = None

    def say_bye(self):
        print("See u later alligator")

    def set_name(self, name):
        self.name = name
        return self.name

    def say_hello(self):
        if self.name is not None:
            print(f"Hello, human! My name is {self.name}")
        else:
            print('У робота нет имени')


c3po = Robot()
c3po.say_hello()
c3po.set_name('R2D2')
c3po.say_hello()
c3po.say_bye()

r = Robot()
r.set_name('Chappy')
r.say_hello()

d = Robot()
d.say_hello()
d.set_name('Wally')
d.say_hello()

