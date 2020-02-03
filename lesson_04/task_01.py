# homework. lesson: 04, task: 01

"""
Задача:

Реализовать скрипт, в котором должна быть предусмотрена
функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия.

Для выполнения расчета для конкретных значений необходимо
запускать скрипт с параметрами.
"""


import argparse
from typing import Union


Rational = Union[int, float]


def employee_salary(hours: Rational, rate: Rational, premium: Rational = 0) -> Rational:
    """Calculate employee's salary.

    Formula for calculation: (`hours` * `rate`) + `premium`.

    Parameters
    ----------
    hours : int, float
    rate : int, float
    premium : int, float

    Returns
    -------
    int, float
        A salary itself.
    """
    return (hours * rate) + premium


parser = argparse.ArgumentParser(
    description="Calculate employee's salary by formula: "
                "(`hours` * `rate`) + `premium`"
)
parser.add_argument(
    'hours',
    type=float,
    help='A number represents the hours for which the salary is made.'
)
parser.add_argument(
    'rate',
    type=float,
    help='A number represents the count of money for each hour.'
)
parser.add_argument(
    '--premium',
    type=float,
    default=0.0,
    required=False,
    help='A number represents the premium. Default value: 0'
)

args = parser.parse_args()
print(employee_salary(args.hours, args.rate, args.premium))
