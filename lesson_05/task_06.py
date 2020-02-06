# homework. lesson: 05, task: 06

"""
Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.

Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и
общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


from pathlib import Path
import re


script_dir_path = Path(__file__).resolve().parent
origin_file_path = script_dir_path.joinpath('origin_files', 'task_06_origin')


subjects_with_hours = {}
with open(origin_file_path) as file:
    for line in file:
        subject, hours_str = line.split(':', 1)
        hours_list = map(int, re.findall(r'\d+', line))

        subjects_with_hours[subject] = sum(hours_list)

print(subjects_with_hours)

