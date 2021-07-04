class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма z1 и z2 равна\nz = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение z1 и z2 равно\nz = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


z_1 = ComplexNumber(2, -2)
z_2 = ComplexNumber(1, -1)
print(z_1 + z_2)
print(z_1 * z_2)