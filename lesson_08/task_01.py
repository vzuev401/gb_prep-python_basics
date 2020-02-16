# homework. lesson: 08, task: 01

"""
Реализовать класс «Дата», функция-конструктор которого
должна принимать дату в виде строки формата «день-месяц-год».

В рамках класса реализовать два метода.
- Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число».
- Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12).

Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, as_string: str):
        self.as_string = as_string

    @classmethod
    def as_numbers(cls, as_string: str):
        return tuple(map(
            int, as_string.split('-')
        ))

    @staticmethod
    def is_valid(as_string: str):
        def year_is_leap(year: int):
            if not year % 400:
                return True
            return not (year % 4 or not year % 100)

        try:
            day, month, year = map(int, as_string.split('-'))
        except ValueError:
            return False

        if month in (1, 3, 5, 7, 8, 10, 12):
            return day in range(1, 32)
        elif month in (4, 6, 9, 11):
            return day in range(1, 31)
        elif month == 2:
            return day in (range(1, 30) if year_is_leap(year) else range(1, 29))

        return False


print(Date.as_numbers('30-04-2025'))
print(Date.is_valid('29-02-2104'))

