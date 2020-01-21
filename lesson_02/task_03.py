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

