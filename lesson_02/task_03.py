# months_list = [
#     *(['winter'] * 2),
#     *(['spring'] * 3),
#     *(['summer'] * 3),
#     *(['autumn'] * 3),
#     *(['winter'] * 1),
# ]

# This initialization is cheaper (and readable maybe)
months_list = [
    'winter',
    'winter',

    'spring',
    'spring',
    'spring',

    'summer',
    'summer',
    'summer',

    'autumn',
    'autumn',
    'autumn',

    'winter',
]

months_dict = dict(enumerate(months_list, start=1))

month_number = int(input('Input a number of month (from 1 to 12): '))

print(f'list : {month_number} -- {months_list[month_number - 1]}')
print(f'dict : {month_number} -- {months_dict[month_number]}')

