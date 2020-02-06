# homework. lesson: 05, task: 07

"""
Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о
фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл,
вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в
словарь (со значением убытков).

Пример списка: [
    {
        “firm_1”: 5000,
        “firm_2”: 3000,
        “firm_3”: 1000
    },
    {
        “average_profit”: 2000
    }
]

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""


import json
from pathlib import Path
from statistics import mean

from tools import get_or_make_output_folder_near_file as get_folder


output_folder_path = get_folder(__file__)
output_file_path = output_folder_path.joinpath('task_07_output_file.json')

script_dir_path = Path(__file__).parent
origin_file_path = script_dir_path.joinpath('origin_files', 'task_07_origin')


firms_data = {}

with open(origin_file_path) as file:
    for line in file:
        name, form, revenue, expenses = line.split()
        firms_data[name] = int(revenue) - int(expenses)

average_profit = mean([val for val in firms_data.values() if val > 0])

with open(output_file_path, 'w') as file:
    json.dump(
        [firms_data, {'average_profit': average_profit}],
        file
    )

