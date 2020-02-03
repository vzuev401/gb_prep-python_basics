# homework. lesson: 04, task: 06, part: b

"""
Задача:

Реализовать скрипт, представляющий бесконечный итератор,
повторяющий элементы некоторого списка, определенного заранее.
"""


from typing import Iterator, Sequence, TypeVar

from task_06_01 import count


T = TypeVar('T')


def cycle(sequence: Sequence[T]) -> Iterator[T]:
    """Iterator returning elements from the sequence.

    If previous element was last in sequence, then current is first.

    Parameters
    ----------
    sequence : list, tuple, range, str, bytes, bytearray

    Returns
    -------
    iterator
    """
    for index in count(0):
        yield sequence[index % len(sequence)]


if __name__ == '__main__':
    import sys

    if not sys.argv[2:]:
        print(
            'Script takes at least 2 positional parameters: \n'
            '    last (int) - count of elements; \n'
            '    others - elements to repeat. \n'
        )
    else:
        list_ = sys.argv[1:-1]
        stop_index = int(sys.argv[-1])

        for index, element in enumerate(cycle(list_)):
            if index == stop_index:
                break
            print(element)



