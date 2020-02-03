# homework. lesson: 04, task: 03

"""
Задача:

Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
"""


print([num for divisor in (20, 21) for num in range(divisor, 241, divisor)])