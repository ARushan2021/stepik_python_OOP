class Date:

    def __init__(self, d, m, y):
        self.day = ('0' + str(d))[-2:]
        self.month = ('0' + str(m))[-2:]
        self.year = ('000' + str(y))[-4:]

    @property
    def date(self):
        return f'{self.day}/{self.month}/{self.year}'

    @property
    def usa_date(self):
        return f'{self.month}-{self.day}-{self.year}'

d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 999)

print(d1.date) # 05/10/2001
print(d1.usa_date) # 10-05-2001
print(d2.date) # 15/03/0999
print(d2.usa_date) # 03-15-0999
