sum_ = 0
q_index = None

while q_index is None:
    user_input = input('Enter numbers separated by spaces (q - to stop the loop): ')
    sequence = user_input.split()

    if 'q' in sequence:
        q_index = sequence.index('q')
        sequence = sequence[:q_index]

    try:
        numbers = [int(element) for element in sequence]
    except ValueError:
        print(user_input, 'is not valid sequence')
        continue

    sum_ += sum(numbers)
    print('Sum: ', sum_)

