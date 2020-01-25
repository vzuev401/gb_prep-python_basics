sequence_input = input(
    'Input elements divided by ";"\n'
    'Note: whitespaces around an element will be a part of it.\n'
    '\n'
    'Your sequence: '
)

sequence = sequence_input.split(';')
processed_sequence = sequence.copy()

for i in range(1, len(l := processed_sequence), 2):
    l[i - 1], l[i] = l[i], l[i - 1]

print()
print(f'Your sequence:      {sequence}')
print(f'Processed sequence: {processed_sequence}')

