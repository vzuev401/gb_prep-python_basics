# homework. lesson: 08, task: 02

"""
Создайте собственный класс-исключение,
обрабатывающий ситуацию деления на нуль.

Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class CustomZeroDivisionError(ZeroDivisionError):
    ...


try:
    dividend = float(input('Dividend: '))
    divisor = float(input('Divisor : '))

    if divisor == 0:
        raise CustomZeroDivisionError

except (ValueError, CustomZeroDivisionError):
    print('Error')
else:
    print('Result of division:', dividend / divisor)
finally:
    print('Bye.')

