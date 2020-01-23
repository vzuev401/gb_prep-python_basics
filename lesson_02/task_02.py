user_input = input(
    'Input elements divided by ";"\n'
    'Note: left and right whitespaces around an element will be part of it.\n\n'
    'Your elements: '
)

user_list = user_input.split(';')
processed_user_list = user_list.copy()

# `len(l) - 1` guarantees that `l[i + 1]` will exists
for i in range(0, len(l := processed_user_list) - 1, 2):
    l[i], l[i + 1] = l[i + 1], l[i]

print()
print(f'Your list:      {user_list}')
print(f'Processed list: {processed_user_list}')

