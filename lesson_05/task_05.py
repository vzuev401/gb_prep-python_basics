# homework. lesson: 05, task: 05

"""
Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


from tools import get_or_make_output_folder_near_file as get_folder


output_folder_path = get_folder(__file__)
file_path = output_folder_path.joinpath('task_05_output_file')

with open(file_path, 'w+') as file:
    file.writelines(input('Input numbers: '))

    file.seek(0)
    numbers = map(float, file.read().split())

    print('Sum:', sum(numbers))

