class Nicola:
    # __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        if self.name != 'Николай':
            self.name = f'Я не {self.name}, я Николай!'
        self.age = age

nic = Nicola('Николай', 33)
vladimir = Nicola('Владимир', 22)

print(nic.name)
print(vladimir.name)

vladimir.surname = 'er'
print(vladimir.surname)