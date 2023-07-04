import collections


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:

    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    def deposit(self, value):
        self.__balance = self.__balance + value

    def payment(self, value):
        if value > self.__balance:
            print('Не хватает средств на балансе. Пополните счет')
            return False
        else:
            self.__balance = self.__balance - value
            return True


class Cart:

    def __init__(self, User):
        self.user = User
        self.goods = {}
        self.__total = 0

    def add(self, Product, quantity=1):
        self.goods[Product] = self.goods.get(Product, 0) + quantity
        self.__total += quantity * Product.price


dog = Product('ovcharka', 150)
vasya = User('Vasya')

telegka1 = Cart(vasya)
telegka1.add(dog, 2)

print(telegka1.goods)
