# homework. lesson: 04, task: 06, part: a

"""
Задача:

Реализовать скрипт, представляющий бесконечный итератор,
генерирующий целые числа, начиная с указанного
"""

from typing import Iterator


def count(start: int) -> Iterator[int]:
    """Iterator of integer numbers from `start`.

    Parameters
    ----------
    start : int

    Returns
    -------
    iterator
    """
    while True:
        yield start
        start += 1


if __name__ == '__main__':
    import sys

    if not sys.argv[2:]:
        print(
            'Script takes 2 positional parameters: \n'
            '    first (int) - first element in sequence; \n'
            '    second (int) - last element in sequence. \n'
            '\n'
            'If second < first - only first will be printed.'
        )
    else:
        init_int = int(sys.argv[1])
        stop_int = int(sys.argv[2])

        for num in count(init_int):
            print(num)

            if num >= stop_int:
                break

