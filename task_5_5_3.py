import re


class PasswordInvalidError(Exception):
    pass


class PasswordLengthError(PasswordInvalidError):
    def __str__(self):
        return 'Пароль должен быть не менее 8 символов'


class PasswordContainUpperError(PasswordInvalidError):
    def __str__(self):
        return 'Пароль должен содержать хотя бы одну заглавную букву'


class PasswordContainDigitError(PasswordInvalidError):
    def __str__(self):
        return 'Пароль должен содержать хотя бы одну цифру'


class User:

    def __init__(self, username, password=None):
        self.username = username
        self.password = password

    def set_password(self, value):
        if len(value) < 8:
            raise PasswordLengthError
        if value == value.lower():
            raise PasswordContainUpperError
        if re.search('[0-9]', value) is None:
            raise PasswordContainDigitError
        self.password = value




assert issubclass(PasswordInvalidError, Exception)
assert issubclass(PasswordLengthError, PasswordInvalidError)
assert issubclass(PasswordContainUpperError, PasswordInvalidError)
assert issubclass(PasswordContainDigitError, PasswordInvalidError)

user = User("johndoe")

try:
    user.set_password("weakpwd")
except PasswordLengthError as e:
    print(e)

try:
    user.set_password("strongpassword8")
except PasswordContainUpperError as e:
    print(e)

try:
    user.set_password("Safepassword")
except PasswordContainDigitError as e:
    print(e)

user.set_password("SecurePass123")
assert user.password == 'SecurePass123'
