class UnitedKingdom:

    def get_capital(self):
        print('London is the capital of Great Britain.')

    def get_language(self):
        print('English is the primary language of Great Britain.')


class Spain:

    def get_capital(self):
        print('Madrid is the capital of Spain.')

    def get_language(self):
        print('Spanish is the primary language of Spain.')


obj_uk = UnitedKingdom()
obj_spa = Spain()
for country in (obj_spa, obj_uk):
    country.get_capital()
    country.get_language()