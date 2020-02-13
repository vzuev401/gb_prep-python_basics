from operator import add, sub, mul, truediv


class Cell:
    def __init__(self, size: int):
        if not size > 0:
            raise ValueError('Not positive size of cell.')

        self.size = size

    def __add__(self, other: 'Cell'):
        return Cell(self.size + other.size)

    def __sub__(self, other: 'Cell'):
        if (result_size := self.size - other.size) > 0:
            return Cell(result_size)

        print('!!! The result of subtraction is not positive')

    def __mul__(self, other: 'Cell'):
        return Cell(self.size * other.size)

    def __truediv__(self, other: 'Cell'):
        if (result_size := self.size // other.size) > 0:
            return Cell(result_size)

        print('!!! The result of division is not positive')

    def __str__(self):
        return f'Cell-{self.size}'

    def make_order(self, in_row: int):
        rows, rest = divmod(self.size, in_row)

        return (f'{"*" * in_row}\n' * rows) + ('*' * rest)


cell_1 = Cell(16)
cell_2 = Cell(10)

for sign, operation in (
    ('+', add),
    ('-', sub),
    ('*', mul),
    ('/', truediv),
):
    print(f'Operation "{sign}":')
    print(f'{cell_1} {sign} {cell_2} = {operation(cell_1, cell_2)}')
    print(f'{cell_2} {sign} {cell_1} = {operation(cell_2, cell_1)}')
    print()

for cell in (cell_1, cell_2):
    print(f'{cell} order with 4 each row:')
    print(cell.make_order(4))
    print()

