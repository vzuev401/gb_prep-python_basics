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

