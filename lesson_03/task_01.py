# homework lesson: 3, task: 1

"""
Задача:


Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление.

Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


from enum import Enum
from typing import Union, Optional


class Sign(Enum):
    POSITIVE = '+'
    NEGATIVE = '-'


def div(
    dividend: Union[int, float, complex],
    divisor: Union[int, float, complex],
    *,
    zero_sign: Optional[Sign] = None
) -> Union[float, complex]:
    """Divides the `dividend` by the `divisor`.

    Result will satisfy `div(a, b) * b == a` if `divisor` is not equal to 0.
    If `divisor` is unsigned 0, then the result is undefined.
    If `divisor` is signed 0 with `zero_sign`, then the result of the division
    may be `inf` or `-inf` or `nan` (also, for real and imag parts of complex).

    Parameters
    ----------
    dividend : int, float, complex
    divisor : int, float, complex
    zero_sign: Sign, optional

    Returns
    -------
    float, complex

    Examples
    --------
    >>> div(2.0, 1.0)
    2.0

    >>> div(float('-inf'), -3)
    inf

    >>> div(2, float('inf'))
    0.0

    >>> div(4, 0)
    nan

    >>> div(4, 0, zero_sign=Sign.NEGATIVE)
    -inf

    >>> div(0, 0, zero_sign=Sign.NEGATIVE)
    nan

    >>> div(complex(1, 2), 0)
    (nan+nanj)

    >>> div(complex(1, -2), 0, zero_sign=Sign.POSITIVE)
    (inf-infj)

    >>> div(4, complex(1, 2))
    (0.8-1.6j)

    """
    if not divisor:
        # division by complex always divides zero by zero
        if type(divisor) == complex:
            return complex(float('nan'), float('nan'))

        # if division divides a non-zero `dividend` by a signed zero
        if dividend and zero_sign:
            sign_mul = 1 if zero_sign is Sign.POSITIVE else -1

            if type(dividend) == complex:
                return complex(
                    sign_mul * float('inf') * dividend.real,
                    sign_mul * float('inf') * dividend.imag
                )
            return sign_mul * float('inf') * dividend

        # if `dividend` is equal to 0, or `divisor` is a non-signed zero
        if type(dividend) == complex:
            return complex(float('nan'), float('nan'))
        return float('nan')

    return dividend / divisor


def __input_number_with_sign(
    number_name: str,
    stop_string: str = 'q'
) -> (Union[float, complex], Optional[Sign]):
    """Get a number from user.

    Executes a loop asking for user's input while
    this input will not represent a number (int or float or complex) or
    will not be a string 'q'.
    Also returns a sign of user's number if
    first char of user's string is '+' or '-".

    Parameters
    ----------
    number_name : str
        Name used in a message asking for user's input.
    stop_string : str, optional
        User's input that will prevent next iteration.

    Returns
    -------
    ({int, float, complex}, {Sign, None})
        Tuple with a number as first element and
        an optional Sign as second element

    """
    message_incorrect_value = (
        '\n'
        'Incorrect value "{0}": \n'
        '"{0}" does not represent complex or float or int'
        '\n'
    )
    number = None

    while (user_input := input(f'Enter a {number_name}: ').strip()) != stop_string:
        if not user_input:
            print(message_incorrect_value.format(user_input))
            continue

        try:
            number = int(user_input)
            break
        except ValueError:
            pass

        try:
            number = float(user_input)
            break
        except ValueError:
            pass

        try:
            number = complex(user_input)
            break
        except ValueError:
            print(message_incorrect_value.format(user_input))

    sign = None if (s := user_input[0]) not in ('+', '-') else Sign(s)

    return number, sign


if __name__ == '__main__':
    print(
        'Division. Enter "q" to quit.',
        '',
        'For complex numbers use form [sign][<float_or_int><sign>]<float_or_int>j.',
        'Example: 1.2+3j, -2+0j, +9-0j.',
        'Note: two signs in a row is an incorrect input.',
        '',
        sep='\n'
    )

    while True:
        dividend, _ = __input_number_with_sign('dividend')
        if dividend is None:
            break
        divisor, sign = __input_number_with_sign('divisor')
        if divisor is None:
            break

        print(
            f'\n'
            f'{dividend} / {divisor} = {div(dividend, divisor, zero_sign=sign)}'
            f'\n'
        )

