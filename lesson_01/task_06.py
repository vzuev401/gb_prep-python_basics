current_distance = float(input(
    'The athlete begins an everyday jogging with the distance (km): '
))
desired_distance = float(input('Desired distance is .. km at least: '))

day = 1
while current_distance < desired_distance:
    current_distance *= 1.1
    day += 1


print(day)

