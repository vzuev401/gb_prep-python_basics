# homework. lesson: 05, task: 03

"""
Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


from pathlib import Path
from statistics import mean


script_dir_path = Path(__file__).resolve().parent
origin_file_path = script_dir_path.joinpath('origin_files', 'task_03_origin')

with open(origin_file_path) as file:
    salaries = []
    for line in file.readlines():
        last_name, salary = line.split()
        salary = int(salary)

        if salary < 20000:
            print(last_name)

        salaries.append(salary)

    print()
    print(f'Average salary: {mean(salaries):.2f}')

