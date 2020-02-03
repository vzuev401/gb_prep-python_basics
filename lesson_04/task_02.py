# homework. lesson: 04, task: 02

"""
Задача:

Представлен список чисел.
Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
"""


from random import choices, randint


sequence = choices(range(100), k=randint(5, 15))
processed_sequence = [
    sequence[i]
    for i in range(1, len(sequence))
    if sequence[i] > sequence[i-1]
]

print(f'Initial sequence  : {sequence}')
print(f'Processed sequence: {processed_sequence}')

