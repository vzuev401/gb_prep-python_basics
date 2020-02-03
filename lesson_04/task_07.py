# homework. lesson: 04, task: 07

"""
Задача:

Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
"""

from typing import Generator


def fact(n: int) -> Generator[int, None, int]:
    current = 1
    for i in range(2, n):
        yield current
        current *= i
    return current


for num in fact(15):
    print(num)

