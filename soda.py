class Soda:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingridient = ingredient
        else:
            self.ingridient = None

    def show_my_drink(self):
        if self.ingridient:
            print(f'Газировка - {self.ingridient}')
        else:
            print('Обычная газировка')

cola = Soda('Кола')
zz = Soda()
sss = Soda(4)
cola.show_my_drink()
zz.show_my_drink()
sss.show_my_drink()