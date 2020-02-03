# homework. lesson: 04, task: 05

"""
Задача:

Реализовать формирование списка,
используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
"""


from functools import reduce
from operator import mul


sequence = (number for number in range(100, 1001) if not number % 2)

# print(reduce(mul, range(100, 1001, 2)))
print(reduce(mul, sequence))



