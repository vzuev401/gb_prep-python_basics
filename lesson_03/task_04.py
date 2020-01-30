# homework lesson: 3, task: 4

"""
Задача:


Программа принимает действительное положительное число x и
целое отрицательное число y.

Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).

При решении задания необходимо обойтись без
встроенной функции возведения числа в степень.
"""


def my_func(x, y):
    result = x
    for _ in range(1, -y):
        result *= x

    return 1 / result


def my_func_2(x, y):

    if (x_str := str(x)).find('.') == -1:
        x_nominator = x
        x_denominator = 1
    else:
        x_nominator = int(x_str.replace('.', ''))
        x_denominator_str = '1'

        for _ in range(1, len(x_str) - x_str.index('.')):
            x_denominator_str += '0'

        x_denominator = int(x_denominator_str)

    result_nominator, result_denominator = x_nominator, x_denominator

    for _ in range(1, -y):
        n = result_nominator
        d = result_denominator

        for _ in range(1, x_nominator):
            result_nominator += n
        for _ in range(1, x_denominator):
            result_denominator += d

    return result_denominator / result_nominator

