# homework. lesson: 05, task: 02

"""
Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""


from pathlib import Path


script_dir_path = Path(__file__).resolve().parent
origin_file_path = script_dir_path.joinpath('origin_files', 'task_02_origin')

with open(origin_file_path) as file:
    lines = file.readlines()

    print('Count of lines:', len(lines))
    print('Count of words:')
    for number, line in enumerate(lines, start=1):
        print(f'- line {number}: {len(line.split())} ({line.strip()})')

