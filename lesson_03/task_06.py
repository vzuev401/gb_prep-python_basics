def int_func(word):
    shift = 32
    cap_first = chr(ord(word[0]) - shift)
    return cap_first + word[1:]


user_input = input('Enter a line: ')
processed_words = [int_func(word) for word in user_input.split()]
print(' '.join(processed_words))

