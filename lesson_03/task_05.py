# homework lesson: 3, task: 5

"""
Задача:


Программа запрашивает у пользователя строку чисел,
разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.

Пользователь может продолжить ввод чисел, разделенных пробелом и
снова нажать Enter. Сумма вновь введенных чисел будет
добавляться к уже подсчитанной сумме.

Но если вместо числа вводится специальный символ,
выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу.
"""

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

