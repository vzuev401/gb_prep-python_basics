strange_list = [
    None,
    bool(),
    int(),
    float(),
    complex(),
    str(),
    list(),
    dict(),
    set(),
    frozenset(),
    tuple(),
    bytes(),
    bytearray(),
]

for elem in strange_list:
    print(f'{str(type(elem)):<20} : {elem}')

