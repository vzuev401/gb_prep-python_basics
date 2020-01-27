user_sequence = input(
    'Input elements divided by ";"\n'
    'Note: whitespaces around an element will be a part of it.\n'
    '\n'
    'Sequence: '
)

sequence = user_sequence.split(';')

e_sequence = sequence[::2]
o_sequence = sequence[1::2]

is_last_unpaired = len(e_sequence) - len(o_sequence)

processed_sequence = []

for i in range(len(sequence) // 2):
    processed_sequence.append(o_sequence[i])
    processed_sequence.append(e_sequence[i])

if is_last_unpaired:
    processed_sequence.append(e_sequence[-1])


print()
print(f'Your list     : {sequence}')
print(f'Processed list: {processed_sequence}')

