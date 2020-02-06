# homework. lesson: 05, task: 04

"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и
считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


from pathlib import Path

from tools import get_or_make_output_folder_near_file as get_folder


TRANSLATIONS = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

output_folder_path = get_folder(__file__)
output_file_path = output_folder_path.joinpath('task_04_output_file')

script_dir_path = Path(__file__).parent
origin_file_path = script_dir_path.joinpath('origin_files', 'task_04_origin')


with open(origin_file_path, encoding='UTF-8') as file:
    lines = file.readlines()

with open(output_file_path, 'w', encoding='UTF-8') as file:
    for line in lines:
        number = line.split(' - ', 1)

        if len(number) > 1 and number[0] in TRANSLATIONS:
            line = f'{TRANSLATIONS[number[0]]} - {number[1]}'

        file.write(line)

