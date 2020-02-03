# homework. lesson: 04, task: 04

"""
Задача:

Представлен список чисел.
Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.

Для выполнения задания обязательно использовать генератор.
"""


from random import choices


count = 20000
sequence = choices(range(count // 4), k=count)

# set(_list) will always be shorter than _list.
#
# According to https://wiki.python.org/moin/TimeComplexity,
# operation `element in set` in worst case costs O(len(_set))
# (for list this operation costs O(len(_list)) in average case),
# so we can to pop the element from the set using `difference_update`
# to decrease `len(_set)` with each unique element in _list.
#
# _list.count(n) in average case also costs O(len(_list)),
# so it would be better to use it if we sure, that we didn't
# meet the number `n` before.

set_ = set(sequence)
processed_sequence = [
    number
    for number in sequence
    if number in set_
    and set_.difference_update({number}) is None
    and sequence.count(number) == 1
]

print(sequence)
print(processed_sequence)


assert all((
    sequence.count(item) == 1
    for item in sequence
    if item in processed_sequence
))

