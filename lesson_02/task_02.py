user_input = input(
    'Input elements divided by ";"\n'
    'Note: left and right whitespaces around an element will be part of it.\n\n'
    'Your elements: '
)

user_list = user_input.split(';')
processed_user_list = user_list.copy()

for i in range(1, len(l := processed_user_list), 2):
    l[i - 1], l[i] = l[i], l[i - 1]

print()
print(f'Your list:      {user_list}')
print(f'Processed list: {processed_user_list}')

