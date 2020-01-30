# homework lesson: 3, task: 3

"""
Задача:


Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(first, second, third):
    if first >= third and second >= third:
        return first + second
    elif first >= second and third >= second:
        return first + third
    else:
        return second + third

