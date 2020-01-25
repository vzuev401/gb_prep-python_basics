from random import choices, randint


def suitable_index_in_non_increasing_sequence(element, sequence):
    """Position to insert `element` in non-increasing `sequence`.

    The result is such position in the `sequence`,
    which allows to insert the an `element` into the `sequence` and
    keep the`sequence` as non-increasing.

    Parameters
    ----------
    element
        Object that has the same type as objects in sequence.
    sequence : list
        List of objects of one type.

    Returns
    -------
    int
        An index of the suitable position.

    Notes
    -----
    Objects should implement “rich comparison” methods [1]_.

    References
    ----------
    .. [1] “Rich comparison” methods
           https://docs.python.org/3.8/reference/datamodel.html#object.__lt__
    """
    if not sequence or sequence[0] <= element:
        return 0
    elif sequence[-1] >= element:
        return len(sequence)

    left, right = 0, len(sequence)
    middle = (left + right) // 2

    # `middle` will be an index fits to insert `element` into the sequence,
    # to keep the sequence as non-increasing
    #
    # so in the resulting list it will looks like
    # [.., sequence[middle - 1], element, sequence[middle], ..]

    while True:
        if sequence[middle - 1] < element:
            middle, right = (middle + left) // 2, middle
        elif element < sequence[middle]:
            left, middle = middle, (middle + right) // 2
        else:
            break

    return middle


rating_list = choices(range(1, 10), k=randint(0, 10))
rating_list.sort(reverse=True)

print('Current rating:', rating_list)

while (user_input := input('Input a natural number: ')).isdigit():
    user_number = int(user_input)

    index = suitable_index_in_non_increasing_sequence(user_number, rating_list)

    # Find the rightmost available position in `rating_list` for `user_number`
    while index < len(rating_list) and user_number == rating_list[index]:
        index += 1

    rating_list.insert(index, user_number)

    print('\nCurrent rating:', rating_list)

