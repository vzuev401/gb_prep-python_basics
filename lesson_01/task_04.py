number = int(input('Input an integer: '))

_num, max_digit = number // 10, number % 10
while (max_digit < 9) and (_num > 0):
    _num, last_digit = _num // 10, _num % 10

    if last_digit > max_digit:
        max_digit = last_digit


print(f'"{max_digit}" is max digit for a number "{number}"')

