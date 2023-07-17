class Building:

    def __init__(self, floors):
        self.values = [None for i in range(0, floors)]

    def __setitem__(self, key, value):
        self.values[key - 1] = value

    def __getitem__(self, key):
        return self.values[key-1]

    def __delitem__(self, key):
        self.values[key - 1] = None


a = Building(5)
print(a.values)
print(type(a.values))
a[2] = 'sber'
print(a.values)
print(a.__getitem__(2))
a.__delitem__(2)
print(a.values)

iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])



