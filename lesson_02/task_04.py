user_input = input('Input some line: ')

user_words = user_input.split()

for num, word in enumerate(user_words, start=1):
    print(f'{num:>3}. {word[:10]}')

