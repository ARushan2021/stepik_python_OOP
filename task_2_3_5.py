class CustomLabel:

    def __init__(self, text, **kwargs):
        self.text = text
        for key, value in kwargs.items():
            self.__dict__[key] = value

    def config(self, **kwargs):
        self.__dict__.update(kwargs)


label1 = CustomLabel(text="Hello Python", fg="#eee", bg="#333")
label2 = CustomLabel(text="Username")
label3 = CustomLabel(text="Password", font=("Comic Sans MS", 24, "bold"), bd=20, bg='#ffaaaa')
label4 = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')
label5 = CustomLabel(text="qwwerty", a=20, b='#ffaaaa', r=[3, 4, 5, 6], p=32)

assert label1.__dict__ == {'text': 'Hello Python', 'fg': '#eee', 'bg': '#333'}
assert label2.__dict__ == {'text': 'Username'}
assert label3.__dict__ == {'text': 'Password', 'font': ('Comic Sans MS', 24, 'bold'), 'bd': 20, 'bg': '#ffaaaa'}
assert label4.__dict__ == {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}
assert label5.__dict__ == {'text': 'qwwerty', 'a': 20, 'b': '#ffaaaa', 'r': [3, 4, 5, 6], 'p': 32}

print(label1.__dict__)
print(label2.__dict__)
print(label3.__dict__)
print(label4.__dict__)
print(label5.__dict__)

label4.config(color='red', bd=100)
label5.config(color='red', bd=100, a=32, b=432, p=100, z=432)

assert label4.__dict__ == {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}
assert label5.__dict__ == {'text': 'qwwerty', 'a': 32, 'b': 432, 'r': [3, 4, 5, 6], 'p': 100,
                           'color': 'red', 'bd': 100, 'z': 432}
