from pprint import pprint

# Note: first field will be used as title at print
DETAILS_FIELDS = (
    ('name', str),
    ('price', float),
    ('count', int),
    ('unit', str),
)
MESSAGE_INPUT = 'Enter a command (`help` for available commands): '
MESSAGE_HELP = \
    f'Available commands:\n' \
    f'    "add"        - to create a new position\n' \
    f'    "analytics"  - to print an analytics\n' \
    f'    "goods"      - to print info about goods as-is\n' \
    f'    "help"       - to print current message\n' \
    f'    "stop"       - to exit\n'

goods = []

while (user_input := input(MESSAGE_INPUT).lower()) != 'stop':

    if user_input == 'add':
        print('Fill fields:')

        details = {}
        for field, field_type in DETAILS_FIELDS:
            details[field] = field_type(input(f'  {field:<8}: '))

        item_id = len(goods) + 1
        title_field_name = DETAILS_FIELDS[0][0]

        goods.append((item_id, details))

        print(f'\nAdded "{details[title_field_name]}" - {item_id}\n')

    elif user_input == 'analytics':
        analytics = {field: [] for field, _ in DETAILS_FIELDS}

        for _, details in goods:
            for field, value in details.items():
                analytics[field].append(value)

        print()
        pprint(analytics)
        print()

    elif user_input == 'goods':
        print()
        pprint(goods)
        print()

    else:
        print(MESSAGE_HELP)

