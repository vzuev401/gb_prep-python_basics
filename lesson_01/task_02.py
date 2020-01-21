seconds = int(input('Input a time in seconds: '))

minutes, seconds = divmod(seconds, 60)
hours, minutes = divmod(minutes, 60)

print(f'{hours:02}:{minutes:02}:{seconds:02}')

