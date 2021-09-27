class Comparison:
    def __init__(self, string_1, string_2):
        self.string_1 = string_1
        self.string_2 = string_2

    def compair(self):
        if len(self.string_1) == len(self.string_2):
            return f'Строка {self.string_1} равна строке {self.string_2}'

        elif len(self.string_1) > len(self.string_2):
            return f'Строка {self.string_1} больше, чем строка {self.string_2}'

        else:
            return f'Строка {self.string_1} меньше, чем строка {self.string_2}'


comp1 = Comparison('qw5e', 'iu55y')
print(comp1.compair())