revenue = float(input("Input firm's revenue: "))
expenses = float(input("Input firm's expenses: "))

if revenue > expenses:
    print('Your company has PROFIT!')

    profit = revenue - expenses
    print(f'Gross margin: {profit / revenue:.5f}')

    employees_count = int(input('How many employees does your company have? Answer: '))

    profit_per_employee = profit / employees_count
    print(f'Profit per employee: {profit_per_employee:.3f}')

elif revenue < expenses:
    print('Your firm works at a LOSS')
else:
    print('Break-even: neither a loss nor a profit')
    print('https://en.wikipedia.org/wiki/Break-even')

