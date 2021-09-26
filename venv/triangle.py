'''
https://smartiqa.ru/python-workbook/class#1
'''
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):

        if not isinstance(self.a, int) or not isinstance(self.b, int) or not isinstance(self.c, int):
            return 'Нужно вводить только числа!'
        elif self.a < 0 or self.b < 0 or self.c < 0:
            return 'С отрицательными числами ничего не выйдет!'

        elif (self.a + self.b < self.c) or (self.a + self.c < self.b) or (self.b + self.c < self.a):
            return 'Жаль, но из этого треугольник не сделать'
        else:
            return 'Ура, можно построить треугольник!'

first = TriangleChecker(1,2,3)
second = TriangleChecker(1,2,5)
third = TriangleChecker(-4,5,6)
fouth = TriangleChecker('re', 5,6)

print(first.is_triangle())
print(second.is_triangle())
print(third.is_triangle())
print(fouth.is_triangle())
