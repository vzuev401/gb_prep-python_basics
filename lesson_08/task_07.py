# homework. lesson: 08, task: 07

"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел.

Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров.

Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, real: float = 0, imag: float = 0):
        self.real = real
        self.imag = imag

    def __add__(self, other: 'Complex'):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other: 'Complex'):
        real = (self.real * other.real) - (self.imag * other.imag)
        imag = (self.real * other.imag) + (self.imag * other.real)

        return Complex(real, imag)

    def __str__(self):
        return f'({self.real},{self.imag}j)'


c1 = Complex(2, 3)
c2 = Complex(-1, 1)

print('c1:', c1)
print('c2:', c2)
print()
print('c1 + c2 =', c1 + c2)
print('c1 * c2 =', c1 * c2)

