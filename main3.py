class MethodOverriding:
    def __init__(self):
        x = X()
        y = Y()
        y.method_2()
        x.method_1()
        y.method_1()
        x = y
        x.method_1() # № 1
        x.method_2() # № 2


class X:
    def method_1(self):
        print("m1 ~ X")


class Y(X):
    def method_1(self):
        print("m1 ~ Y")

    def method_2(self):
        print("m2 ~ Y")


MethodOverriding()

