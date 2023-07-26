class NewInt(int):

    def __init__(self, value):
        self.value = value

    def repeat(self, n=2):
        return int(str(self.value) * n)

    def to_bin(self):
        return int(str(bin(self)[2:]))


a = NewInt(500)

print(bin(a))

print(a.to_bin())

