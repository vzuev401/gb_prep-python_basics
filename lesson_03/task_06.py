# homework lesson: 3, task: 6

"""
Задача:


Реализовать функцию int_func(),
принимающую слово из маленьких латинских букв и
возвращающую его же, но с прописной первой буквой.

Например, print(int_func(‘text’)) -> Text.
"""


def int_func(word):
    shift = 32
    cap_first = chr(ord(word[0]) - shift)
    return cap_first + word[1:]


user_input = input('Enter a line: ')
processed_words = [int_func(word) for word in user_input.split()]
print(' '.join(processed_words))

