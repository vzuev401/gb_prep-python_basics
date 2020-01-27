user_sequence = input(
    'Input elements divided by ";"\n'
    'Note: whitespaces around an element will be a part of it.\n'
    '\n'
    'Sequence: '
)

sequence = user_sequence.split(';')

e_sequence = sequence[::2]
o_sequence = sequence[1::2]

e_sequence.reverse()
o_sequence.reverse()

processed_sequence = []

for _ in range(len(sequence) // 2):
    processed_sequence.append(o_sequence.pop())
    processed_sequence.append(e_sequence.pop())

if e_sequence:
    processed_sequence.append(e_sequence.pop())


print()
print(f'Your list     : {sequence}')
print(f'Processed list: {processed_sequence}')

