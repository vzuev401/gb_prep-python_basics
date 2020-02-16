# homework. lesson: 08, task: 03

"""
Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""


import re


class NotANumberException(Exception):
    ...


sequence = []
pattern = r'^[+-]?\d+\.?\d*$'

while (user_input := input('Number: ')) != 'stop':
    try:
        if re.match(pattern, user_input) is None:
            raise NotANumberException
    except NotANumberException:
        print('Not a valid value:', user_input)
    else:
        sequence.append(float(user_input))
        print('Successfully added:', user_input)
    finally:
        print('Current sequence: ', end='')
        print(*sequence, sep=', ')
        print()

