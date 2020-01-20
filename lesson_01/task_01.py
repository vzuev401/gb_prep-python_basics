def create_var_info(variable):
    """Create an info message about a variable using format `var_type: var_value`

    Parameters
    ----------
    variable
        The variable itself

    Returns
    -------
    str
        Message in format `var_type: var_value`

    """
    return f'{str(type(variable)):<16}: {variable}'


some_int_var = 123
some_str_var = 'One hundred twenty three'
some_float_var = 12.3
some_bool_var = True
some_dict_var = {
    1: 'one',
    2: 'two',
    'three': 3,
}

print('Init values: ')
for var in (
        some_bool_var,
        some_str_var,
        some_float_var,
        some_bool_var,
        some_dict_var):
    print(create_var_info(var))


print('\nAn input block: ')
users_values = []

# Prompt for a user's input while an input line is not empty.
while (users_input := input('Input some value (Leave line empty to stop the loop): ')) != '':
    # Try to cast an input in an order:
    #   - int;
    #   - float;
    #   - str (leave as str).
    try:
        users_input = int(users_input)
    except ValueError:
        try:
            users_input = float(users_input)
        except ValueError:
            pass

    users_values.append(users_input)

print('\nUser values: ')
for var in users_values:
    print(create_var_info(var))

