class One:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Two(One):

    def __init__(self, x, y, z):
        self.z = z
        super().__init__(x, y)


rt = Two(1, 3, 5)
print(rt.x)
print(rt.y)
print(rt.z)

# commit