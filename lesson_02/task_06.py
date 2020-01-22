from pprint import pprint


details_fields = (
    ('name', str),
    ('price', float),
    ('count', int),
    ('unit', str),
)

message_input = 'Enter a command (`help` for available commands): '
message_help = \
    f'Available commands:\n' \
    f'    {"add":<10} - to create a new position\n' \
    f'    {"analytics":<10} - to print an analytics\n' \
    f'    {"goods":<10} - to print info about goods as-is\n' \
    f'    {"help":<10} - to print current message\n' \
    f'    {"stop":<10} - to exit\n'

goods = []

while (user_input := input(message_input).lower()) != 'stop':

    if user_input == 'add':
        print('Fill fields:')

        details = {}
        for field, field_type in details_fields:
            details[field] = field_type(input(f'  {field:<8}: '))
        goods.append((len(goods) + 1, details))

        print(f'\nAdded "{goods[-1][1]["name"]}" - {goods[-1][0]}\n')

    elif user_input == 'analytics':
        analytics = {field: [] for field, _ in details_fields}

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
        print(message_help)

