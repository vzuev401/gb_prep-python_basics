from typing import Sequence


class Matrix:
    def __init__(self, as_list: Sequence):
        if not type(as_list) in (list, tuple):
            raise ValueError(
                f'as_list has type {type(as_list)}. '
                f'Should be a tuple or a list'
            )

        # check rows have equal lengths
        if not len(set(map(len, as_list))) == 1:
            raise ValueError('Rows have different lengths')

        self.as_list = as_list

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.as_list)

    def __add__(self, other: 'Matrix'):
        result = list(map(
            lambda pair_rows: list(map(sum, zip(*pair_rows))),
            zip(self.as_list, other.as_list)
        ))

        return Matrix(result)


first_matrix = Matrix([
    [1, 2],
    [3, 4],
    [1, 3],
])
second_matrix = Matrix([
    [-1, 0],
    [10, -10],
    [0, 0],
])

print('Matrix 1:')
print(first_matrix)
print()

print('Matrix 2:')
print(second_matrix)
print()

print('Their sum:')
print(first_matrix + second_matrix)

