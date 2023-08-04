class NegativeDepositError(Exception):
    def __str__(self):
        return "Нельзя пополнить счет отрицательным значением"


class InsufficientFundsError(Exception):
    def __str__(self):
        return "Недостаточно средств для снятия"


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, value):
        if value < 0:
            raise NegativeDepositError
        else:
            self.balance += value

    def withdraw(self, value):
        if value > self.balance:
            raise InsufficientFundsError
        else:
            self.balance -= value


try:
    raise InsufficientFundsError("Недостаточно средств")
except Exception as e:
    if not isinstance(e, InsufficientFundsError):
        raise ValueError('Реализуйте исключение InsufficientFundsError')

try:
    raise NegativeDepositError("Внесено отрицательное значение")
except Exception as e:
    if not isinstance(e, NegativeDepositError):
        raise ValueError('Реализуйте исключение NegativeDepositError')

account = BankAccount(100)
assert account.balance == 100

account.deposit(50)
assert account.balance == 150

account.withdraw(75)
assert account.balance == 75

try:
    account.withdraw(100)
except InsufficientFundsError as e:
    print(e)  # "Недостаточно средств"

assert account.balance == 75

try:
    account.deposit(-50)
except NegativeDepositError as e:
    print(e)  # "Внесено отрицательное значение"
