class CustomButton:

    def __init__(self, text, **kwargs):
        self.text = text
        for key, value in kwargs.items():
            self.__dict__[key] = value

    def config(self, **kwargs):
        self.__dict__.update(kwargs)

    def click(self):
        try:
            self.command()
        except AttributeError:
            print('Кнопка не настроена')
        except TypeError:
            print('Кнопка сломалась')








